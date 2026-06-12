---
name: antigravity-browser-extension
description: Antigravity tarayıcı eklentisini, izole Chrome profilini ve /browser slash komutunu kullanarak otonom web gezinmesi, canlı test ve UI otomasyonu.
---

# Antigravity Browser Extension Skill

Bu yetenek (skill), Antigravity Chrome Eklentisi kullanılarak web tarayıcısı üzerinde otonom test ve UI etkileşimi gerçekleştirmeyi sağlar.

## Ne Zaman Kullanılmalı?
- "Şu web uygulamasını test et" dendiğinde.
- "Tarayıcıda şu işlemi yap" veya "Google'a git" dendiğinde.
- UI/UX değişikliklerinin canlı olarak tarayıcıda görülmesi ve doğrulanması (browser-in-the-loop) gerektiğinde.
- `/browser` slash komutu üzerinden spesifik bir tarayıcı görevi istendiğinde.

## Nasıl Kullanılır?
1. Doğrudan `browser_subagent` aracını çağırarak bu eklentiyi kullanabilirsin.
2. Kullanıcı chat ekranında `/browser <komut>` yazdığında otomatik olarak tarayıcı görevi başlar.

## Kritik Kurallar
1. **İzole Profil & Güvenlik:** Ajanın etkileşimleri kullanıcının kişisel verilerini korumak için ayrı bir (isolated) Chrome profilinde çalışır.
2. **Kayıt ve Anotasyon:** Tüm tarayıcı etkileşimleri kaydedilir. Kullanıcılar görsel ekran görüntüsünde (screenshot) alan işaretleyerek "Buraya buton ekle" gibi görsel notlar (Visual Annotations) bırakabilir. Ajan bu notları dikkate alarak kodu düzenler.
3. **Sorun Giderme:** "failed to resolve CDP URLs" gibi eklenti bağlantı hataları alınırsa, kullanıcıya Antigravity IDE'yi yeniden başlatmasını ve mavi "Setup" butonundan izinleri/yüklemeyi kontrol etmesini söyleyin.
4. **URL İzinleri:** Eğer ajan belirli bir URL'ye gidemiyorsa, bunun IDE "User Settings > Browser" kısmındaki Allowlist/Denylist yüzünden engellenip engellenmediğini kontrol etmesini söyleyin.
