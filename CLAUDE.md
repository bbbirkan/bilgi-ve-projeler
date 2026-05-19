# SISTEM BAĞLAM DOSYASI
> Bu dosya, bu sunucuya bağlanan her yapay zeka asistanının (Claude Code, Hermes, OpenCode vb.)
> okuyarak hızlıca bağlamı kavraması için yazılmıştır.
> Son güncelleme: 2026-05-19

> **YAPILACAKLAR:** `/root/YAPILACAKLAR.md` — Birkan'ın tüm görev listesi burada.
> Her yeni görev, karar veya tamamlanan iş oraya kaydedilmeli.

---

## KİM OLDUĞUMUZ

**Kullanıcı:** Birkan Kalyon
- GitHub: `bbbirkan`
- E-posta: `8birkan@gmail.com`
- Rol: Yapay zeka sistemleri kurucusu / otomasyon mimarı

**Sunucu:** Contabo VDS
- Hostname: `vmi2701691`
- OS: Ubuntu 24.04.3 LTS
- RAM: 7.8 GB (3.5 GB kullanımda)
- Disk: 145 GB (43 GB dolu, 102 GB boş)
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
AI Orkestratör (GPT-5.5 varsayılan, GLM-4.7 delegasyon)
        ↓
OpenCode / Claude Code (headless kodlama)
        ↓
GitHub / Trello / YouTube / Borsa / Medium API'ları
```

---

## KURULU SİSTEMLER VE DURUMU

### 1. Hermes Agent — AKTİF ✅
- **Konum:** `/usr/local/lib/hermes-agent`
- **Versiyon:** v0.13.0 (432 commit geride — `hermes update` bekliyor)
- **Servis:** `hermes-gateway.service` aktif ve çalışıyor
- **Config:** `~/.hermes/config.yaml` veya proje içindeki `cli-config.yaml`

**Mevcut model konfigürasyonu:**
```yaml
model.default: openai/gpt-5.5
model.provider: openrouter
delegation.model: z-ai/glm-4.7
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

### 2. OpenCode — KURULU, AUTH YOK ⚠️
- **Versiyon:** 1.14.51
- **Konum:** `/usr/bin/opencode`
- **Durum:** NovitaAI API key var (`NOVITA_API_KEY` env), ama hiç oturum yok
- **Yapılacak:** `opencode auth add` ile provider eklenmeli
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

### 5. Redis — KURULU DEĞİL ❌
- Plan: `apt install redis-server`
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

---

### Proje O — Orchester ✅ TAM ÇALIŞIYOR (2026-05-19)
**Repo:** `github.com/bbbirkan/2026-orchester`
**Dizin:** `/root/2026-orchester`
**Port:** 8006
**Servis:** `orchester.service` (systemd, boot'ta otomatik başlar)

**Amaç:** API key yok, sadece subscription. 3 CLI (Claude Code + Google Gemini + OpenCode/DeepSeek)
aynı soruyu paralel/chain/sequential modda işler, sentez üretir.

**Gerçek akış (Terminal Orchester — subscription-only):**
```
Telegram → Hermes Gateway → localhost:8006/v1 → terminal_orchester.py
         → [Claude CLI + OpenCode CLI paralel]
         → Gemini CLI sentezi
         → SSE stream → Telegram yanıtı
         → debates/TIMESTAMP.md olarak kaydedilir
```

**Hermes entegrasyonu (~/.hermes/config.yaml):**
```yaml
model:
  default: terminal-orchester
  provider: custom:orchester
custom_providers:
  - name: orchester
    base_url: http://localhost:8006/v1
    api_mode: chat_completions
agent:
  max_turns: 1          # loop önleme — kritik
toolsets: []            # hermes-cli toolset'i kapat — kritik
platform_toolsets:
  cli: []               # agentic loop önleme — kritik
  telegram:
  - hermes-telegram
```

**Teknik detaylar (öğrenildi):**
- Hermes tüm custom provider isteklerinde `stream: true` gönderir → SSE zorunlu
- Orchestration 45-90sn sürer → keepalive SSE (`": keepalive\n\n"`) her 5sn gönderilmeli
- Loop tespiti: messages içinde assistant varsa son yanıtı geri döndür, yeniden çalıştırma
- `CLAUDE_CODE_BUBBLEWRAP=1` env gerekli (root olarak çalıştırmak için)
- Gemini timeout: 180sn (120sn yetersizdi)

**Servis yönetimi:**
```bash
systemctl status orchester.service
journalctl -u orchester -f
systemctl restart orchester.service
```

**CLI test:**
```bash
hermes -z "Test sorusu"   # tam chain'i test eder, ~60-90sn sürer
curl http://localhost:8006/health
```

**Bilinen sorun:** Basit selamlamalar ("nasılsın") için de 3 CLI çalışır — orantısız.
Çözüm: routing katmanı eklenecek (kısa mesaj → sadece Claude).

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

## TEKNİK HEDEFLER (Araştırılmış, Uygulanmamış)

### 1. eBPF + Redis Streams + FastAPI Mimarisi
- eBPF LSM hook'ları ile sandbox izolasyonu (Docker yerine)
- Redis Streams ile ajan mesaj kuyruğu
- FastAPI üzerinden API katmanı
- **Engel:** Redis kurulu değil

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
- Delegasyon: `z-ai/glm-4.7` (OpenRouter)
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
~/.ssh/trade_push        ← GitHub'a bağlanan tek yetkili key
~/.ssh/trade_push.pub    ← bbbirkan hesabına kayıtlı
```

### Her Oturumda SSH Agent'ı Başlat

SSH agent oturum başında ölüyor. Git push yapmadan önce mutlaka çalıştır:

```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/trade_push
ssh -T git@github.com     # "Hi bbbirkan!" görünmeli
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

# Hermes güncelleme (bekliyor)
cd /usr/local/lib/hermes-agent && hermes update

# OpenCode auth (bekliyor)
opencode auth add

# Redis kurulum (bekliyor)
apt install -y redis-server && systemctl enable --now redis-server

# Aktif portlar
ss -tlnp

# Projeleri test et
cd /root/2026-medium-reader && uvicorn main:app --port 8004
cd /root/2026-hermes-trello-agent && uvicorn main:app --port 8005
```

---

## ÖNCEKİ KARAR VE SEÇIMLER

- **model.max_tokens: 8192** — 402 hatası (provider max token aşımı) nedeniyle sabitlendi
- **GLM-4.7 delegation için** — ekonomik ve yeterli: `reasoning_effort: low`, `max_spawn_depth: 1`
- **Compression aktif** — uzun konuşmalarda bağlam sıkıştırma (`threshold: 0.4`, `target_ratio: 0.15`)
- **`birkan-ai-video` skill kaldırılmalı** — `birkan-video-watch` ile çakışıyor, ikincisi kullanılacak
- **Mac path'leri Linux'a taşınmamış** — `birkan-video-production-kit` VPS'te tam çalışmıyor
- **Nexus-1 → YT Harvester** — isim değiştirildi (2026-05-19)
- **Tauri 2.0 tercih edildi** — Chrome Extension + Tauri masaüstü app roadmap belirlendi
- **yt-dlp PyInstaller'a gömülmez** — YouTube haftalık değişir, frozen binary bozulur

---

*Bu dosya `/root/CLAUDE.md` konumunda — sunucuya bağlanan tüm AI asistanları buradan başlamalı.*
