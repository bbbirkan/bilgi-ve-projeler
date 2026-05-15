---
name: birkan-model-secim
description: "Birkan için aylık AI model seçim kararı — LMSYS Arena, Artificial Analysis ve OpenRouter'dan gerçek benchmark verileri çekerek profesyonel PDF tablo oluşturur. Sadece PDF atar, Telegram'a mesaj yazmaz. Her ay başı çalışır. Her firmadan max 2 model kuralı."
trigger:
  - "Haziran model seçeceğiz"
  - "model secim"
  - "PDF model"
  - "aylık model"
---

# 🤖 Birkan Model Seçim Skill'i

Bu skill, Birkan'ın her ay başı talep ettiği AI model seçim sürecini tam otomasyonla çalıştırır. Sadece PDF oluşturur ve atar — Telegram'a mesaj yazmaz.

---

## 🔄 Çalışma Formatı (Otomatik)

1. Birkan "Haziran için model seçeceğiz" derse → bu skill tetiklenir
2. Sistem:
   - LMSYS Arena'dan güncel ELO/rank verilerini çeker
   - OpenRouter'dan fiyat ve context bilgilerini çeker
   - Artificial Analysis'dan benchmark puanlarını çeker
   - Türkçe karakterli profesyonel PDF oluşturur
   - PDF'yi Birkan'a gönderir
3. Birkan seçim yapar → config güncellenir

---

## 📊 Tablo Kuralları

### Firma Başı Max 2 Model
- Her AI firmasından (OpenAI, Anthropic, Google, vs.) en fazla 2 model kullanılır
- Böylece çeşitlilik sağlanır, tek firma bağımlılığı önlenir
- ÜST AJAN ve ALT AJAN listeleri tamamen ayrık olmalı (disjoint set)

### ÜST AJAN — Telegram Sohbet (Kalite Odaklı)
- 10 seçenek
- Kalite + performans öncelikli
- Daha pahalı modeller tercih edilebilir
- Telif: Yaratıcı yazarlık, kodlama, araştırma

### ALT AJAN — Gateway/Cron (Maliyet Odaklı)
- 12 seçenek
- Maliyet + hız öncelikli
- Ucuz modeller tercih edilmeli
- Telif: Arka plan işleri, cron job'lar, otomasyon

---

## 📁 Çıktı Tablo Formatı

Her model için şu sütunlar olur:

| # | Firma | Model | Fiyat | Context | LMSYS | ⭐ En İyi Olduğu Alanlar |
|---|-------|-------|-------|---------|-------|--------------------------|

- ⭐ sütunu: OpenRouter model sayfalarından ve LMSYS Arena'dan derlenen en iyi olduğu 3 alan
- Seçili model sarı renkle highlight edilir
- Final tablo altta yeşil kutu içinde gösterilir

---

## 🔧 Veri Kaynakları

### 1. LMSYS Arena (lmarena.ai)
- ELO puanları ve rank
- Text, WebDev, Code, Image, Video kategorileri
- Web sayfasından scrape edilir

### 2. OpenRouter (openrouter.ai)
- Fiyat (input/output per 1M tokens)
- Context length
- Weekly token usage
- Model açıklamaları

### 3. Artificial Analysis (artificialanalysis.ai)
- Benchmark puanları (MMLU, HumanEval, MATH, vs.)
- Intelligence Index
- Fiyat/performans karşılaştırması

---

## 🔍 Web Kazıma Yöntemi

### LMSYS Arena'dan Veri Çekme

```bash
# Direkt HTML çek ve model isimlerini ayıkla
curl -sL "https://lmarena.ai/leaderboard" \
  -H "Accept: text/html" \
  -H "User-Agent: Mozilla/5.0" | \
  grep -oP 'claude-[a-z0-9-]*|gpt-[a-z0-9.-]*|gemini-[a-z0-9.-]*|kimi-[a-z0-9.-]*|deepseek-[a-z0-9.-]*' | \
  sort -u | head -30
```

### OpenRouter'dan Model Listesi

```bash
curl -s "https://openrouter.ai/api/v1/models" | python3 -c "
import json, sys
data = json.load(sys.stdin)
models = data.get('data', [])
targets = ['claude', 'deepseek', 'qwen', 'kimi', 'gpt-5', 'gpt-4', 'grok', 'gemini', 'minimax']
for m in models:
    name = m.get('name', '').lower()
    for t in targets:
        if t.lower() in name:
            ctx = m.get('context_length', 0)
            pricing = m.get('pricing', {})
            in_p = float(pricing.get('in', 0))
            out_p = float(pricing.get('out', 0))
            print(f\"{m.get('id')} | ctx:{ctx//1000}K | \${in_p:.6f} in\")
            break
" | sort -t'|' -k3 -rn
```

### OpenRouter Model Detay Sayfası

Her model için detaylı özellikler:
```
https://openrouter.ai/{provider}/{model-id}
```
Örnek: https://openrouter.ai/anthropic/claude-sonnet-4.6

Bu sayfada:
- Model açıklaması
- Fiyat
- Context length
- Weekly tokens
- Benchmark puanları (Code Categories, WebDev, vs.)
- En iyi olduğu alanlar

---

## 📄 PDF Oluşturma

### Gerekli Kütüphane
```python
pip install reportlab
# veya
uv pip install reportlab
```

### PDF Şablonu (execute_code ile)

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Türkçe font kaydet
pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

pdf_path = "/root/Hermes-Model-Secim-{Ay}-{Yil}.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('Title', fontName='DejaVu-Bold', fontSize=16, ...)
section_style = ParagraphStyle('Section', fontName='DejaVu-Bold', fontSize=12, ...)
normal = ParagraphStyle('Normal', fontName='DejaVu', fontSize=9, ...)

elements = []
elements.append(Paragraph("🤖 Hermes — Model Seçimi | {Ay} {Yil}", title_style))

# Tablo sütunları
header = ['#', 'Firma', 'Model', 'Fiyat', 'Ctx', 'LMSYS', '⭐ En İyi Olduğu Alanlar']
data = [
    ['1', 'Anthropic', 'Claude Sonnet 4.6', '$3/M', '1M', '1524', 'Coding, iteratif geliştirme'],
    # ... 10 veya 12 satır
]

col_widths = [0.6*cm, 1.8*cm, 3.2*cm, 1.5*cm, 1.2*cm, 1.3*cm, 6.2*cm]
t = Table([header] + data, colWidths=col_widths)
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f3460')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'DejaVu-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 8),
    ('GRID', (0,0), (-1,-1), 0.3, colors.HexColor('#c0c0c0')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f4ff')]),
    # Seçili satır highlight
    ('BACKGROUND', (0,3), (-1,3), colors.HexColor('#fff3cd')),
    ('FONTNAME', (0,3), (-1,3), 'DejaVu-Bold'),
]))
elements.append(t)

# Final tablo (yeşil kutu)
result_data = [
    ['🧠 ÜST AJAN', 'OpenAI', 'GPT-5.4 Pro', '$5/M', '1M', '~1470', 'Yaratıcı yazarlık, multimodal'],
    ['⚙️ ALT AJAN', 'Google', 'Gemini 3.1 Flash', '$0.5/M', '1M', '~1400', 'Uzun bağlam, hız'],
]

doc.build(elements)
print(f"PDF hazır: {pdf_path}")
```

---

## 🚫 Önemli Kurallar

1. **Sadece PDF atılır — Telegram'a mesaj yazılmaz** (aksi belirtilmedikçe)
2. **Türkçe karakterler için DejaVu font kullanılır** —aksi halde çıkmaz
3. **Her firma max 2 model** — ayrık seçim (disjoint set)
4. **Ücretsiz modeller pas geçilir** — güvenilirlik endişesi
5. **Memory güncellenir** — seçilen model kombinasyonu kaydedilir

---

## 📝 Memory Güncelleme

Her seçimden sonra memory güncellenir:
```
Model seçim {Ay} {Yil}: ÜST={Model}, ALT={Model}. Her ay başı güncellenir.
```

---

## 🔗 İlgili Skills

- `ai-skill-pipeline` — Genel bilgi işleme pipeline
- `birkan-ai-model-scout` — Model benchmark bilgileri
- `hermes-agent` — Hermes konfigürasyonu

---

*Bu skill Birkan'ın model seçim sürecini 2 saatlik araştırmayı ~5 dakikaya indirir.*