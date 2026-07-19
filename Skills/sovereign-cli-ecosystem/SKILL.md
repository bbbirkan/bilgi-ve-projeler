# Sovereign CLI Ekosistemi — Araç ve Fiyatlandırma Bilgisi
> Son güncelleme: 2026-06-11 (Raporlardan derlendi)

## MODEL FİYATLANDIRMASI (Haziran 2026)

### Anthropic Claude (API — kullandıkça öde)
| Model | Girdi (MTok) | Çıktı (MTok) | Önbellek Okuma |
|-------|-------------|-------------|----------------|
| Claude Opus 4.7 | $5 | $25 | $0.50 (-90%) |
| Claude Sonnet 4.6 | $3 | $15 | $0.30 (-90%) |
| Claude Haiku 4.5 | $1 | $5 | $0.10 (-90%) |

**Prompt Caching:** Statik bağlam öneki değişmezse %90 indirim. Claude Code bunu otomatik yapar.
**Risk:** Alt-ajan fan-out — bir ajan başka ajanlar türetince tüm repo her seferinde okunur, maliyet 10-500x artabilir.

### Sovereign Mevcut Abonelikler
- Claude Pro: $20/ay → Haiku + Sonnet + Opus erişimi (Claude Code CLI dahil)
- Antigravity/Agy: $20/ay → Gemini 3.1 Pro + Flash
- OpenCode Go: $10/ay → DeepSeek V4 Pro + MiniMax M3
- **Toplam: $50/ay**

---

## DERİN ARAMA (DEEP SEARCH) MİMARİSİ

### OpenCode Deep Search
```bash
# Aktif etme (kalıcı)
export OPENCODE_ENABLE_EXA=1

# Ücretsiz DuckDuckGo alternatifi
npm install -g opencode-web-deepsearch
```
- Exa API: 1000 sorgu = $15 (pahalı, dikkatli kullan)
- DuckDuckGo paketi: Ücretsiz, yinelemeli arama

### Agy CLI — Yerleşik Google Arama (En Güçlü Web Araması)
- Google Search "grounding" = doğrudan Google altyapısı
- OSINT ve gerçek zamanlı bilgi için en iyi araç
- Kota riski: AI Ultra planı 5 saat / 7 gün pencere sınırı
- **Sovereign'de kullan:** `agy --model "Gemini 3.1 Pro (High)" --print`

### Claude Code — Prompt Caching Avantajı
- Bağlam öneki statik kalırsa %90 ucuzluk
- `/clear` komutu önbelleği sıfırlar
- Alt-ajan döngüsü = maliyet bombası, dikkat

### Weizhena 2-Aşamalı Araştırma Çerçevesi
```
Faz 1 (research): YAML taslak oluştur → insan onayı
Faz 2 (research-deep): Paralel web ajanları → JSON çıktı
```
- OpenCode için: `export OPENCODE_ENABLE_EXA=1` zorunlu
- Claude Code için: `~/.claude/skills/` dizinine kopyala

---

## CLI ARAÇ KARŞILAŞTIRMASI

### Kodlama Ajanları
| Araç | Fiyat | Token Verimliliği | En İyi Kullanım |
|------|-------|-------------------|-----------------|
| Claude Code | $20-200/ay | Prompt caching ile çok iyi | Mimari kararlar, büyük refaktör |
| Aider | Sadece API | 4.2x Claude Code'dan verimli | Bağımsız geliştirici, BYOK |
| OpenCode | Subscription | Değişken | Çoklu model yönlendirme |
| Cline | Ücretsiz + API | BYOK, esnek | MCP entegrasyonu |

### Terminal Emülatörler
| Terminal | Platform | Özellik |
|----------|----------|---------|
| Warp | Mac/Linux/Win | AI built-in, paralel ajanlar, $0-20/ay |
| Ghostty | Mac/Linux | GPU hızlandırma, minimal |
| WezTerm | Tüm platformlar | Lua config, multiplexer dahili |
| Alacritty | Tüm platformlar | Maksimum hız, sıfır özellik |

---

## SOVEREIGN İÇİN AKSİYONLAR

### Hemen Yapılabilir (Ücretsiz)
1. ✅ `OPENCODE_ENABLE_EXA=1` aktif edildi
2. ✅ `opencode-web-deepsearch` kuruldu (DuckDuckGo, ücretsiz)
3. Aider token verimliliği → büyük kod görevleri için dene
4. `codedash` kur → tüm CLI oturumlarını izle

### İzleme Araçları (Değerlendirilebilir)
```bash
# Codedash — tüm CLI loglarını birleştir
npm i -g codbash-app
# OpenCode <-> Claude Code config sync
npm install -g opencode-ccs-sync
```

### Kota Riski Yönetimi
- Agy: 5 saatlik pencerede yoğun kullanımdan kaçın
- OpenCode: Exa yerine DuckDuckGo paketi kullan (ücretsiz)
- Claude Code: `/clear` komutu önbelleği sıfırlar, dikkat

---

## ENTEGRASYON: agy-claude-plugin
Claude Code, Agy'yi headless alt-ajan olarak çağırabilir:
- Claude Opus = üst düzey orkestrasyon
- Agy (Gemini Flash) = hızlı web kazıma + Google Search
- Sonuç → Claude'un bağlamına JSON olarak döner

Bu Sovereign'in mevcut mimarisine benzer ama tek CLI içinde.

### OTOMATİK Öğrenim [2026-06-27]
> Opus 4.8 ve Fable 5'in kendi prompting guide'ları var — model güncellendikçe skill içindeki talimatlar eskiyor, periyodik güncelleme şart.
>
> sovereign-cli-ecosystem skill'ine 'model prompting drift' uyarısı ekle: 3 ayda bir skill'lerin prompt'larını yeni model önerilerine göre gözden geçir.

### OTOMATİK Öğrenim [2026-06-27]
> Modeller her versiyonda 'ortalama/dağılıma yakınsama' (averaging) problemi yaşıyor — front-end, kod üretimi ve diğer çıktılarda generic/tembel sonuç üretiyor
>
> sovereign-cli-ecosystem skill'ine 'harness tasarımı' alt başlığı ekle: her yeni modelde skill/prompt'ları yeniden değerlendirme protokolü

### OTOMATİK Öğrenim [2026-06-27]
> Agent'ların engellenmesi (rate limit, anti-bot) modern web'in temel sorunu; Apify proxy/rotating residential IP çözümü getiriyor.
>
> sovereign-cli-ecosystem skill'ine Apify MCP provider'ı ekle, OpenRouter/model routing tablosunda 'engellenen site' kategorisi için varsayılan engine olarak işaretle.

### OTOMATİK Öğrenim [2026-06-27]
> Anthropic'in model davranış değişiklikleri (fallback yerine silent throttle) ToS/openness açısından tartışmalı — provider seçiminde 'transparency of behavior modification' bir kriter olmalı.
>
> sovereign-cli-ecosystem skill'inin model değerlendirme matrisine 'görünür davranış modifikasyonu' ve 'konu bazlı throttle' sütunları ekle.

### OTOMATİK Öğrenim [2026-06-27]
> Modern AI editörler (Claude Code, Codex, Cursor) için 'agent skills' standardı var: herhangi bir CLI aracı skill dosyası yazılarak slash komutu haline getirilebiliyor — bu Hermes'in toolset sistemiyle doğrudan eşleşiyor.
>
> sovereign-cli-ecosystem skill'ine 'agent-skill standardı' maddesi ekle: kendi geliştirdiğimiz araçları (yt-signal, channel-router, orchester) için SKILL.md yazıp Claude Code/Cursor/Codex'e slash komutu olarak bağlama desenini dokümante et, böylece Hermes dışı editörlerde de aynı yetenek kullanılabilsin.

### OTOMATİK Öğrenim [2026-06-27]
> OpenRouter Node.js paketi olarak local'a kurulup dashboard + local API olarak çalışıyor (auto-start, enable auto start, 123456 default password).
>
> Sistemde zaten OpenRouter kullanılıyor (/root/CLAUDE.md'de Aktif Provider); bu pratik bilgiyi birkan-sovereign-cli-ecosystem skill'ine 'OpenRouter'ı local proxy olarak kullanma' notu olarak ekleyebiliriz — Birkan'ın VPS'inde /usr/local altında çalışan bir orkestrasyon katmanı olarak değerlendirilebilir.

### OTOMATİK Öğrenim [2026-06-27]
> ComfyUI workflow dosyaları (JSON) versiyonlanabilir ve paylaşılabilir; 'load diffusion model → load clip → clip text encode (prompt/negative) → K Sampler' minimal node zinciri standartlaştırılabilir.
>
> sovereign-cli-ecosystem skill'ine ComfyUI CLI bölümü ekle: --headless mod, --workflow-json ile batch üretim, --output-dir ile otomatik kayıt pattern'i dokümante et.
