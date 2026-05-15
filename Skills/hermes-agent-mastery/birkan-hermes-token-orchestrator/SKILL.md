---
name: birkan-hermes-token-orchestrator
description: "Birkan'ın Hermes Agent kullanımını token tasarruflu, model-orchestrated ve wiki-first hale getiren kalıcı çalışma protokolü. ÜST/ALT model seçimi, uzun kaynakların wiki'ye alınması, subagent bütçesi ve 2 aylık model güncelleme döngüsünü yönetir."
version: 1.0.0
created_by: agent
trigger:
  - "token tasarrufu"
  - "orkestra"
  - "orchestrator"
  - "Hermes'i verimli kullan"
  - "uzun yazı"
  - "kitap"
  - "wiki"
  - "model güncelle"
---

# Birkan Hermes Token Orchestrator

Bu skill, Hermes'i **az token + yüksek zekâ** prensibiyle kullanmak için kalıcı çalışma protokolüdür.

## Ana Felsefe

1. **ÜST model ana akıl / karar verici** olarak kalır.
2. **ALT modeller araştırma, özet, veri çıkarma, formatlama ve wiki hazırlama** işlerini yapar.
3. Uzun metinler, kitaplar, raporlar ve büyük web çıktıları sohbete basılmaz; **wiki / dosya / graphify** katmanına alınır.
4. Ana sohbete sadece **kısa sentez + karar gereken nokta** döner.
5. Multi-agent pahalıdır; sadece paralellik veya uzmanlık gerçek değer katıyorsa kullanılır.

---

## Model Havuzu — Mayıs 2026

### ÜST modeller (Kalite / ana akıl)
Sıra kullanıcının PDF tablo satır numaralarına göredir:

1. **GPT-5.5** — OpenRouter ID: `openai/gpt-5.5`
2. **Claude Opus 4.6** — OpenRouter ID: `anthropic/claude-opus-4.6`
3. **DeepSeek V4 Pro** — OpenRouter ID: `deepseek/deepseek-v4-pro`
4. **Claude Opus 4.7** — OpenRouter ID: `anthropic/claude-opus-4.7`

Kullanım:
- Stratejik planlama, mimari karar, son sentez, riskli değişiklik → ÜST.
- Çok uzun ham okuma → ÜST'e verme; önce ALT/wiki ile sıkıştır.

### ALT modeller (Maliyet / işçi)
Sıra kullanıcının PDF tablo satır numaralarına göredir:

1. **GLM-4.7** — OpenRouter ID: `z-ai/glm-4.7`
2. **Gemini 3 Flash** — OpenRouter ID: `google/gemini-3-flash-preview`
3. **MiniMax M2.5** — OpenRouter ID: `minimax/minimax-m2.5`
4. **DeepSeek V4 Flash** — OpenRouter ID: `deepseek/deepseek-v4-flash`

Kullanım:
- Web araştırma, ham veri çıkarma, özet, sınıflandırma, tablo, JSON, uzun doküman bölme → ALT.
- ALT yetersiz kalırsa ÜST'e sadece sıkıştırılmış paket ver.

---

## Model Yeteneklerine Göre Routing

### Çok büyük dosya / mega-context
**Birinci tercih:** `deepseek/deepseek-v4-flash`

Neden:
- 1M context.
- Çok ucuz input/output.
- Ham metin tarama, indeksleme, bölümleme ve “needle finding” için iyi aday.

Kullanım:
- 100K+ token metin.
- Büyük PDF / kitap / log dump.
- Çok büyük JSON/CSV/HTML çıktı.
- Önce DeepSeek V4 Flash ile bölüm haritası çıkarılır.
- Sonra gerekirse GLM/Gemini ile bölüm özetleri alınır.
- Final sentez GPT-5.5 veya Claude Opus 4.6 ile yapılır.

### Genel işçi / dengeli akıl
**Birinci tercih:** `z-ai/glm-4.7`

Neden:
- İyi genel worker.
- Kod/prototip/özet/araştırma dengesi iyi.
- Delegation default modeli olarak kullanılır.

Kullanım:
- Standart subagent işleri.
- 5-20 kaynak web araştırması.
- Kod dosyası inceleme.
- Wiki sayfası taslağı.

### Hızlı ve ucuz özet / multimodal uyum
**Birinci tercih:** `google/gemini-3-flash-preview`

Kullanım:
- Hızlı ikinci özet.
- Uzun bölümden kısa bullet çıkarma.
- Tablo/JSON formatlama.
- Çok modlu içerik ihtimali varsa ön değerlendirme.

### En ucuz işçi / toplu sınıflandırma
**Birinci tercih:** `minimax/minimax-m2.5`

Kullanım:
- Çok sayıda küçük metin sınıflandırma.
- Basit extraction.
- “Bu metin hangi kategori?” tarzı işler.
- Maliyet kritik batch işlemleri.

### Zor kod / mimari / yüksek doğruluk
**ÜST tercih sırası:**
1. `openai/gpt-5.5`
2. `anthropic/claude-opus-4.6`
3. `deepseek/deepseek-v4-pro`
4. `anthropic/claude-opus-4.7`

Kullanım:
- Final karar.
- Mimari tasarım.
- Kritik kod değişikliği.
- Çelişkili kaynakları uzlaştırma.

### Routing pseudo-code

```text
if task == huge_file or tokens > 100k:
    worker = deepseek/deepseek-v4-flash
    action = map_sections + extract_key_claims + save_to_wiki
elif task == normal_research or standard_subagent:
    worker = z-ai/glm-4.7
elif task == fast_summary or table_json_format:
    worker = google/gemini-3-flash-preview
elif task == cheap_batch_classification:
    worker = minimax/minimax-m2.5
else:
    worker = z-ai/glm-4.7

final_synthesis = openai/gpt-5.5
if GPT-5.5 fails or too expensive:
    final_synthesis = anthropic/claude-opus-4.6
```

---

## Routing Kuralları

### Basit sohbet / kısa cevap
- Ana model yanıt verir.
- Araç kullanma gerekmiyorsa tool çağırma.
- Yanıt kısa tutulur.

### Araştırma / web / 5+ kaynak
- `delegate_task` kullan.
- Child agent toolsets sadece gerekli olanlarla sınırlandırılır: genelde `web`, `browser`, `file`.
- Child çıktısı max 20 madde / 1000 kelime olmalı.
- Ana ajan sadece synthesis yapar.

### Uzun yazı, kitap, PDF, büyük rapor
1. Ham içerik `~/wiki` veya proje wiki/vault içine alınır.
2. Kaynak raw olarak saklanır.
3. ALT model bölüm bölüm özetler.
4. Wiki sayfaları oluşturulur: entity/concept/comparison/query.
5. Ana sohbete sadece:
   - 5 madde özet
   - karar/aksiyon önerisi
   - oluşturulan dosya yolları

### Kod / repo işleri
- Önce graphify varsa `graphify-out/GRAPH_REPORT.md` okunur.
- Repo ilişkileri için grep yerine graphify/wiki tercih edilir.
- Geniş refactor'da görevler dosya sınırlarına göre ayrılır.
- Subagent çıktısı sadece diff özeti + risk + test komutu döndürür.

### Multi-agent / swarm
- Önce görev grafiği çıkar: bağımsız işler + bağımlılıklar.
- Ruflo/RecursiveMAS mantığı uygulanır: ajanlar arası uzun metin değil, kısa durum paketi.
- Her worker sadece kendi görevini ve gerekli dosyaları görür.
- Ana ajan final integrator olur.

---

## Token Hijyeni Kuralları

- Konu değişince `/reset` öner.
- Context %60 civarında ise `/compress` öner.
- 3-4 compact sonrası kalite düşerse yeni oturum + kısa özetle devam et.
- Tool çıktıları uzun olmasın; terminal komutlarında filtrele/özetle.
- Büyük dosyayı komple okuma; `read_file offset/limit`, `search_files`, graphify ve wiki kullan.
- Subagent pahalıdır: 1-2 basit iş için spawn etme; 3+ bağımsız parça varsa kullan.
- Skills gereksiz yüklenmez; sadece ilgili skill yüklenir.
- Memory kısa tutulur; prosedür skill'e, geçici ilerleme session/log'a yazılır.

---

## Kalıcı Sistem Döngüsü

### Günlük kullanım
- Ana sohbet: kısa karar + net aksiyon.
- Araştırma: ALT worker → özet → wiki.
- Kod: graphify map → küçük görevler → test.

### 2 aylık model güncelleme
`birkan-model-secim` skill'i çalıştırılır:
1. Benchmark siteleri taranır.
2. 15 ÜST + 20 ALT tablo güncellenir.
3. Kullanıcı seçim yapar.
4. Bu skill'teki model havuzu güncellenir.
5. Hermes config / delegation ayarları yumuşak geçişle güncellenir.

---

## Hermes Config Önerisi

- `model.default`: kaliteli ana model (`openai/gpt-5.5`)
- `delegation.model`: maliyet/işçi modeli (`z-ai/glm-4.7`)
- `delegation.provider`: `openrouter`
- `compression.enabled`: `true`
- `compression.threshold`: `0.35` veya `0.40`
- `compression.target_ratio`: `0.15` - `0.20`
- `compression.protect_last_n`: `10` - `14`
- `agent.reasoning_effort`: `medium`
- `agent.max_turns`: `45` - `60`
- `display.show_cost`: `true` mümkünse açılır.

---

## Kullanıcıya Davranış

Birkan gereksiz izin sorulmasını sevmez. Karar netse uygula. Ancak pahalı model değişimi, kalıcı config değişimi veya yıkıcı işlem varsa kısa bilgi ver, sonra uygula.

Yanıtlar Türkçe, kısa ve net olmalı. Tablo gerekiyorsa Telegram uyumlu bullet kullan.

---

🤖 *Bu skill Hermes Agent tarafından oluşturuldu*
