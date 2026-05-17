---
name: birkan-system-context
description: |
  Birkan'ın Contabo VDS sunucusunun tam sistem bağlamı. Bu sunucuda çalışan tüm AI asistanların
  (Claude Code, Hermes, OpenCode) bilmesi gereken altyapı, aktif projeler, API anahtarları ve
  çalışma kuralları. Şu durumlarda kullan:
  - "sistemi anlat", "ne var sunucuda", "neler kurulu"
  - Proje durumu sorgulandığında
  - GitHub push/commit yapılacağında (SSH kuralları)
  - Yeni araç veya servis eklenecekken
  - Herhangi bir deploy, servis restart, config değişikliği öncesi
  KAYNAK DOSYA: /root/CLAUDE.md (Claude Code canonical) + bilgi-ve-projeler/SUNUCU_CONTEXT.md
  Son güncelleme: 2026-05-17
---

# Sistem Bağlam — Birkan Kalyon / vmi2701691

## KİM

**Kullanıcı:** Birkan Kalyon (`bbbirkan`, `8birkan@gmail.com`)
Rol: AI sistemleri kurucusu / otomasyon mimarı. Kısa ve direkt Türkçe iletişim ister.
Yıkıcı operasyonlar dışında onay istemeden otonom çalış.

**Sunucu:** Contabo VDS — Ubuntu 24.04.3, RAM 7.8GB, Disk 145GB

---

## EKOSİSTEM MİMARİSİ

```
Kullanıcı (Telegram / Discord / WhatsApp)
        ↓
Hermes Agent Gateway  [hermes-gateway.service — AKTİF]
        ↓
AI Orkestratör  [GPT-5.5 varsayılan | GLM-4.7 delegasyon]
        ↓
OpenCode / Claude Code  [headless kodlama]
        ↓
GitHub / Trello / YouTube / Borsa API'ları
```

---

## KURULU SİSTEMLER

| Sistem | Durum | Konum / Not |
|--------|-------|-------------|
| Hermes Agent | ✅ AKTİF | `/usr/local/lib/hermes-agent` — v0.13.0 |
| OpenCode | ⚠️ AUTH YOK | `/usr/bin/opencode` — `opencode auth add` yapılmalı |
| Docker | ✅ AKTİF | v28.5.1 — portlar: 80,443,8000,8080,6001,6002 |
| eBPF | ✅ MEVCUT | bpftool v7.4.0, LSM hook destekli |
| Redis | ❌ YOK | `apt install redis-server` ile kurulacak |
| Python | ✅ | 3.12.3 sistem / 3.11.15 venv |
| Node.js | ✅ | 22.22.2 |
| yt-dlp | ✅ | 2026.03.17 |
| ffmpeg | ✅ | 6.1.1 |
| Whisper | ❌ | Groq API üzerinden kullanılıyor |

**Hermes model config:**
```yaml
model.default: openai/gpt-5.5        # OpenRouter
delegation.model: z-ai/glm-4.7       # OpenRouter
delegation.max_iterations: 50
compression.enabled: true
compression.threshold: 0.4
```

---

## AKTİF PROJELER

| Proje | Repo | Durum |
|-------|------|-------|
| Trello + Hermes Haftalık Ajan | `bbbirkan/2026-hermes-trello-agent` | Planlama aşaması |
| Hermes Mobil App | `bbbirkan/2026-hermes-mobile-app` | Scaffold hazır |
| YouTube Otomasyon | — | Kısmen çalışıyor (Groq Whisper API) |
| Borsa/Trading | n8n workflow | Veri kaynakları bağlı değil |

---

## API PROVIDER'LAR

| Provider | Durum | Konum |
|----------|-------|-------|
| OpenRouter | ✅ | `~/.hermes/.env` |
| Groq | ✅ | `~/.hermes/.env` |
| NovitaAI | ✅ | `NOVITA_API_KEY` env |
| Anthropic | ? | Kontrol edilmeli |

---

## GIT / GITHUB KURALLARI

**ALTIN KURAL: HTTPS değil, SSH kullan.**

```bash
# Her oturumda önce çalıştır:
eval $(ssh-agent -s)
ssh-add ~/.ssh/trade_push
ssh -T git@github.com   # "Hi bbbirkan!" çıkmalı

# Push komutu:
GIT_SSH_COMMAND="ssh -i /root/.ssh/trade_push -o StrictHostKeyChecking=no" \
git push -u origin main
```

SSH key: `~/.ssh/trade_push` → `bbbirkan` hesabına kayıtlı
Remote format: `git@github.com:bbbirkan/REPO_ADI.git`

Yeni repo oluşturma için `.git-credentials`'daki token çalışıyor (sadece API, push için SSH).

---

## ÇALIŞMA KURALLARI

1. Hermes config bozma — `/usr/local/lib/hermes-agent/` dikkatli düzenle
2. Config değişikliği sonrası → `systemctl restart hermes-gateway`
3. `max_tokens: 8192` sabitle — provider limiti
4. Tüm skills → `bilgi-ve-projeler/Skills/` + GitHub push
5. Graphify güncellemesi → `graphify update .`
6. Commit imzası: `🤖 Hermes-AI-Assisted:` prefix

---

## SYNC NOTU

Bu dosya iki yerden senkronize edilir:
- **Canonical kaynak:** `/root/CLAUDE.md` (Claude Code okur)
- **Hermes skill:** `~/.hermes/skills/birkan-system-context/SKILL.md` (bu dosya)
- **GitHub yedek:** `bilgi-ve-projeler/Skills/birkan-system-context/SKILL.md`

Güncelleme olduğunda her üçünü birden güncelle.
