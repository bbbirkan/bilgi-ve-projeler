---
name: birkan-video-pipeline
description: |
  3 kademeli akıllı video anlama pipeline'ı — ÇEK → DİNLE → İZLE.
  YouTube, TikTok, Instagram, Loom, lokal MP4 desteklenir.
  Her kademe başarısız olunca bir sonrakine geçer, kullanıcıya ne yaptığını söyler.
  Görsel frame analizi (İZLE) sadece içerik gerektiriyorsa ve token harcandığında kullanıcıya bildirilir.
tags: [video, youtube, transcript, whisper, ffmpeg, yt-dlp, vision, frame-analysis]
---

# 🎬 Video Pipeline Skill — Çek → Dinle → İzle

## Ne Zaman Kullanılır (Trigger)
- "Bu videoyu izle / analiz et / özetle" + URL
- YouTube, TikTok, Instagram, Vimeo, Loom, X linki verildiğinde
- Lokal `.mp4 / .mov / .mkv` analiz edilecekse
- Birkan özellikle belirtmediği sürece en hafif kademeyle başla

---

## 3 Bağımsız Mod — Ne Zaman Hangisi?

### Mod Seçim Kuralı

```
Kullanıcı "izle / iyi anla / derinlemesine analiz et" dedi?
  → İZLE modunu kullan (görsel bağlam kritik)

İçerik görsel mi? (demo, grafik, kod ekranı, sunum slaytı)
  → Sen karar ver: İZLE moduna geç, "izliyorum" de

Standart bilgi sorusu, özet, transkript yeterli mi?
  → ÇEK → başarısız → DİNLE

Her şey başarısız?
  → SOR
```

**Her modda kullanıcıya söyle:**
- "Transkripti çektim ✓" 
- "Ses indirip Whisper ile dinledim ✓"
- "İzliyorum — frame analizi yapıyorum, biraz token harcayacak..."
- "Erişemedim, şunları deneyebilirsin..."

---

### Modların Avantajları

| Mod | Hız | Maliyet | Ne Kazandırır |
|-----|-----|---------|---------------|
| **ÇEK** | Saniyeler | Sıfır | Altyazı/transkript varsa anında al |
| **DİNLE** | 1-3dk | Düşük (Groq) | Altyazı yoksa sesi Whisper ile metne çevir — çıktı yine düz metin |
| **İZLE** | 3-10dk | Orta (token) | Görsel bağlam, grafik, demo, kod ekranı, slayt |

**Not:** DİNLE, ÇEK'in fallback'idir — altyazı bulamazsan sesi metne çevirirsin. Ton/vurgu/duygu bilgisi Whisper'da kaybolur, çıktı düz metin olur. Gerçek anlama avantajı sadece **İZLE**'dedir.

**İZLE modunun eşsiz avantajları:**
- Transkriptte olmayan bilgiler: grafik trendi, kod ekranı, sunum slaytı, ürün demosu
- Görsel karşılaştırma: "bu grafikte X artıyor ama transkriptte bahsedilmiyor"
- Teknik demolar: ekranda ne yapıldığını kelimeler anlatmaz

---

## Mod A — ÇEK → DİNLE (Boru Hattı)

### A1 — ÇEK: Deneme 1 (Standart)

```bash
yt-dlp --write-auto-sub --write-sub --sub-lang tr,en \
  --skip-download -o /tmp/video_%(id)s VIDEO_URL

ls /tmp/video_*.vtt /tmp/video_*.srt 2>/dev/null
```

Altyazı dosyası bulunduysa → analiz et, **dur**.

### A2 — ÇEK: Deneme 2 (Bot koruması varsa)

```bash
# Android client ile dene
yt-dlp --extractor-args "youtube:player_client=android" \
  --write-auto-sub --skip-download -o /tmp/video_%(id)s VIDEO_URL

# Hala yok? Cookies ile dene
yt-dlp --cookies-from-browser chrome \
  --write-auto-sub --skip-download -o /tmp/video_%(id)s VIDEO_URL

# Hala yok? jina.ai (metadata + açıklama, tam transkript değil)
curl -sL "https://r.jina.ai/VIDEO_URL" -A "Mozilla/5.0" | head -200
```

Altyazı bulunduysa → analiz et, **dur**.
İkinci denemeden sonra da yok → **DİNLE'ye geç**.

### A3 — DİNLE: Whisper Fallback

```bash
# Ses indir
yt-dlp -x --audio-format mp3 --audio-quality 0 \
  -o /tmp/video_%(id)s.%(ext)s VIDEO_URL

# Groq Whisper ile metne çevir
curl -s https://api.groq.com/openai/v1/audio/transcriptions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -F "file=@/tmp/video_ID.mp3" \
  -F "model=whisper-large-v3" \
  -F "language=tr" | python3 -c "import sys,json; print(json.load(sys.stdin)['text'])"
```

**25MB üzeri ses:**
```bash
ffmpeg -i /tmp/video_ID.mp3 -f segment -segment_time 600 \
  -c copy /tmp/video_part_%03d.mp3
# Her parçayı ayrı Whisper'a gönder, birleştir
```

DİNLE de başarısız → **SOR**.

---

## Kademe 2 — DİNLE (Orta, Groq Whisper)

Hedef: Sesi indir, Whisper ile transkribe et.

```bash
# Ses indir (mp3, en iyi kalite)
yt-dlp -x --audio-format mp3 --audio-quality 0 \
  -o /tmp/video_%(id)s.%(ext)s VIDEO_URL

# Groq Whisper ile transkript al (hızlı + ucuz)
# ~/.hermes/.env içinde GROQ_API_KEY olmalı
curl -s https://api.groq.com/openai/v1/audio/transcriptions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -F "file=@/tmp/video_ID.mp3" \
  -F "model=whisper-large-v3" \
  -F "language=tr" | python3 -c "import sys,json; print(json.load(sys.stdin)['text'])"
```

**Ses 25MB'ı aşarsa:**
```bash
# ffmpeg ile parçala (10 dakikalık dilimler)
ffmpeg -i /tmp/video_ID.mp3 -f segment -segment_time 600 \
  -c copy /tmp/video_part_%03d.mp3
# Her parçayı ayrı ayrı Whisper'a gönder, birleştir
```

**Groq başarısız → OpenAI Whisper fallback:**
```bash
curl -s https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "file=@/tmp/video_ID.mp3" \
  -F "model=whisper-1"
```

---

## Kademe 3 — İZLE (Pahalı, Frame Analizi)

**Ne zaman kullanılır:**
- Transkript alındı ama konu görsel anlama gerektiriyor (grafik, demo, teknik görsel)
- Transkript hiç alınamadı ama video kritik
- Kendi kararın: içerik görsel bağlam olmadan tam anlaşılamıyorsa

**Kullanıcıya söyle:** "İçeriği tam anlamak için frame analizi yapıyorum, biraz token harcayacak."

```bash
# Video indir
yt-dlp -o /tmp/video_%(id)s.mp4 VIDEO_URL

# Süreye göre frame rate hesapla
# ≤30sn  → fps=1   (~30 frame)
# 30s-3dk → fps=0.5 (~60-90 frame)
# 3dk-10dk → fps=0.2 (~36-120 frame)
# Max 100 frame (token bütçesi)

DURATION=$(ffprobe -i /tmp/video_ID.mp4 -show_entries format=duration \
  -v quiet -of csv="p=0" | cut -d. -f1)

if [ $DURATION -le 30 ]; then FPS=1
elif [ $DURATION -le 180 ]; then FPS=0.5
else FPS=0.2
fi

ffmpeg -i /tmp/video_ID.mp4 -vf "fps=${FPS}" \
  /tmp/frames_%03d.jpg -loglevel quiet

# Frame sayısı 100'ü geçmesin
ls /tmp/frames_*.jpg | wc -l
```

Frame'leri + mevcut transkripti birleştirerek Claude Vision ile analiz et.

---

## Kademe 4 — SOR

Her şey başarısız olduğunda:

```
Şu yöntemlerle erişmeye çalıştım ama olmadı:
- yt-dlp (altyazı, android client, cookies)
- jina.ai metin çıkarıcı
- Ses indirme + Whisper

Seçeneklerin:
1. Transkripti kendin kopyala yapıştır
2. Video dosyasını yükle (lokal MP4)
3. Videonun konusunu anlat, oradan devam edelim
```

---

## İZLE Moduna Kendi Kararınla Geçme Kriterleri

Kullanıcı söylemese bile izle:
- İçerik görsel demo veya ekran kaydı ise
- Transkript aldın ama anlamak için "görmek" gerekiyorsa
- "Daha iyi anla / derinlemesine analiz et" gibi istekler

Transkript yeterliyse **asla** izleme — token harca, zaman harca demek.

---

## Desteklenen Platformlar
YouTube, TikTok, Twitter/X, Instagram, Vimeo, Loom, Dailymotion, Twitch VOD + 1000+ site

## Limitler
| Limit | Detay |
|-------|-------|
| En iyi sonuç | 10 dakika altı |
| Max frame | 100 |
| Max Whisper | 25 MB (~50dk mono ses) |
| Private içerik | Desteklenmiyor |

## Araçlar (VPS'te kurulu)
- `yt-dlp` v2026.03.17 → `/usr/local/bin/yt-dlp`
- `ffmpeg` → `/usr/bin/ffmpeg`
- `GROQ_API_KEY` → `~/.hermes/.env`

---

## Eski Skill'lerle İlişki
Bu skill `birkan-video-watch` + `birkan-ai-video` yerine geçer.
- `birkan-video-watch` → arşivde, bot koruması notları buraya taşındı
- `birkan-ai-video` → arşivde, Mac path'leri içeriyordu (VPS'te çalışmıyordu)
