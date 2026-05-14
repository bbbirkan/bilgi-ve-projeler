# claude-website-builder (10.000 Dolarlık Web Sitesi İş Akışı)

**Ne işe yarar:**
Hiçbir tasarım (UI/UX) veya kodlama geçmişi gerektirmeden, Claude Code yapay zeka ajanını kullanarak profesyonel, temiz ve Framer Motion animasyonlarına sahip, premium kalitede bir web sitesi üretmenizi sağlayan 4 adımlık bir iş akışıdır.

**Nasıl çalışır:**
Klasik ve kısıtlayıcı şablonlar (template) kullanmak yerine; Anthropic'in terminal ajanı Claude Code'u "UI UX Pro Max Skill" yeteneğiyle tasarımsal açıdan eğitir. Gerekli pürüzsüz geçişleri Framer Motion ile sağlar ve modern, göze hitap eden bileşenleri (component) 21st.dev kütüphanesinden çekerek siteyi otomatik olarak inşa eder.

**Ne zaman kullanılır:**
- Hızlıca (yaklaşık 5 dakikada) prodüksiyon kalitesinde, animasyonlu bir web sitesi ayağa kaldırmak istendiğinde
- Kodlar tamamen sizin kontrolünüzde kalarak (vendor lock-in olmadan) özelleştirilebilir bir siteye ihtiyaç duyulduğunda
- Sıfırdan tasarım yapmadan 21st.dev gibi kütüphanelerden premium arayüz bileşenleri kullanılmak istendiğinde

**Kurulum ve kullanım:**
Bu akışı kullanabilmek için bilgisayarınızda **Node.js** yüklü olmalıdır. Ardından sırasıyla şu adımlar izlenir:

1. **Claude Code'u Kurun:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
2. **Projenize Framer Motion'ı Ekleyin (Terminali proje dizininde açarak):**
   ```bash
   npm install framer-motion
   ```
3. **Tasarım Yeteneğini (Skill) Yükleyin:**
   İndirdiğiniz "UI UX Pro Max Skill" dosyasını Claude Code içerisindeyken yüklemesi için direktif verin.
4. **Bileşenleri (Components) Ekleyin:**
   `https://21st.dev` adresine gidin, beğendiğiniz bileşenin entegrasyon satırını kopyalayın ve Claude Code'a yapıştırın. Yapay zeka kalanı sizin yerinize halledecektir.

**Limitler / dikkat edilecekler:**
- Bu sürecin işlemesi için aktif bir internet bağlantısına ve Terminal (Mac/Linux/Windows) erişimine ihtiyaç vardır.
- Belirtilen "UI UX Pro Max" isimli skill dosyasının önceden edinilmiş ve bilgisayarda hazır bulunması gerekir.
- Framer Motion kurulumunun mutlaka kod projesinin oluşturulduğu (package.json bulunan) ana dizinde yapılması kritik önem taşır.
