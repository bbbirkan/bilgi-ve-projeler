# Knowledge Pipeline

> Türkçe sunum + LLM-Wiki skill'i. Ham sohbetleri, bir şemayla disipline edilen, aranabilir ve büyüyen bir wiki'ye dönüştürme deseni.

## İçerik

- **[index.html](./index.html)** — Terminal/matrix estetiğiyle tek dosyalık sunum. 8 sahne, SPACE ile sahne sahne ilerler. YouTube videoları için hazır.
- **[SKILL.md](./SKILL.md)** — `llm-wiki` skill'i. Claude Code veya başka bir LLM ajanıyla kalıcı, birikimli bir bilgi arşivi inşa etmek için genel-amaçlı desen.
- **[PROMPTS.md](./PROMPTS.md)** — Üç hazır prompt (INGEST / QUERY / LINT). Placeholder'larla configurable. Kopyala-yapıştır hazır.

## Sunumu aç

Canlı versiyon (GitHub Pages):
```
https://selmakcby.github.io/knowledge-pipeline/
```

Lokalde:
```bash
open index.html
```

Kontroller: `SPACE` / `CLICK` ile ilerlet · `R` ile sıfırla · `←` ile geri al

## Skill'i kullanma

`SKILL.md`'yi LLM ajanına göster (Claude Code, Codex, vb.) ve "bu desen'e göre bana bir vault kur" de. Ajan klasör yapısını, `CLAUDE.md` şemasını, `index.md` ve `log.md` iskeletini üretir.

Alan-bağımsız: araştırma, kitap okuma, ürün geliştirme, kişisel gelişim, takım wiki'si — hepsi için aynı pattern.

## Desen özeti

```
RAW (immutable)  →  WIKI (LLM writes)  ←  SCHEMA (disciplines)
     ↓                     ↓                      ↓
 ham kaynaklar         markdown graf         anayasa dosyası
```

Üç operasyon:
- **INGEST** — yeni kaynak geldiğinde wiki'ye entegre et, çapraz-referansları güncelle
- **QUERY** — soruları wiki üzerinden cevapla, iyi cevapları yeni sayfa olarak geri-dosyala
- **LINT** — periyodik sağlık kontrolü: çelişkiler, orphan'lar, eksik bağlantılar

Daha fazla detay için [SKILL.md](./SKILL.md)'ye bak.

## Lisans

MIT. İstediğin gibi kullan, değiştir, paylaş.
