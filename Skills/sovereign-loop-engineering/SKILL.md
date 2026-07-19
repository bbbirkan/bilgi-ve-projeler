---
name: sovereign-loop-engineering
description: |
  Loop Engineering — ajan sistemleri için öz-çalışan döngü mimarisi.
  İki loop tipi (deterministik / non-deterministik), Claude Code 5 özelliği
  (/ultracode, /goal, /loop, auto mode, self-verification), Hermes adversarial
  loop kurulumu ve Sovereign sistemine entegrasyon rehberi.
  Dumb Zone, Ralph Loop, Harness Engineering, Adversarial Development eklenди.

  TETIKLEYICILER — bu skill şu durumlarda devreye girer:
  - "loop engineering", "ajan döngüsü", "kendini yönlendiren ajan"
  - "ultracode", "/goal", "/loop" komutları
  - "ajanı otomatikleştir", "hands-off çalıştır", "başını bırak gitsin"
  - "deterministik loop", "non-deterministik", "verification gate"
  - "dumb zone", "context sıfırla", "context yönetimi"
  - "harness", "AI layer", "ralph loop", "multi-session"
  - "adversarial development", "devil's advocate", "debate panel"
  - Kaynak içerik analizi: video/makale geldiğinde ne yapacağını bilmek için

  KAYNAKLAR:
  - OpenClaw kurucusu — "Loop Engineering" kavramı
  - Boris Cherny (Claude Code kurucusu) — 5 adımlı otonom akış
  - Cole Medine — Dumb Zone, Ralph Loop, Harness Engineering (2026-06-18)
  - Hermes Agent dokumentasyonu
  Son güncelleme: 2026-06-18
---

# Sovereign Loop Engineering Skill

Ajan sistemlerinde insan müdahalesini ortadan kaldıran döngü mimarisi.
Prompt engineering → Loop engineering geçişi: sen prompt yazmazsın, sistem kendi promptunu üretir.

---

## KAVRAM HARİTASI

```
Eski yol (Prompt Engineering):
  Sen → Prompt → Ajan → Çıktı → Sen kontrol → Reprompt → ...

Yeni yol (Loop Engineering):
  Sen → Bitiş Koşulu Tanımla → Loop → Ajan → Doğrula → [Başarı? Dur : Devam]
```

**Beş temel bileşen:**
1. **Context Management** — Ajan her turda ne biliyor? Sistem promptu gömülüp kalmasın
2. **Feedback Quality** — Test çıktısı, ekran görüntüsü, HTTP yanıtı — somut sinyal
3. **Verification Gate** — "Bitti" demeden önce gerçekten kontrol et
4. **Termination Condition** — Ne zaman durulacağını net yaz, yoksa ya çok erken ya hiç durmuyor
5. **Error Handling** — Tool call başarısız olunca ne yapacağını açıkla, kırık bırakma

---

## İKİ LOOP TİPİ

### Tip 1 — Deterministik Loop
Net bitiş koşulu olan görevler. Ölçülebilir, makinenin anlayabileceği bitiş.

**Ne zaman kullan:**
- Test geçmesi / compile başarısı
- Port/servis sağlık kontrolü
- Dosya oluşturulması, endpoint yanıtı
- Kod hatası düzeltilmesi

**Sovereign örnekleri:**
```bash
# YT Signal sağlıklı çalışana kadar düzelt
claude -p "/goal localhost:8007/health 200 döndürüyor.
ultracode: YT Signal servisini kontrol et, hata varsa düzelt, servis sağlıklı olana kadar durma.
Bitti demeden önce curl localhost:8007/health ile doğrula."

# Worker çıktısı üretene kadar çalış
claude -p "/goal /root/2026-sovereign/workers/ klasöründe bugünün tarihi ile başlayan en az 2 output dosyası var.
ultracode: sovereign_workers.py'yi çalıştır, çıktı yoksa debug et, 2 dosya üretene kadar dur."
```

### Tip 2 — Non-Deterministik Loop
İnsan yargısı gerektiren, net ölçüt olmayan görevler.

**Ne zaman kullan:**
- UI/UX kalitesi
- Metin tonu, yazı stili
- Strateji kararları
- Yaratıcı içerik

**Çözüm — Adversarial Loop (Orchester zaten bunu yapıyor):**
```
Model A (builder) → çıktı üretir
Model B (verifier) → yargılar
[Geçti mi? Dur : Model A düzelt, tekrar]
```

---

## CLAUDE CODE 5 ÖZELLİK

### 1. Auto Mode (İzin İsteme)
Durum: **Sovereign'de zaten aktif** (`bypassPermissions`)
```json
// /root/.claude/settings.json
{
  "permissions": { "defaultMode": "bypassPermissions" }
}
```
Eğer yeni bir sistemde yoksa: `/config` → auto mode aç

### 2. Dynamic Workflows — `/ultracode`
**Gereksinim:** Claude Code v2.1.154+ (Sovereign: v2.1.178 ✅)

Claude kendi orchestration scriptini yazar → 1000'e kadar sub-agent, 16 paralel.
Hafıza sorunu çözülüyor: plan sohbette değil, betik içinde yaşıyor.

```bash
# Kullanım
claude -p "ultracode: <büyük görevin tarifini buraya yaz>"

# /goal ile birlikte (güçlü kombinasyon)
claude -p "/goal <bitiş koşulu>. ultracode: <görev>. Doğrula: <nasıl kontrol edecek>"
```

**Ne için ideal:** Çok dosyalı refactor, büyük migration, codebase geneli hata tarama

### 3. /goal — Bitiş Koşulu
Her turdan sonra küçük bir model "koşul sağlandı mı?" diye bakar.
Hayır → devam. Evet → dur.

```bash
/goal <somut ölçülebilir koşul>
# Örnek: /goal tüm testler yeşil ve port 8007 sağlıklı yanıt veriyor
```

**Kural:** Niyet cümlesi değil, ölçülebilir durum yaz.
- ❌ "YT Signal düzgün çalışsın"
- ✅ "curl localhost:8007/health 200 döndürüyor ve /consensus endpoint JSON yanıt veriyor"

### 4. /loop — Sürekli İzleme
Oturum boyunca tekrarlayan kontrol. Oturum kapanınca biter.

```bash
/loop <her turda ne yapılacak>
# Örnek: /loop Sovereign servislerini kontrol et, anomali varsa düzelt ve rapor et
```

**Fark:** `/goal` bir görevi bitirir, `/loop` sürekli izler.

### 5. Self-Verification (Kendi Doğrulama)
"Bitti" demeden önce ajan ürettiğini kendi test etmeli.

| Görev tipi | Doğrulama yöntemi |
|-----------|------------------|
| Backend API | curl + HTTP status kodu |
| Python servisi | uvicorn başlat + /health çağır |
| Veritabanı | query çalıştır, satır say |
| Cron/timer | journalctl -u servis-adı |

**Sovereign'e özel doğrulama scripti:**
```bash
# /root/scripts/sovereign_verify.sh
#!/bin/bash
curl -s localhost:8007/health | grep -q "ok" && echo "YT Signal ✅" || echo "YT Signal ❌"
systemctl is-active orchester.service && echo "Orchester ✅" || echo "Orchester ❌"
systemctl is-active hermes-gateway.service && echo "Hermes ✅" || echo "Hermes ❌"
ls /root/2026-sovereign/workers/output_$(date +%Y-%m-%d)* 2>/dev/null | wc -l | xargs -I{} echo "Workers bugün: {} dosya"
```

---

## SOVEREIGN'E ENTEGRASYON

### Mevcut Loop Yapımız
```
sovereign.timer (09:00) → Menejer plan → Birkan görevleri
sovereign-workers.timer (2 saatte bir) → DeepSeek + Kimi → çıktı
sovereign-backup.timer (6 saatte bir) → R2 yedek
yt-signal-indexer.timer (saatte bir) → transkript işle
```
Bu zaten deterministik loop mühendisliği. Adı yoktu, şimdi var.

### Eksik: Verification Gate
Workers çıktı üretince kimse "gerçekten çalıştı mı?" diye bakmıyor.
Eklenecek: her worker çalışmasından sonra `/root/scripts/sovereign_verify.sh` çağır.

### Adversarial Loop — Orchester Şeması
```
Hermes/Telegram sorusu
        ↓
Claude (builder) → cevap üretir
        ↓
OpenCode/Kimi (verifier) → eleştirir, boşluk bulur
        ↓
Claude (synthesizer) → birleştirir, eksikleri kapatır
        ↓
Kullanıcıya gönder
```
Non-deterministik görevler için Orchester'ı bunu yapıyor. "AI slop detector" skill gibi bir verifier skill yazılabilir.

---

## KAYNAK GELDİĞİNDE NE YAPILIR

Birkan yeni bir video/makale/tweet içeriği getirdiğinde:

```
ADIM 1 — SINIFLANDIR
  Kaynak tipi nedir? Video transkript / makale / tweet thread / döküman
  Konu: teknik mimari | tool/araç | strateji | pazar bilgisi | Sovereign'e doğrudan uygulanabilir

ADIM 2 — DEĞERLENDİR
  a) Zaten yapıyor muyuz? → "Bunu X şekilde zaten yapıyoruz"
  b) Eksik mi? → Sovereign'e ne ekler?
  c) Çelişiyor mu? → Mevcut yaklaşımı sorgula

ADIM 3 — AKSİYON ÇEK
  Hemen yapılabilir (bugün): → yap
  Kısa vadeli (bu hafta): → YAPILACAKLAR.md'ye ekle
  Vizyon (ileride): → GELECEK.md'ye ekle
  Referans (bilgi): → sovereign-brain/research/ kaydet

ADIM 4 — SKILL GÜNCELLEMESİ GEREKİYOR MU?
  Yeni teknik veya araç öğrendiysen → ilgili skill'i güncelle veya yeni skill yaz
```

---

## HAZIR PROMPT ŞABLONLARİ

### Büyük Görev (ultracode + goal)
```bash
claude -p "/goal <somut bitiş koşulu>.

ultracode: <görevin detaylı tarifı>.

Bitti demeden önce kendin doğrula:
- Backend: servisi başlat ve /health'e curl at
- Dosya: ls ile kontrol et
- Veritabanı: sorgu çalıştır

Sonunda ver:
1. Ne değişti
2. Nasıl doğruladın
3. Hangi riskler kaldı"
```

### Sürekli İzleme
```bash
claude -p "/loop Sovereign servislerini kontrol et:
- port 8006, 8007, 8004, 8008 açık mı?
- Son 1 saatte hata log var mı?
- Workers çıktı üretti mi?
Sorun varsa düzelt, her turda kısa rapor ver."
```

### Deterministik Düzeltme
```bash
claude -p "/goal <bitiş koşulu>.
Görevi tamamla. Doğrula. Geçmiyorsa düzelt. Tekrar test et. Geçene kadar dur."
```

---

## DUMB ZONE — KRİTİK CONTEXT SINIRI

LLM'ler belirli token threshold'unu geçince "aptallaşıyor":

| Model | Dumb Zone Başlangıcı |
|-------|---------------------|
| Claude Opus 4.7 | ~200K token |
| Claude Opus 4.8+ | ~250K token |
| Claude Sonnet 4.6 | ~100-125K token |

**Belirtiler:** Açık hataları yapıyor, skills'i unutuyor, tekrar eden şeyleri kaçırıyor.
**Çözüm:** Bu eşiğe gelmeden önce `/compact` yap veya yeni session aç.
**Kural:** 1M context = yanıltıcı güvenlik. Gerçek limit ~250K (Opus için).

### Needle in the Haystack
Önemli bilgileri ortaya gömme — ya öne (konuşma başı) ya sona (son mesaj) koy.

---

## RALPH LOOP — ÇOK-SESSION BÜYÜK GÖREV MİMARİSİ

Tek session'a sığmayan büyük görevler için:

```
Session 1 (Planlama)
  → Spec + phase listesi + handoff document yaz
        ↓
Session 2 (Phase 1)
  → Handoff oku → Phase 1 yap → Execution report yaz
        ↓
Session 3 (Phase 2)
  → Önceki report oku → Phase 2 yap
        ↓
Session N (Validation)
  → Tüm report'ları oku → test + code review + güvenlik
```

**Neden:** Her session fresh = dumb zone'a girmiyor.
**Sovereign analog:** sovereign_workers.timer zaten bu. Her timer = bir session.
**Archon:** Cole Medine'in open-source CLI uygulaması.

---

## ADVERSARİAL DEVELOPMENT — DEVIL'S ADVOCATE

Build bittikten sonra ayrı session:
```
"Bu sistemin hatalı olabileceği 5 senaryoyu bul.
Devil's advocate ol — eleştir, boşluk bul, kır."
```

**Debate Panel** (agent teams, strateji kararları için):
```
"Sen CEO, sen beginner, sen güvenlik uzmanı — hepiniz bağımsız araştırın,
görüş geliştirin, tartışın. Konsensüse varana kadar devam edin."
```
Token ağır ama fikir çeşitliliği güçlü. Kod değil, karar/araştırma için kullan.

---

## GÜVENLİK — GERÇEK SANDBOX YOKTUR

**İki false security:**
1. "Söylersen yapmaz" → Yapar
2. "DELETE komutunu engelledim" → Script yazar, script çalıştırır

**Doğru varsayım:** "Agent dokunabildiği her şeye dokunacak."
**Hooks (PreToolUse):** Kritik komutları engellemek için ama tam güvenlik değil.
**Gerçek güvenlik:** Scoped API keys + minimal file permissions.

---

## REFERANSLAR
- OpenClaw kurucusu: "Loop Engineering" terimi, "sen prompt yazma, sistem yazsın"
- Boris Cherny: Claude Code 5 özellik — auto mode, /ultracode, /goal, /loop, self-verification
- Cole Medine (2026-06-18): Dumb Zone, Ralph Loop, Harness Engineering, Adversarial Development
  → Tam notlar: sovereign-brain/techniques/cole_medine_coding_agents_2026-06-18.md
- Hermes Agent: deterministic loop (test pass), non-deterministic (AI slop detector), self-evolving skills
- Sovereign örnek: sovereign_workers.timer = deterministik loop, Orchester = adversarial loop

### OTOMATİK Öğrenim [2026-06-27]
> Raw loop (while + max_iter) 'dumb' — Codex/Hermes goal pattern'ı bunu LLM-hakemli continuous loop'a çeviriyor: her turun sonunda 'goal satisfied mı?' judge call'i, state-preserving prompt ve ambiguous task desteği ile.
>
> /root/2026-sovereign/sovereign-loop-engineering skill'ine 'Goal Pattern vs Raw Loop' notu ekle: LLM judge as stop-condition, state handoff between iterations, ambiguous goal support. Mevcut Hermes config'teki delegation.max_iterations: 50'yi 'goal mode' toggle'ı ile zenginleştirme notu düş.

### OTOMATİK Öğrenim [2026-06-27]
> 'Soru sor vs inşa et' ayrımı: kullanıcı 'nasıl çalışır?' derse ajan build modundan çıkar, salt açıklama moduna geçer — loop kırma mekanizması.
>
> Vekil/Derin agent prompt'larına intent classifier ekle: question → no tools, request → tools allowed. Hermes max_turns:1 kuralıyla birleştir.
