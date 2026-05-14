# superpowers (Proje Müdürü)

**Ne işe yarar:**
Claude Code'un doğrudan koda atlamak yerine önce plan yapmasını, test yazmasını ve ürettiği işi incelemesini (review) sağlayan "Proje Müdürü" yeteneğidir. Toplulukta 136K GitHub yıldızına sahiptir.

**Nasıl çalışır:**
Kod yazım sürecini parçalara bölerek proje yönetimi mantığıyla ilerler. Geliştirmeye başlamadan önce bir yol haritası (plan) çıkarır, testleri kurgular ve kodlamayı bitirdikten sonra kendi ürettiği kodu kalite kontrolden geçirir.

**Ne zaman kullanılır:**
- Karmaşık ve büyük projelerde direkt kodlama yerine planlı ve kontrollü ilerlemek gerektiğinde
- Claude'un "Proje müdürü" perspektifiyle kod geliştirme sürecini denetlemesi istendiğinde
- Kendi yazdığı kodu test edip kalitesini artırarak hata oranını düşürmesi beklendiğinde

**Kurulum ve kullanım:**
```bash
git clone https://github.com/obra/superpowers
```

**Limitler / dikkat edilecekler:**
- Ajanın planlama, test ve review gibi ekstra adımları gerçekleştirmesi işlem süresini ve harcanan token miktarını (maliyetini) artırabilir.
- Hızlı ve ufak tefek değişiklikler (hotfix) için biraz fazla prosedürel gelebilir.
