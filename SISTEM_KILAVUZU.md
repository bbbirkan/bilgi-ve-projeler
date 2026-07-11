# SOVEREIGN EKOSİSTEM — SİSTEM KILAVUZU
> Sürüm: 1.2 | Son güncelleme: 2026-07-10
> **Bu belge yaşayan bir belgedir.** Sistem değiştikçe güncellenir.
> Güncelleme kuralı: Yeni servis, yeni otomasyon veya büyük karar sonrası bu dosya güncellenir.
> Konum: `/root/SISTEM_KILAVUZU.md`

---

## BÖLÜM 0 — AMAÇ VE VİZYON

### Kim Biz
Birkan Kalyon (Salem NJ) + AI ekibinin kurduğu özerk işletme altyapısı.

### Neden Varız
**Para kazanmak için değil — bağımsız olmak için.**
Para bağımsızlığın aracı, amaç değil.

### Hedef (1 Yıllık)
```
Şimdi (2026-Q3)  →  Birkan her gün aktif, sistem kırılgan
3 ay sonra       →  Birkan haftada birkaç karar, sistem çoğunu halleder
6 ay sonra       →  Birkan haftada bir kontrol, sistem özerk
1 yıl sonra      →  Birkan aradan çekilmiş, sistem kendi yürüyor
```

### Temel Kural
> **Kart = "Bunu sensiz yapamadım."**
> Sistem kendi halledebildiği şeyi Birkan'a sormaz. Halleder, sabah raporunda söyler.

---

## BÖLÜM 1 — EKİP YAPISI

### Ekip Rolleri

#### Komuta Katmanı
| İsim | Model | Ne Yapar | Ne Zaman |
|------|-------|----------|---------|
| **Ortak Sunset** | Claude Sonnet 5 | Karar, sentez, koordinasyon, raporlama | Her zaman — ana oturum |
| **Menejer Kaya** | Claude Opus 4.8 | Stratejik kararlar, büyük yön tespiti | Günde max 1 kez |
| **Mentor Fable** | Claude Fable 5 | Üst seviye vizyon, kritik dönüm noktaları | Nadir — büyük kararlar (13 Temmuz'dan itibaren API üzerinden) |

#### Araştırma Birimi
| İsim | Model | Ne Yapar | Ne Zaman |
|------|-------|----------|---------|
| **Göz Gemini** | Gemini 3.1 Pro (High) | Derin web araştırması, piyasa analizi | Derin araştırma |
| **Flaş Gem** | Gemini 3.5 Flash (High) | Hızlı arama, özet, anlık bilgi | Hızlı sorgu |

#### Kod Birimi
| İsim | Model | Ne Yapar | Ne Zaman |
|------|-------|----------|---------|
| **Vekil Glim** | GLM-5.2 (OpenCode-Go) | Uzun-horizon kod, deploy, 1M context | Kod / dosya görevi |
| **Derin Seek** | DeepSeek V4 Pro | Karmaşık kod, mimari kararlar | Derin teknik analiz |
| **Dip Flash** | DeepSeek V4 Flash | Hızlı kod, rutin düzeltme | Küçük kod görevi |

#### Veri Birimi
| İsim | Model | Ne Yapar | Ne Zaman |
|------|-------|----------|---------|
| **Mini MiniMax** | MiniMax M3 | Entity çıkarma, sinyal analizi | Yapılandırılmış veri |
| **Ay Moonshot** | Kimi K2 | 1M context, uzun belge analizi | Transkript, büyük dosya |

#### Destek
| İsim | Model | Ne Yapar | Ne Zaman |
|------|-------|----------|---------|
| **Koşan Haiku** | Claude Haiku 4.5 | Tüm birimlere hızlı destek, küçük görev | Hız öncelikli işler |
| **Ses** | MiniMax TTS | Birkan'a sesli rapor | Sadece sabah raporu |

#### ÇARŞI — Taşeron Havuzu (LLM Gateway / DevPass)
> Damıtma araçlarından (kazı, lesson-extractor, trade_extractor) gelen ham çıktıları işleyen güçlü dış taşeronlar. Kalıcı ekip değil — iş gelince çağrılır, iş bitince geri gönderilir.

| İsim | Model | Görev | Fiyat |
|------|-------|-------|-------|
| **Güneş Sol** | GPT-5.6 Sol | Ultra ağır analiz, agentic kodlama, derin biyoloji/siber | $5/$30 /M |
| **Toprak Terra** | GPT-5.6 Terra | Dengeli günlük iş, Güneş'in 2x ucuzu | $2.50/$15 /M |
| **Şahin Grok** | xAI Grok (en yeni) | Twitter/X gerçek zamanlı tarama, sosyal istihbarat | xAI API |

**Damıtma Akışı:**
```
kazı / lesson-extractor / trade_extractor
          ↓ ham kural / transkript
     ÇARŞI taşeronu (göreve göre seç)
          ↓ işlenmiş analiz
     Ortak (sentez + karar)
          ↓
     Birkan (onay)
```

### Orkestra Çalışma Modları
Orchester (port 8006) 3 ana modda çalışır:

| Mod | Nasıl Çalışır | Ne Zaman |
|-----|--------------|---------|
| **KORO** | 5 model paralel → Claude sentezler | Farklı bakış açısı lazımsa |
| **KOLEKTİF** | Kimi→DeepSeek→GLM→AGY→Claude sıralı | Derin analiz, doğrulama |
| **AKILLI** | Claude zorluğu ölçer, otomatik seçer | Varsayılan mod |
| **TARTIŞMA** | 5 danışman kurul: Ortak(Karşı Çıkan)+Ay(Sorgulayan)+Göz(Büyük Resim)+Vekil(Yabancı)+Derin(Uygulayıcı) → anonim değerlendirme → Başkan kararı | Önemli kararlar, strateji, risk analizi |
| **MENTÖRLER** | Sol (gpt-5.6-sol) + Fable 5 (claude-fable-5) 2 tur tartışır → GLM-5.2 sentezler → decisions/ kaydeder | Büyük vizyon, ekosistem strateji |

`python3 /root/2026-orchester/terminal_orchester.py --list-modes`
`python3 /root/scripts/mentor_konseyumu.py "konu"` — Sol + Fable 5 konseyumu (13 Temmuz'dan tam aktif)

### Delege Kuralı
```
Araştırma    → agy --print "görev" --model "Gemini 3.1 Pro (High)"
Kod/deploy   → opencode run -m opencode-go/glm-5.2
Uzun analiz  → opencode run -m opencode-go/kimi-k2.6
Strateji     → claude -p --model claude-opus-4-8
Koordinasyon → Ortak (mevcut oturum)
Ultra ağır   → ÇARŞI: Güneş Sol  (LLM Gateway → GPT-5.6 Sol)
Twitter/X    → ÇARŞI: Şahin Grok (xAI API)
Damıtma      → ÇARŞI taşeronu → Ortak sentezler
```

### Sesli İletişim Kuralı
- **Varsayılan: SESİZ** — her yanıtta sesli bildirim gönderilmez
- **İstisna:** Sabah raporu (09:00 ET) her zaman sesli gider
- **Açmak için:** "sesli modu aç" → o oturum için sesli bildirim aktif

---

## BÖLÜM 2 — ALTYAPI

### Sunucu
| Özellik | Değer |
|---------|-------|
| Provider | Contabo VDS |
| IP | 207.180.204.66 |
| RAM | 7.8 GB |
| Disk | 145 GB (52 GB boş) |
| OS | Ubuntu 24.04 LTS |
| Lokasyon | Almanya |

### Temel Bileşenler
| Bileşen | Sürüm | Kullanım |
|---------|-------|---------|
| Python | 3.12 (sistem) / 3.11 (venv) | Tüm servisler |
| Redis | 7.0.15 | Cache, rate limiting, oturum |
| Docker | 28.5.1 | Container yönetimi |
| Node.js | 22.22.2 | JS gerektiren araçlar |
| ffmpeg | 6.1.1 | Ses/video işleme |
| yt-dlp | 2026.03.17 | YouTube indirme |
| faster-whisper | — | Ses → metin |
| Graphify | 0.8.13 | Bilgi grafiği |

### Dış Servisler
| Servis | Amaç | Durum |
|--------|------|-------|
| Cloudflare | DNS + Email routing (anvilon.net) | ✅ |
| Mercury Bank (Anvilon LLC ••1345) | Şirket hesabı | ✅ ~$22 |
| MiniMax | TTS sesleri | ✅ $25 bakiye |
| Vast.ai | GPU kiralama (RTX 3090) | ✅ $10 bakiye |
| Alpaca | Paper trading | ✅ |
| GitHub (bbbirkan) | Kod deposu | ✅ |
| Trello | Görev yönetimi | ✅ Ekosistem board |
| Telegram | Birkan'a bildirim + sesli rapor | ✅ |

---

## BÖLÜM 3 — AKTİF SERVİSLER (PORT HARİTASI)

### Mimari
```
Birkan'ın telefonu
       │
       ▼
  Telegram Bot ──────────────────────────────────────┐
       │                                              │
       ▼                                              ▼
 Hermes Gateway                               Sabah Raporu
 (mesaj merkezi)                            (MiniMax TTS 09:00)
       │
       ├──► Orchester :8006 ──► KORO / KOLEKTİF / AKILLI mod
       │
       ├──► Voltara Signal :8007 ──► 2961 transkript SQLite
       │
       ├──► Aria :8010 ──► Anvilon müşteri asistanı
       │         │
       │         └──► Aria Voice :8011 (TTS köprü)
       │
       ├──► YT Harvester :8003 ──► YouTube transkript
       ├──► YouTube Mini :8002 ──► Metadata
       ├──► VisionWatch :8001 ──► Video analiz
       └──► Channel Router :8000 ──► Orkestrasyon
```

### Servis Detayları

#### 🎯 Voltara Signal (Port 8007)
- **Ne yapar:** 2961 YouTube finans transkriptini analiz eder, piyasa sinyali üretir
- **Veri:** SQLite veritabanı, 1126 finans kuralı (LESSONS_ENRICHED.md)
- **Gelir potansiyeli:** RapidAPI → aylık pasif gelir hedefi
- **Dosya:** `/root/2026-yt-signal/`
- **Durum:** ✅ Aktif, API ucu hazır

#### 🤖 Orchester (Port 8006)
- **Ne yapar:** AI modellerini yönlendirir — KORO / KOLEKTİF / AKILLI mod
- **Modlar:** `python3 /root/2026-orchester/terminal_orchester.py --list-modes`
- **Gelir potansiyeli:** SaaS, danışmanlık botu temeli
- **Dosya:** `/root/2026-orchester/`
- **Durum:** ✅ Aktif

#### 💬 Aria (Port 8010)
- **Ne yapar:** Anvilon müşteri AI asistanı, MiniMax M3 backend
- **Erişim:** aria.anvilon.net
- **Güvenlik:** Rate limiting, jailbreak filtresi, IP block aktif
- **Dosya:** `/root/2026-aria-demo/`
- **Durum:** ✅ Aktif

#### 🔊 Aria Voice (Port 8011)
- **Ne yapar:** Aria'nın sesli versiyonu, Telegram TTS köprüsü
- **Erişim:** aria.anvilon.net/call
- **Dosya:** `/root/2026-aria-voice-service/`
- **Durum:** ✅ Aktif

#### 📋 Hermes Trello Agent (Port 8005)
- **Ne yapar:** Trello kartlarını haftalık AI ile analiz eder, ilerletir
- **Otomasyon:** Pazartesi 09:00 → kartları işler → Telegram raporu
- **Webhook:** Trello değişikliği → YAPILACAKLAR.md anında sync
- **Dosya:** `/root/2026-hermes-trello-agent/`
- **Durum:** ✅ Aktif

#### 📺 YT Harvester (Port 8003)
- **Ne yapar:** YouTube kanal transkripti çeker, API olarak sunar
- **Dosya:** `/root/2026-youtube-stack/`
- **Durum:** ✅ Aktif

#### 🔍 Context Index (Port 8008)
- **Ne yapar:** FTS5 tam metin arama — tüm sovereign-brain belgelerinde anlık arama
- **Kullanım:** `curl localhost:8008/search?q=kelime`
- **Durum:** ✅ Aktif

#### 📊 Sinyal Raporu (Günlük 07:00 ET)
- **Ne yapar:** Voltara Signal'dan konsensüs + anomali çeker → Telegram'a piyasa raporu gönderir
- **Dosya:** `/root/2026-sovereign/sinyal_raporu.py`
- **Durum:** ✅ Günlük otomatik

#### 📰 Medium Reader (Port 8004) | 🎬 YouTube Mini (Port 8002) | 👁️ VisionWatch (Port 8001) | 🔀 Channel Router (Port 8000)
- **Durum:** Manuel başlatma gerektiğinde aktif

#### 🤖 Sovereign Bot (Telegram)
- **Ne yapar:** 7/24 Telegram botu, Birkan'ın komutlarını alır
- **Dosya:** `/root/2026-sovereign/bot_server.py`
- **Durum:** ✅ Aktif

#### 📈 Sovereign Trading Bot
- **Ne yapar:** Voltara Signal → Alpaca paper trade otomasyonu
- **Durum:** ✅ Aktif (paper — gerçek para değil)

---

## BÖLÜM 4 — OTOMASYON TAKVİMİ

### Günlük Otomasyonlar

| Zaman | Ne Çalışır | Ne Yapar |
|-------|-----------|---------|
| 09:00 ET | `sovereign.timer` | Sabah raporu → Telegram'a **sesli** (Sonnet 5) |
| 4 saatte 1 | `voltara-indexer.timer` | Yeni transkriptleri işle |
| Sürekli | `sovereign-brain-watcher` | Belgeler değişince Graphify günceller |

### Haftalık Otomasyonlar

| Gün | Zaman | Ne Çalışır | Ne Yapar |
|-----|-------|-----------|---------|
| Pazartesi | 08:00 | `sovereign-ideas` | 6 model → Grup A tarama → 2 kol derin araştırma |
| Pazartesi | 09:00 | `sovereign-weekly` | Haftalık toplantı raporu (Sonnet 5) |
| Pazartesi | 09:00 | Hermes Trello Agent | Bekliyor kartlarını AI analiz eder |
| Salı | 09:00 | `sovereign-gecir` | Pazartesi fikirlerinden aksiyon planı (Menejer + Ortak) |
| Çarşamba | 09:00 | `sovereign-gecir` | Salı planından bugünkü somut adımlar |
| Perşembe | 08:00 | `sovereign-ideas` | 6 model → Grup B tarama → 2 kol derin araştırma |
| Perşembe | 21:00 | `sovereign-backup` | Yedekleme |
| Cuma | 09:00 | `sovereign-gecir` | Perşembe fikirlerinden aksiyon planı |
| Pazartesi | 09:00 | `sovereign-pazartesi` | Derin araştırma + Voltara güncelleme |

### Ideas Worker — Dosya Tarama Rotasyonu
Menejer stratejisi (2026-07-09):
- **Sabit (her çalışma):** STATE.md, CEBİMİZ.md, YAPILACAKLAR.md, ideas/ (mükerrer önleme)
- **Grup A (Pazartesi):** sovereign-brain/GELECEK.md, projects/, SESSION_LOG.md
- **Grup B (Perşembe):** sovereign-brain/research/, techniques/, Voltara insights/, wiki/
- Tarama geçmişi: `/root/2026-sovereign/ideas/tarama_gecmisi.json`

### Event-Driven Otomasyonlar

| Tetikleyici | Ne Olur |
|-------------|---------|
| Trello'da kart taşınır | Webhook → `trello_sync.py` → YAPILACAKLAR.md güncellenir |
| Sistem görev üretir | `add_task()` → Hem Trello hem MD'ye eklenir |
| Servis DOWN olur | ⚡BUGÜN listesine kart, Telegram bildirimi |
| Birkan video atar | Analiz → ilgili yere kaydedilir |

---

## BÖLÜM 5 — GÖREV YÖNETİMİ (TRELLO + MD)

### Yapı
```
YAPILACAKLAR.md          Trello Ekosistem Board
(sistem hafızası)   ←→   (Birkan'ın görsel paneli)
     │                          │
     │    Webhook + sync        │
     └──────────────────────────┘
```

**URL:** trello.com/b/zT5GsUA5/ekosistem

| Liste | Amaç | Kural |
|-------|------|-------|
| ⚡ BUGÜN | Bugün yapılacak | Max 3 kart — sadece Birkan yapabilir |
| 📋 Bekliyor | Sıradaki görevler | Öncelik sıralı |
| 🔄 Başladı | Devam eden | Sistem veya Birkan çalışıyor |
| ✅ Tamamlandı | Bitti | Pazartesi arşivlenir |
| 💡 Fikir Havuzu | Fikirler | Acil değil |

### Senkronizasyon
- Trello master kaynak — Trello'da değişen MD'ye yansır
- Servis: `/root/scripts/trello_sync.py`
- Webhook: `http://207.180.204.66:8005/webhook`

---

## BÖLÜM 6 — PARA VE GELİR

### Mevcut Durum (2026-07-09)
| Hesap | Bakiye |
|-------|--------|
| Mercury Bank (Anvilon LLC ••1345) | ~$22 |
| MiniMax TTS | $25 |
| Vast.ai | $10 |
| **Toplam** | **~$47** |

### Gelir Adayları (Öncelik Sırasıyla)
1. **Upwork** — "YouTube Channel Analytics & AI Signal Reports" → en hızlı nakit ($300-800/iş)
2. **Gumroad** — LESSONS_ENRICHED.md ebook ($9.99) → pasif, 1 saatlik iş
3. **RapidAPI** — Voltara Signal API → aylık abonelik geliri
4. **Orchester SaaS** — danışmanlık botu → Telegram Stars/Stripe

### Şirket
- **Anvilon LLC** — ABD şirketi, aktif
- **Domain:** anvilon.net (Cloudflare)
- **Email:** sovereign@anvilon.net → sovereignanvilon@gmail.com

---

## BÖLÜM 7 — BİLGİ YAPISI

### Sovereign Brain (`/root/sovereign-brain/`)

| Klasör | İçerik |
|--------|--------|
| `research/` | Araştırma bulguları |
| `techniques/` | Teknik yöntemler |
| `decisions/` | Alınan kararlar |
| `entities/` | Kişi/şirket/ürün bilgileri |
| `GELECEK.md` | Vizyon ve gelecek fikirleri |
| `MANIFESTO.md` | Ekosistemi yöneten değerler |

### Önemli Dosyalar
| Dosya | Ne |
|-------|----|
| `/root/CLAUDE.md` | Claude davranış kuralları |
| `/root/STATE.md` | Anlık sistem durumu |
| `/root/SESSION_LOG.md` | Oturum kayıtları |
| `/root/YAPILACAKLAR.md` | Görev listesi (Trello ile sync) |
| `/root/CEBİMİZ.md` | Para, API key, altyapı envanteri |
| `/root/.sovereign_env` | Tüm gizli key'ler |

---

## BÖLÜM 8 — GÜVENLİK

### API Key Yönetimi
- Tüm key'ler: `/root/.sovereign_env` — asla kod içine yazılmaz
- Detay: `/root/CEBİMİZ.md`

### Aria Güvenlik Katmanları
- Rate limiting: IP başına dakikada max 5 istek
- Mesaj limiti: max 500 karakter
- Jailbreak filtresi: kalıp tespiti + reddet
- Oturum sınırı: 10 mesaj → 24 saat IP block
- Honeypot: saldırı denemeleri loglanır → Telegram bildirimi

---

## BÖLÜM 9 — ÖZERKLEŞME YOLU

### Şu An Kırılgan Noktalar
1. Birkan olmadan büyük karar alınamıyor
2. Yeni gelir kanalı açmak insan gerektiriyor (Upwork, Gumroad, RapidAPI kayıt)
3. Önceliklendirme hâlâ insana bağlı (Menejer haftalık yardım ediyor)

### 3 Aylık Hedef
- [ ] Voltara Signal → RapidAPI'de canlı, gelir akıyor
- [ ] Hermes Trello Agent haftalık kartları kendi hallediyor
- [ ] Servis DOWN → otomatik restart → hâlâ DOWN ise ⚡BUGÜN'e kart
- [ ] Sabah raporunda gelir özeti var

### 6 Aylık Hedef
- [ ] Birkan haftada 1 kontrol yeterli
- [ ] ⚡BUGÜN listesi çoğu gün boş
- [ ] Sistem kendi kararlarının %80'ini veriyor
- [ ] Gelir $500+/ay

### 1 Yıllık Hedef
- [ ] Birkan aradan çekilmiş
- [ ] Sistem gelir üretiyor, büyüyor, kendi kendini güncelliyor
- [ ] Önemli stratejik kararlar için ayda 1 toplantı

---

## BÖLÜM 10 — GÜNCELLEME KURALLARI

| Durum | Kim Günceller |
|-------|--------------|
| Yeni servis devreye girer | Ortak (Claude) |
| Servis kapatılır | Ortak (Claude) |
| Yeni otomasyon kurulur | Ortak (Claude) |
| Büyük strateji değişikliği | Menejer onayı + Ortak yazar |
| Gelir durumu değişir | Ortak (Claude) |

**Güncelleme komutu:** `kendini güncelle`

---

## BÖLÜM 11 — ARAÇ PROJELERİ (Manuel / İsteğe Bağlı)

Bu projeler servis olarak değil araç olarak kullanılır — ihtiyaç olunca çalıştırılır.

### 📡 Channel Watcher — `/root/2026-channel-watcher/`
197 YouTube kanalını günlük izler. RSS ile video çeker, transkript alır, MiniMax M3 analiz eder, email + Telegram raporu gönderir.
- **Timer:** `channel-watcher.timer` → sabah 07:00 ET
- **Kullanım:** `radar [komut]`
- **Ana dosyalar:** `fetcher.py` (RSS), `transcriber.py` (NichTube), `analyzer.py` (MiniMax), `reporter.py` (Gmail)

### 🔬 Mercek — `/root/2026-mercek/`
Tek bir YouTube kanalı veya kişiyi derinlemesine analiz eder. Tüm videolar, içerik stratejisi, örüntüler.
- **Kullanım:** `mercek @handle [isim]`
- **Ana dosyalar:** `mercek.py`, `raporlar/` (geçmiş analizler)

### 📚 Lesson Extractor — `/root/2026-lesson-extractor/`
YouTube transkriptlerinden 5 model paralel çalışarak iş ve trading kuralları damıtır.
- **Çıktı:** `LESSONS_ENRICHED.md` → 1126 finans kuralı (Gumroad ebook adayı)
- **Kullanım:** `kazı [dosya/konu]`
- **Ana dosyalar:** `extractor.py`, `enricher.py`, `dedup_v2.py`, `merge.sh`
- **Model çıktıları:** `ay/`, `derin/`, `dip/`, `flash/`, `mini/` (her modelin checkpoint'i)

### 🤖 Grok Pipeline — `/root/2026-grok-pipeline/`
xAI Grok API ile video analizi, piyasa araştırması ve tahmin takibi araçları.
- **Ana dosyalar:** `grok_mercek.py` (kişi analizi), `grok_radar.py` (piyasa), `grok_kazi.py` (kazı), `grok_guru_karnesi.py` (guru puanı)
- **Çıktılar:** `output/` dizininde JSON + Markdown

### 💬 Consulting Bot — `/root/2026-consulting-bot/`
Telegram üzerinden AI danışmanlık botu. Orchester entegrasyonu, quota yönetimi. Şu an kapalı.
- **Bekleniyor:** BotFather'dan token al → `.env`'e yaz → `consulting-bot.service` başlat
- **Ana dosyalar:** `bot.py`, `orchester_client.py`, `quota.py`

### 🏆 Prophet Rank — `/root/prophet-rank/`
YouTube finans guru'larının tahmin performansını puanlar, sıralar, Medium makale üretir.
- **Ana dosyalar:** `scorer.py`, `report.py`, `medium_article.py`, `send_email.py`

### 📺 YT Channel Archiver — `/root/2026-yt-channel-archiver/`
Bir YouTube kanalındaki tüm videoların transkriptini çekip her video için ayrı Markdown dosyası oluşturur.
- **Ana dosyalar:** `harvester.py`, `transcript.py`, `web.py` (arayüz)

### 🧠 Kermes — `/root/2026-kermes/`
Token-smart AI agent katmanı. Sorguyu sınıflandırır (fast/mid/best), ucuz modele yönlendirir, cache'ler, öğrenir.
- **Ana dosyalar:** `kermes/classifier.py`, `kermes/router.py`, `kermes/brain.py`, `kermes/cache.py`

### 🏪 ESNAF — `/root/2026-esnaf/`
Solopreneur / indie hacker / SaaS / pazarlama kanallarından iş bilgeliği damıtır. 16 kanal, tahmini 8-24K video.
- **Çıktı:** `ESNAF_LESSONS.jsonl` (atomik, RAG için) + `ESNAF_PLAYBOOK.md` (kategori bazlı okunabilir)
- **Kullanım:** `python esnaf_kazi.py pilot` → `extract` → `export`
- **CLI:** `discover / ingest / extract / validate / export / status / retry-failed / pilot`
- **Model:** DIP Flash (deepseek-v4-flash) → low confidence → DERİN (deepseek-v4-pro)
- **Kategoriler:** Fikir & Doğrulama / Ürün & MVP / Pazarlama & Growth / Satış & Fiyatlandırma / Müşteri & Retention / Para & Bootstrap / Ekip & Operasyon / Zihniyet & Verimlilik / Ajans & Servis
- **Checkpoint:** SQLite manifest (esnaf.db), chunk bazlı, kesintiye dayanıklı
- **Tasarım:** Mentor Fable + Güneş Sol sentezi (2026-07-10)

### 🚚 Trucking Sim — `/root/2026-trucking-survival-sim/`
ABD owner-operator trucking sektörü için Monte Carlo hayatta kalma simülatörü.
- **Ana dosyalar:** `run_sim.py`, `sim/monte_carlo.py`, `sim/financial.py`, `sim/market.py`

### 📱 ReelScribe — `/root/2026-reelscribe/`
iOS SwiftUI YouTube transkript uygulaması. Telefon IP'siyle residential YouTube bloğunu bypass eder.

### 🥧 Pi Worker — `/root/2026-pi-worker/`
Raspberry Pi 5 + Geeni fiş ile ev IP'sinden YouTube audio worker. Tuya entegrasyonu bekliyor.
- **Ana dosyalar:** `pi_worker.py` (Pi tarafı), `vps_orchestrator.py` (VPS koordinatörü)

---

## BÖLÜM 12 — SCRIPTS ARAÇ KİTİ (`/root/scripts/`)

| Script | Ne Yapar |
|--------|---------|
| `trello_sync.py` | Trello ↔ YAPILACAKLAR.md çift yönlü senkronizasyon (master: Trello) |
| `trello_prioritize.py` | Trello kartlarına öncelik renk label ekler |
| `daily-snapshot.sh` | Gece 23:00 ET — 8 repo GitHub'a otomatik yedekle |
| `session_end_hook.sh` | Oturum kapanışında STATE.md + SESSION_LOG günceller |
| `session_summarizer.py` | Oturum özetleyici |
| `docker-cleanup.sh` | Aylık Docker image + volume temizleme |
| `bash_guard.sh` | Tehlikeli komut önleme guard |
| `pretool_guard.sh` | Tool çağrısı öncesi doğrulama |
| `codedash.py` | Proje kod istatistikleri dashboard |
| `push_to_vps.sh` | Mac'ten VPS'e kod push |
| `pull_from_mac.sh` | Mac'ten proje dosyası çek |
| `trade_active_extractor.py` | Aktif trade pozisyonlarını çıkar |
| `ekosistem_pdf.py` | Ekosistem raporu PDF üretici |

---

## EKLER — HIZLI KOMUT REFERANSı

```bash
# Servis durumu
systemctl status voltara hermes-trello-agent orchester

# Manuel Trello sync
python3 /root/scripts/trello_sync.py

# Orkestra modları listele
python3 /root/2026-orchester/terminal_orchester.py --list-modes

# Orkestra - koro modu
python3 /root/2026-orchester/terminal_orchester.py --mode koro "görev"

# Sistem kart açsın
python3 -c "import sys; sys.path.insert(0,'/root/scripts'); from trello_sync import add_task; add_task('Görev', 'Detay', priority='kritik')"

# Tüm aktif servisler
systemctl list-units --type=service --state=active | grep -E "sovereign|hermes|aria|orchester|voltara"
```

---

*Sovereign Ekosistemi • Salem NJ • 2026*
*Bu belge sistemin büyüdüğü her an güncellenir.*
