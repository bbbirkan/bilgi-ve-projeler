# knowledge-pipeline

Ham sohbet/kaynak → disiplinli, aranabilir, büyüyen wiki dönüşüm deseni. Türkçe sunum + `llm-wiki` Claude Code skill'i + 3 hazır prompt. Selma Kocabıyık'ın video içeriğinden.

**Canlı sunum:** https://selmakcby.github.io/knowledge-pipeline/

## Ne İşe Yarar

LLM'in ham girdileri (sohbetler, notlar, makaleler) tutarlı, birikimli bir knowledge base'e dönüştürmesini sağlayan yapısal desen. Wiki bir şema (anayasa) tarafından disipline edilir — LLM keyfi yazmaz, kurallara göre yazar.

```
RAW (immutable)  →  WIKI (LLM writes)  ←  SCHEMA (disciplines)
     ↓                     ↓                      ↓
 ham kaynaklar         markdown graf         anayasa dosyası
```

## 3 Temel Operasyon

| Operasyon | Ne zaman | Ne yapar |
|-----------|----------|----------|
| **INGEST** | Yeni kaynak gelince | Wiki'ye entegre et, çapraz-referansları güncelle |
| **QUERY** | Soru sorulunca | Wiki üzerinden cevapla, iyi cevapları yeni sayfa yap |
| **LINT** | Periyodik | Çelişkiler, orphan'lar, eksik bağlantıları bul |

## Repo İçeriği

| Dosya | Açıklama |
|-------|----------|
| `index.html` | Terminal/matrix estetiğiyle 8 sahnelik sunum. `SPACE` ile ilerler |
| `SKILL.md` | `llm-wiki` skill — vault kurmak için Claude Code'a göster |
| `PROMPTS.md` | INGEST / QUERY / LINT için kopyala-yapıştır hazır 3 prompt |

## Nasıl Kullanılır

```bash
# Sunumu lokalde aç
open index.html
# Kontroller: SPACE/CLICK ilerlet · R sıfırla · ← geri al
```

**Skill'i Claude Code'a vermek için:**
```
SKILL.md'yi göster ve "bu desene göre bana bir vault kur" de
→ Ajan klasör yapısını, CLAUDE.md şemasını, index.md ve log.md iskeletini üretir
```

## Alan Bağımsızlığı

Aynı pattern şunlar için çalışır:
- Araştırma notları
- Kitap okuma arşivi
- Ürün geliştirme wiki'si
- Kişisel gelişim takibi
- Takım dokümantasyonu

## Ne Zaman Kullanılır

- Ham sohbet/not yığınının biriktiğini, ama aranabilir olmasını istiyorsan
- LLM'in her seferinde sıfırdan başlamak yerine öğrendiklerini biriktirmesini istiyorsan
- Claude Code'a alan-spesifik bir wiki inşa ettirmek istiyorsan

**Kaynak:** [selmakcby/knowledge-pipeline](https://github.com/selmakcby/knowledge-pipeline) · MIT
