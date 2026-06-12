# Antigravity Browser Extension

**URL:** https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd?pli=1

## Nedir?
Google Antigravity platformu için geliştirilmiş resmi Chrome eklentisidir. Yapay zeka ajanlarının tarayıcıyı "görmesine", test etmesine, canlı sayfa renderlamasına ve web uygulamalarıyla etkileşime girmesine olanak tanır. MCP (ChromeDevTools, Playwright) alternatiflerine kıyasla teknik olmayan kullanıcılar için çok daha kolaydır ve otomatik kayıt yeteneklerine sahiptir.

## Teknik Altyapı ve Kayıt (Recording) Mimarisi
- **Özel Model:** Tarayıcıdaki aksiyonlar (tıklama, form doldurma, kaydırma) ana model yerine özel olarak eğitilmiş **`Gemini 2.5 Pro UI Checkpoint`** modeli tarafından yönetilir.
- **Otomatik Kayıt (Auto-save):** Ajan tarayıcıyı kullanırken arka planda sürekli kayıt alır.
  - Önemli anların (key moments) fotoğraf ve videoları şu dizinde tutulur: `~/.gemini/antigravity-ide/brain/<session_id>/`
  - Tüm oturumun devasa ekran görüntüsü arşivi şu dizinde tutulur: `~/.gemini/antigravity-ide/browser_recordings/`
- **User Agent & Kısıtlamalar:** Playwright/Puppeteer'a göre daha temiz bir User Agent sunar ancak güvenlik politikaları gereği **Captcha türü bulmacaları çözmeyi reddeder**.

## Temel Özellikler ve Güvenlik Modeli
1. **Görsel Geri Bildirim ve Otomatik Test:** Ajan uygulamayı kodlarken gerçek zamanlı olarak arayüzü test eder.
2. **Görsel Anotasyonlar (Visual Annotations):** Kullanıcı ekran görüntüsünün bir bölümünü işaretleyip (highlight) notlar bırakabilir; ajan bu notlara göre kodu günceller.
3. **Isolated Profile (İzole Profil):** Ajanın işlemleri tamamen ayrı bir Chrome profili içinde çalışır.
4. **Allowlist & Denylist:** Ajanın hangi URL'lere erişebileceği IDE'nin "Browser" ayarlarından yönetilir.

## Gelişmiş Kullanım İş Akışları (Advanced Workflows)
- **UX & Front-end Research:** Antigravity'ye belirli referans tasarım sitelerini gezdirip otomatik olarak biriktirdiği ekran görüntülerini ve videoları, yeni tasarım fikirleri veya Stitch + Nano Banana Pro gibi AI kurgularına girdi (referans kütüphanesi) olarak sunabilirsiniz.

## Kurulum ve Tetikleme
- **Otomatik Tetikleme:** IDE'de web gerektiren bir komut verdiğinizde (ör: "Help me test this web app") ajan izin ister.
- **Kurulum:** Chat panelindeki mavi "Setup" butonuyla Chrome Web Store'dan kurulur.
- **Manuel Çağrı:** Ajanı tarayıcı için manuel tetiklemek isterseniz `/browser` komutunu kullanabilirsiniz.
