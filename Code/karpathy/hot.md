# Hot Cache — En Son Bilginin Özeti

**Son güncelleme:** 2026-05-09  
**Amaç:** Claude her oturumda önce bunu okur. 500 kelime max. Index'ten önce geliyor.

---

## Bu Wiki Ne İçin?

LLM/Yapay Zeka alanındaki kaynakları (Karpathy videoları, makaleler, notlar) kalıcı, aranabilir bir bilgi arşivine dönüştürmek. Andrej Karpathy'nin "LLM Wiki" konseptini uyguluyoruz.

## Son Eklenen İçerikler

- `raw/articles/karpathy-llm-wiki-rehberi-tr.md` — Türkçe LLM Wiki kurulum rehberi (Karpathy konsepti, INGEST/QUERY/LINT workflow'ları, hot.md kavramı)
- `karpathy-ozet.md` — Knowledge Pipeline sistemi özeti (RAW→WIKI←SCHEMA mimarisi)

## Aktif Kavramlar

- **LLM Wiki** — RAG'a alternatif, sadece markdown dosyalarıyla çalışan bilgi sistemi
- **INGEST** — Ham kaynak → wiki sayfası dönüşüm operasyonu  
- **QUERY** — Index'ten başlayıp ilgili sayfaya giderek cevap üretme
- **LINT** — Periyodik wiki sağlık kontrolü (orphan, çelişki, eksik link)
- **hot.md** — 500 kelimelik sıcak önbellek (bu dosya)

## Sistem Durumu

- Vault kuruldu: ✅
- Klasör yapısı: ✅ (raw/, sources/, entities/, concepts/, decisions/, syntheses/, archive/)
- CLAUDE.md: ✅
- index.md: ✅
- log.md: ✅
- hot.md: ✅ (yeni eklendi)
- İlk içerik ingest: ❌ (henüz yapılmadı)

## Bir Sonraki Adım

İlk gerçek kaynağı ingest etmek. Önerilen: `raw/articles/karpathy-llm-wiki-rehberi-tr.md`
