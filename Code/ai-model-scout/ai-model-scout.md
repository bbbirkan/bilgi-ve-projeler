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

### Ucuz (<$0.30/M input)
| Rank | Model | Input | Güçlü Yan |
|------|-------|-------|-----------|
| 1 | **MiMo-V2-Flash** | $0.10 | Hız, agentic |
| 2 | **DeepSeek V4 Flash** | $0.14 | 1M context, tool use |
| 3 | **GLM-4.7 Flash** | $0.07 | Ucuz, 200k context |
| 4 | **Qwen3.5 35B** | $0.25 | 95% tool use |

### Orta ($0.30-2/M input)
| Rank | Model | Input | Güçlü Yan |
|------|-------|-------|-----------|
| 1 | **Kimi K2.6** | $0.95 | 96% tool use, 44% terminal |
| 2 | **MiMo-V2.5-Pro** | $1.00 | 94% tool use, 1M context |
| 3 | **DeepSeek V4 Pro** | $1.74 | 96% tool use, 46% terminal |

### Premium (>$2/M input)
| Rank | Model | Input | Güçlü Yan |
|------|-------|-------|-----------|
| 1 | **Claude Sonnet 4.6** | $3.00 | En dengeli, en kaliteli |
| 2 | **Gemini 3.1 Pro** | $2.00 | Google entegrasyonu |

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
