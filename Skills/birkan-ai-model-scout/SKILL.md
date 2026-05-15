---
name: ai-model-scout
description: |
  AI model fiyat/performans karşılaştırması ve akıllı model yönlendirme skill'i.
  OpenRouter ve Novita AI fiyatlarını karşılaştırır, leaderboard'lardan en iyi modelleri bulur,
  göreve göre en uygun + ucuz modeli önerir veya otomatik seçer.

  Bu skill'i şu durumlarda kullan:
  - "hangi model daha iyi/ucuz", "model karşılaştır", "en iyi LLM hangisi"
  - "OpenRouter vs Novita", "model fiyatları", "leaderboard sıralaması"
  - "model değiştir", "daha ucuz model bul", "fiyat/performans analizi"
  - /model-scout, /best-model, /model-compare komutları
---

# 🔭 AI Model Scout — Fiyat/Performans Yönlendirici

Birkan'ın kullandığı iki platform ve leaderboard kaynaklarına göre en iyi modeli bulan sistem.

---

## 🔑 API Anahtarları (Sistemde Kayıtlı)

| Platform | Amaç | Key (env'de) |
|----------|------|--------------|
| **OpenRouter** (Hermes) | Hermes'in ana API'si | `OPENROUTER_API_KEY` |
| **OpenRouter** (genel) | Yedek/genel kullanım | sk-or-v1-c010867... |
| **Novita AI** | Ucuz alternatif + görsel/video | `NOVITA_API_KEY` |

---

## 📊 Fiyat Karşılaştırması: OpenRouter vs Novita AI

### 🤖 LLM Modelleri

| Model | OpenRouter Input | OpenRouter Output | Novita Input | Novita Output | Kazan |
|-------|-----------------|-------------------|--------------|---------------|-------|
| **DeepSeek V4 Flash** | $0.14/M | $0.28/M | $0.14/M | $0.28/M | 🟰 Eşit |
| **MiMo-V2-Flash** | $0.10/M | $0.30/M | $0.10/M | $0.30/M | 🟰 Eşit |
| **Kimi K2.6** | $0.95/M | $4.00/M | $0.95/M | $4.00/M | 🟰 Eşit |
| **Qwen3.5 35B** | $0.25/M | $2.00/M | $0.25/M | $2.00/M | 🟰 Eşit |
| **Llama 3.3 70B** | $0.10/M | $0.32/M | $0.135/M | $0.40/M | 🟢 OpenRouter |
| **GLM-4.7 Flash** | $0.07/M | $0.40/M | $0.07/M | $0.40/M | 🟰 Eşit |
| **Llama 3.1 8B** | $0.04/M | $0.04/M | $0.02/M | $0.05/M | 🟢 Novita |

### 🎨 Görsel/Video (Sadece Novita AI)
| Servis | Fiyat |
|--------|-------|
| Image Generation (512x512) | $0.001/image |
| Seedance 1.5 Video (720p/5s) | ~$0.065/video |
| Remove Background | $0.017/image |
| Flux.1 Kontext Dev | $0.0225/image |

**Sonuç:** LLM için fiyatlar neredeyse aynı. Novita'nın avantajı: **Görsel + Video API** var, OpenRouter yok.

---

## 🏆 Leaderboard Kaynakları (En İyi Modelleri Bulmak İçin)

Hermes bu siteleri tarayarak güncel model sıralamalarını kontrol edebilir:

| Site | Ne Ölçüyor | URL |
|------|-----------|-----|
| **LMSYS Chatbot Arena** | Genel zeka, chat kalitesi (ELO) | https://lmarena.ai |
| **Artificial Analysis** | Fiyat/performans, hız, zeka endeksi | https://artificialanalysis.ai |
| **Vals.ai Vibe-Code** | Kod yazma kalitesi | https://www.vals.ai/benchmarks/vibe-code |
| **SuperGPQA** | Bilimsel muhakeme | https://supergpqa.github.io |
| **Arena AI Leaderboard** | Kapsamlı benchmark | https://arena.ai/leaderboard/text |

### Leaderboard'dan Model Araştırma Komutu
```bash
# Artificial Analysis'ten güncel sıralama çek
curl -s https://artificialanalysis.ai/api/models 2>/dev/null | head -100

# OpenRouter'dan mevcut modelleri listele
curl -s -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  https://openrouter.ai/api/v1/models | python3 -c "
import sys,json
models = json.load(sys.stdin)['data']
for m in sorted(models, key=lambda x: float(x.get('pricing',{}).get('prompt',999))):
    inp = float(m.get('pricing',{}).get('prompt',0))*1_000_000
    out = float(m.get('pricing',{}).get('completion',0))*1_000_000
    ctx = m.get('context_length',0)
    if inp > 0:
        print(f\"{m['id']:<60} \${inp:.3f}/\${out:.3f}  {ctx:>10,} ctx\")
" 2>/dev/null | head -30
```

---

## 🎯 Görev → Model Yönlendirme Stratejisi

```
Kullanıcı sorusu/görevi
         ↓
    [KATEGORI TESPİT]
         ↓
┌─────────────────────────────────────────────┐
│ Basit sohbet / kısa cevap                   │
│   → MiMo-V2-Flash (Novita/OR) $0.10/M       │
├─────────────────────────────────────────────┤
│ Trade analizi / araştırma                   │
│   → DeepSeek V4 Flash $0.14/M               │
├─────────────────────────────────────────────┤
│ Derin analiz / karmaşık akıl yürütme        │
│   → Kimi K2.6 $0.95/M                       │
├─────────────────────────────────────────────┤
│ Kod yazma / agentic görev                   │
│   → DeepSeek V4 Pro $1.74/M                 │
├─────────────────────────────────────────────┤
│ Görsel oluşturma (logo, banner vb.)         │
│   → Novita AI Flux/Seedream $0.02-0.03      │
├─────────────────────────────────────────────┤
│ Video oluşturma                             │
│   → Novita AI Seedance/Kling $0.07+/video   │
├─────────────────────────────────────────────┤
│ Kritik karar / en kaliteli cevap            │
│   → Claude Sonnet 4.6 (OpenRouter) $3/M     │
└─────────────────────────────────────────────┘
```

---

## 🔄 Model Değiştirme Komutları (Hermes için)

```bash
# Hermes modelini değiştir (sunucuda)
ssh root@207.180.204.66

# Config dosyasını düzenle
nano /root/.hermes/config.yaml
# default: "deepseek/deepseek-v4-flash"  ← burası

# Restart et
hermes gateway restart
```

### Hızlı Geçiş Komutları
```bash
# Ucuz+Hızlı (günlük)
sed -i 's|default: ".*"|default: "deepseek/deepseek-v4-flash"|' /root/.hermes/config.yaml

# Orta seviye (analiz)
sed -i 's|default: ".*"|default: "moonshotai/kimi-k2.6"|' /root/.hermes/config.yaml

# En kaliteli (kritik)
sed -i 's|default: ".*"|default: "anthropic/claude-sonnet-4-6"|' /root/.hermes/config.yaml

hermes gateway restart
```

---

## 💰 Novita AI Kullanımı (Görsel/Video İşler)

```python
import requests

NOVITA_KEY = "sk_wwJyuVBiKjWZXz9waJC5XBFzPyX6vHcqEnvKYBZPNcU"

# Görsel oluştur
response = requests.post(
    "https://api.novita.ai/v3/async/txt2img",
    headers={"Authorization": f"Bearer {NOVITA_KEY}"},
    json={
        "model_name": "dreamshaper_8_93211.safetensors",
        "prompt": "professional logo design",
        "width": 512,
        "height": 512,
        "steps": 20
    }
)
task_id = response.json()["task_id"]
# → $0.001/görsel
```

---

## 📈 Güncel En İyi Modeller (Mayıs 2026)

### 🏆 LMSYS Chatbot Arena — Genel Zeka (ELO) + Fiyat
> Kaynak: https://lmarena.ai (güncel: 15 saat önce güncellendi)

| Sıra | Model | ELO | Input | Output | Context | Değerlendirme |
|------|-------|-----|-------|--------|---------|---------------|
| 1 | **Claude Opus 4.6 Thinking** | 1502 | $5.00 | $25.00 | 1M | 🏆 En iyi ELO |
| 2 | **Claude Opus 4.7 Thinking** | 1500 | $5.00 | $25.00 | 1M | 🏆 En iyi ELO |
| 3 | **Claude Opus 4.6** | 1498 | $5.00 | $25.00 | 1M | Premium |
| 4 | **Claude Opus 4.7** | 1492 | $5.00 | $25.00 | 1M | Premium |
| 5 | **Meta muse-spark** | 1490 | ? | ? | ? | Yeni model |
| 6 | **Gemini 3.1 Pro Preview** | 1489 | $2.00 | $12.00 | 1M | İyi fiyat |
| 7 | **Gemini 3 Pro** | 1486 | ? | ? | ? | - |
| 8 | **GPT-5.5 High** | 1484 | $5.00 | $30.00 | 1M | Pahalı |
| 9 | **GPT-5.4 High** | 1479 | $2.50 | $15.00 | 1M | Orta fiyat |
| 10 | **Grok 4.20 Beta1** | 1479 | $1.25 | $2.50 | 2M | 2M context! |

---

## 💰 Fiyat/Performans — Güncel OpenRouter Tablosu

### 🟢 EN İYİ DEĞER (Düşük Fiyat + Yüksek Performans)

| Model | Input | Output | Context | Kullanım |
|-------|-------|--------|---------|----------|
| **deepseek/deepseek-v4-flash:free** | FREE | FREE | 1M | ⭐ Her şey için |
| **qwen/qwen3.5-flash-02-23** | $0.07 | $0.26 | 1M | ⭐ Gateway/cron |
| **qwen/qwen3.5-9b** | $0.04 | $0.15 | 262K | Basit işler |
| **mistralai/mistral-nemo** | $0.02 | $0.03 | 131K | En ucuz! |
| **meta-llama/llama-4-scout** | $0.08 | $0.30 | 327K | Açık kaynak |
| **minimax/minimax-m2.5** | $0.15 | $1.15 | 196K | Mini işler |
| **mistralai/ministral-3b-2512** | $0.10 | $0.10 | 131K | Ucuz denge |

### 🟡 ORTA SEVİYE (Fiyat/Performans Dengesi)

| Model | Input | Output | Context | Kullanım |
|-------|-------|--------|---------|----------|
| **qwen/qwen3-coder-30b-a3b-instruct** | $0.07 | $0.27 | 160K | Kod yazma |
| **deepseek/deepseek-v4-flash** | $0.13 | $0.25 | 1M | Araştırma |
| **mistralai/devstral-small** | $0.10 | $0.30 | 131K | Kod +Ucuz |
| **minimax/minimax-m2.7** | $0.28 | $1.20 | 196K | Mevcut (Telegram) |
| **google/gemini-3.1-flash-lite** | $0.25 | $1.50 | 1M | 1M + Ucuz |
| **qwen/qwen3-coder-flash** | $0.20 | $0.97 | 1M | Kod + 1M |

### 🔴 PREMIUM (Yüksek Kalite)

| Model | Input | Output | Context | Kullanım |
|-------|-------|--------|---------|----------|
| **deepseek/deepseek-v4-pro** | $0.43 | $0.87 | 1M | ⭐ Reasoning |
| **kimi-k2.6** | $0.73 | $3.49 | 262K | Tool use |
| **x-ai/grok-4.20** | $1.25 | $2.50 | 2M | 2M context |
| **qwen/qwen3-max** | $0.78 | $3.90 | 262K | Reasoning |
| **google/gemini-3.1-pro-preview** | $2.00 | $12.00 | 1M | Google ecosystem |
| **anthropic/claude-sonnet-4.6** | $3.00 | $15.00 | 1M | Premium sohbet |
| **anthropic/claude-opus-4.7** | $5.00 | $25.00 | 1M | En kaliteli |

---

## 📊 YAPAY ZEKA INTELLIGENCE INDEX (Artificial Analysis)
> Kaynak: https://artificialanalysis.ai — 10 benchmark ortalaması

**Zeka Sıralaması:**
1. GPT-5.5 (xhigh) — En yüksek
2. GPT-5.5 (high)
3. Claude Opus 4.7 (max)
4. Gemini 3.1 Pro Preview

**Hız Sıralaması (token/s):**
1. Mercury 2 → 905 t/s
2. Gemini 3.1 Flash-Lite → 338 t/s
3. Qwen3.5 2B → hızlı

**Context Liderleri:**
1. Llama 4 Scout → **10M context** 🔥
2. Grok 4.20 → 2M
3. Grok 4.1 Fast → 2M

---

## 🎯 GÖREV TABANLI MODEL ÖNERİLERİ

| Görev | Öneri | Sebep |
|-------|-------|-------|
| **Günlük sohbet** | `qwen3.5-flash-02-23` | $0.07, 1M ctx, hızlı |
| **Araştırma/analiz** | `deepseek-v4-flash:free` | ÜCRETSİZ, 1M, iyi kalite |
| **Kod yazma** | `qwen3-coder-flash` | $0.20, 1M, açık kaynak |
| **Yaratıcı yazarlık** | `kimi-k2.6` | $0.73, 262K, iyi kalite |
| **Trade bot** | `deepseek-v4-pro` | $0.43, 1M, reasoning |
| **Agentic görev** | `claude-sonnet-4.6` | $3.00, en dengeli |
| **Gateway/cron** | `qwen3.5-flash-02-23` | $0.07, 1M, çok ucuz |
| **Kritik karar** | `claude-opus-4.7` | $5.00, en yüksek ELO |

---

## 📈 BÜTÇE SENARYOLARI

| Senaryo | Model Seçimi | Aylık Maliyet (tahmini) |
|---------|--------------|------------------------|
| **Sıfır bütçe** | Her yerde `deepseek-v4-flash:free` | $0 |
| **Ekonomik** | Telegram: `qwen3.5-flash` / Cron: `mistral-nemo` | ~$3-5 |
| **Standart** | Telegram: `kimi-k2.6` / Cron: `qwen3-flash` | ~$10-15 |
| **Premium** | Telegram: `claude-sonnet` / Kod: `qwen3-coder` / Cron: `qwen3-flash` | ~$30-50 |

---

## 🔍 Hermes'in Model Araştırması Nasıl Yapar

Kullanıcı "en iyi modeli bul" veya "fiyat karşılaştır" dediğinde:

1. `artificialanalysis.ai` veya `openrouter.ai/rankings` sayfasını oku
2. Mevcut Hermes config modelini kontrol et
3. Daha iyi/ucuz seçenek varsa öner
4. Onay alınırsa `config.yaml`'ı güncelle ve gateway'i restart et

```bash
# Örnek: OpenRouter'daki en ucuz 10 modeli listele
curl -s -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  https://openrouter.ai/api/v1/models | python3 -c "
import sys,json
data = json.load(sys.stdin)['data']
models = [(float(m.get('pricing',{}).get('prompt',999)), m) for m in data]
for price, m in sorted(models)[:10]:
    print(f\"\${price*1e6:.3f}/M  {m['id']}\")
"
```

---

## 📁 Referanslar

- [OpenRouter Models](https://openrouter.ai/models)
- [Novita AI Pricing](https://novita.ai/pricing)
- [Artificial Analysis](https://artificialanalysis.ai)
- [LMSYS Arena](https://lmarena.ai)
- [Vals.ai Code Bench](https://www.vals.ai/benchmarks/vibe-code)
- [SuperGPQA](https://supergpqa.github.io)
- [Arena AI](https://arena.ai/leaderboard/text)

---

**Oluşturulma:** 2026-05-10  
**Sahibi:** Birkan (Anvilon LLC)  
**Hermes Konumu:** `/root/.hermes/skills/birkan-ai-model-scout/SKILL.md`
