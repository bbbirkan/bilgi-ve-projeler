# Antigravity Browser Extension

**URL:** https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd?pli=1

## Nedir?
Google Antigravity platformu için geliştirilmiş resmi Chrome eklentisidir. Yapay zeka ajanlarının tarayıcıyı "görmesine", test etmesine, canlı sayfa renderlamasına ve web uygulamalarıyla etkileşime girmesine olanak tanır.

## Temel Özellikler ve Güvenlik Modeli
1. **Görsel Geri Bildirim ve Otomatik Test:** Ajan uygulamayı kodlarken gerçek zamanlı olarak arayüzü test eder, ekran görüntüleri ve aksiyon videoları (WebP) kaydeder.
2. **Görsel Anotasyonlar (Visual Annotations):** Kullanıcı ekran görüntüsünün bir bölümünü işaretleyip (highlight) "Buraya login butonu ekle" gibi görsel notlar bırakabilir; ajan bu notlara göre kodu günceller.
3. **Isolated Profile (İzole Profil):** Ajanın işlemleri, kişisel verilerinizi korumak için tamamen ayrı bir Chrome profili içinde çalışır.
4. **Allowlist & Denylist:** Ajanın hangi URL'lere erişebileceği Antigravity IDE'nin User Settings > Browser bölümünden (İzin Verilenler/Engellenenler listesi) yönetilir.

## Kurulum ve Tetikleme
- **Otomatik Tetikleme:** IDE Playground'da web tarayıcısı gerektiren bir istek yapıldığında (ör: "Help me test this web app") ajan yetki ister.
- **Kurulum:** Chat panelindeki mavi "Setup" butonuna tıklandığında Chrome Web Store'a yönlendirilir ve "Add to Chrome" ile kurulur.
- **Manuel Çağrı (Slash Command):** Ajanı tarayıcıyı okuması veya gezinmesi için manuel yönlendirmek isterseniz chat ekranına `/browser` komutu yazarak kullanabilirsiniz.

## Kullanım Amacı (Birkan İçin)
- Web projelerinin canlı UI testi ve görsel doğrulanması.
- `browser_subagent` veya `/browser` slash komutuyla hedef URL'lerin izole ortamda otomatik çalıştırılması.
- Eklenti sorun yaratırsa User Settings'ten "Browser Tools" kapatılabilir.
