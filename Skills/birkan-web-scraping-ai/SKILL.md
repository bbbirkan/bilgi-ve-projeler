---
name: web-scraping-ai
description: |
  AI destekli web scraping rehberi. Crawl4AI + DeepSeek/Groq kombinasyonu ile
  JavaScript ağırlıklı ve Cloudflare korumalı siteleri scrape etme; Pydantic
  şema tabanlı yapılandırılmış JSON çıktısı; BeautifulSoup alternatifleri.

  TRIGGER: web scraping, crawl4ai, deepseek scraping, cloudflare bypass, html parse,
           web kazıma, site scraping, veri çekme, apify, linkedin scraping,
           instagram scraping, lead generation, google maps scraping, kişi bul, potansiyel müşteri
---

# AI Web Scraping — Crawl4AI + LLM Stack

## Ne Zaman Kullan
- JavaScript render edilmiş sayfalari scrape ederken (SPA, React, Next.js)
- Cloudflare veya diğer anti-bot sistemleri engelliyor olduğunda
- BeautifulSoup yeterli olmadığında (dinamik içerik)
- Ham HTML'den yapılandırılmış JSON çıkarmak istediğinde

---

## 2026 Standart Stack

```
Ham URL
  ↓
Crawl4AI (async DOM tarama + HTML temizleme → Markdown)
  ↓
DeepSeek V3 / Groq (ucuz LLM, Pydantic şema → JSON)
  ↓
Yapılandırılmış veri (fiyat, isim, iletişim, vb.)
```

**Neden bu kombinasyon:**
- Crawl4AI built-in HTML cleaning yapar → gereksiz nav/ad/footer çıkar
- Temiz Markdown = %70-90 token azalması (ham HTML vs Markdown)
- DeepSeek V3 / Groq = ucuz + hızlı LLM işleme
- Pydantic şema = hallüsinasyon güvenliği, tip kontrolü

---

## Temel Kullanım

```python
import asyncio
from crawl4ai import AsyncWebCrawler
from pydantic import BaseModel
import json

# 1. Çıktı şemasını tanımla
class ProductInfo(BaseModel):
    name: str
    price: float | None
    description: str
    availability: bool

# 2. Sayfayı tara ve temizle
async def scrape(url: str) -> str:
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return result.markdown   # temiz Markdown döner

# 3. LLM ile yapılandırılmış veriye çevir (DeepSeek)
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key="...",
    base_url="https://api.deepseek.com"
)

async def extract(markdown: str, schema: type[BaseModel]) -> BaseModel:
    response = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": f"Extract data as JSON matching this schema: {schema.model_json_schema()}"},
            {"role": "user", "content": markdown}
        ],
        response_format={"type": "json_object"},
    )
    return schema.model_validate_json(response.choices[0].message.content)

# Kullanım
async def main():
    md = await scrape("https://example.com/product/123")
    product = await extract(md, ProductInfo)
    print(product.model_dump())

asyncio.run(main())
```

---

## Cloudflare ve Anti-Bot Bypass

```python
# Yöntem 1: Crawl4AI playwright modu (JS render)
async with AsyncWebCrawler(
    headless=True,
    browser_type="chromium",
) as crawler:
    result = await crawler.arun(
        url=url,
        wait_for="css:.product-price",  # element yüklenmesini bekle
        js_code="window.scrollTo(0, document.body.scrollHeight)"  # lazy load
    )

# Yöntem 2: curl_cffi (Cloudflare bypass için)
from curl_cffi.requests import AsyncSession

async with AsyncSession() as session:
    response = await session.get(
        url,
        impersonate="chrome124",   # Cloudflare fingerprint bypass
        allow_redirects=True,
    )
    html = response.text
```

> **Not:** `cf_clearance` cookie'si IP'ye bağlıdır. VPS'ten aldığın cookie Mac'te çalışmaz. curl_cffi aynı makinede kullan.

---

## Toplu Scraping (Paralel)

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def scrape_many(urls: list[str], max_concurrent: int = 5) -> list[str]:
    sem = asyncio.Semaphore(max_concurrent)
    
    async def scrape_one(url: str) -> str:
        async with sem:
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=url)
                return result.markdown
    
    return await asyncio.gather(*[scrape_one(u) for u in urls])

# Ucuz Groq ile toplu işle
from groq import AsyncGroq

groq = AsyncGroq(api_key="...")

async def extract_groq(markdown: str, prompt: str) -> str:
    response = await groq.chat.completions.create(
        model="llama-3.3-70b-versatile",   # hızlı ve ucuz
        messages=[{"role": "user", "content": f"{prompt}\n\n{markdown}"}]
    )
    return response.choices[0].message.content
```

---

## Yaygın Hatalar

| Hata | Neden | Çözüm |
|------|-------|-------|
| BeautifulSoup boş döner | JS render edilen içerik | Crawl4AI playwright modunu kullan |
| Cloudflare 403 | httpx fingerprint tanındı | curl_cffi `impersonate="chrome124"` |
| LLM yanlış veri çıkardı | Prompt çok genel | Pydantic şema + JSON mode kullan |
| Token limiti aşıldı | Ham HTML gönderildi | Önce Crawl4AI ile Markdown'a çevir |
| Rate limit | Çok hızlı istek | Semaphore ile max_concurrent sınırla |

---

## Kurulum

```bash
pip install crawl4ai pydantic openai groq curl-cffi

# Playwright tarayıcıları indir (ilk kurulumda bir kez):
playwright install chromium
```

---

---

## Apify — Yönetilen Scraping Platformu (40.000+ Actor)

Crawl4AI kendin yazıyorsun. Apify hazır scraper. LinkedIn, Instagram, TikTok,
Google Maps, Reddit, Twitter gibi kendi başına erişilmesi zor sitelerde Apify kullan.

### Ne zaman Apify, ne zaman Crawl4AI?

| Durum | Araç |
|-------|------|
| Genel site, HTML temizleme yeterli | Crawl4AI + LLM |
| LinkedIn, Instagram, TikTok (oturum/fingerprint gerekir) | Apify actor |
| 40.000+ hazır scraper arasından seçim | Apify store |
| Sonuçları otomatik Supabase/Notion'a kaydet | Apify MCP Connector |
| Belirli aralıklarla otomatik çalıştır | Apify Schedules |

### Temel Kavramlar

- **Actor** — Tek bir scraping işi yapan paket. Her site için ayrı actor var.
- **Saved Task** — Aynı actorü tekrar çalıştırmak için ayar şablonu (sorgu/lokasyon önceden dolu).
- **Schedule** — Saved Task'ı otomatik çalıştır (saatlik, 6 saatte bir, günde bir vb.)
- **Dataset** — Actor'ün ürettiği yapılandırılmış JSON çıktısı. Her run'ın dataset ID'si var.
- **MCP Connector** — Dataset → Supabase/GitHub/Notion'a aktaran köprü.

### Apify + Supabase + Hermes Pipeline

```
Apify actor (LinkedIn/Google Maps/Reddit...)
       ↓ JSON dataset
Apify Universal MCP Connector
       ↓ satır satır yaz
Supabase tablosu
       ↓
Hermes Agent (SUPABASE_URL + service_role key)
       ↓ skor, analiz, sırala, ulaş
Telegram / Discord raporu + cron job
```

### Supabase kurulum (bir kez)

```sql
-- SQL Editor'da tablo oluştur
CREATE TABLE leads (
  id SERIAL PRIMARY KEY,
  profile_url TEXT UNIQUE,
  name TEXT,
  title TEXT,
  location TEXT,
  lead_score INT,
  rating TEXT,
  reasoning TEXT,
  fit_tags TEXT[],
  rated_at TIMESTAMP
);
```

Hermes için gerekli iki şey:
- `SUPABASE_URL` — Project Overview'dan kopyala
- `SUPABASE_SERVICE_ROLE_KEY` — Settings > API > Secret key

### Apify MCP Connector kurulum

1. Apify Console → Settings → API & Integrations → MCP Connectors
2. "Add a connector" → isim ver → Supabase project URL + personal access token
3. Actor store'dan "Universal MCP Connector" aç → dataset ID + MCP connector seç → çalıştır

### Hermes'e Supabase bağlama

```
Hermes'e söyle: "Find the proper place to store env keys and save these:
  SUPABASE_URL=https://xxxx.supabase.co
  SUPABASE_SERVICE_ROLE_KEY=eyJ..."
```

Sonra: "Connect to Supabase and check the leads table." → çalışıyorsa hazır.

### Hermes cron job (otomasyon)

```
Hermes'e gönder:
"Every day at 8am, read the public leads table in Supabase, find rows where
lead_score IS NULL, score each from 0-100 for fit, write back lead_score,
rating, reasoning, fit_tags, rated_at. Then send me a top-5 digest."
```

Hermes bunu otomatik cron job olarak kaydeder.

### LinkedIn Actor önerisi (oturum gerektirmeyen)

Apify store'da "LinkedIn profile scraper" ara → oturum ve cookie gerektirmeyen,
ban riski düşük actor'ü seç. Full mod: profil verisi + email arama. Max 20-50 ile test et.

### Dikkat

- LinkedIn TOS: kişisel kullanım meşru, toplu ticari kazıma gri alan. Kendi araştırmanı yap.
- Personal access token: kısa süreli oluştur (1 saat / 1 gün). Paylaşma.
- Service role key: tüm Supabase'e erişim verir. .env'de tut, commit etme.

---

## Kaynaklar
- Crawl4AI: docs.crawl4ai.com
- DeepSeek API: platform.deepseek.com
- curl_cffi: github.com/yifeikong/curl_cffi
- Apify: console.apify.com | apify.com/store
