---
name: prompt-autoresearch
description: |
  Autoresearch pattern'ını Hermes/Claude skill promptlarına ve sistem promptlarına uygular.
  Researcher+Judge çift-ajan döngüsüyle prompt varyantları üretir, binary eval ile skorlar,
  iyileri saklar, kötüleri atar. Gece boyunca otonom prompt optimizasyonu yapar.

  TRIGGER bu skill'i şu durumlarda çağır:
  - "prompt iyileştir", "skill optimize et" istendiğinde
  - Bir Hermes skill'inin trigger oranı düşükse
  - "autoresearch prompt için" / "prompt-autoresearch başlat" dendiğinde
  - Sistem promptu veya SKILL.md açıklaması optimize edilmek istendiğinde
---

# Prompt AutoResearch — Otonom Prompt Optimizasyon Döngüsü

Autoresearch pattern'ının prompt optimizasyonuna uyarlanmış hali.
Hedef: bir Hermes skill'ini veya sistem promptunu insan müdahalesi olmadan iyileştirmek.

## Döngü Mimarisi

```
Researcher Agent
  → mevcut prompt'u okur
  → 1 varyant üretir (description, trigger, body değişikliği)
  → varyantı kaydet

Judge Agent  (hedef içeriği/zararlı örneği GÖRMEZ)
  → varyantı binary checklist'e göre değerlendirir
  → skor üretir (0-10)

Kural:
  skor > baseline → sakla, yeni baseline yap
  skor ≤ baseline → geri al
  → tekrar
```

## Binary Eval Kriterleri (Prompt için 10 Soru)

1. Trigger koşulları net ve özel mi? (muğlak kelimeler yok mu?) Evet/Hayır
2. Description tek cümlede ne yaptığını açıklıyor mu? Evet/Hayır
3. Yanlış tetiklenmeyi önleyecek SKIP koşulu var mı? Evet/Hayır
4. Skill'in çıktısı öngörülebilir ve tutarlı mı? Evet/Hayır
5. Gereksiz kelime/paragraf yok mu? Evet/Hayır
6. Komut örnekleri somut ve çalışır mı? Evet/Hayır
7. Başka bir skill ile çakışma riski var mı? (Evet = -2 puan) Evet/Hayır
8. Hermes'in anlayacağı Türkçe/İngilizce karışımı doğru mu? Evet/Hayır
9. Description, skill'i doğru senaryoda tetikler mi? Evet/Hayır
10. Kullanıcı bu promptu okumadan skill'i doğru çağırabilir mi? Evet/Hayır

*10 Evet = 10 puan. Baseline'dan yüksekse sakla.*

## Kullanım

```bash
# Hermes üzerinden başlat
hermes -z "prompt-autoresearch başlat: kermes"

# Claude Code üzerinden başlat
# Bu klasörde Claude Code'u aç ve şunu söyle:
"~/.claude/skills/kermes/SKILL.md üzerinde prompt-autoresearch döngüsü başlat.
 program.md'yi oku ve 10 iterasyon yap."
```

## program.md Şablonu

Optimize etmek istediğin skill klasörüne bu dosyayı koy:

```markdown
# Prompt Research Program

## Hedef
SKILL.md'nin description ve trigger bölümlerini optimize et.
Baseline skor: [ilk eval skorunu buraya yaz]

## Kısıtlar
- Sadece frontmatter description ve trigger satırlarını değiştir
- Her iterasyonda en fazla 3 satır değiştir
- Body (içerik) bölümüne dokunma

## Eval Prosedürü
10 soruluk binary checklist ile her varyantı değerlendir.
Skoru experiments.md'ye kaydet: [varyant] → [skor] → [karar]

## Döngü
ASLA DURMA. Skor iyileşmiyorsa farklı bir değişiklik dene.
```

## İlgili Skill'ler

- `autoresearch` — genel pattern ve Researcher+Judge framework
- `content-autoresearch` — aynı pattern, Instagram/Reels içerik optimizasyonu için
