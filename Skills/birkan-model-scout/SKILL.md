---
name: model-scout
description: |
  AI model fiyat/performans karşılaştırması ve akıllı model seçimi.
  OpenRouter ve Novita AI fiyatlarını karşılaştırır, leaderboard'lardan en iyi
  modelleri bulur, göreve göre en uygun + ucuz modeli önerir.
  Ayrıca aylık Birkan model seçim kararını PDF olarak üretir.

  TRIGGER bu skill'i şu durumlarda çağır:
  - "hangi model daha iyi/ucuz", "model karşılaştır", "en iyi LLM hangisi"
  - "model seçimi", "aylık model", "benchmark", "fiyat/performans"
  - "OpenRouter vs Novita", "model değiştir", "daha ucuz model bul"
  - /model-scout, /best-model, /model-compare komutları
---

# Model Scout — Fiyat/Performans Yönlendirici

## Birkan'ın API Anahtarları

| Platform | Key |
|----------|-----|
| OpenRouter (Hermes) | `sk-or-v1-c010867...` (CLAUDE.md'de) |
| OpenRouter (Hermes2) | `sk-or-v1-050965...` (CLAUDE.md'de) |
| Novita AI | `sk_bv4O7Tp...` (CLAUDE.md'de) |

## Mevcut Model Seçimleri (2026-05)

### ÜST Tier (En İyi Kalite)
| # | Model | Benchmark | Fiyat (Input/Output) |
|---|-------|-----------|----------------------|
| 1 | GPT-5.5 | LiveBench %80.7 | $5/$20 per M |
| 2 | Claude Opus 4.7 | SWE-bench %75.6 | $15/$75 per M |
| 3 | DeepSeek V4 Pro | Açık ağırlıklı | $0.55/$2.75 per M |
| 4 | Gemini 2.5 Pro | Uzun context | $1.25/$10 per M |

### ALT Tier (Maliyet Odaklı)
| # | Model | Kullanım | Fiyat |
|---|-------|----------|-------|
| 1 | DeepSeek V4 Flash | Hızlı görevler | $0.14/$0.28 per M |
| 2 | GLM-4.7 | Türkçe güçlü | $0.10/$0.10 per M |
| 3 | Gemini 2.5 Flash | Google özellikleri | $0.15/$0.60 per M |
| 4 | Llama 3.3 70B | Açık kaynak | $0.10/$0.10 per M |

### Subscription CLIs (Sıfır API Maliyeti)
| CLI | Model | Aylık Maliyet |
|-----|-------|---------------|
| Claude Code | Claude Opus 4.x | $20 (Pro) |
| OpenCode | DeepSeek V4 Pro | ~$20 (Zen) |
| AGY | Gemini 2.5 Pro | $10 (Advanced) |

## Görev → Model Eşleşmesi

```
Genel sohbet, basit soru   → Orchester (ücretsiz)
Kod yazma, debug           → Orchester veya DeepSeek V4 Pro
Uzun doküman analizi       → Gemini 2.5 Pro ($)
Görüntü analizi            → Claude Opus 4.7 veya GPT-5.5 ($)
Yaratıcı yazı              → Claude Opus 4.7 ($)
Çok hızlı/basit            → GLM-4.7 veya DeepSeek Flash ($)
```

## Leaderboard Kaynakları

- LiveBench: livebench.ai
- LMSys Chatbot Arena: chat.lmsys.org
- SWE-bench (kod): swebench.com
- MMLU Pro: papers with code
- Birkan Aylık PDF: model-secim skill ile üretilir

## Aylık Model Seçim Süreci

Her ayın başında:
1. Bu skill ile güncel leaderboard verilerini çek
2. Fiyat/performans matrisini güncelle
3. PDF rapor üret (`zen-office-pdf` skill ile)
4. Hermes ve Kermes config'lerini güncelle

Her firmadan max **2 model** kuralı geçerlidir.
