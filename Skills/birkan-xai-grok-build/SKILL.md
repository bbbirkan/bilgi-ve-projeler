---
name: birkan-xai-grok-build
description: xAI API ve Grok Build CLI kullanım kılavuzu — model seçimi, batch API, araçlar, ses/görsel API, headless dosya yazma pattern
metadata:
  type: reference
  tags: [xai, grok, build, api, llm, cli, batch, voice, image]
  created: 2026-07-06
---

# xAI / Grok Build Skill

## Grok Build CLI — Headless Dosya Yazma (KRİTİK)

`grok -p "..."` → sadece stdout'a yazar, dosyaya YAZMAz  
Dosya yazdırmak için:
```bash
grok --permission-mode bypassPermissions --always-approve --no-plan \
     --cwd /hedef/dizin --output-format plain \
     -p "görev açıklaması"
```

Versiyon: `grok` v0.2.87, path: `/root/.grok/bin/grok`  
Default model: `grok-composer-2.5-fast`  
Alternatif: `--model grok-build` (file-writing optimize)

## xAI API — Temel

```
Base URL: https://api.x.ai/v1
Auth:     XAI_API_KEY env var (Bearer token)
Compat:   OpenAI SDK ile çalışır — sadece base_url değiştir
```

## Model Hiyerarşisi ve Fiyatlandırma

| Model | Input (1M token) | Output (1M token) | Kullanım |
|-------|-----------------|-------------------|---------|
| `grok-4` | $3.00 | $15.00 | Akıl yürütme, karmaşık analiz |
| `grok-4.3` | $1.25 | $2.50 | Standart kod + analiz |
| `grok-3` | $3.00 | $15.00 | Orta karmaşıklık |
| `grok-3-mini` | $0.30 | $0.50 | Hızlı, basit görevler |
| `grok-build-0.1` | $1.00 | $2.00 | Agentic/dosya yazma görevleri |
| `grok-2-vision` | $2.00 | $10.00 | Görsel analiz |

Tercih sırası: `grok-4.3` → genel; `grok-4` → karmaşık; `grok-3-mini` → hızlı/ucuz

## Batch API — %20 İndirim

```python
import xai_sdk

client = xai_sdk.Client()
batch = client.batches.create(
    requests=[{"model": "grok-4.3", "messages": [...]}],
    completion_window="24h"
)
# Async, 24 saate kadar işlenir
# Aynı anahtarlar, %20 daha ucuz
```

Ne zaman: bulk analiz, 100+ transcript işleme, kritik değil işler

## Context Compaction

```
POST /v1/responses/compact
```
Uzun konuşmaları küçültür, token tasarrufu sağlar. Uzun Orchester oturumlarında kullan.

## Araçlar (Tools / Agentic)

| Araç | Ne işe yarar |
|------|-------------|
| `web_search` | Güncel web araması |
| `x_search` | Twitter/X araması |
| `code_execution` | Sandbox Python çalıştırma |
| `collections_search` | xAI'ın içerik koleksiyonları |
| `mcp` | MCP server entegrasyonu |

Kullanım: API isteğinde `tools` parametresi ile belirt.

## Ses API

```
STT (transcription): POST /v1/audio/transcriptions
TTS (synthesis):     POST /v1/audio/speech  (model: grok-2-audio)
Realtime:            wss://api.x.ai/v1/audio/realtime
```

Fiyat: ~$0.006/dakika STT, ~$0.015/1K karakter TTS

## Görsel API (Imagine)

```
Görsel: POST /v1/images/generations  (model: aurora)
Video:  POST /v1/videos/generations
```

Aurora: $0.07/görsel (1024x1024). Video: ayrı fiyatlandırma.

## OpenAI SDK ile Kullanım

```python
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["XAI_API_KEY"],
    base_url="https://api.x.ai/v1"
)
response = client.chat.completions.create(
    model="grok-4.3",
    messages=[{"role": "user", "content": "..."}]
)
```

## Karar Ağacı — Ne Zaman Ne Kullan

```
Tek seferlik kod/dosya görevi    → Grok Build CLI (--permission-mode bypassPermissions)
100+ item bulk işleme            → Batch API (grok-4.3, %20 indirim)
Hızlı / ucuz / basit             → grok-3-mini
Web araması gerekli              → grok-4.3 + web_search tool
Görsel analiz                    → grok-2-vision
Ses transkripsiyonu              → /v1/audio/transcriptions
Uzun konuşma token optimizasyonu → /v1/responses/compact
```

## API Key Lokasyonu

`~/.hermes/.env` → `XAI_API_KEY=...`  
CEBİMİZ.md → güncel bakiye ve limit bilgisi

## SuperGrok Trial (2026-07-06)

7 günlük trial aktif — maksimum kullanım penceresi.  
Trial bitince: normal ücretlendirme (grok-4.3 en verimli seçenek).
