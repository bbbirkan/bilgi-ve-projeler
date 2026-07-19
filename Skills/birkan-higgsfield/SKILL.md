---
name: higgsfield
description: |
  Higgsfield AI ile görsel ve video üretimi. Şunlarda kullan:
  görsel/video üret, ürün fotoğrafı, marketplace kart, Soul karakter eğit,
  reklam videosu, UGC video, ürün animasyonu, Virality Predictor (video analizi),
  "higgsfield generate", "ürün fotoğrafı çek", "marketplace listesi için görsel",
  "Soul ID oluştur", "yüzümü öğret". Higgsfield CLI gerekli.
argument-hint: "[ne istiyorsun] [--image dosya] [--mode mod]"
allowed-tools: Bash
---

# Higgsfield — Tüm Yetenekler

## Bootstrap (her seferinde kontrol et)
```bash
which higgsfield || curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
higgsfield account status  # "Session expired" → higgsfield auth login
```

---

## 1. Genel Görsel / Video Üretimi

```bash
higgsfield generate create <model> --prompt "..." [flags] --wait
```

### Model Seçimi
| İstenen | Model |
|---------|-------|
| Genel görsel (default) | `gpt_image_2` |
| Video (default, 4-15s) | `seedance_2_0` |
| Karakter / anime / karikatür | `nano_banana_2` |
| Reklam / UGC video | `marketing_studio_video` |
| Sinematik görsel | `text2image_soul_v2` |
| Lokasyon / ortam görseli | `soul_location` |
| Video analizi (virality) | `brain_activity` |

```bash
# Görsel
higgsfield generate create gpt_image_2 --prompt "neon şehir" --aspect_ratio 16:9 --wait

# Video
higgsfield generate create seedance_2_0 --prompt "kamera içeri giriyor" --start-image ./foto.png --duration 12 --wait

# Video virality analizi
higgsfield generate create brain_activity --video ./reklam.mp4 --wait
```

### Media Bayrakları
| Bayrak | Ne için |
|--------|---------|
| `--image <dosya/id>` | Referans görsel |
| `--start-image` | Videonun ilk karesi |
| `--end-image` | Videonun son karesi |
| `--video <dosya/id>` | Referans video |

---

## 2. Ürün Fotoğraf Çekimi

```bash
higgsfield product-photoshoot create --mode <mod> --prompt "..." --image ./urun.jpg --count 3
```

### Mod Seçimi
| Mod | Ne zaman |
|-----|----------|
| `product_shot` | Stüdyo / katalog / beyaz arka plan |
| `lifestyle_scene` | Gerçek ortamda ürün (mutfak, outdoor) |
| `closeup_product_with_person` | El, yüz, güzellik uygulaması |
| `moodboard_pin` | Dikey Pinterest pin |
| `hero_banner` | Geniş web/e-posta başlığı |
| `social_carousel` | IG/LinkedIn kaydırmalı post (3-10 görsel) |
| `ad_creative_pack` | Meta/TikTok/Pinterest reklam seti |
| `virtual_model_tryout` | Modelde ürün (giyim, aksesuar) |
| `conceptual_product` | Uçan/sıçrayan/CGI ürün |
| `restyle` | Mevcut görselin stilini değiştir |

```bash
higgsfield product-photoshoot create \
  --mode lifestyle_scene \
  --prompt "kahve markası, sabah mutfak sahne" \
  --image ./kutu.jpg --count 3
```

---

## 3. Marketplace Kartları

```bash
higgsfield marketplace-cards create --scope <kapsam> --prompt "..." --image ./urun.png
```

| Kapsam | İçerik |
|--------|--------|
| `main` | 1 ana görsel |
| `product-images` | Ana + 5 ürün görseli |
| `aplus` | Ana + 7 A+ modül |
| `full-set` | Hepsi (13 görsel) |

```bash
higgsfield marketplace-cards create \
  --scope full-set \
  --prompt "premium cilt serumu, minimalist marketplace" \
  --image ./serum.jpg
```

---

## 4. Marketing Studio (Reklam Videosu)

```bash
# Ürünü ekle (URL'den)
higgsfield marketing-studio products fetch --url https://shop.example.com/urun --wait

# Avatar listesi
higgsfield marketing-studio avatars list --json

# Reklam oluştur
PRODUCT='["<product_id>"]'
AVATAR='[{"id":"<avatar_id>","type":"preset"}]'
printf "$PRODUCT" > /tmp/p.json && printf "$AVATAR" > /tmp/a.json

higgsfield generate create marketing_studio_video \
  --prompt "ürün tanıtımı" \
  --avatars @/tmp/a.json \
  --product_ids @/tmp/p.json \
  --mode ugc --duration 15 --aspect_ratio 9:16 --wait
```

Modlar: `ugc`, `ugc_how_to`, `ugc_unboxing`, `product_showcase`, `tv_spot`

---

## 5. Soul Character (Yüz Eğitimi)

```bash
# Eğit (5-20 fotoğraf, farklı açılar)
higgsfield soul-id create --name "Birkan" --soul-2 \
  --image ./foto1.jpg --image ./foto2.jpg --image ./foto3.jpg
higgsfield soul-id wait <id>  # ~30dk bekle

# Listele
higgsfield soul-id list

# Kullan (generate ile)
higgsfield generate create text2image_soul_v2 \
  --prompt "..." --soul-id <ref_id> --quality 2k --wait
```

> Not: Soul eğitimi Basic+ plan gerektirir.

---

## Hatalar
| Hata | Çözüm |
|------|-------|
| `Session expired` | `higgsfield auth login` |
| `Missing required params: prompt` | Prompt ekle |
| `Invalid aspect_ratio` | Geçerli: 16:9, 9:16, 1:1, 4:3, 3:4 |
| `Minimum Basic plan` | Ücretli plan gerekli (Soul için) |
