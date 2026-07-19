---
name: antigravity-browser-extension
description: Antigravity tarayıcı eklentisini kullanarak otonom web gezinmesi, canlı test ve UI otomasyonu. "CDP hatası", "browser çalışmıyor", "failed to resolve CDP URLs", "open_browser_url", "tarayıcı aç", "web test et", "browser automation" dendiğinde kullan. Chrome'u remote debugging ile başlatma çözümünü içerir.
---

# Antigravity Browser Extension Skill

Bu skill, Antigravity Chrome Eklentisi kullanılarak web tarayıcısı üzerinde otonom test, araştırma ve UI etkileşimi gerçekleştirmeyi sağlar.

## Ne Zaman Kullanılmalı?
- "Şu web uygulamasını test et" dendiğinde
- "Rakip siteleri gez ve UX analizi yap" dendiğinde
- UI/UX değişikliklerinin canlı tarayıcıda doğrulanması gerektiğinde
- `/browser` slash komutu üzerinden tarayıcı görevi istendiğinde
- **Browser otomasyon hatası** alındığında (CDP, port, bağlantı sorunları)

## Nasıl Kullanılır?
1. `browser_subagent` aracını doğrudan çağır
2. Kullanıcı `/browser <komut>` yazdığında otomatik başlar

## Teknik Bilgiler
- **Model:** Tarayıcı aksiyonları için `Gemini 2.5 Pro UI Checkpoint` modeli kullanılır
- **Kayıt:** Tüm oturum `~/.gemini/antigravity-ide/browser_recordings/` altına kaydedilir
- **İzole Profil:** İşlemler ayrı bir Chrome profilinde çalışır
- **Captcha:** Güvenlik kuralları gereği captcha çözülmez
- **Agent Browser:** `~/.agent-browser/browsers/chrome-*/` altında özel binary bulunur

---

## ⚠️ KRİTİK ÇÖZÜM: "failed to resolve CDP URLs" Hatası

**Hata Mesajı:**
```
failed to create browser context: failed to resolve CDP URLs: 
could not resolve IP for 127.0.0.1
```

**Kök Neden:** Antigravity, `~/.agent-browser/` içindeki özel "Google Chrome for Testing" kullanır. Önceki oturumdan kalan process veya yanlış port nedeniyle CDP bulunamıyor.

### ✅ ÇÖZÜM — Şu Adımları Uygula

```bash
# ADIM 1: Chrome'u tamamen kapat
osascript -e 'tell application "Google Chrome" to quit'
sleep 2

# ADIM 2: Chrome'u remote debugging ile başlat (binary doğrudan!)
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --no-first-run \
  --no-default-browser-check &

# ADIM 3: Bağlantıyı doğrula
sleep 4 && curl -s http://127.0.0.1:9222/json/version
```

**Başarılı çıktı:** `{"Browser": "Chrome/149.x.x.x", ...}`

### 🔍 Hızlı Kontrol
```bash
ps aux | grep "remote-debugging-port=9222" | grep -v grep
```

### ❌ Çalışmayan Yöntem
```bash
# BU ÇALIŞMAZ — open komutu argümanları geçiremez
open -a "Google Chrome" --args --remote-debugging-port=9222
```

### Sorun Giderme Kararları
| Durum | Çözüm |
|-------|-------|
| `failed to resolve CDP URLs` hatası | Yukarıdaki ÇÖZÜM adımlarını uygula |
| `action timed out` hatası | Chrome remote debugging ile açık mı? Kontrol et |
| Captcha ile karşılaştı | Görevi sonlandır, manuel devam et |
| İzin hatası | IDE'de Setup → Browser izinleri kontrol et |

**Kanıtlanmış:** 2026-06-12, Birkan ile Google "birkan" araması bu yöntemle başarıyla tamamlandı. ✅
