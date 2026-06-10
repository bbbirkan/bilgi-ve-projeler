---
name: birkan-chrome-extension-mv3
description: "2026 Chrome eklenti geliştirme rehberi: Manifest V3 mimarisi, Service Worker yaşam döngüsü, state yönetimi, DNR kuralları, Offscreen Documents, Shadow DOM, Vite/CRXJS entegrasyonu, Chrome Web Store SEO (Tiered Bucket), monetizasyon (Freemium, Reverse Trial, Dodo Payments, ExtensionPay), güvenli ödeme mimarisi ve Wedge stratejisi. 'Chrome eklenti yaz', 'MV3', 'extension geliştir', 'CWS SEO', 'eklenti monetizasyon', 'manifest v3' gibi konularda kullan."
---

# 2026 Chrome Eklenti Geliştirme — Manifest V3 Tam Rehberi

> Kaynak: 2026 Stratejik Araştırma Raporu (Haziran 2026)

---

## MV3 Temel Değişiklikler — Hızlı Referans

| MV2 | MV3 Karşılığı | Neden |
|-----|---------------|-------|
| `background.scripts` | `background.service_worker` | Ana thread'i bloke etmemek için |
| `XMLHttpRequest()` | `fetch()` API | Promise tabanlı, güvenli async |
| `window.setTimeout/setInterval` | `chrome.alarms` API | SW uykuya geçince sıfırlanır |
| `localStorage` | `chrome.storage.local` veya `session` | SW ↔ content script async erişim |
| DOM manipülasyonu | Offscreen Documents | SW'da DOM yasak |
| `webRequestBlocking` | `declarativeNetRequest` | Trafik tarayıcı motoruna devredildi |
| Remotely hosted code | Yok — hepsi bundle içinde | eval/innerHTML yasak |

---

## Service Worker Yaşam Döngüsü

**Kritik:** SW 30 saniye hareketsizlikte uyur. Global değişkenler ölür.

```js
// YANLIŞ — SW uykuya geçince sıfırlanır
let isAuthenticated = true;

// DOĞRU — kalıcı depolama kullan
await chrome.storage.local.set({ isAuthenticated: true });
const { isAuthenticated } = await chrome.storage.local.get('isAuthenticated');
```

### SW'yi Uyanık Tutma (Gerektiğinde)
```js
// Her 25 saniyede ping — 30sn eşiğinin altında
chrome.alarms.create('keepAlive', { periodInMinutes: 0.4 });
chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === 'keepAlive') chrome.runtime.getPlatformInfo(() => {});
});
```
> **Uyarı:** Gereksiz kullanım mağaza politikası ihlali sayılabilir.

---

## Depolama API Seçimi

| API | Kalıcılık | Kota | Content Script Erişimi | Kullanım |
|-----|-----------|------|------------------------|----------|
| `chrome.storage.session` | Oturum boyunca (RAM) | 10 MB | Varsayılan kapalı | Auth token, geçici state |
| `chrome.storage.local` | Kalıcı (disk) | 10 MB (∞ izinle) | Açık | Ayarlar, önbellek |
| `chrome.storage.sync` | Google Sync | 100 KB | Açık | Çok cihazlı ayarlar |

### Premium Abonelik Durumu Önbellekleme (TTL ile)
```js
// Ödeme sonrası kaydet
await chrome.storage.local.set({
  premium: { status: 'active', cachedAt: Date.now(), ttl: 3600000 }
});

// Her işlemde kontrol
const { premium } = await chrome.storage.local.get('premium');
if (premium && Date.now() - premium.cachedAt < premium.ttl) {
  // Yerel önbellek geçerli, ağa gitme
} else {
  // Sunucudan taze veri çek
}
```

---

## DeclarativeNetRequest (DNR) Kuralları

```json
{
  "id": 1,
  "priority": 1,
  "action": { "type": "redirect", "redirect": { "url": "https://example.com" } },
  "condition": { "urlFilter": "||ads.example.com", "resourceTypes": ["script"] }
}
```

### Limit Tablosu (2026)
| Kural Türü | Limit |
|------------|-------|
| Statik kurallar (toplam) | 30.000 |
| Aynı anda aktif ruleset | 50 |
| Dinamik kurallar | 30.000 (5.000 unsafe) |
| Oturum kuralları | 5.000 |
| Regex kuralları (her tür) | 1.000 (maks 2KB/kural) |

**Kritik Tuzak:** Yüksek öncelikli kural başlığı `set` veya `remove` yaparsa, düşük öncelikli kural sadece `append` yapabilir.

---

## Offscreen Documents

Service Worker'da DOM gerektiren işlemler için:

```js
// Offscreen belge oluştur (önce kontrol et)
async function ensureOffscreen() {
  const existing = await chrome.runtime.getContexts({
    contextTypes: ['OFFSCREEN_DOCUMENT']
  });
  if (existing.length) return;
  await chrome.offscreen.createDocument({
    url: 'offscreen.html',
    reasons: ['CLIPBOARD'], // veya DOM_SCRAPING, AUDIO_PLAYBACK, IFRAME_SCRIPTING
    justification: 'Pano işlemi için DOM erişimi'
  });
}

// İşlem bittikten sonra kapat (bellek sızıntısı önleme)
await chrome.offscreen.closeDocument();
```

**Kısıt:** Aynı profile anda yalnızca 1 Offscreen Document.

---

## Modern Geliştirme Stack (Vite + CRXJS)

### manifest.json (MV3 şablonu)
```json
{
  "manifest_version": 3,
  "name": "Extension Adı",
  "version": "1.0.0",
  "background": { "service_worker": "src/background/index.ts" },
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["src/content/index.ts"]
  }],
  "action": { "default_popup": "src/popup/index.html" },
  "permissions": ["storage", "activeTab"],
  "host_permissions": ["https://api.yourdomain.com/*"]
}
```

### CSS İzolasyonu (Shadow DOM)
```js
// React uygulamasını Shadow DOM içine render et
const host = document.createElement('div');
document.body.appendChild(host);
const shadowRoot = host.attachShadow({ mode: 'open' });

// Tailwind CSS'i shadow içine enjekte et
import styles from './styles.css?raw';
const styleEl = document.createElement('style');
styleEl.textContent = styles;
shadowRoot.appendChild(styleEl);

// React render
const container = document.createElement('div');
shadowRoot.appendChild(container);
createRoot(container).render(<App />);
```

### Static Asset URL Düzeltme (CRXJS)
```js
// YANLIŞ — host origin'e çözümlenir
import logo from './logo.svg';

// DOĞRU — eklenti origin'e çözümler
import logoPath from './logo.svg';
const logoUrl = chrome.runtime.getURL(logoPath);
```

---

## Chrome Web Store SEO — Tiered Bucket Modeli

### Sıralama Formülü
```
Skor = (TextMatch × Ağırlık) × AktifKullanıcıOranı × f(Yüklemeİvmesi)
```

**İki faz:**
1. **Metin eşleştirme** → Başlık/açıklama anahtar kelimeleri kovayı belirler
2. **Davranışsal metrikler** → Aktif Kullanıcı Oranı + Yükleme İvmesi sıralamayı belirler

### Kritik Kurallar
- **Aktif Kullanıcı Oranı > her şey** — hedef kitle dışından gelen (Product Hunt teknoloji kitlesi) hızlı terk oranı SEO'yu kalıcı olarak bozar
- Her 1.000 yükleme için ~4.2 yorum gerekiyor (organik)
- İlk 72 saat hedefli yükleme ivmesi algoritma tetikler

### Mağaza Görselleri
| Varlık | Boyut | Not |
|--------|-------|-----|
| İkon | 128x128 | Çok sade, araç çubuğunda küçülür |
| Promo Tile | 440x280 | Logo + kısa tagline |
| Ekran görüntüsü | 1280x800 veya 640x400 | Eklentinin bağlam içi kullanımı |

---

## İzin Stratejisi ve İnceleme Süresi

| İzin | İnceleme Süresi | Tavsiye |
|------|-----------------|---------|
| `activeTab` | 1-3 gün | **Tercih et** — yalnızca tıklama anında erişim |
| `<all_urls>` | 1-3 hafta | Kaçın — zorunluysa gerekçelendir |
| `tabs` | 1-3 hafta | Sadece gerekirse |

### İyi İzin Gerekçesi Örneği
```
"Eklentimiz X işlevini yerine getirmek için, kullanıcı butona tıkladığında
yalnızca aktif sekmenin DOM ağacına bildirim enjekte eder (activeTab).
Arka planda hiçbir dinleme yapılmamaktadır. Dış sunucu iletişimi yalnızca
https://api.ourdomain.com/* ile sınırlıdır."
```

---

## Monetizasyon Mimarisi

### Freemium + Reverse Trial
```
Yükleme → 7 gün tüm Pro özellikler açık (kart yok)
        → Süre dolunca kilitlenir
        → "Alışkanlık kazandıktan sonra satın al"
```

**Dönüşüm oranları:**
- Genel araçlar: aylık $3-5
- B2B araçlar: aylık $10-25
- Yıllık plan: %40-50 indirim

### Ödeme Platformları Karşılaştırması

| Platform | Model | Ücret | Not |
|----------|-------|-------|-----|
| **Dodo Payments** | MoR | %4 + $0.40 | Eklentiler için en popüler, lisans key desteği |
| **ExtensionPay** | Stripe Wrapper | %5 + Stripe | En kolay entegrasyon, sunucu gerektirmez |
| **Lemon Squeezy** | MoR | %5 + $0.50 | UI mükemmel, Stripe satın alması sonrası risk |
| **Paddle** | MoR | %5 + $0.50 | Kurumsal, yavaş onay |

### MV3'te Güvenli Ödeme Akışı
```
Kullanıcı "Premium Al" tıklar
  → chrome.tabs.create({ url: Stripe_Checkout_URL })
  → Kullanıcı harici sekmede ödeme yapar
  → Stripe webhook → backend DB günceller
  → SW fetch() ile lisansı doğrular
  → chrome.storage.local'e TTL ile kaydeder
```

**Kural:** Eklenti içine Stripe.js gömme — MV3 CSP engeller, inceleme reddeder.

### Zero Trust Lisans Mimarisi
```
Premium özellik tetiklenir
  → SW → backend API isteği (Auth Token header'da)
  → Backend lisansı doğrular
  → Şifreli sonuç döner
```
Asıl iş mantığını eklentiye koyma — her şey backend'de.

---

## OAuth & ID Dondurmak

Geliştirme ortamında dinamik ID = OAuth kırılır.

```json
// manifest.json — mağazadaki public key'i buraya ekle
{
  "key": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA..."
}
```

Key, mağazadan alınır: Geliştirici Paneli → Eklenti → More info → Public key.

Bu sayede local development ID = production ID = OAuth çalışır.

---

## Onboarding (İlk 10 Dakika Kritik)

```js
chrome.runtime.onInstalled.addListener(({ reason }) => {
  if (reason === 'install') {
    chrome.tabs.create({ url: chrome.runtime.getURL('onboarding.html') });
  }
});
```

**Onboarding sayfasında:**
1. İkonu nasıl "Pin"leyeceğini gösteren GIF
2. Eklentinin "Aha! anı"nı simüle eden etkileşim

---

## Wedge Stratejisi (B2B Giriş Noktası)

```
Niş + Acı veren problem + Sıfır sürtünme
  → Ücretsiz eklenti (LinkedIn, Gmail, Jira üzerinde çalışır)
  → Kullanıcı günlük alışkanlık geliştirdi
  → "Bu 100 kişiye otomatik kampanya başlatmak ister misin?"
  → SaaS platformuna yumuşak geçiş
```

**Sonuç:** CAC ≈ 0, her gün marka hatırlatması.

---

## Hızlı Kontrol Listesi

- [ ] Service Worker'da global değişken yok → `chrome.storage` kullan
- [ ] `eval()` / `innerHTML` yok
- [ ] Dış JS CDN'den çekme yok
- [ ] `activeTab` kullan, `<all_urls>` kaçın
- [ ] `.map` dosyaları production bundle'dan çıkar
- [ ] Shadow DOM ile CSS izolasyonu
- [ ] `manifest.json` içinde `key:` ile ID dondurulmuş (geliştirme için)
- [ ] Ödeme akışı harici sekme üzerinden
- [ ] Onboarding sayfası → PIN GIF'i
- [ ] Mağaza Promo Tile 440x280 değer önerisi var
