---
name: antigravity-browser-extension
description: Antigravity tarayıcı eklentisini, izole Chrome profilini ve /browser slash komutunu kullanarak otonom web gezinmesi, canlı test ve UI otomasyonu.
---

# Antigravity Browser Extension Skill

Bu yetenek (skill), Antigravity Chrome Eklentisi kullanılarak web tarayıcısı üzerinde otonom test, araştırma ve UI etkileşimi gerçekleştirmeyi sağlar.

## Ne Zaman Kullanılmalı?
- "Şu web uygulamasını test et" dendiğinde.
- "Rakip siteleri gez ve UX analizi yap" dendiğinde (Otomatik alınan ekran görüntüleri referans olarak kullanılır).
- UI/UX değişikliklerinin canlı olarak tarayıcıda görülmesi ve doğrulanması (browser-in-the-loop) gerektiğinde.
- `/browser` slash komutu üzerinden spesifik bir tarayıcı görevi istendiğinde.

## Nasıl Kullanılır?
1. Doğrudan `browser_subagent` aracını çağırarak bu eklentiyi kullanabilirsin.
2. Kullanıcı chat ekranında `/browser <komut>` yazdığında otomatik olarak tarayıcı görevi başlar.

## Kritik Kurallar
1. **Model & Altyapı:** Tarayıcı manipülasyonu (tıklama, kaydırma vb.) için arka planda `Gemini 2.5 Pro UI Checkpoint` adlı özel model görev yapar.
2. **Kayıt (Recording) Mekanizması:** Ajanın tüm oturumu otomatik olarak `~/.gemini/antigravity-ide/browser_recordings/` ve önemli anlar `brain/<session_id>/` altına kaydedilir. Ajanı UX referans kütüphanesi oluşturmak için gezintiye yollayabilirsiniz.
3. **Captcha:** Ajan daha temiz bir User Agent kullansa da, güvenlik kuralları gereği Captcha tarzı bulmacaları kesinlikle çözmez. Bu tür sitelerde takılırsanız görevi sonlandırın.
4. **İzole Profil & Güvenlik:** Etkileşimler kullanıcının kişisel verilerini korumak için ayrı bir Chrome profilinde çalışır.
5. **Anotasyon:** Kullanıcı ekran görüntülerine (screenshot) işaretleme (highlight) yaparak yorum bırakabilir, bu görsel yorumları kod düzenlerken ana girdi olarak alın.
6. **Sorun Giderme:** "failed to resolve CDP URLs" hatası alınırsa, Antigravity IDE yeniden başlatılmalı ve "Setup" butonundan izinler kontrol edilmelidir. Erişim engelleri için "User Settings > Browser" altındaki Allowlist/Denylist'i kontrol edin.
