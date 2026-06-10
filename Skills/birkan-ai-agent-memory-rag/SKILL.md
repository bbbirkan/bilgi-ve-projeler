# AI Agent Memory & RAG — Karar + Uygulama

## Ne Zaman Kullan
- Hermes'e veya herhangi bir ajana bellek/bilgi mimarisi eklerken
- "RAG mı kursam, LLM Wiki mi?" sorusunu yanıtlarken
- Sıfırdan LLM Wiki vault kurarken
- Birkan'ın mevcut memory sistemiyle ne eksik olduğunu anlamak istediğinde

---

## Adım 0 — Mimari Seç

Dört pattern. Hangisini seçeceğin veri boyutuna ve soruya göre:

| | RAG | CAG | LLM Wiki (Karpathy) | GBrain (Garry Tan) |
|--|-----|-----|--------------------|--------------------|
| **Soru tipi** | "Bu corpus'ta X nerede?" | "Tüm belgeni biliyorum, sor" | "Bu konu hakkında ne biliyoruz?" | "Bunu otomatik yap" |
| **Öğrenir mi** | Hayır — her sorguda sıfır | Hayır — statik context | Evet — wiki büyür, kompound olur | Evet — eylem alır |
| **Veri boyutu** | Büyük (>500K token) | **Küçük (<500K token)** | Orta-büyük, yapılandırılmış | Herhangi |
| **Ne zaman iyi** | Büyük corpus, arama ağırlıklı | **Stabil data, tam context gerekiyor** | Bilgi birikmeli, analiz ağırlıklı | Otonom, cron tabanlı |
| **Olgunluk** | Production-ready | Production-ready (2026) | 2026'da güçlü ve pratik | Erken, kırılgan |
| **Birkan'da karşılığı** | — | Küçük proje dökümantasyonu | `memory/*.md` sistemi + bu vault | Hermes skills + cron job'lar |

### CAG Karar Kuralı
```
veri < 500K token VE statik (sık değişmiyor)?
  → CAG kullan: tüm içeriği context'e yükle, RAG karmaşıklığı yok
  
veri > 500K token VE statik?
  → MiniMax M3 ile Batch-CAG: 1M context, 50-100 doküman tek seferde
  
veri > 1M token VEYA dinamik (sürekli güncelleniyor)?
  → RAG veya LLM Wiki kullan
```

**CAG (Cache-Augmented Generation):** Tüm dökümantasyonu tek seferde context'e yükle, her sorgu için hem retrieval hem embedding gerekmiyor. Claude'un büyük context penceresi + prompt caching ile maliyetini düşür.

> **CAG Maliyet Uyarısı (doğrulanmış):** 500K tokenlık bağlam, günde 1.000 işlem varsa sadece önbellek maliyeti ~$75/gün. 500+ doküman yüklendiğinde token limit hataları ve dikkat dağılması (attention dilution) başlar. "LLM bağlam penceresi büyüdü, RAG öldü" → yanlış. Kurumsal ölçekte **Hibrit RAG-CAG** standart haline geldi.

> **Düzeltme:** "RAG öldü, CAG aldı" iddiası asılsız. Büyük corpus için RAG zorunlu; CAG küçük stabil veri için kullanılabilir.

### MiniMax M3 — Batch-CAG (1M Context)

**OpenRouter model ID:** `minimax/minimax-m3`  
**Fiyat:** $0.30/M input · $1.20/M output (indirimli dönem)  
**Context:** 1.000.000 token — tek promptta 50-100 transkript işlenebilir  
**Weights:** Hugging Face'de `MiniMaxAI/MiniMax-M3` (Haziran 2026)

**Ne zaman kullan:**
- Büyük corpus batch analizi (transkript indeksleme, entity extraction)
- Embedding gerekmeden semantik arama
- "Bu 80 videoda BTC geçiyor mu?" tarzı tek seferlik sorular
- GPT-5.5 / Claude'un %5-10 maliyetiyle aynı kalite

**Batch-CAG örneği:**
```python
# 50 transkripti tek seferde işle
batch = "\n\n---\n\n".join(transcripts[:50])
prompt = f"""Aşağıdaki {len(batch)} video transkriptinde:
1. Geçen her ticker sembolü (TSLA, BTC, ETH...)
2. Her ticker için sentiment (bullish/bearish/neutral)
3. Fiyat hedefleri varsa
4. Piyasayla ilgisi olmayan içerik varsa işaretle

{batch}"""
# → OpenRouter: minimax/minimax-m3
```

**Temel ders:** RAG retriever'dır — arar, bulur, üretir. Her sorguda sıfırdan başlar.
LLM Wiki kompilatördür — biriktirir, birleştirir, büyür. **Write-path olmadan read-path yetmez.**

---

## Birkan'ın Mevcut Sistemiyle Karşılaştırma

```
LLM Wiki (Karpathy)          Birkan'ın memory sistemi
──────────────────────        ──────────────────────────────
raw/ → LLM → wiki pages       konuşma → Claude → memory/*.md
[[wikilink]] cross-refs        MEMORY.md index
INGEST/QUERY/LINT ops          ad-hoc güncelleme
Obsidian graph view            düz dosya okuma
```

**Eksikler:** otomatik write-path (Claude sormadan yazmıyor), cross-reference zayıf, kaynak ingestion yok. Bu vault deseni o eksikleri kapatır.

---

## LLM Wiki — Vault Kurulumu

### Klasör yapısı

```
vault/
├── CLAUDE.md           ← şema/anayasa (en kritik dosya)
├── index.md            ← içerik kataloğu
├── log.md              ← append-only olay kaydı
├── raw/                ← ham kaynaklar (ASLA DEĞİŞTİRME)
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── sources/            ← her ham kaynak için özet sayfası
├── entities/           ← kişiler, ürünler, organizasyonlar
├── concepts/           ← soyut kavramlar, terimler
├── decisions/          ← kararlar + gerekçe
└── syntheses/          ← çok-kaynaklı sentez sayfaları
```

Yapı alana göre uyarlanır. Birkan için trade wiki örneği:
```
raw/articles/, raw/papers/
entities/  → hisseler, protokoller, borsalar
concepts/  → stratejiler, indikatörler, risk modelleri
decisions/ → "Alpaca'ya geçtim çünkü..."
syntheses/ → "ETF rotasyon vs kripto momentum karşılaştırması"
```

---

## 3 Temel Operasyon

### INGEST — Yeni kaynak ekle

Ham klasöre kaynak koy, "bunu işle" de. Ajan:
1. Kaynağı okur
2. Anahtar çıkarımları tartışır
3. `sources/` altına özet sayfası yazar
4. `index.md`'yi günceller
5. İlgili `entities/` ve `concepts/` sayfalarını çapraz-günceller
6. Tutarsızlık varsa işaretler (`⚠ Çelişki: Kaynak A şunu derken...`)
7. `log.md`'ye zaman damgalı giriş ekler

Tek kaynak 10–15 sayfaya dokunabilir. **Toplu mı tek tek mi:** ikisi de geçerli — şemana yaz.

### QUERY — Soruyu wiki üzerinden yanıtla

Ajana wiki'ye soru sor. Ajan:
1. `index.md`'yi okur
2. İlgili sayfaları bulur ve okur
3. Cevabı sentezler, her iddia için kaynak referansı verir
4. **Kritik:** iyi cevaplar wiki'ye yeni sayfa olarak geri dosyalanır — sohbet geçmişinde kaybolmaz

### LINT — Wiki sağlık kontrolü (periyodik)

Ajana "wiki sağlık kontrolü yap" de. Kontrol eder:
- Sayfalar arası çelişkiler
- Yeni kaynaklarla geçersiz kalmış iddialar (stale claims)
- Hiçbir yerden link almayan orphan sayfalar
- Eksik veya tek yönlü çapraz-referanslar
- Araştırılacak yeni sorular ve kaynak önerileri

---

## index.md ve log.md

### `index.md` — içerik kataloğu
Her sayfa için: link + tek satır özet + opsiyonel metadata. **Ajan her INGEST'te günceller.** ~100 kaynak, ~birkaç yüz sayfaya kadar embedding tabanlı RAG ihtiyacını ortadan kaldırır.

### `log.md` — zamansal kayıt

```
## [2026-06-06] ingest | Medium Makale — Claude Code Token Tasarrufu
## [2026-06-06] query | "Walk-forward nedir?" → filed: concepts/walk-forward-opt.md
## [2026-06-07] lint | 2 stale claim, 1 orphan düzeltildi
```

Parse etmek için: `grep "^## \[" log.md | tail -10`

---

## CLAUDE.md Şeması — Ne İçermeli

Wiki'nin anayasası. En az şunlar:

1. **Amaç** — bu wiki hangi alanda, hangi sorulara cevap arıyor
2. **Klasör yapısı** — her klasörün ne içerdiği
3. **Sayfa formatı** — frontmatter alanları, başlık sırası, link konvansiyonları
4. **Naming convention** — kebab-case mi, varlık isimleri nasıl kanonikleştirilir
5. **Ingest workflow** — adım adım ne yapılır
6. **Yasaklar** — `raw/` yazmak yasak, kaynaksız iddia yasak, sayfa silme yasak (archive et)

---

## Hard Rules

1. **`raw/` immutable** — ajan sadece okur, asla yazar
2. **Her iddia kaynaklı** — hangi raw dosyadan geldiğini belirt
3. **Çelişki silinmez, işaretlenir** — `⚠ Çelişki:` ile görünür yere yaz
4. **Çift-yönlü link** — bir sayfayı güncellerken ona link veren sayfaları da kontrol et
5. **Her operasyon log'lanır** — zaman damgalı `log.md`'ye
6. **Sayfa silinmez, archive edilir** — `archive/` altına taşı, tarih korunur

---

## İlk Vault Kurulum Adımları

```
1. Klasör yapısını kur (raw/, sources/, entities/, concepts/, decisions/)
2. index.md ve log.md iskelet dosyalarını oluştur
3. CLAUDE.md'yi yaz — alana özgü bölümleri ekle
4. Obsidian ile aç, graph view'i kontrol et
5. İlk kaynağı raw/ içine koy, "ingest et" de
6. Sonucu gez, naming/format beğenmediysen şemayı güncelle, tekrar çalıştır
```

Obsidian Web Clipper eklentisi + yt-dlp transkript → `raw/` iş akışı için `karpathy-obsidian` skill'ine bak.

---

## Agentic RAG — LangGraph 2026 Mimarisi

Basit "getir ve üret" çizgiselliğini kıran döngüsel akış:

```
Retrieve → Generate → [Hallucination Node] → EVET: yanıt döndür
                              ↓ HAYIR
                      Query Transformation → Retrieve (tekrar)
```

**Hallucination Node** — her üretim adımından sonra çalışır:
1. **Grounding**: yanıt, alınan belgelerle örtüşüyor mu?
2. **Utility**: yanıt kullanıcının sorusunu gerçekten çözüyor mu?

İkisi de başarılıysa yanıtı döndür. Biri başarısızsa sorgu yeniden yazılır (Query Transformation), döngü başa döner. Sistem kendini kendi kendine düzeltir (self-correcting).

### Syftr — Pareto Optimizasyonu
DataRobot'un Syftr aracı LATS, ReAct, Critique Agent gibi 10²³ agent konfigürasyon alanına Bayesian Optimization uygular:
- "Pareto Budayıcısı" — verimsiz düğüm kombinasyonlarını erkenden eler
- Sonuç: en yüksek doğrulukta maliyeti **9 kata kadar** düşüren konfigürasyonlar
- Kaynak: `github.com/datarobot/syftr`

**Ne zaman lazım:** Prodda maliyet/doğruluk dengesi kurmaya çalışan, çok düğümlü Agentic RAG sistemleri.
**Ne zaman gerekmez:** İlk kurulum, küçük proje (<1000 doküman).

---

## Hazır Açık Kaynak Araçlar (2026)

### LLM Wiki — `nashsu/llm_wiki`
Karpathy LLM Wiki pattern'inin tam masaüstü uygulaması. **v0.4.23 → 8 Haziran 2026**

- **Platform:** Tauri + React (macOS/Windows/Linux native)
- **LLM support:** OpenAI, Anthropic (Claude), Google, Ollama, custom
- **Ne yapar:** Dökümanları → otomatik wiki (interlinked Markdown)
- **Teknik:** Two-step CoT → sayfa üret → çapraz-referans
- **GitHub:** `github.com/nashsu/llm_wiki`

**Birkan için neden uygun:** Tauri (zaten bilinen), Claude destekli, sıfır API maliyeti (subscription), YT transkript → wiki dönüşümü için ideal.

**Kurulum:**
```bash
# Release'den .AppImage indir (Linux)
wget https://github.com/nashsu/llm_wiki/releases/latest/download/llm-wiki_*.AppImage
chmod +x llm-wiki_*.AppImage && ./llm-wiki_*.AppImage
```

---

### WeKnora — `Tencent/WeKnora`
RAG + Ajan + Wiki, tümü bir arada. v0.5.0 → Wiki Mode GA

- **Platform:** Web UI (Docker ile kurulur)
- **Wiki Mode:** Ajan otomatik olarak Markdown wiki oluşturur + knowledge graph
- **Agentic:** ReAct Agent, MCP araçları, web search entegrasyonu
- **GitHub:** `github.com/Tencent/WeKnora`

**Ne zaman WeKnora:** Tek arayüzden RAG + Ajan + Wiki istiyorsan, web UI yeterliyse.  
**Ne zaman llm_wiki:** Masaüstü native, Tauri tabanlı, sade wiki istiyorsan.

---

## LangChain / LlamaIndex — 2026 Durumu

Hermes + Claude tabanlı mevcut yapı RAG için yeterli. Ekstra framework = ekstra teknik borç. Bu pattern'i doğrudan Claude Code + Obsidian ile kur — LangChain/LlamaIndex katmanına ihtiyaç yok.

## Vector DB "Ölüyor mu"?

Hayır — clickbait. Hybrid search (dense vector + BM25) güçleniyor ama Vector DB'nin yerini almıyor. LLM Wiki orta ölçekte vector DB ihtiyacını kaldırır; büyük corpus için hâlâ gereklidir.
