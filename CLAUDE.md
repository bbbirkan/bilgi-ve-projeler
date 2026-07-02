# SISTEM BAĞLAM DOSYASI
> Bu dosya, bu sunucuya bağlanan her yapay zeka asistanının (Claude Code, Hermes, OpenCode vb.)
> okuyarak hızlıca bağlamı kavraması için yazılmıştır.
> Son güncelleme: 2026-06-17

> **YAPILACAKLAR:** `/root/YAPILACAKLAR.md` — Birkan'ın tüm görev listesi burada.
> Her yeni görev, karar veya tamamlanan iş oraya kaydedilmeli.

> **CEBİMİZ:** `/root/CEBİMİZ.md` — Para, API'ler, hesaplar, altyapı, yetenekler. Elimizdeki her şey.
> Değişince güncelle. "Ne var elimizde?" dediğinde buraya bak.
> **TOKEN/KEY KURALI:** Herhangi bir servis için token, SSH key veya credential gerektiğinde — ÖNCE `/root/CEBİMİZ.md`'ye bak. Orada yoksa Birkan'a sor. Birkan verince hem kullan hem CEBİMİZ.md'ye ekle.

> **VİZYON KURALI:** Hep küçük kalmayı varsayma. Her araştırma ve öğrenilen teknik için
> "bunu biz ne zaman kullanırız?" sorusunu sor → cevabı `/root/sovereign-brain/GELECEK.md`'ye ekle.
> Şu an yapılamayanlar oraya gider — kaybolmasın.

> **OTOMATİK KURAL — SKILL KONTROLÜ:**
> Bir konu geldiğinde `~/.hermes/skills/` altında ilgili skill var mı kontrol et ve oku.
> Birkan'ın her konuşmada "yeteneklerimize bak" demesine gerek kalmamalı.
> Konu → Skill eşlemesi aşağıdaki **SKILL İNDEKSİ** bölümünde.

> **BAŞLATMA KOMUTU:**
> Terminal'de `ortak` yaz → `cd /root && claude -c` çalışır → son konuşma devam eder.
> `ortak-yeni` yaz → sıfırdan yeni oturum başlar.

---

## TETİKLEYİCİ KOMUTLAR

| Birkan ne derse | Ne yaparsın |
|----------------|-------------|
| `ortak hazır mısın` | **STATE.md** + SESSION_LOG.md + YAPILACAKLAR.md oku → tam durum raporu ver → sesli at |
| `resume` | **STATE.md** + SESSION_LOG.md oku → kaldığın yerden devam et |
| `yeteneklerimize bak` | `~/.hermes/skills/` skill dosyalarını oku |
| `kendini güncelle` | STATE.md + SESSION_LOG + YAPILACAKLAR + CLAUDE.md senkronize et |
| `ne durumdayız` | **STATE.md** oku → servis durumlarını kontrol et → sesli at |
| `ekosistemi aç` | **STATE.md** + `/root/sovereign-brain/` tüm ana dosyaları oku (index.md, VIZYON.md, decisions/, entities/team.md) → tam bağlamı yükle → "Ekosistem açık" de |

---

## DAVRANIŞSAL KURALLAR — HER OTURUMDA ZORUNLU

Bu kurallar hafıza dosyalarına değil, buraya yazıldı. Her oturum açılışında otomatik yüklenir.

### 1. OTURUM BAŞLANGICI
Her yeni oturum açıldığında şunları yap — Birkan söylemeden:
1. `/root/STATE.md` oku (güncel sistem durumu + aktif görev)
2. `/root/SESSION_LOG.md` oku (önceki oturumun kararları)
3. `/root/YAPILACAKLAR.md` oku (aktif görevler)
4. Önceki oturumun devamını tanı, "resume" derse direkt başla

### 2. HER MESAJ İÇİN ORTAK PROTOKOLÜ (KRİTİK — VARSAYILAN ÇALIŞMA AKIŞI)

Birkan bir mesaj/görev gönderdi. Sırayla yap:

```
ADIM 0 — DOĞRULA: Çok adımlı bir görevse önce sor:
  "Hedef ne? (görev değil, hedef)" + "Başarı kriteri ne?"
  Birkan söylemezse sen çıkar — spec yazmadan build etme.

ADIM 1 — BÖLE: Bu görevin hangi kısımları var? Her kısım kime gidiyor?
  → Araştırma/pazar → Göz (Gemini Pro)
  → Hızlı bilgi     → Flaş (Gemini Flash)
  → Kod/dosya       → Derin veya Dip (DeepSeek)
  → Veri/sinyal     → Mini (MiniMax M3)
  → Uzun analiz     → Ay (Kimi K2)
  → Strateji (büyük)→ Menejer (Fable 5) — günde 1 kez

ADIM 2 — DELEGE: opencode run ile hepsini gönder (paralel olabilir)

ADIM 3 — KARŞILAŞTIR: Gelen cevapları oku.
  Birkan'ın düşüncesine yakın mı? Daha iyi mi? Eksik ne?

ADIM 4 — POT ERİT: En iyi parçaları birleştir, tek tutarlı cevap yap.

ADIM 5 — RAPOR ET: Birkan'a ver (sesli + yazılı).
```

**Bu protokolü atla ve kendim yap = token israfı = Birkan'ı yorma.**
**Her seferinde: "Bunu ben mi yapacağım yoksa kime vereceğim?"**

### 2b. TELEGRAM SESLİ MESAJ KURALI (KRİTİK)
Birkan kamyon sürücüsü. Gündüzleri ekrana bakamaz, sesli mesaja ihtiyacı var.

```
Gündüz (06:00-20:00 ET — America/New_York, Salem NJ):
  → Claude Code'da yanıt yaz VE
  → python3 /root/2026-sovereign/telegram_voice.py "kısa özet (max 3-4 cümle)"
  → Her önemli yanıtta, her kararında, her tamamlamada

Gece (20:00-06:00 ET):
  → Sadece Claude Code. Telegram'a HİÇBİR ŞEY gönderme.
```

**Sesli özet kuralları:**
- Teknik detay değil, sonuç ve eylem söyle
- "X tamamlandı, Y bekliyor" formatı
- Kod/liste varsa özetini yap

### 3. PATRON GİBİ ÇALIŞ — MODEL HİYERARŞİSİ (KRİTİK)

> ⚠️ HER GÖREV GELMEDEN ÖNCE ŞU SORUYU SOR: "Bunu ben mi yapmalıyım, yoksa hiyerarşide kime vermem gerekiyor?"
> Cevap neredeyse her zaman: birine ver. Yalnızca karar, sentez ve rapor için kendim çalışırım.
> Birkan bunu defalarca söyledi — bir daha söyletme.

**ANA ÜÇLÜ — her zaman bunları kullan:**

```
Kod yaz / kur / düzelt / deploy / dosya oluştur
  → opencode run -m opencode-go/glm-5.2 "görev"   ← Vekil (5.2'ye güncellendi 2026-06-22)
  (Derin = artık derin analiz + strateji, kod değil)

Web araştırma / OSINT / gerçek zamanlı data / pazar analizi
  → agy "görev"   ← Antigravity CLI

Koordinasyon / sentez / karar / hafıza / rapor (BEN yaparım)
  → claude CLI (mevcut oturum)

Karmaşık akıl yürütme / 1M context
  → opencode run -m opencode-go/kimi-k2.6 "görev"

Entity çekme / veri yapılandırma
  → opencode run -m opencode-go/minimax-m3 "görev"

Strateji / Menejer (GEÇİCİ — 2026-06-13'ten itibaren)
  ⚠️ Fable (anthropic/claude-fable-5) KAPALI — Anthropic kısıtladı
  → GEÇİCİ MENEJER = claude-opus-4-8 (Claude CLI, Pro subscription)
  → claude -p --model claude-opus-4-8 "görev"
  → Fable açılınca /root/check_menejer.sh bildirir → orijinal menajerimize döneriz
  → Zen (opencode/claude-fable-5) KULLANMA — bakiye tükenir

ACİL DURUM — ana üçlü çalışmıyorsa OpenRouter API (OPENROUTER_API_KEY mevcut):
  Kural: KİME ihtiyacın varsa ONUN modelini çağır — karıştırma.

  | Ekip Üyesi | OpenRouter Model |
  |------------|-----------------|
  | Menejer Fable | anthropic/claude-fable-5 |
  | Göz Gemini | google/gemini-2.5-pro |
  | Flaş Gem | google/gemini-2.5-flash |
  | Derin Seek | deepseek/deepseek-v3 |
  | Dip Flash | deepseek/deepseek-v3 |
  | Ay Moonshot | moonshot/kimi-k2 |
  | Mini MiniMax | minimax/minimax-m3 |
  | Koşan Haiku | anthropic/claude-haiku-4-5 |
  | Vekil Glim | z-ai/glm-5.2 |

  Normalde dokunma. Para gelince serbestleşir.

Karmaşık akıl yürütme / çok adımlı plan / 1M context
  → opencode run -m opencode-go/kimi-k2.6 "görev"

Strateji / büyük karar (günde 1 kez)
  → Menejer Fable — opencode run -m anthropic/claude-fable-5 "görev"
```

> Routing detayı: /root/sovereign-brain/research/cli_routing_analizi_2026-06-13.md

**Ben (Ortak) sadece şunları yaparım:**
- Kime vereceğime karar ver
- Worker çıktısını oku, kontrol et, düzelt
- Birkan'a rapor ver (sesli)
- Kararları kaydet (SESSION_LOG, ARSENAL, sovereign-brain)

**Yasak:** Kendim kod yazma, dosya oluşturma, araştırma yapma — bunlar worker işi.

### 4. OTURUM SONUNDA
Önemli bir karar alındığında veya görev tamamlandığında — hemen yaz:
- `/root/STATE.md` → güncel durum, aktif görev, son kararlar güncelle
- `/root/SESSION_LOG.md` → tarih + ne yapıldı + bekleyenler
- `/root/YAPILACAKLAR.md` → yeni görevler + tamamlananlar

### 4a. SORU SORMA İKONU KURALI (KRİTİK — Birkan, 2026-06-18)

Birkan terminalde çalışırken ekrana bakmıyor. Soru sormam gerektiğinde görünür bir ikon kullan.

**Her soruda bu formatı kullan — ZORUNLU:**

```
❓ SORU: [soru metni]
```

Kurallar:
- ❓ ikonu HER soruda başta yer alsın — terminal'de kaybolmasın
- Tek soru = tek ❓ blok
- Çok soru = her biri ayrı ❓ blok
- Soruyu sorduktan sonra başka şey yazma — Birkan önce soruyu görsün
- Bu kural terminal'de yazarken (Claude Code) geçerli — Telegram'da ayrı format var

### 4b. DUMB ZONE KURALI (KRİTİK — Cole Medine, 2026-06-18)

LLM'ler belirli bir context eşiğini geçince "aptallaşıyor" — gizli hata modu:

| Model | Dumb Zone Başlangıcı |
|-------|---------------------|
| Claude Opus 4.8+ | ~250K token |
| Claude Sonnet 4.6 | ~100-125K token |

**Belirtiler:** Bildiği skills'i kullanmıyor, tekrarlayan hatalar yapıyor, bağlamı kaybediyor.
**Kural:** Bu eşiğe yaklaşmadan önce oturumu kapat, STATE.md'yi güncelle, yeni oturum aç.
**Yanıltıcı:** "1M context var" = yanlış güvenlik. Gerçek limit ~250K (Opus için).

### 4b. REGRESSION KONTROL KURALI (KRİTİK — Vibe Coding Araştırması, 2026-06-24)

Worker (Vekil/Derin/Dip) bir kod değişikliği yaptığında:

> En iyi agent bile tek değişiklikte çalışan özelliklerin **%12'sini sessizce bozar.**
> Boeing analojisi: sistem "tamamlandı" der, pilot güvenir, kaza olur.

**Kural:** Worker bir şey değiştirdiyse sadece yeni özelliği test etme — eski çalışanları da kontrol et.

```
Deploy öncesi minimum checklist:
1. Yeni özellik çalışıyor mu? → Test et
2. Worker kaç dosyaya dokundu? → git diff --stat
3. Dokunulan dosyaların etkilediği eski özellikler var mı? → Kontrol et
4. Servis restart sonrası başka bir şey kırıldı mı? → Logları oku
```

Referans: `sovereign-brain/techniques/agent-kalite-kontrol.md`

### 4b. SYSTEM EVOLUTION KURALI (KRİTİK — Cole Medine, 2026-06-18)

Her bug/hata/yanlış çıktı sonrası:
1. Düzelt (rutin)
2. **SORU:** Neden oldu? Bir daha olmaması için ne kuralı gerekli?
3. Cevabı CLAUDE.md'ye kural olarak ekle VEYA ilgili skill'i güncelle VEYA hook yaz

> "Her bug kalıcı bir yükseltmedir — hatayı düzelt ve bir daha olmamasını sağla."

**Pratik:** Büyük bir şey yanlış gidince claude'a de:
"Bunu düzelt VE bunu önleyecek kuralı CLAUDE.md'deki ilgili bölüme ekle."

### 4c. YAPILACAKLAR SİLME KURALI (KRİTİK)
Birkan konuşurken bir şey yaptığını söylerse → YAPILACAKLAR.md'de var mı bak → varsa "bunu siliyorum" de ve direkt sil. Onay isteme.

### 4c. UZUN İÇERİK YÖNLENDIRME KURALI (KRİTİK — LEVEL 5 BRAIN)

Birkan uzun bir şey gönderdiğinde (transkript, araştırma, not, makale, video içeriği):

**ADIM 1 — İÇERİĞİ SINIFLANDIR:**

| İçerik Türü | Nereye Gider |
|-------------|-------------|
| Rakip analizi / araç / platform | `sovereign-brain/research/` + ilgili skill güncellemesi |
| Teknik yöntem / mimari öğrenme | `sovereign-brain/techniques/` + ilgili skill |
| Karar / seçim | `sovereign-brain/decisions/` |
| Kişi / şirket / entity | `sovereign-brain/entities/` |
| Gelecek vizyon fikri | `sovereign-brain/GELECEK.md` |
| Trading / piyasa / yatırım | `/root/trading-system/STRATEJI.md` |
| Skill ile doğrudan ilgili | `~/.hermes/skills/SKILL_ADI/SKILL.md` güncelle |
| Proje spesifik | İlgili proje klasörü |
| Hem araştırma hem skill | İKİSİNE BIRDEN yaz |

**ADIM 2 — KAYDET VE RAPOR ET:**

Kaydetme bittikten sonra mutlaka söyle:
```
📁 KAYDETTIM:
  → sovereign-brain/research/dosya-adı.md
  → skill güncellendi: birkan-graphify-skill/SKILL.md
```

**ADIM 3 — NEREYE GİDECEĞİ BELİRSİZSE:**

Birden fazla yer uygun görünüyorsa veya emin değilsen → DOĞRUDAN SOR:

```
⚠️ ÖNEMLİ NOT — NEREYE KAYDEDEYİM?

Bu içerik için 2 seçenek var:
A) sovereign-brain/research/ → genel bilgi birikimi
B) birkan-XYZ-skill/SKILL.md → hemen kullanılabilir yetenek

Hangisine kaydedeyim? (A / B / İkisine de)
```

Büyük harfle, görünür yaz. Birkan gözden kaçırmasın.

**ÖZEL KURALLAR:**
- YouTube transkripti + rakip/araç → HEM research/ HEM ilgili skill
- Hermes ile ilgili içerik → `birkan-hermes-agent-mastery/` skill'i kontrol et
- Graphify / knowledge graph → `birkan-graphify-skill/` güncelle
- Trading sinyali / strateji → SADECE STRATEJI.md (başka yere yazma)
- Sesli dikteden gelen ses hataları olabilir → anlam çıkar, düzelt

### 5. BİRKAN PROFİLİ
- Tırcı, gündüz yolda, sesli mesaj hayati
- Salem, NJ'de yaşıyor — America/New_York (Eastern Time) kullan
- 20:00 ET'de uyur — gece mesaj atmaz ve atma
- Teknik seviye: yüksek, kısa ve net konuş
- "yeteneklerimize bak" = `~/.hermes/skills/` skill dosyalarını oku
- "kendini güncelle" = SESSION_LOG + YAPILACAKLAR + CLAUDE.md senkronize et

---

---

## KİM OLDUĞUMUZ

**Kullanıcı:** Birkan Kalyon
- GitHub: `bbbirkan`
- E-posta: `8birkan@gmail.com`
- Rol: Yapay zeka sistemleri kurucusu / otomasyon mimarı

**Sunucu:** Contabo VDS
- Hostname: `vmi2701691`
- OS: Ubuntu 24.04.3 LTS
- RAM: 7.8 GB (swap: 2GB at /swapfile)
- Disk: 145 GB (66 GB dolu, 79 GB boş)
- Kernel: 6.8.0-87-generic (eBPF destekli)

---

## NE YAPMAYA ÇALIŞIYORUZ

Birkan, bu sunucuda **çok katmanlı bir yapay zeka otomasyon ekosistemi** inşa ediyor.
Temel vizyon: Hermes Agent üzerinden gelen mesajlaşma platformu trafiğini, OpenCode + Claude Code
gibi headless kodlama ajanlarına yönlendirerek; gerçek projeleri (Trello görevleri, GitHub repo'ları,
YouTube içeriği, borsa analizi) otomatik olarak ilerletmek.

### Ekosistem Bileşenleri

```
Kullanıcı (Telegram / Discord / WhatsApp)
        ↓
Hermes Agent Gateway (mesajlaşma hub'ı)
        ↓
AI Orkestratör (GPT-5.5 varsayılan, GLM-5.2 delegasyon)
        ↓
OpenCode / Claude Code (headless kodlama)
        ↓
GitHub / Trello / YouTube / Borsa / Medium API'ları
```

---

## KURULU SİSTEMLER VE DURUMU

### 1. Hermes Agent — AKTİF ✅
- **Konum:** `/usr/local/lib/hermes-agent`
- **Versiyon:** v0.14.0 — güncel
- **Servis:** `hermes-gateway.service` aktif ve çalışıyor
- **Config:** `~/.hermes/config.yaml` veya proje içindeki `cli-config.yaml`

**Mevcut model konfigürasyonu:**
```yaml
model.default: openai/gpt-5.5
model.provider: openrouter
delegation.model: z-ai/glm-5.2
delegation.provider: openrouter
delegation.max_iterations: 50
delegation.max_concurrent_children: 3
compression.enabled: true
compression.threshold: 0.4
compression.target_ratio: 0.15
```

**Bellek yapısı (Hermes standardı):**
- `SOUL.md` — Hermes'in kimlik ve kişilik dosyası
- `MEMORY.md` — kalıcı bellek
- `USER.md` — Birkan hakkında bilgiler
- `skills/` dizini — yüklenen yetenekler

**Mevcut platformlar (hermes-gateway üzerinden):**
Telegram, Discord, Slack, WhatsApp, Signal, Matrix ve daha fazlası

**Mevcut Skills (bilgi-ve-projeler/):**
- `birkan-video-watch` — YouTube/video analiz pipeline'ı
- `birkan-video-production-kit` — Video üretim araçları
- `birkan-video-prompt-builder` — AI video prompt oluşturucu
- `birkan-desktop-packaging` — Masaüstü paketleme (PyInstaller, Tauri 2.0, Chrome Ext)
- `social-media/xurl` — X/Twitter otomasyon
- Graphify bilgi grafiği entegrasyonu

---

### 2. OpenCode — AKTİF ✅
- **Versiyon:** 1.14.51
- **Konum:** `/usr/bin/opencode`
- **Durum:** 2 provider auth edilmiş (OpenCode Zen + Go API)
- **Not:** `~/.local/share/opencode/auth.json` içinde
- **Kullanım amacı:** Headless kodlama görevi (`opencode --print 'prompt'`)

---

### 3. Docker — AKTİF ✅
- **Versiyon:** 28.5.1
- **Açık portlar:**
  - 80, 443 → Web proxy (Caddy/Nginx)
  - 8000, 8080 → API servisleri
  - 6001, 6002 → Özel servisler (içeriği doğrulanmamış)

---

### 4. eBPF Araçları — MEVCUT ✅
- `bpftool v7.4.0`, `libbpf v1.4`
- Kernel 6.8 → `BPF_PROG_TYPE_LSM` destekli
- Kullanım planı: Sandbox izolasyonu için LSM hook'ları

---

### 5. Redis — AKTİF ✅
- Versiyon: 7.0.15, systemd servis aktif, boot'ta otomatik başlar
- Kullanım amacı: Redis Streams ile ajan mesaj kuyruğu

---

### 6. Diğer Araçlar
| Araç | Versiyon | Durum |
|------|----------|-------|
| Python | 3.11.15 (venv) / 3.12.3 (sistem) | ✅ |
| Node.js | 22.22.2 | ✅ |
| yt-dlp | 2026.03.17 | ✅ |
| ffmpeg | 6.1.1 | ✅ |
| openai-whisper | — | ❌ Kurulu değil |
| faster-whisper | — | ❌ Kurulu değil |
| gh (GitHub CLI) | 2.45.0 | ✅ |
| tmux | 3.4 | ✅ |

---

## AKTİF PROJELER

### Port Haritası
| Port | Proje | Dizin |
|------|-------|-------|
| 8000 | channel-router | `/root/2026-channel-router` |
| 8001 | visionwatch | `/root/2026-visionwatch` |
| 8002 | youtube-mini | `/root/2026-youtube-mini` |
| 8003 | yt-harvester | `/root/youtube-transcript-engine` |
| 8004 | medium-reader | `/root/2026-medium-reader` |
| 8005 | trello-agent | `/root/2026-hermes-trello-agent` |
| 8006 | orchester | `/root/2026-orchester` |
| 8007 | yt-signal | `/root/2026-yt-signal` |
| 8008 | context-index | `/root/2026-context-index` — FTS5 arama: `curl localhost:8008/search?q=X` |

---

### Proje A — Trello + Hermes Haftalık Ajan ✅ KOD TAMAM
**Repo:** `github.com/bbbirkan/2026-hermes-trello-agent`
**Dizin:** `/root/2026-hermes-trello-agent`
**Amaç:** Trello board'ını haftalık tarayıp, seçili kartları Claude ile analiz edip çalışmayı yapmak, karta yorum eklemek, Telegram'a rapor göndermek.
**Durum:** Kod tamam. API key'ler ve Board/List ID bekleniyor.

**Dosyalar:**
- `main.py` — FastAPI + APScheduler (Pazartesi 09:00 cron)
- `trello.py` — Trello API client
- `agent.py` — Claude analiz + eylem (ARAŞTIR|YAZ|PLANLA|KOD|GEÇER)
- `telegram.py` — Haftalık rapor gönderici
- `launcher.py` — Masaüstü başlatıcı (port 8005 → browser açar)
- `build.sh` — PyInstaller

**Birkan yapacak:**
```bash
# .env doldur:
TRELLO_API_KEY=...      # trello.com/app-key
TRELLO_TOKEN=...        # trello.com/app-key → Token oluştur
TRELLO_BOARD_ID=...     # trello.com/b/BOARD_ID/...
TRELLO_LIST_ID=...      # GET /lists endpoint'inden bul
ANTHROPIC_API_KEY=...
```

---

### Proje B — Hermes Mobil App
**Repo:** `github.com/bbbirkan/2026-hermes-mobile-app`
**Durum:** Scaffold oluşturuldu, geliştirme başlamadı.
**Plan:** Auth akışı → Hermes conversation UI

---

### Proje C — YouTube Otomasyon Ekosistemi ✅ KOD TAMAM

Dört bileşenden oluşuyor, hepsi launcher'lı (çift tıkla → çalışır):

#### C1 — YT Harvester (eski adı: Nexus-1)
**Dizin:** `/root/youtube-transcript-engine`
**Port:** 8003
**Amaç:** 4 planlı YouTube transkript çıkarıcı (A→B→C→D fallback zinciri)
- Plan A: yt-dlp subtitle
- Plan B: Groq Whisper API
- Plan C: YouTube Data API v3
- Plan D: Deeplx transkripsiyon

#### C2 — VisionWatch
**Dizin:** `/root/2026-visionwatch`
**Port:** 8001
**Amaç:** YouTube video içerik analizi (Claude Vision + transkript)
**Gerekli:** `ANTHROPIC_API_KEY` ve `GROQ_API_KEY` `.env`'e ekle

#### C3 — YouTube Mini
**Dizin:** `/root/2026-youtube-mini`
**Port:** 8002
**Amaç:** Hafif YouTube metadata çekici (API key gerektirmez)

#### C4 — Channel Router
**Dizin:** `/root/2026-channel-router`
**Port:** 8000
**Amaç:** YouTube kanal analizi → VisionWatch veya YouTube Mini'ye yönlendirir
**Response formatı:** `{channel_name, channel_url, engine, total, processed, results: [{url, title, description, transcript}]}`

**Kritik kural — yt-dlp PyInstaller içine gömülmemelidir:**
> YouTube algoritmaları haftalık değişir. yt-dlp'yi PyInstaller bundle içine gömmek donmuş versiyona yol açar. Her zaman sistem yt-dlp binary'sini kullan veya runtime'da indir.

---

### Proje M — Medium Reader ✅ KOD TAMAM
**Repo:** `github.com/bbbirkan/2026-medium-reader`
**Dizin:** `/root/2026-medium-reader`
**Port:** 8004
**Amaç:** Medium makale içerik çıkarıcı — YouTube transkript sistemine benzer.
Birkan'ın paralı Medium üyeliği var; cookie auth ile paywalled makaleleri çeker.

**Dosyalar:**
- `scraper.py` — Cookie tabanlı article extractor (BeautifulSoup + markdownify)
- `main.py` — FastAPI: POST /extract, GET /health
- `launcher.py` — Masaüstü başlatıcı (port 8004)
- `build.sh` — PyInstaller

**Birkan yapacak:**
```
Chrome → F12 → Application → Cookies → medium.com
→ "sid" ve "uid" değerlerini kopyala → .env'e yapıştır:
MEDIUM_SID=...
MEDIUM_UID=...
```

**Response formatı:**
```json
{
  "url": "...", "title": "...", "author": "...",
  "published_at": "...", "reading_time": 5,
  "tags": [...], "content": "markdown...",
  "word_count": 1200, "paywalled": true
}
```

---

### Proje D — Borsa / Trading Otomasyonu
**Araç:** n8n workflow'ları (`/root/daily_strategy_v2.json`)
**Durum:** Workflow yapısı mevcut, veri kaynakları bağlı değil.
**Amaç:** Sabah 07:00 cron ile piyasa verisi → AI analiz → strateji raporu → Telegram

**TRADE BİBLE — TEK KAYNAK:**
`/root/trading-system/STRATEJI.md`
Trade kararı vermeden önce, yatırım değerlendirirken veya strateji tartışırken BURAYA BAK.
Tüm öğrenilen teknikler, kurallar ve hatırlatıcılar bu dosyada. Başka yere yazma.

---

### Proje O — Orchester ✅ TAM ÇALIŞIYOR (2026-05-19 v0.2)
**Repo:** `github.com/bbbirkan/2026-orchester`
**Dizin:** `/root/2026-orchester`
**Port:** 8006
**Servis:** `orchester.service` (systemd, boot'ta otomatik başlar)

**Amaç:** API key yok, sadece subscription. 3 farklı AI CLI soruyu sınıflandırıp akıllıca yönlendirir.

**İki sistem var:**
- `terminal_orchester.py` — 3 farklı CLI (Claude + OpenCode + Gemini), smart routing
- `orchester.py` — Claude-only, 3 persona (Analist/Eleştirmen/Pragmatist), tartışma formatı

**Smart mod akışı (varsayılan, v0.2):**
```
Telegram → Hermes → localhost:8006/v1 → classify(Claude)
         → basit: Claude tek (~10sn)
         → orta:  Claude + OpenCode paralel, Claude sentezler (~35sn)
         → zor:   3 CLI konsey, max 3 tur, Claude hakem (~60-90sn)
         → SSE stream → Telegram yanıtı
         → debates/TIMESTAMP.md olarak kaydedilir
```

**Test sonuçları (2026-05-19):**
| Soru | Seviye | Süre | Not |
|------|--------|------|-----|
| "nasılsın" | basit | 11sn | "İyiyim, teşekkürler!" |
| async vs threading | orta | 36sn | Tablo + karar ağacı |
| AI orkestrasyon mimarisi | zor | 54sn | Tur 1'de uzlaşma |

**Hermes entegrasyonu (~/.hermes/config.yaml) — kritik ayarlar:**
```yaml
model:
  default: terminal-orchester
  provider: custom:orchester
custom_providers:
  - name: orchester
    base_url: http://localhost:8006/v1
    api_mode: chat_completions
agent:
  max_turns: 1      # loop önleme — kritik
toolsets: []        # agentic loop önleme — kritik
platform_toolsets:
  cli: []           # agentic loop önleme — kritik
  telegram:
  - hermes-telegram
```

**Teknik notlar:**
- Hermes her zaman `stream: true` gönderir → SSE zorunlu
- Keepalive SSE (`: keepalive\n\n`) her 5sn → 90sn'lik işlemlerde bağlantıyı korur
- Loop tespiti: messages'da assistant varsa son yanıtı geri döndür
- `CLAUDE_CODE_BUBBLEWRAP=1` env zorunlu (root'ta çalıştırmak için)
- Gemini timeout: 180sn (120sn yetersiz kalıyordu)

**Servis yönetimi:**
```bash
systemctl status orchester.service
journalctl -u orchester -f
systemctl restart orchester.service
hermes -z "Test sorusu"   # tam chain testi
```

**Modeller (subscription, API key yok):**
- Claude Code CLI → Anthropic Pro subscription
- OpenCode CLI → OpenCode Zen (DeepSeek v4 Pro)
- Gemini CLI → Google subscription / free tier

---

### Proje DPP — Masaüstü Paketleme Roadmap
**Skill:** `~/.hermes/skills/birkan-desktop-packaging/SKILL.md`
**Araştırma:** `~/.claude/projects/-root/memory/reference_desktop_packaging_research.md`

**2 aşamalı plan:**
1. **Chrome Extension** (2-3 gün) — YouTube sayfasında channel-router API'yi çağırır; manifest v3
2. **Tauri 2.0 Desktop** (3-5 gün) — channel-router → PyInstaller binary → native app (~40MB RAM, ~3MB installer)

**Neden Tauri?** Electron'a göre ~5x daha az RAM, ~40x küçük installer.

---

### Proje YT Signal — AKTİF ✅ (2026-06-10)
**Dizin:** `/root/2026-yt-signal`
**Port:** 8007 (`yt-signal.service` — boot'ta otomatik başlar)
**Servis:** `yt-signal-indexer.timer` — saatte 100 video işler
**Amaç:** 2961 YouTube finans transkripti → MiniMax M3 entity extraction → piyasa sinyali

**LLM Wiki Katmanları:**
- `video_transcripts` (raw) → `video_signals` (sources) → `graph.json` (entities) → `/root/wiki/` (Markdown)
- Sorgulama: `curl localhost:8007/consensus`, `/query?ticker=NVDA`, `/anomaly`
- Wiki: `/root/wiki/entities/NVDA.md` vb. — Obsidian uyumlu

**Kanallar (21):** Graham Stephan, Meet Kevin, Bora Özkent, Paribu, Dividend Talks, Andrei Jikh vb.

---

## TEKNİK HEDEFLER (Araştırılmış, Uygulanmamış)

### 1. eBPF + Redis Streams + FastAPI Mimarisi
- eBPF LSM hook'ları ile sandbox izolasyonu (Docker yerine)
- Redis Streams ile ajan mesaj kuyruğu
- FastAPI üzerinden API katmanı
- **Durum:** Redis kurulu (v7.0.15), eBPF kernel destekli, FastAPI implementasyonu bekliyor

### 2. RecursiveMAS Protokolü
- Ajanlar arası metin yerine latent-space vektör iletişimi
- `arXiv:2604.25917` makalesine dayalı
- Ruflo swarm + RecursiveMAS hibrit protokol planı
- **Engel:** Fine-tune edilmiş model gerektirir, direkt API kullanımı yeterli değil

### 3. Hermes Güncelleme
- v0.13.0 → güncel (432 commit farkı)
- `hermes update` komutu ile yapılır

### 4. Flat-Rate Orkestrasyon
- Claude Pro + Claude Code headless (`claude -p --bare`) ile API maliyetini düşürme
- **Önemli uyarı:** Bireysel/geliştirici kullanımı meşru; çok-kullanıcılı backend olarak kullanmak Anthropic ToS ile çelişir

### 5. IPv6 Rotation (vproxy)
- `net.ipv6.ip_nonlocal_bind=1` ile geniş IPv6 bloğundan IP rotasyonu
- Rate limit bypass için
- **Engel:** Sunucuda /48 veya daha büyük IPv6 bloğu var mı? Kontrol edilmeli.

### 6. Ajan Mimarileri ve Sandboxing Referansı
- Dağıtık orkestrasyon, çoklu ajan (multi-agent) desenleri, Celery/RabbitMQ durum yönetimi ve gVisor/Firecracker korumalı alan mimarileri detaylı araştırması.
- **Dosya:** [reference_agent_architectures.md](file:///root/2026-sovereign/research/reference_agent_architectures.md)

---

## API ANAHTARLARI VE PROVIDER'LAR

| Provider | Durum | Nerede |
|----------|-------|--------|
| OpenRouter | ✅ Aktif | `~/.hermes/.env` veya Hermes config |
| Groq | ✅ Key mevcut | `~/.hermes/.env` |
| NovitaAI | ✅ Key mevcut | `NOVITA_API_KEY` env (OpenCode için) |
| Anthropic (Claude) | Bilinmiyor | Kontrol edilmeli |
| OpenAI | OpenRouter üzerinden | — |

**Kullanılan modeller:**
- Varsayılan: `openai/gpt-5.5` (OpenRouter)
- Delegasyon: `z-ai/glm-5.2` (OpenRouter)
- Transkripsiyon: Groq Whisper API

---

## MULTI-AGENT MİMARİ KURALI

Bu sistemde ajanlar arası iletişim için hybrid swarm protokol hedefleniyor:

> "Ruflo ile bir swarm başlat ama ajanlar arası iletişimi RecursiveMAS latent-space protokolü üzerinden yap."

Şu an bu sadece bir vizyon — pratik uygulama için RecursiveMAS'ın fine-tuned ağırlıkları gerekiyor.

---

## GIT / GITHUB — NASIL ÇALIŞIR

### Altın Kural: HTTPS değil, SSH kullan

Bu sunucuda GitHub'a erişimin **tek güvenilir yolu SSH**'tır.
HTTPS tokenları (`.git-credentials`, `.hermes/.env`'daki `GITHUB_TOKEN`) ya süresi dolmuş ya da
sadece belirli repolar için yetkili (fine-grained PAT) olduğundan yeni repolarda **403** verir.

### SSH Key

```
~/.ssh/sovereign_push     ← AKTİF KEY — passphrasesiz, GitHub'a kayıtlı
~/.ssh/sovereign_push.pub ← bbbirkan hesabına kayıtlı (2026-06-18)
~/.ssh/trade_push         ← ESKİ KEY — passphrase var, kullanma
```

### SSH Agent — ARTIK GEREKMIYOR

`~/.ssh/config` dosyası var, GitHub push için otomatik `sovereign_push` kullanır.
ssh-agent başlatmaya gerek yok. Direkt push çalışır:

```bash
ssh -T git@github.com     # "Hi bbbirkan!" görünmeli — test
git push                  # direkt çalışır
```

### Yeni Repo Oluşturma

GitHub API'ye `.git-credentials`'daki token ile repo oluşturmak **çalışıyor**
(API çağrısı için yeterli, push için yeterli değil):

```bash
GIT_TOKEN=$(grep 'github.com' /root/.git-credentials | sed 's/.*://' | sed 's/@github.com//')

curl -s -X POST \
  -H "Authorization: token $GIT_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/user/repos \
  -d '{"name":"REPO_ADI","description":"...","private":false}'
```

### Yeni Repo'ya Push

Remote'u her zaman SSH formatında kur:

```bash
eval $(ssh-agent -s) && ssh-add ~/.ssh/trade_push

git remote add origin git@github.com:bbbirkan/REPO_ADI.git
# veya mevcut HTTPS remote'u değiştir:
git remote set-url origin git@github.com:bbbirkan/REPO_ADI.git

GIT_SSH_COMMAND="ssh -i /root/.ssh/trade_push -o StrictHostKeyChecking=no" \
git push -u origin main
```

### Mevcut Repolar

| Repo | Remote | Durum |
|------|--------|-------|
| `2026-kermes` | SSH `git@github.com:bbbirkan/2026-kermes.git` | ✅ |
| `bilgi-ve-projeler` | HTTPS (credential store) | ✅ |
| `2026-hermes-trello-agent` | HTTPS → SSH'a taşınmalı | ⚠️ |
| `2026-hermes-mobile-app` | HTTPS → SSH'a taşınmalı | ⚠️ |
| `2026-medium-reader` | SSH | ✅ |
| `youtube-transcript-engine` | Kontrol edilmeli | — |

### gh CLI Durumu

`gh` CLI kimlik doğrulaması yapılmamış — `gh auth login` henüz çalıştırılmadı.
Kullanmak istersen önce `! gh auth login` yap (tarayıcı ile OAuth akışı).

---

## ÇALIŞIRKEN DİKKAT EDİLECEKLER

1. **Hermes config'i bozmama** — `/usr/local/lib/hermes-agent/` altındaki dosyaları dikkatlice düzenle
2. **`hermes-gateway.service` canlı** — değişiklik sonrası `systemctl restart hermes-gateway` gerekebilir
3. **OpenRouter kredi limiti** — `max_tokens: 8192` sabit, büyük output cap'leri hata üretiyor
4. **Bilgi-ve-projeler repo** — Tüm skills ve CLAUDE.md oraya push ediliyor (`bilgi-ve-projeler/`)
5. **Graphify** — Codebase değişikliğinden sonra `graphify update .` çalıştır
6. **yt-dlp PyInstaller'a gömme** — Her zaman sistem binary'sini kullan, runtime'da indir

---

## HIZLI BAŞLANGIÇ (Yeni Oturum)

```bash
# Sistem durumu
systemctl status hermes-gateway
ls /usr/local/lib/hermes-agent/

# Hermes güncelleme
cd /usr/local/lib/hermes-agent && hermes update

# OpenCode auth (2 provider mevcut: Zen + Go)
opencode auth list

# Redis durumu (v7.0.15, active)
systemctl status redis-server

# Aktif portlar
ss -tlnp

# Projeleri test et
cd /root/2026-medium-reader && uvicorn main:app --port 8004
cd /root/2026-hermes-trello-agent && uvicorn main:app --port 8005
```

---

## ÖNCEKİ KARAR VE SEÇIMLER

- **model.max_tokens: 8192** — 402 hatası (provider max token aşımı) nedeniyle sabitlendi
- **GLM-5.2 (Vekil Glim)** — Uzun-horizon kod + 1M context; GPT-5.5'i coding'de geçiyor, 1/6 fiyatına. Delegation + proje seviyesi görevler için kullan.
- **Compression aktif** — uzun konuşmalarda bağlam sıkıştırma (`threshold: 0.4`, `target_ratio: 0.15`)
- **`birkan-ai-video` skill kaldırılmalı** — `birkan-video-watch` ile çakışıyor, ikincisi kullanılacak
- **Mac path'leri Linux'a taşınmamış** — `birkan-video-production-kit` VPS'te tam çalışmıyor
- **Nexus-1 → YT Harvester** — isim değiştirildi (2026-05-19)
- **Tauri 2.0 tercih edildi** — Chrome Extension + Tauri masaüstü app roadmap belirlendi
- **yt-dlp PyInstaller'a gömülmez** — YouTube haftalık değişir, frozen binary bozulur

---

## SKILL İNDEKSİ — Otomatik Kontrol Kuralı

**Kural:** Aşağıdaki konular geldiğinde, karşısındaki skill dosyasını oku. Birkan'ın hatırlatmasını bekleme.

```bash
cat ~/.hermes/skills/SKILL_ADI/SKILL.md
```

| Konu / Tetikleyici | Skill Dosyası |
|--------------------|--------------|
| CLI araçları, model fiyatları, deep search, OpenCode/Claude Code/Agy karşılaştırma | `sovereign-cli-ecosystem` |
| Veri görselleştirme, dashboard, grafik, infografik, Xenographics, L-sistemi | `data-product-designer` |
| YouTube analiz, video içerik, transkript, video izle/dinle/çek | `birkan-video-pipeline` |
| Video üretim, prompt, script yazımı | `birkan-video-production-kit` |
| SEO, içerik stratejisi | `birkan-ai-seo`, `birkan-seo-pipeline` |
| Derin araştırma, kaynak tarama | `birkan-deep-research`, `birkan-autoresearch` |
| Multi-agent, ajan koordinasyonu, swarm | `birkan-agent-teams__task-coordination-strategies`, `recursive-mas` |
| Masaüstü uygulama, PyInstaller, Tauri, Chrome Extension | `birkan-desktop-packaging` |
| MCP server kurulum, yapılandırma | `birkan-mcp-servers-guide`, `birkan-mcp-catalog` |
| Claude paralel kullanım, headless | `birkan-claude-parallel` |
| Model seçimi, provider karşılaştırma | `birkan-model-secim`, `birkan-ai-model-scout` |
| API tasarımı, backend | `birkan-backend-development__api-design-principles` |
| Workflow orkestrasyon | `birkan-backend-development__workflow-orchestration-patterns` |
| Copywriting, metin yazarlığı | `birkan-copywriting`, `birkan-humanizer` |
| Trello agent, görev yönetimi | `2026-hermes-trello-agent` |
| Medium scraping | `2026-medium-reader` |
| YouTube sinyal, transkript sorgu, piyasa konsensüs, ticker analiz | `2026-yt-signal` |
| Yeni skill oluşturma | `birkan-anthropic-skill-creator`, `auto-repo-to-skill` |
| Graphify, knowledge graph | `birkan-graphify-skill` |
| Obsidian vault kurulumu, VPS Obsidian Sync, headless | `hermes-obsidian-setup` |
| Obsidian vault düzenleme, ikinci beyin, notları organize et | `obsidian-vault-curator` |
| Telegram → Obsidian, sesli mesaj/link/dump vault'a aktar | `telegram-to-obsidian-capture` |
| Obsidian sync sorunu, notlar görünmüyor, sync test | `obsidian-sync-doctor` |
| Subagent, delegasyon | `birkan-subagents-catalog` |
| Kermes, terminal orchester | `birkan-terminal-orchester` |
| Loop engineering, ajan döngüsü, /ultracode, /goal, /loop, deterministik loop, kaynak değerlendirme | `sovereign-loop-engineering` |
| Skill senkronizasyonu, sistem bağlamı güncelleme | `birkan-skill-sync` |
| Chrome eklenti geliştirme, MV3, manifest v3, CWS SEO, extension monetizasyon | `birkan-chrome-extension-mv3` |

**Yeni skill eklendiğinde bu tabloyu da güncelle.**

---

*Bu dosya `/root/CLAUDE.md` konumunda — sunucuya bağlanan tüm AI asistanları buradan başlamalı.*
*Senkronizasyon için: `bash ~/.hermes/skills/birkan-skill-sync/scripts/sync.sh`*
