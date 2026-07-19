---
name: kermes
description: |
  Kermes projesi — lansman stratejisi, rakip analizi, GitHub büyüme planı.
  Kermes: Hermes üzerine kurulu AI maliyet optimizasyon katmanı.
  Ana fikir: "$" prefix → API (ücretli), "$" yok → Orchester (ücretsiz).
  GitHub: github.com/bbbirkan/2026-kermes

  TRIGGER bu skill'i şu durumlarda çağır:
  - "kermes lansmanı", "nasıl büyütürüz", "github trending" konuşulduğunda
  - Product Hunt, Hacker News, Reddit lansman planı sorulduğunda
  - Kermes mimarisi veya rakip karşılaştırması istendiğinde
  - "kermes nedir", "kermes nasıl çalışır" sorulduğunda
---

# Kermes — AI Maliyet Optimizasyon Katmanı

## Nedir

Hermes üzerine kurulu router. Tek kural:
- `$` ile başlayan mesaj → API (metered)
- Normal mesaj → Orchester (Claude CLI + OpenCode + AGY, sıfır token maliyeti)

**GitHub:** github.com/bbbirkan/2026-kermes
**Yerel:** `/Users/birkan/Desktop/Work /2026 Kermes/`

## Mimari

```
Kullanıcı mesajı
      │
      ├── "$..." → API (DeepSeek/GPT/Claude API)
      │
      └── normal → Orchester → Claude CLI + OpenCode + AGY
                               (subscription, $0 per query)
```

## Rakip Analizi

| Araç | Odak | GitHub ⭐ | Tehdit |
|------|------|-----------|--------|
| OpenClaw | Kişisel asistan, 22+ platform | 372K+ | Farklı segment |
| LiteLLM | 100+ provider proxy | ~35K | Doğrudan rakip |
| RouteLLM | ML classifier routing | ~15K | Doğrudan rakip |
| Bifrost | Go tabanlı AI gateway | Yükselen | Doğrudan rakip |

**Kermes'in farkı:** Subscription CLI'ları (Claude, OpenCode, AGY) ücretsiz backend olarak kullanır. Rakipler hep API → API router.

## Lansman Sıralaması

1. **GitHub** → README güçlü, demo GIF ekle, topics: `hermes`, `llm-router`, `ai-cost`
2. **Hacker News** → "Show HN: I built a router that uses $0 API calls for 80% of queries"
3. **Reddit** → r/LocalLLaMA, r/MachineLearning
4. **Product Hunt** → Hazırlık: demo video, maker comment'ler

## Zamanlama

- **GitHub Trending:** Salı-Çarşamba, 09:00-11:00 ET
- **HN Show HN:** Pazartesi-Çarşamba, 08:00-10:00 ET
- **Product Hunt:** 00:01 PT (herhangi bir gün)

## Mesajlaşma

Çekici: "Your subscriptions are sitting idle while your API meter runs."
Rakip pozisyon: "Not API → API. Subscription → free. API → only when you ask."
