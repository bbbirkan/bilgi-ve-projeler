---
name: montage
description: |
  Elimdeki video kliplerini birleştir, müzik bindirle, altyazı ekle.
  ffmpeg tabanlı, lokal çalışır. Higgsfield çıktılarını veya herhangi bir
  video dosyasını işlemek için kullan.
tags: [video, ffmpeg, montage, subtitle, music, merge, concat, post-processing]
---

# Montage Skill — Video Birleştirme & Post-Processing

## Ne Zaman Kullanılır
- "Bu klipleri birleştir / birleştirip tek video yap"
- "Arkaplan müziği ekle"
- "Altyazı / subtitle ekle / yak"
- "Klipleri sırala + müzik + altyazı → final video"
- Higgsfield'dan gelen video parçalarını bir araya getirmek

---

## Ortam Kontrolü

```bash
which ffmpeg && ffmpeg -version 2>&1 | head -1
# Beklenen: /opt/homebrew/bin/ffmpeg — ffmpeg version 8.x
```

---

## 1. Klipleri Birleştirme (Concat)

```bash
# Dosya listesi oluştur
printf "file '%s'\n" /path/to/clip1.mp4 /path/to/clip2.mp4 /path/to/clip3.mp4 > /tmp/clips.txt

# Birleştir (re-encode olmadan — aynı codec ise)
ffmpeg -f concat -safe 0 -i /tmp/clips.txt -c copy /tmp/output_merged.mp4

# Farklı codec/çözünürlük karışıksa re-encode yap
ffmpeg -f concat -safe 0 -i /tmp/clips.txt \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 192k \
  /tmp/output_merged.mp4
```

---

## 2. Arkaplan Müziği Bindirme

```bash
# Müziği video süresine göre kırp + karıştır
ffmpeg -i /tmp/output_merged.mp4 -i /path/to/music.mp3 \
  -filter_complex "[1:a]volume=0.3[music];[0:a][music]amix=inputs=2:duration=first[aout]" \
  -map 0:v -map "[aout]" \
  -c:v copy -c:a aac -b:a 192k -shortest \
  /tmp/output_with_music.mp4

# Sadece müzik (orijinal ses yoksa veya istemiyorsa)
ffmpeg -i /tmp/output_merged.mp4 -i /path/to/music.mp3 \
  -map 0:v -map 1:a \
  -c:v copy -c:a aac -shortest \
  /tmp/output_with_music.mp4
```

---

## 3. Altyazı Ekleme

### A) Soft subtitle (ayrı track — kapatılabilir)
```bash
# SRT dosyası varsa
ffmpeg -i /tmp/output_with_music.mp4 -i /path/to/subtitles.srt \
  -c copy -c:s mov_text \
  /tmp/output_final.mp4
```

### B) Hardcode subtitle (videoya yakılır)
```bash
# SRT dosyasını videoya yak
ffmpeg -i /tmp/output_with_music.mp4 \
  -vf "subtitles=/path/to/subtitles.srt:force_style='FontSize=24,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,Outline=2'" \
  -c:a copy \
  /tmp/output_final.mp4
```

### C) Basit metin overlay (SRT yoksa)
```bash
# Sabit metin
ffmpeg -i /tmp/input.mp4 \
  -vf "drawtext=text='Ürün Adı':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=h-100:shadowx=2:shadowy=2" \
  -c:a copy /tmp/output_text.mp4
```

---

## 4. Tam Pipeline (Birleştir + Müzik + Altyazı)

```bash
# Adım 1: Birleştir
printf "file '%s'\n" clip1.mp4 clip2.mp4 clip3.mp4 > /tmp/clips.txt
ffmpeg -f concat -safe 0 -i /tmp/clips.txt -c:v libx264 -crf 23 -c:a aac /tmp/merged.mp4

# Adım 2: Müzik ekle
ffmpeg -i /tmp/merged.mp4 -i music.mp3 \
  -filter_complex "[1:a]volume=0.25[bg];[0:a][bg]amix=inputs=2:duration=first[out]" \
  -map 0:v -map "[out]" -c:v copy -c:a aac -shortest /tmp/merged_music.mp4

# Adım 3: Altyazı yak
ffmpeg -i /tmp/merged_music.mp4 \
  -vf "subtitles=subs.srt" \
  -c:a copy /tmp/final_output.mp4

echo "Tamamlandı: /tmp/final_output.mp4"
```

---

## 5. Çözünürlük & Format

```bash
# Dikey (TikTok/Instagram Reels) 1080x1920
ffmpeg -i input.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" \
  -c:a copy output_vertical.mp4

# Kare (Instagram Feed) 1080x1080
ffmpeg -i input.mp4 -vf "scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080" \
  -c:a copy output_square.mp4

# YouTube 1920x1080
ffmpeg -i input.mp4 -vf "scale=1920:1080" -c:a copy output_hd.mp4
```

---

## 6. Hızlı Trim (Kırpma)

```bash
# ss=başlangıç, to=bitiş
ffmpeg -i input.mp4 -ss 00:00:05 -to 00:00:30 -c copy output_trimmed.mp4
```

---

## Temizlik

```bash
rm -f /tmp/clips.txt /tmp/merged.mp4 /tmp/merged_music.mp4
echo "Geçici dosyalar temizlendi ✓"
```

---

## İlgili Skill'ler

- `video-pipeline` → Video analiz & transkript
- `higgsfield-generate` → AI video üretimi
- `higgsfield-product-photoshoot` → Ürün fotoğrafı → packshot
