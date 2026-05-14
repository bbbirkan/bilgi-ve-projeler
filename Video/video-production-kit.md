# video-production-kit

Claude Code için **video düzenleme + altyazı + YouTube paketleme** agent sistemi. Ham konuşma kaydını alır, 5 bağımsız agent'a dağıtır — transkript, kesim listesi, SRT altyazı, YouTube açıklaması ve sosyal medya paylaşımı. CapCut farkındalıklı, ffmpeg + Whisper tabanlı. Türkçe içeriğe optimize.

> Yapımcı: [Selma Kocabıyık](https://github.com/selmakcby) — 23 yaşında AI mühendisi, kendi YouTube workflow'undan doğdu.

## Ne İşe Yarar

22 dakikalık ham kayıt → 7 dakikalık yayına hazır YouTube videosu. Manuel iş: ~15 dakika. El ile yapılsaydı: ~3 saat.

## 5 Agent

| Agent | Görevi |
|-------|--------|
| **transcript-agent** | CapCut timeline / video dosyasından Türkçe transkript (Whisper turbo) |
| **cut-list-agent** | Ham kayıt → "şu saniyeden şu saniyeye sil" kesim listesi |
| **subtitle-agent** | Word-level SRT, yazım düzeltmeli (Cloud→Claude, Versal→Vercel gibi) |
| **description-agent** | YouTube açıklaması + bölüm zaman damgaları |
| **social-agent** | X thread + Instagram caption |

Her agent kendi context'inde çalışır, birbirine karışmaz. Ana Claude orkestrasyon yapar.

## Nasıl Çalışır

Doğal dilde çağırırsın, Claude doğru agent'ı devreye alır:

```
"timeline 03'ün altyazısını çıkar"          → subtitle-agent → SRT
"bu videoma YouTube açıklaması yazar mısın" → description-agent → açıklama + bölümler
"21 dakikalık kaydı 5 dakikaya indir"       → cut-list-agent → CapCut kesim listesi
```

## CapCut Entegrasyonu

CapCut Mac'in `draft_info.json` dosyasını parse eder:
- Hangi timeline'da çalışıldığı otomatik belirlenir
- Vol=0 (sessiz) segmentler transkriptten çıkarılır
- Çıkan SRT'nin saniyeleri **birebir CapCut timeline saniyelerine** denk gelir

CapCut kullanmıyorsan da çalışır — sadece video dosyası verirsin.

## Ne Zaman Kullanılır

- Türkçe YouTube videoları üretiyorsan
- Ham konuşma kayıtlarını düzenlemek/kesmek istiyorsan
- Altyazı, açıklama ve sosyal medya metnini her video için tekrar tekrar yazıyorsan
- CapCut + Claude Code workflow'u kuruyorsan

## Kurulum

```bash
git clone https://github.com/selmakcby/video-production-kit.git
cd video-production-kit
pip install -r requirements.txt
brew install ffmpeg   # macOS
claude                # Claude Code açılınca agent'ları otomatik bulur
```

**Gereksinimler:** macOS/Linux · Python 3.10+ · ffmpeg · Claude Code · ~2 GB disk (Whisper ilk çalışmada indirilir)

## Klasör Yapısı

```
.claude/agents/      ← 5 agent (Claude otomatik yükler)
scripts/             ← ffmpeg + Whisper Python yardımcıları
prompts/             ← Şablonlar
examples/            ← Gerçek vaka çalışması
docs/                ← CapCut entegrasyon detayı
```

## Limitler

- Windows test edilmedi
- Şu an Türkçe + İngilizce'ye optimize (diğer diller PR ile eklenebilir)
- DaVinci / Premiere desteği yok (issue açılabilir)

**Kaynak:** [selmakcby/video-production-kit](https://github.com/selmakcby/video-production-kit) · MIT
