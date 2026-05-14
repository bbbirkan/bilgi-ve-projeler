# marketingskills

**Ne işe yarar:**
Claude Code ve diğer yapay zeka ajanları (AI agents) için pazarlama odaklı görevleri (SEO, metin yazarlığı, CRO, analitik vb.) yerine getirmelerini sağlayan yetenekler (skills) koleksiyonudur. Ajanların pazarlama işlerini daha iyi kavramasına ve en iyi uygulamaları (best practices) kullanmasına yardımcı olur.

**Nasıl çalışır:**
Her bir yetenek, ajanlara belirli pazarlama görevleri için özel bilgi ve iş akışları sağlayan bir markdown dosyasıdır (`.md`). Sistem, tüm yeteneklerin referans aldığı bir ana `product-marketing-context` dosyası üzerinden çalışır ve ajanlar bu sayede ürününüzü, hedef kitlenizi ve pazar konumlandırmanızı anlayıp birbirine bağlı yetenekleri (örn. SEO ↔ Metin Yazarlığı) birbiriyle tutarlı bir şekilde uygular.

**Ne zaman kullanılır:**
- AI ajanlarına (Claude Code, Cursor vb.) pazarlama odaklı görevler yaptırmak istediğinizde
- Dönüşüm optimizasyonu (CRO), A/B test kurguları veya açılış sayfası (landing page) iyileştirmeleri yaparken
- Soğuk e-posta (cold email) dizileri, satış metinleri veya reklam kopyaları oluştururken
- Teknik SEO denetimi (SEO audit), analitik kurulumu veya büyüme mühendisliği (growth engineering) taktiklerini hayata geçirirken

**Kurulum ve kullanım:**
Repo projede bulunduğunda güncellemeleri çekebilirsiniz:
```bash
# Repo içinde güncel kalmak için:
git pull

# Projenize yetenekleri eklemek için CLI komutu (önerilen):
npx skills add coreyhaines31/marketingskills

# Claude Code plugin olarak eklemek için (Claude Code içerisinden):
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills
```

**Limitler / dikkat edilecekler:**
- Her proje için `product-marketing-context.md` dosyasının mutlaka oluşturulması ve ürün/hedef kitle bilgilerinin doldurulması gerekir.
- Kullanılacak ajanın (AI tool) Agent Skills standartlarını (`.agents/skills/` veya benzeri klasör yapılarını) okuyabiliyor olması gereklidir.
- Sadece referans bir kaynak / komut setidir; tam otomatik bir bot değil, sizin kullandığınız AI ajanını pazarlama konusunda yönlendiren kural setlerinden oluşur.
