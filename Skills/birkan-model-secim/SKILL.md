---
name: birkan-model-secim
description: "Birkan için aylık AI model seçim kararı — 40+ benchmark sitesinden gerçek verilerle profesyonel PDF tablo oluşturur. Sadece PDF atar, Telegram'a mesaj yazmaz. Her ay başı çalışır. Her firmadan max 2 model kuralı."
trigger:
  - "Haziran model seçeceğiz"
  - "model secim"
  - "PDF model"
  - "aylık model"
  - "model seçimi"
  - "benchmark"
---

# 🤖 Birkan Model Seçim Skill'i (v3)

Bu skill, Birkan'ın her ay başı talep ettiği AI model seçim sürecini tam otomasyonla çalıştırır. Sadece PDF oluşturur ve atar — Telegram'a mesaj yazmaz.

> **Kaynak:** Bu skill, Birkan'ın sağladığı 2026 benchmark rehberi ile oluşturulmuştur. 40+ benchmark sitesi, 8 kategori, tam metodoloji dahil.

---

## 🔄 Çalışma Formatı (Otomatik)

1. Birkan "Haziran için model seçeceğiz" derse → bu skill tetiklenir
2. Sistem:
   - LMSYS Arena'dan güncel ELO/rank verilerini çeker
   - OpenRouter'dan fiyat ve context bilgilerini çeker
   - Artificial Analysis'den benchmark puanlarını çeker
   - 40+ benchmark sitesinden özellikler derlenir
   - Türkçe karakterli profesyonel PDF oluşturur
   - PDF'yi Birkan'a gönderir
3. Birkan seçim yapar → config güncellenir

---

## 📊 Tablo Kuralları

### Firma Başı Max 2 Model
- Her AI firmasından (OpenAI, Anthropic, Google, vs.) en fazla 2 model kullanılır
- ÜST AJAN ve ALT AJAN listeleri tamamen ayrık olmalı (disjoint set)
- Aynı model iki listede yer alamaz

### ÜST AJAN — Telegram Sohbet (Kalite Odaklı)
- 10 seçenek
- Kalite + performans öncelikli
- Telif: Yaratıcı yazarlık, kodlama, araştırma, multimodal

### ALT AJAN — Gateway/Cron (Maliyet Odaklı)
- 12 seçenek
- Maliyet + hız öncelikli
- Telif: Arka plan işleri, cron job'lar, otomasyon

---

## ⚠️ PITFALLS

### ⚠️ Kafadan sallama KABUL EDİLMEZ
- **Hata:** Model seçimleri memory'den yapıldı. Kullanıcı çok kızdı: "kafadan sallıyorsun".
- **Doğru yöntem:** Tablo oluşturmadan ÖNCE LMSYS Arena, OpenRouter ve Artificial Analysis'dan gerçek veriler çekilir. Hafızadan/sezgisel veri çekilmez.

### ⚠️ ⭐ sütunu boş bırakılmamalı
- **Hata:** İlk tablolarda en iyi olduğu alanlar belirtilmedi. "Anlaşılmıyor" geldi.
- **Doğru yöntem:** Her model için virgülle ayrılmış 2-3 "en iyi olduğu alan" yazılır.

### ⚠️ Telegram'a sadece PDF at
- Mesaj yazılmaz — kullanıcı net istedi.

---

## 📁 Çıktı Tablo Formatı
## 📁 Çıktı Tablo Formatı

Her model için şu sütunlar olur:

| # | Firma | Model | Fiyat | Context | LMSYS | ⭐ En İyi Olduğu Alanlar |
|---|-------|-------|-------|---------|-------|--------------------------|

- ⭐ sütunu: OpenRouter model sayfalarından ve benchmark sitelerinden derlenen en iyi olduğu alanlar (virgülle ayrılmış)
- Seçili model sarı renkle highlight edilir
- Final tablo altta yeşil kutu içinde gösterilir

---

## 🔧 40+ Veri Kaynağı (Tam Liste — Gerçek Doğrulanmış Veriler)

> ⚠️ BİRİAN'IN KRİTER LİSTESİ: Kullanıcı AI'lara kriter listesi verir, AI'lar verileri çekip Türkçe rapor hazırlar. Birkan raporu bana verir, ben PDF'e dökerim. Bu sayede veriler kafadan değil, gerçek benchmark sitelerinden çekilmiş olur.

### Yöntem: AI'ya Verilecek Kriter Prompt'u

```
Aşağıdaki 40+ benchmark sitesinden ve OpenRouter API'den gerçek verileri çekerek TÜRKÇE bir rapor hazırla.

ÜST AJAN (15 model) + ALT AJAN (20 model) = 35 model
Her model için: Fiyat, Context, LMSYS ELO, LiveBench, SWE-bench, En iyi olduğu alanlar

Kaynaklar: lmarena.ai, openrouter.ai, livebench.ai, swebench.com, artificialanalysis.ai
Şartlar: Ücretli modeller, max 2/firma, ayrık listeler
```

### 1. Genel (Çok-Yetenekli) Liderlik Tabloları

| # | Site | URL | Odak |
|---|------|-----|------|
| 1 | **LMArena** | lmarena.ai | İnsan tercihi (Elo) — altın standart |
| 2 | **Artificial Analysis** | artificialanalysis.ai | Intelligence Index v4.0 + fiyat/hız |
| 3 | **LiveBench** | livebench.ai | Kirlenme-dirençli akademik |
| 4 | **Vellum** | vellum.ai/llm-leaderboard | Frontier tek-sayfa karşılaştırma |
| 5 | **LLM-Stats** | llm-stats.com | Bileşik skor (300+ model) |
| 6 | **BenchLM** | benchlm.ai | 230+ model × 190+ benchmark |
| 7 | **Onyx Tier** | onyx.app/llm-leaderboard | S/A/B/C/D tier görünümü |
| 8 | **HF Open LLM** | huggingface.co/spaces/open-llm-leaderboard | **ARŞİVLENDİ** (Haziran 2025) |

### 2. Kodlama (Coding) Benchmarkları

| # | Site | URL | Odak |
|---|------|-----|------|
| 9 | **SWE-bench** | swebench.com | GitHub issue çözme |
| 10 | **Scale SEAL Pro** | scale.com/leaderboard | Kontaminasyon-dirençli, 4 dilli |
| 11 | **LiveCodeBench** | livecodebench.github.io | Kirlenme-dirençli kod |
| 12 | **Aider Polyglot** | aider.chat/docs/leaderboards | Çok-dilli kod düzenleme |
| 13 | **Terminal-Bench** | tbench.ai | CLI/terminal agent |
| 14 | **BigCodeBench** | bigcode-bench.github.io | Pratik kütüphane kullanımı |
| 15 | **CodeSOTA** | codesota.com/code-generation | Kod SOTA derleyici |

### 3. Akıl Yürütme (Reasoning) & Matematik

| # | Site | URL | Odak |
|---|------|-----|------|
| 16 | **GPQA Diamond** | github.com/idavidrein/gpqa | Lisansüstü bilim QA |
| 17 | **HLE** | lastexam.ai | "Son akademik sınav" |
| 18 | **FrontierMath** | epoch.ai/frontiermath | Araştırma matematik |
| 19 | **AIME 2026** | artificialanalysis.ai/evaluations/aime | Olimpiyat matematiği |
| 20 | **ARC-AGI-2/3** | arcprize.org | Akıcı zekâ |

### 4. Multimodal (Görsel & Ses)

| # | Site | URL | Odak |
|---|------|-----|------|
| 21 | **MMMU-Pro** | mmmu-benchmark.github.io | Üniversite seviyesi görsel QA |
| 22 | **OpenVLM Leaderboard** | huggingface.co/spaces/opencompass/open_vlm_leaderboard | 100+ VLM |
| 23 | **MathVista** | mathvista.github.io | Görsel matematik |
| 24 | **AA Image Arena** | artificialanalysis.ai/image | Görsel üretim Elo |
| 25 | **AA Video Arena** | artificialanalysis.ai/video/leaderboard | Video üretim |
| 26 | **MMAU-Pro** | sakshi113.github.io/mmau_homepage | Ses akıl yürütme |
| 27 | **HF Open ASR** | huggingface.co/spaces/hf-audio/open_asr_leaderboard | Konuşma tanıma |
| 28 | **TTS Arena** | huggingface.co/spaces/TTS-AGI/TTS-Arena-V2 | Metinden-konuşmaya |

### 5. Agent / Tool-Use Benchmarkları

| # | Site | URL | Odak |
|---|------|-----|------|
| 29 | **GAIA** | huggingface.co/spaces/gaia-benchmark/leaderboard | Genel asistan agent |
| 30 | **WebArena** | webarena.dev | Web sandbox agent |
| 31 | **OSWorld** | os-world.github.io | Masaüstü computer use |
| 32 | **τ²-bench** | github.com/sierra-research/tau-bench | Tool + policy + sim user |
| 33 | **BFCL** | gorilla.cs.berkeley.edu/leaderboard.html | Function calling |
| 34 | **HAL (Princeton)** | hal.cs.princeton.edu | Holistic agent + maliyet |
| 35 | **MLE-bench** | github.com/openai/mle-bench | Veri-bilimi agent |

### 6. Hız / Maliyet / Verimlilik

| # | Site | URL | Odak |
|---|------|-----|------|
| 36 | **Artificial Analysis Speed** | artificialanalysis.ai | TPS, TTFT, fiyat |
| 37 | **LLM-Stats** | llm-stats.com | LLM Stats Score |
| 38 | **PricePerToken** | pricepertoken.com | Anlık fiyat tabloları |
| 39 | **OpenRouter Rankings** | openrouter.ai/rankings | Gerçek kullanım popülaritesi |

### 7. Güvenlik (Safety) Benchmarkları

| # | Site | URL | Odak |
|---|------|-----|------|
| 40 | **AILuminate** | mlcommons.org/benchmarks/ailuminate | Endüstri standardı güvenlik |
| 41 | **HELM Safety** | crfm.stanford.edu/helm/safety | Holistik + safety |
| 42 | **TrustLLM** | trustllmbenchmark.github.io | 6 boyut güvenilirlik |
| 43 | **HarmBench** | harmbench.org | Jailbreak/red-team dayanıklılığı |

---

## 🔍 Web Kazıma Yöntemi

### LMArena'dan Gerçek Zamanlı Veri

```bash
curl -sL "https://lmarena.ai/leaderboard" \
  -H "Accept: text/html" \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" \
  --compressed | grep -oP 'claude-[a-z0-9-]+|gpt-[a-z0-9.-]+|gemini-[a-z0-9.-]+|kimi-[a-z0-9.-]+' | sort -u | head -30
```

### OpenRouter'dan Model Listesi + Fiyat

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
            tokens = m.get('tokens_used', 0)
            print(f\"{m.get('id')} | ctx:{ctx//1000}K | \${in_p:.6f}in \${out_p:.6f}out | used:{tokens}\")
            break
" 2>&1 | sort -t'|' -k4 -rn | head -20
```

### OpenRouter Model Detay Sayfası (Browser)

Her model için detaylı özellikler:
```
https://openrouter.ai/{provider}/{model-id}
```
Örnek: https://openrouter.ai/anthropic/claude-sonnet-4.6

Bu sayfada:
- Model açıklaması (en iyi olduğu alanlar)
- Fiyat (input/output per 1M tokens)
- Context length
- Weekly token usage
- LMSYS ELO ve rank
- Category Performance (Code, WebDev, vs.)

### Artificial Analysis'dan Intelligence Index

```bash
curl -s "https://artificialanalysis.ai/api/models" 2>/dev/null || \
curl -sL "https://artificialanalysis.ai/models" | grep -i "intelligence\|score\|rank" | head -20
```

---

## 📄 PDF Oluşturma

### Gerekli Kütüphane
```bash
uv pip install reportlab pillow
```

### Font Kayıt (Türkçe İçin)
```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
```

### PDF Şablonu
```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

pdf_path = f"/root/Hermes-Model-Secim-{Ay}-{Yil}.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm,
    topMargin=1.5*cm, bottomMargin=1.5*cm)

title_s = ParagraphStyle('T', fontName='DejaVu-Bold', fontSize=16, ...)
section_s = ParagraphStyle('Se', fontName='DejaVu-Bold', fontSize=12, ...)

e = []
e.append(Paragraph(f"🤖 Hermes — Model Seçimi | {Ay} {Yil}", title_s))

# ⭐ sütunuyla tablo
header = ['#', 'Firma', 'Model', 'Fiyat', 'Ctx', 'LMSYS', '⭐ En İyi Olduğu Alanlar']
data = [
    ['1', 'Anthropic', 'Claude Sonnet 4.6', '$3/M', '1M', '1524', 'Coding, iteratif geliştirme, karmaşık kod tabanı navigasyonu'],
    ['3', 'OpenAI', 'GPT-5.4 Pro ★', '$5/M', '1M', '~1470', 'Yaratıcı yazarlık, multimodal, ileri düzey reasoning'],
    # ... 10 veya 12 satır
]
cw = [0.5*cm, 1.7*cm, 3.0*cm, 1.4*cm, 1.1*cm, 2.2*cm, 6.1*cm]
t = Table([header]+data, colWidths=cw)
t.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#0f3460')),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('FONTNAME',(0,0),(-1,0),'DejaVu-Bold'),
    ('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#c0c0c0')),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f0f4ff')]),
    ('BACKGROUND',(0,3),(-1,3),colors.HexColor('#fff3cd')),  # Seçili satır
    ('FONTNAME',(0,3),(-1,3),'DejaVu-Bold'),
]))
e.append(t)
doc.build(e)
```

---

## 📋 Kullanım Senaryosuna Göre Hızlı Seçim

| Amacınız | Bakılacak Tablolar |
|----------|-------------------|
| Genel "en iyi sohbet modeli" | LMArena Overall + AA Intelligence Index |
| Kodlama agent'ı | SWE-bench Pro, LiveCodeBench, Terminal-Bench Hard |
| Tool-calling / API | BFCL v3/v4, τ²-bench, GAIA |
| Computer-use / browser | OSWorld, WebArena |
| Bilim / matematik araştırma | GPQA Diamond, HLE, FrontierMath |
| Görsel akıl yürütme | MMMU-Pro, OpenVLM Leaderboard |
| Sesli AI | MMAU-Pro, AIR-Bench |
| Fiyat / hız optimizasyonu | Artificial Analysis (TPS + fiyat) |
| Güvenlik / compliance | AILuminate, TrustLLM, HarmBench |
| Açık-ağırlıklı (self-host) | LLM-Stats Open LLM, BenchLM |

---

## ⚠️ Metodolojik Uyarılar (CRITICAL)

1. **Saturasyon:** MMLU, HumanEval, MBPP, GSM8K, MATH-500 — frontier modellerde ayırt edici değil. Bunun yerine GPQA Diamond, HLE, FrontierMath, SWE-bench Pro, LiveCodeBench, ARC-AGI-2/3 kullan.
2. **Veri kontaminasyonu:** Public benchmarklar zamanla eğitim verisine sızar. Live testler (LiveBench, LiveCodeBench, SWE-bench Live) daha güvenilir.
3. **Scaffold etkisi:** Agent benchmarklarında aynı model + farklı harness arasında 5–10 puan fark olabilir. Skorları harness etiketiyle birlikte oku.
4. **Self-reported vs. Independent:** Model üreticisinin raporladığı skor ile bağımsız ölçümler arasında ciddi farklar olabilir. Bağımsız sayıları tercih et.
5. **Tek skor tek hikâye değildir:** Bileşik skorlar farklı ağırlıklandırmalarla yapılır. En az 3 farklı kaynak birlikte değerlendir.
6. **HF Open LLM Leaderboard emekli (Haziran 2025):** 2026 muadilleri: LLM-Stats Open LLM, BenchLM, AA open-weight filter.
7. **Reward-hacking:** Berkeley RDI 2026 — başlıca agent benchmarklarının manipüle edilebildiği gösterildi. Tek benchmark'a güvenme.

---

## 🚫 Önemli Kurallar

1. **Sadece PDF atılır — Telegram'a mesaj yazılmaz** (aksi belirtilmedikçe)
2. **Türkçe karakterler için DejaVu font kullanılır** — aksi halde çıkmaz
3. **Her firma max 2 model** — ayrık seçim (disjoint set)
4. **Ücretsiz modeller pas geçilir** — güvenilirlik endişesi
5. **Memory güncellenir** — seçilen model kombinasyonu kaydedilir
6. **Skill otomatik GitHub'a push edilir** — bilgi-ve-projeler/Skills/birkan-model-secim/

---

## 📝 Memory Güncelleme

Her seçimden sonra memory güncellenir:
```
Model seçim {Ay} {Yil}: ÜST={Model}, ALT={Model}. Her ay başı güncellenir.
```

---

## 🔗 İlgili Skills

- `ai-skill-pipeline` — Genel bilgi işleme pipeline
- `birkan-ai-model-scout` — Model benchmark bilgileri (güncellenmiş)
- `hermes-agent` — Hermes konfigürasyonu
- `uncensored-model-router` — Sansür swap

---

*Bu skill Birkan'ın model seçim sürecini ~5 dakikaya indirir. 40+ benchmark sitesi, 8 kategori, tam metodoloji dahil.*
*Kaynak: Birkan'ın sağladığı 2026 LLM Karşılaştırma Rehberi | 40+ benchmark sitesi derlemesi*

---

## 📎 References (references/)

- `references/benchmark-siteleri.md` — 40+ benchmark sitesi tam liste, URL'ler, odak alanları, metodoloji özetleri. Bu dosya oturumda Birkan'ın verdiği benchmark rehberinden derlenmiştir. Her ay model seçimi yapılacağında bu dosyaya başvurularak gerçek veriler çekilir.