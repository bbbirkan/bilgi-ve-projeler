# seo — SEO Plugin (v2)

Claude Code için 4 komutlu, veri odaklı içerik SEO pipeline'ı. Kurulumdan fırsat bulmaya, brief oluşturmaya ve makale yazmaya kadar tam döngüyü kapsar.

## Ne İşe Yarar

Bir web sitesi için SEO içerik stratejisi oluşturur. Ahrefs / SEMrush / DataForSEO gibi gerçek SEO verisini MCP üzerinden çeker, fırsatları önceliklendirir, data-backed brief hazırlar ve yayına hazır makale yazar. 4 komut, tam pipeline.

## Nasıl Çalışır

| Komut | Ne Yapar |
|-------|----------|
| `/start-here` | Tek seferlik kurulum — marka sesi, site profili, rakip analizi oluşturur |
| `/find-opportunities` | Keyword fırsatlarını keşfeder ve önceliklendirir |
| `/create-brief` | Seçilen fırsat için data-backed içerik brief'i oluşturur |
| `/write-content` | Brief'ten yayına hazır makale yazar |

**Otomatik skill yükleme:** Komutlar bağlama göre doğru skill'i (seo-analysis, brief-building, humanizer, brand-voice, reports) otomatik devreye alır.

## Ne Zaman Kullanılır

- Blog / web sitesi için SEO içerik üretmek istediğinde
- Rakip keyword analizi yapıp fırsat bulmak istediğinde
- Marka sesine uygun, insan gibi yazan içerik üretmek istediğinde
- SERP analizi + içerik brief sürecini otomatikleştirmek istediğinde

## Kurulum

**Minimum gereksinim:**

| Hedef | Gereksinim |
|-------|------------|
| Sadece marka sesi + site profili | Hiçbir şey (WebFetch built-in) |
| JS rendering + tam site haritası | Firecrawl |
| Keyword araştırma | Ahrefs, DataForSEO veya SEMrush'tan biri |
| Tam pipeline | Firecrawl + SEO data provider |

**MCP config:** `.mcp.json` dosyasına API key'leri ekle, sonra oturumu yeniden başlat.

```json
// DataForSEO örneği
"dataforseo": {
  "type": "stdio",
  "command": "npx",
  "args": ["dataforseo-mcp-server"],
  "env": {
    "DATAFORSEO_USERNAME": "email@example.com",
    "DATAFORSEO_PASSWORD": "api-password"
  }
}
```

**Başlatma:** `/start-here` — her şeyi sırayla kurar.

## Çıktı Yapısı

```
brand/
├── brand-voice.md       ← Marka sesi profili
├── competitors.md       ← Rakip profilleri (14 günlük cache)
└── site-profile.md      ← Domain metrikleri (7 günlük cache)

campaigns/
└── YYYY-MM-DD/
    ├── daily-opportunities.html
    ├── {slug}-brief.html
    ├── {slug}-article.md
    └── screenshots/
```

## Limitler

- SEO veri provider olmadan `/find-opportunities` çalışmaz (hard stop)
- Private/JS-heavy siteler için Firecrawl gerekli, yoksa WebFetch fallback
- Ahrefs ve SEMrush aktif abonelik gerektiriyor
