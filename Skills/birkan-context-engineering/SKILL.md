---
name: context-engineering
description: |
  Context Engineering — LLM API maliyetini ve gecikmeyi düşürmek için KV-Cache
  hizalaması, token optimizasyonu, CCR (Compress-Cache-Retrieve) mimarisi.
  Prompt Engineering'in ötesinde: model değil, harness optimize edilir.

  TRIGGER: context engineering, kv-cache, token optimization, prompt caching,
           api cost reduction, context compression, stable prefix
---

# Context Engineering — Harness Optimizasyonu

## Ne Zaman Kullan
- API maliyetleri yüksek, context hızla doluyorsa
- Uzun oturumlarda KV-Cache isabetini artırmak istiyorsan
- Headroom veya benzer API proxy kuruyorsan
- "Model değil, harness" paradigmasını uygularken

---

## Temel Prensip

> "Problem modelin kendisi değil, modeli saran harness."

Aynı modelde:
- Kötü harness: %23 SWE-bench başarı
- İyi harness: %45+ SWE-bench başarı

Context Engineering = modele ne gönderdiğini, hangi sırayla gönderdiğini ve nasıl sıkıştırdığını optimize etmek.

---

## KV-Cache Hizalaması (Stable Prefix / Dynamic Tail)

Anthropic/OpenAI KV-Cache, isteklerin başındaki sabit prefix'i önbellekler. Dinamik veri (tarih, UUID, kullanıcı adı) prefix'e girerse cache her istekte geçersiz olur.

```python
# ❌ YAPMA — Dinamik veri başta, cache kırılıyor
messages = [
    {"role": "system", "content": f"Tarih: {datetime.now()}\nSen bir AI asistansın..."},
    {"role": "user", "content": "Sorum: ..."}
]

# ✅ YAP — Sabit prefix önce, dinamik veri sona
messages = [
    # STABLE PREFIX (değişmez → cache'lenir)
    {"role": "system", "content": "Sen bir AI asistansın. Görevin: ...\nKurallar: ...\n"},
    # DYNAMIC TAIL (değişir → en sona koy)
    {"role": "user", "content": f"[{datetime.now().strftime('%H:%M')}] {user_message}"}
]
```

**Headroom CacheAligner** bunu otomatik yapar: dinamik token'ları (tarih, UUID, session_id) payload'ın sonuna taşır.

---

## Token Sıkıştırma Katmanları

### 1. AST Tabanlı Kod Sıkıştırma
```python
# Ham kod yerine öz yapıyı gönder
# ❌ 500 satır kod = ~3000 token
# ✅ AST özeti = ~200 token

def compress_code_for_context(code: str) -> str:
    """Sadece imzaları, docstrings'i ve önemli blokları tut."""
    import ast
    tree = ast.parse(code)
    
    summary = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            summary.append(f"def {node.name}({[a.arg for a in node.args.args]})")
    
    return "\n".join(summary)
```

### 2. JSON Sıkıştırma (Kneedle Algoritması)
Büyük JSON yanıtlarını istatistiksel alt kümelere indir:
```python
# Headroom SmartCrusher yöntemi
# Büyük array'ler → sample + summary
# {"items": [...1000 items...]} → {"items": [...20 items...], "_summary": "1000 items, avg: X"}
```

### 3. Terminal Çıktısı (RTK)
```bash
# ❌ git diff HEAD~1 → ~21,500 token
# ✅ rtk git diff HEAD~1 → ~2,000 token (error-only, grouped)
rtk <komut>
```

---

## CCR (Compress-Cache-Retrieve) Mimarisi

Headroom'un CCR sistemi — kayıpsız bağlam sıkıştırma:

```
1. Sıkıştır (Compress)
   → Büyük veri/sohbet özetlenir, SQLite'ta orijinal hash ile saklanır

2. Önbellekle (Cache)
   → Özet modele gönderilir, ajanın context'i küçük kalır

3. Geri Getir (Retrieve)
   → Ajan gerek duyduğunda headroom_retrieve(hash) çağırır
   → Orijinal tam veri geri gelir — hiçbir şey kaybolmamış
```

```python
# Ajan perspektifinden:
# Normal akış: büyük JSON al → analiz et
# CCR akış: özet al → detay gerekirse retrieve et

tools = [
    {
        "name": "headroom_retrieve",
        "description": "Compressed context'in orijinal verisini geri getir",
        "parameters": {
            "hash": {"type": "string", "description": "Context hash"}
        }
    }
]
```

---

## Prompt Cache TTL

```python
# Anthropic: varsayılan 5dk → 1 saat uzatmak için
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "Uzun sistem prompt...",
            "cache_control": {"type": "ephemeral"}  # TTL: 1 saat
        }
    ],
    messages=[{"role": "user", "content": "Soru"}]
)
```

Env var ile de etkinleştirilebilir:
```bash
ENABLE_PROMPT_CACHING_1H=1  # Claude Code için
```

---

## Maliyet/Gecikme Dengesi

| Yöntem | Token Tasarrufu | Gecikme Etkisi | Kayıp? |
|--------|-----------------|----------------|--------|
| KV-Cache hizalaması | %40-80 (cache hit) | Düşürür | Yok |
| RTK (terminal) | %60-90 | Yok | Yok |
| Headroom CCR | %47-92 | Çok az | Yok (lossless) |
| AST kodu özeti | %80-95 | Yok | Kısmi (fine) |
| JSON sampling | %70-90 | Yok | Kısmi |

---

## Failure Learning

Headroom'un `headroom learn` özelliği:
- Ajanın geçmişte başarısız olduğu görevleri analiz eder
- "Ne işe yaradı, ne yaramadı" → CLAUDE.md veya MEMORY.md'ye yazar
- Sonraki oturumlarda başarısızlık tekrarlanmaz

```bash
headroom learn --project . --output CLAUDE.md
```

---

## Kaynaklar
- Headroom: github.com/chopratejas/headroom
- RTK: github.com/rtk-ai/rtk
- CBM: github.com/DeusData/codebase-memory-mcp
- agents-best-practices: github.com/DenisSergeevitch/agents-best-practices
