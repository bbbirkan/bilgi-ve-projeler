# claude-video

**Kaynak**: https://github.com/bradautomates/claude-video  
**Yazar**: bradautomates  
**Lisans**: MIT  
**Yıldız**: ~278 ⭐ | **Fork**: ~80

---

## Ne İşe Yarar?

`claude-video`, Claude'a **herhangi bir videoyu izleme yeteneği** kazandıran bir skill/plugin'dir.

Claude normalde bir YouTube linki yapıştırıldığında içeriği tahmin etmek ya da eksik bir transkript kullanmak zorunda kalır. `/watch` komutuyla Claude şunları yapabilir:

- Videoyu indirir (URL veya yerel dosya)
- Karelerini (frame) otomatik oranlarda çıkarır
- Zaman damgalı transkript alır (ücretsiz altyazı veya Whisper API fallback)
- Her kareyi görsel olarak okur
- Videoyu gerçekten "izlemiş" biri gibi soruları yanıtlar

---

## Nasıl Kullanılır?

```
/watch https://youtu.be/VIDEO_ID 30. saniyede ne oluyor?
/watch https://www.tiktok.com/@user/video/123 bunu özetle
/watch ~/Movies/ekran-kaydi.mp4 UI nerede bozuluyor?
/watch https://vimeo.com/123 hangi araçlardan bahsediyor?
```

### Belirli Bir Zaman Aralığına Odaklanma
```bash
/watch https://youtu.be/abc --start 2:15 --end 2:45
/watch video.mp4 --start 50 --end 60
/watch "$URL" --start 1:12:00    # 1sa12dk'dan sona kadar
```

### Ek Parametreler
| Parametre | Açıklama |
|-----------|----------|
| `--max-frames N` | Maksimum kare sayısını sınırla |
| `--resolution W` | Kare genişliği (varsayılan 512px, metin okuma için 1024 önerilir) |
| `--fps F` | Otomatik FPS hesaplamasını geçersiz kıl (max 2 fps) |
| `--whisper groq\|openai` | Whisper backend'ini zorla |
| `--no-whisper` | Transkripti devre dışı bırak, sadece kareler |
| `--out-dir DIR` | Çalışma dosyalarını belirli bir yere kaydet |

---

## Nasıl Çalışır?

1. **URL veya yerel dosya** yapıştırılır (yt-dlp destekli: YouTube, TikTok, Loom, Vimeo, Instagram, X ve 100+ kaynak)
2. **yt-dlp** videoyu geçici dizine indirir
3. **ffmpeg** kareleri otomatik oranlı çıkarır (512px JPEG, max 2fps, max 100 kare)
4. **Transkript** alınır — önce native altyazı (ücretsiz), yoksa Whisper API (Groq veya OpenAI)
5. **Kareler + transkript** Claude'a iletilir (zaman damgalı)
6. Claude her kareyi görsel olarak okur, soruyu yanıtlar

### Kare Bütçesi (Token Maliyeti)
| Video Süresi | Varsayılan Kare | Yoğunluk |
|---|---|---|
| ≤30 saniye | ~30 kare | Yoğun — neredeyse her an |
| 30s – 1dk | ~40 kare | Hâlâ yoğun |
| 1 – 3 dk | ~60 kare | Rahat |
| 3 – 10 dk | ~80 kare | Seyrek ama yeterli |
| >10 dk | 100 kare | Seyrek tarama — `--start/--end` önerilir |

---

## Kurulum

### Claude Code (Önerilen)
```bash
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

### claude.ai (Web)
1. `watch.skill` dosyasını son sürümden indir
2. Settings → Capabilities → Skills → `+` ile yükle
3. "Code execution and file creation" özelliğini etkinleştir

### Codex
```bash
git clone https://github.com/bradautomates/claude-video.git ~/.codex/skills/watch
```

### Manuel / Geliştirici
```bash
git clone https://github.com/bradautomates/claude-video.git ~/.claude/skills/watch
```

---

## API Anahtarları ve Maliyet

| Özellik | Gereksinim | Maliyet |
|---------|-----------|---------|
| İndirme + native altyazı | yt-dlp + ffmpeg | Ücretsiz |
| Whisper fallback (tercih edilen) | Groq API anahtarı | Ucuz ve hızlı |
| Whisper fallback (alternatif) | OpenAI API anahtarı | Standart fiyat |
| Whisper'ı devre dışı bırak | `--no-whisper` | Ücretsiz, sadece kareler |

İlk çalıştırmada `scripts/setup.py --check` otomatik olarak bağımlılıkları kontrol eder:
- **macOS** → `brew install ffmpeg yt-dlp` otomatik çalışır
- **Linux** → `apt`/`dnf`/`pipx` komutlarını yazdırır
- **Windows** → `winget`/`pip` komutlarını yazdırır

---

## Kısıtlamalar

- **En iyi doğruluk**: 10 dakikanın altındaki videolar için. Daha uzunsa `--start/--end` kullan
- **Sabit üst limit**: max 2 fps, max 100 kare
- **Whisper yükleme limiti**: 25MB (mono 16kHz'de ~50 dakika)
- **Özel platformlar desteklenmez**: Giriş gerektiren URL'ler çalışmaz, sadece herkese açık URL ve yerel dosyalar

---

## Proje Yapısı (İndirildi)

```
claude-video/
├── SKILL.md                  # Skill sözleşmesi — tüm yüzeyler tarafından yüklenir
├── scripts/
│   ├── watch.py              # Ana giriş noktası — indirme → kareler → transkript
│   ├── download.py           # yt-dlp sarmalayıcı
│   ├── frames.py             # ffmpeg kare çıkarma + otomatik FPS mantığı
│   ├── transcribe.py         # VTT parse + Whisper orkestrasyon
│   ├── whisper.py            # Groq / OpenAI istemciler
│   ├── setup.py              # Ön kontrol + yükleyici
│   └── build-skill.sh        # claude.ai için watch.skill paketi oluşturur
├── hooks/                    # SessionStart durum hook'u (Claude Code)
├── .claude-plugin/           # plugin.json + marketplace.json
├── .codex-plugin/            # Codex paketleme
└── .github/workflows/        # release.yml — tag'de watch.skill otomatik oluşturur
```

---

## Kullanım Senaryoları

- **İçerik analizi**: Viral bir videonun hook yapısını, açılış karelerini ve transkriptini analiz et
- **Bug teşhisi**: Ekran kaydındaki bir hatayı Claude'a izleterek teşhis ettir
- **Video özetleme**: Uzun videoları 2x izlemek yerine `/watch url özetle` ile bitir
- **Rakip analizi**: Rakip lansmanlarını, reklam kreatiflerini, podcast girişlerini analiz et

---

## Özet

> **claude-video** = Claude'a video izleme yeteneği kazandıran `/watch` komutu.  
> URL veya yerel dosya yapıştır, soru sor — Claude videoyu indirir, karelerini okur, transkriptini alır ve gerçekten izlemiş biri gibi yanıt verir.
