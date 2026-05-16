# SISTEM BAĞLAM DOSYASI
> Bu dosya, bu sunucuya bağlanan her yapay zeka asistanının (Claude Code, Hermes, OpenCode vb.)
> okuyarak hızlıca bağlamı kavraması için yazılmıştır.
> Son güncelleme: 2026-05-16

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
GitHub / Trello / YouTube / Borsa API'ları
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
- `social-media/xurl` — X/Twitter otomasyon
- Graphify bilgi grafiği entegrasyonu

---

### 2. OpenCode — KURULU, AUTH YOK ⚠️
- **Versiyon:** 1.14.51
- **Konum:** `/usr/bin/opencode`
- **Durum:** NovitaAI API key var (`NOVITA_API_KEY` env), ama hiç oturum yok
- **Yapılacak:** `opencode auth` ile provider eklenmeli
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

### Proje A — Trello + Hermes Haftalık Ajan
**Repo:** `github.com/bbbirkan/2026-hermes-trello-agent`
**Amaç:** Trello board'ını haftalık tarayıp, seçili kartları AI ile ilerletmek ve Telegram'a rapor göndermek.
**Durum:** Planlama aşamasında, MVP henüz yazılmamış.
**Mimari:**
```
Trello List → weekly cron → Hermes Worker
→ Kart analizi → Subagent (kod/araştırma)
→ GitHub commit/PR + Trello yorum + Telegram rapor
```

### Proje B — Hermes Mobil App
**Repo:** `github.com/bbbirkan/2026-hermes-mobile-app`
**Durum:** Scaffold oluşturuldu, geliştirme başlamadı.

### Proje C — YouTube Otomasyon Sistemi
**Durum:** Kısmen çalışıyor.
**Eksikler:** Whisper kurulu değil, Mac path'leri Linux'a taşınmamış.
**Çalışan pipeline:** `yt-dlp → ffmpeg → Groq Whisper API → AI analizi`

### Proje D — Borsa / Trading Otomasyonu
**Araç:** n8n workflow'ları (`daily_strategy_v2.json`)
**Durum:** Workflow yapısı mevcut, veri kaynakları bağlı değil.
**Amaç:** Sabah 07:00 cron ile piyasa verisi → AI analiz → strateji raporu.

---

## TEKNİK HEDEFLER (Araştırılmış, Uygulanmamış)

Birkan aşağıdaki mimari geliştirmeleri uygulamayı planlıyor:

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

## ÇALIŞIRKEN DİKKAT EDİLECEKLER

1. **Hermes config'i bozmama** — `/usr/local/lib/hermes-agent/` altındaki dosyaları dikkatlice düzenle
2. **`hermes-gateway.service` canlı** — değişiklik sonrası `systemctl restart hermes-gateway` gerekebilir
3. **OpenRouter kredi limiti** — `max_tokens: 8192` sabit, büyük output cap'leri hata üretiyor
4. **Bilgi-ve-projeler repo** — Tüm skills ve CLAUDE.md oraya push ediliyor (`bilgi-ve-projeler/`)
5. **Graphify** — Codebase değişikliğinden sonra `graphify update .` çalıştır

---

## HIZLI BAŞLANGIÇ (Yeni Oturum)

```bash
# Sistem durumu
systemctl status hermes-gateway
ls /usr/local/lib/hermes-agent/

# Hermes güncelleme (bekliyor)
cd /usr/local/lib/hermes-agent && hermes update

# OpenCode auth
opencode auth add

# Redis kurulum
apt install -y redis-server && systemctl enable --now redis-server

# Aktif portlar
ss -tlnp

# Proje repo'ları
ls /root/2026-project-repos/
```

---

## ÖNCEKİ KARAR VE SEÇIMLER

- **model.max_tokens: 8192** — 402 hatası (provider max token aşımı) nedeniyle sabitlendi
- **GLM-4.7 delegation için** — ekonomik ve yeterli: `reasoning_effort: low`, `max_spawn_depth: 1`
- **Compression aktif** — uzun konuşmalarda bağlam sıkıştırma (`threshold: 0.4`, `target_ratio: 0.15`)
- **`birkan-ai-video` skill kaldırılmalı** — `birkan-video-watch` ile çakışıyor, ikincisi kullanılacak
- **Mac path'leri Linux'a taşınmamış** — `birkan-video-production-kit` VPS'te tam çalışmıyor

---

*Bu dosya `/root/CLAUDE.md` konumunda — sunucuya bağlanan tüm AI asistanları buradan başlamalı.*
