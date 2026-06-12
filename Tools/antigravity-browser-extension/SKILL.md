---
name: antigravity-browser-extension
description: Antigravity tarayıcı eklentisini ve browser_subagent yeteneklerini kullanarak otonom web gezinmesi ve otomasyon.
---

# Antigravity Browser Extension Skill

Bu yetenek (skill), Antigravity Chrome Eklentisi (Antigravity Browser Extension) kullanılarak web tarayıcısı üzerinde otonom işlemler gerçekleştirmeyi sağlar.

## Ne Zaman Kullanılmalı?
- "Şu web sitesini aç ve test et" dendiğinde.
- "Tarayıcıda şu işlemi yap (form doldur, butona tıkla)" dendiğinde.
- UI/UX değişikliklerinin canlı olarak tarayıcıda görülmesi ve doğrulanması (browser-in-the-loop) gerektiğinde.
- Tarayıcıda yapılan bir işlemin video/ekran kaydının alınması istendiğinde.

## Nasıl Kullanılır?
Doğrudan `browser_subagent` aracını çağırarak bu eklentiyi kullanırsın.

```json
{
  "TaskName": "Örnek Tarayıcı Görevi",
  "TaskSummary": "Google'da arama yapma ve ilk sonuca tıklama",
  "Task": "https://google.com adresine git, arama kutusuna 'Antigravity IDE' yaz, enter'a bas ve ilk çıkan sonuca tıkla. İşlem bitince sayfa başlığını raporla.",
  "RecordingName": "google_arama_testi"
}
```

## Kritik Kurallar
1. Eklenti, Antigravity uygulamasının arka planda çalışmasını gerektirir. Eğer eklenti bağlantı hatası veriyorsa, kullanıcıdan Antigravity IDE'yi yeniden başlatmasını veya eklenti izinlerini kontrol etmesini iste.
2. Tüm tarayıcı etkileşimleri otomatik olarak kaydedilir (WebP video olarak artifacts klasörüne). 
3. Subagent'a verdiğin görev (Task) son derece detaylı ve net olmalıdır. Ne yapacağını, nerede duracağını ve tam olarak neyi raporlaması gerektiğini belirtmelisin.
