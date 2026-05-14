# LLM Council — SKILL.md

Karpathy'nin LLM Council metodolojisinden ilham alan bu skill, herhangi bir soruyu veya kararı 5 bağımsız AI danışmandan geçirir, onlara birbirlerini anonim olarak değerlendirtir ve tek bir net verdict üretir.

## Ne İşe Yarar

Tek bir AI'a soru sorduğunda tek bir bakış açısı alırsın. LLM Council bunu çözer: soruyu 5 farklı düşünce stiliyle analiz eder, peer-review yaptırır, chairman tüm çıktıları sentezler. Belirsizliği ortadan kaldırmak için tasarlanmış.

## Nasıl Çalışır

1. **Frame** — Soruyu workspace context'iyle zenginleştirip netleştirir
2. **5 Danışman (paralel)** — Her biri kendi açısından bağımsız analiz yazar
3. **Peer Review (paralel)** — Anonim yanıtlar çapraz değerlendirilir
4. **Chairman Sentezi** — Uzlaşılar, çakışmalar, kör noktalar + net öneri
5. **Verdict** — Chat'te direkt markdown çıktısı

## 5 Danışman

| Danışman | Bakış Açısı |
|----------|-------------|
| **The Contrarian** | Neyin yanlış gidebileceğini arar, fatal flawları tespit eder |
| **First Principles Thinker** | Varsayımları söküp "asıl sorun ne?" diye sorar |
| **The Expansionist** | Herkesin gözden kaçırdığı upside'ı ve potansiyeli arar |
| **The Outsider** | Sıfır bağlamla bakar, expert körleşmesini engeller |
| **The Executor** | "Pazartesi sabahı ne yaparsın?" — sadece icraata bakar |

## Ne Zaman Kullanılır

Tetikleyici ifadeler:
- `council this` / `run the council` / `war room this`
- `pressure-test this` / `stress-test this` / `debate this`
- Gerçek bir tradeoff içeren "Should I X or Y?" soruları

**Kullanılmaz:** Basit evet/hayır, faktüel sorular, yaratım görevleri ("tweet yaz").

## Kullanım

```
council this: [karar veya soru]
```

Örnek:
```
council this: $297'lik Claude Code kursu mu yapsam yoksa ücretsiz kaynak mı? 
Kitlem non-technical solopreneurs.
```

## Limitler

- 10 dakika altı sorular için overkill — basit sorularda kullanma
- En iyi gerçek tradeoff + stake olan kararlarda çalışır
- Transcript kaydı isteğe bağlı (`active/council-transcript-[timestamp].md`)
