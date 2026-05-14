# LLM Wiki — Şema (Anayasa)

Bu dosya, LLM ajanının (Claude, vb.) bu vault'u nasıl yöneteceğini tanımlar.
Ajan bu dosyayı her oturumda okur ve kurallara uyar.

---

## Amaç

Bu wiki, **LLM / Yapay Zeka** alanındaki kaynakları (Andrej Karpathy videoları, makaleler,
notlar, transkriptler) kalıcı, aranabilir ve birikimli bir bilgi arşivine dönüştürür.

Odak soruları:
- Transformerlar, dikkat mekanizması, tokenizasyon nasıl çalışır?
- LLM eğitimi, fine-tuning, RLHF süreçleri nasıl işler?
- Pratik LLM kullanımı ve mühendislik pratikleri nelerdir?

---

## Klasör Yapısı

| Klasör | İçerik |
|--------|--------|
| `raw/articles/` | Ham makaleler, web scrape'leri, markdown'a çevrilmiş blog yazıları |
| `raw/papers/` | Akademik makaleler (PDF veya markdown) |
| `raw/transcripts/` | Video/podcast transkriptleri (YouTube, vb.) |
| `raw/assets/` | Resimler, görseller, ekran görüntüleri |
| `sources/` | Her ham kaynak için LLM tarafından yazılmış özet sayfası |
| `entities/` | Kişiler, modeller, organizasyonlar, ürünler |
| `concepts/` | Soyut kavramlar, terimler, algoritmalar |
| `decisions/` | Alınan kararlar ve gerekçeleri |
| `syntheses/` | Çok kaynaktan sentez, karşılaştırmalar |
| `archive/` | Eski/stale sayfalar (silinmez, buraya taşınır) |

**`raw/` immutable'dır — ajan asla yazmaz, sadece okur.**

---

## Sayfa Formatı

Her wiki sayfası şu frontmatter ile başlar:

```yaml
---
tags: [concept|entity|source|synthesis|decision]
source: raw/... (varsa)
date: YYYY-MM-DD
status: draft|active|stale
---
```

Başlık sırası:
1. `# Başlık`
2. Tek satır özet
3. `## Temel Bilgiler`
4. `## Kaynaklar` (hangi raw dosyadan geldi)
5. `## Bağlantılar` (`[[link]]` formatında)

---

## Naming Convention

- Dosya adları: `kebab-case.md` (küçük harf, tire ile)
- Varlık sayfaları: gerçek isim (`andrej-karpathy.md`)
- Kavram sayfaları: İngilizce terim (`attention-mechanism.md`)
- Source sayfaları: `src-` prefix (`src-karpathy-makemore-video.md`)
- Synthesis sayfaları: `syn-` prefix (`syn-llm-training-overview.md`)

---

## INGEST Workflow

Yeni kaynak geldiğinde sırasıyla:

1. `raw/` içine uygun alt klasöre koy (kullanıcı yapar)
2. Ajan kaynağı okur
3. Ajan anahtar çıkarımları kullanıcıyla kısaca tartışır
4. `sources/src-[isim].md` özet sayfası yazar
5. `index.md`'yi günceller
6. İlgili `entities/` ve `concepts/` sayfalarını günceller veya oluşturur
7. Çelişki varsa ilgili sayfada işaretler (`> ⚠️ Çelişki:`)
8. `log.md`'ye zaman damgalı giriş ekler

---

## QUERY Workflow

Soru geldiğinde:

1. `index.md` okunur
2. İlgili sayfalar belirlenir ve okunur
3. Cevap sentezlenir, her iddia için `[[kaynak]]` referansı verilir
4. Eğer cevap değerliyse → `syntheses/syn-[konu].md` olarak dosyalanır
5. `log.md`'ye query kaydedilir

---

## LINT Workflow (Periyodik — ayda bir veya istendiğinde)

Kontrol edilecekler:
- Hiçbir yerden link almayan orphan sayfalar
- `status: stale` olanlar
- Çelişki işaretleri (`⚠️`) çözüme kavuşmuş mu?
- `index.md`'de eksik sayfalar var mı?
- Tek yönlü linkler (A→B var ama B→A yok)

---

## Yasaklar (Ajan asla yapmamalı)

- `raw/` klasörüne yazma veya değiştirme
- Kaynaksız iddia üretme
- Sayfa silme (sadece `archive/` klasörüne taşıma)
- Mevcut linkleri kontrol etmeden link kullanma
- `log.md`'ye yazmayı atlama

---

## Evrim Notu

Bu şema zamanla değişebilir. Yeni kural eklendiğinde:
- `CLAUDE.md` güncellenir
- `log.md`'ye `[tarih] schema-update | açıklama` kaydedilir
- Eski sayfalar yeni kurala göre yavaş yavaş güncellenir (tek seferlik toplu dönüşüm yapılmaz)
