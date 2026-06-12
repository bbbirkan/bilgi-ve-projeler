# Antigravity Browser Extension

**URL:** https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd?pli=1

## Nedir?
Google Antigravity platformu için geliştirilmiş resmi Chrome eklentisidir. Yapay zeka ajanlarının (benim gibi) tarayıcıyı "görmesine" ve web siteleriyle etkileşime girmesine olanak tanıyan bir köprü görevi görür.

## Temel Özellikler
1. **Tarayıcı Otomasyonu:** Ajanların web sitelerini açmasını, okumasını, gezinmesini, tıklamasını ve kaydırmasını sağlar.
2. **Agentic Geri Bildirim (Browser-in-the-loop):** Geliştirme sürecinde ajanların kod değişikliklerini (özellikle UI güncellemelerini) canlı bir tarayıcı ortamında doğrulamasını sağlar.
3. **Kayıt ve Analiz:** Ajanın tarayıcı üzerinden yaptığı işlemleri otomatik olarak WebP video ve ekran görüntüsü formatında kaydeder.

## Kullanım Amacı (Birkan İçin)
- Web uygulamalarının QA (Kalite Güvence) testlerinin otomatikleştirilmesi.
- Karmaşık web formlarının doldurulması, veri kazıma (scraping) ve araştırma görevleri için doğrudan `browser_subagent` aracıyla tam entegrasyon.
- N8N webhook'ları, Coolify panelleri ve diğer web tabanlı araçların yönetiminde görsel geri bildirim döngüsü oluşturmak.

## Kurulum ve Konfigürasyon
- **Yükleme:** Chrome Web Mağazası'ndan doğrudan yüklenir.
- **İzinler:** Ajanın tarayıcıyla iletişim kurabilmesi için eklentiye "debugging session" başlatma izni verilmelidir.
- **Entegrasyon:** Antigravity IDE içindeki `browser_subagent` komutu, doğrudan bu eklenti üzerinden çalışır.
