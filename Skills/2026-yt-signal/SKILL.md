---
name: 2026-yt-signal
description: |
  YouTube finans transkript sinyal sistemi. 2961 video, 21 kanal (Graham Stephan,
  Meet Kevin, Bora Özkent, Paribu vb.) — ticker bazlı sentiment, konsensüs,
  anomali tespiti. API: localhost:8007. LLM Wiki pattern ile çalışır.
  
  TRIGGER: "transkript", "YouTuber ne diyor", "sinyal", "konsensüs", "bullish/bearish",
  ticker sorgusu (TSLA, BTC, NVDA...), "kanal analizi", "bu hafta ne konuşuldu"
---

# Voltara Signal Skill

YouTube finans transkriptlerinden piyasa sinyali çıkaran sistem.

## Mimari (LLM Wiki Pattern)

```
video_transcripts (raw)     → ham veri, 2961 video, her gün yeni geliyor
       ↓ indexer.py
video_signals (sources)     → ticker, sentiment, signal_type, market_relevance
       ↓ graph_builder.py
graph.json (entities)       → node + edge graph, ticker-kanal ilişkileri
       ↓ export_wiki.py
/root/wiki/entities/*.md    → her ticker için Markdown sayfası (Obsidian uyumlu)
/root/wiki/syntheses/*.md   → haftalık konsensüs
```

**Write-path:** `yt-signal-indexer.timer` — saatte 100 video işler  
**Read-path:** `localhost:8007` API veya aşağıdaki CLI komutları

## API Endpoint'leri

```bash
# Genel durum
curl localhost:8007/stats

# Ticker sorgusu
curl "localhost:8007/query?ticker=NVDA&days=7"
curl "localhost:8007/query?ticker=BTC&sentiment=bullish"

# Haftalık konsensüs
curl "localhost:8007/consensus?days=7"

# Anomali tespiti (bu hafta anormal artış)
curl "localhost:8007/anomaly"
```

## CLI Alternatifleri

```bash
cd /root/2026-yt-signal
venv/bin/python query.py --ticker NVDA --days 7
venv/bin/python query.py --anomaly
venv/bin/python query.py --stats
venv/bin/python graph_builder.py --consensus
```

## Wiki Güncelleme

```bash
cd /root/2026-yt-signal
venv/bin/python graph_builder.py          # graph.json güncelle
venv/bin/python export_wiki.py            # /root/wiki/ Markdown sayfaları güncelle
```

## Kanallar

| Kanal | Odak |
|-------|------|
| Graham Stephan | Genel hisse, gayrimenkul |
| Meet Kevin | Hisse, ekonomi yorumu |
| Andrei Jikh | Kripto, temettü |
| Bora Özkent | Türk yatırım |
| Paribu | Kripto (Türkçe) |
| Dividend Talks | Temettü hisseleri |
| Yatırım 101 | Türk borsa |
| + 14 diğer | Çeşitli finans |

## 6 Katman (Geliştirme Yol Haritası)

1. ✅ **Entity Extraction** — MiniMax M3, çalışıyor
2. ✅ **LLM Wiki Export** — /root/wiki/, çalışıyor
3. ✅ **Cross-Reference & Anomali** — API hazır
4. ⬜ **Piyasa Korelasyonu** — price_outcomes tablosu (Phase 2)
5. ⬜ **Kanal Güvenilirlik Skoru** — ne söyledi vs ne oldu
6. ⬜ **Self-Evolving Bot** — AlphaEvolve döngüsü

## Bağlantılar

- Proje: `/root/2026-yt-signal/`
- Wiki: `/root/wiki/`
- Servis: `systemctl status yt-signal.service`
- Timer: `systemctl status yt-signal-indexer.timer`
- DB: `10.0.3.2:5432 / n8n` (video_transcripts, video_signals)

### OTOMATİK Öğrenim [2026-06-27]
> Inbound brand deal'lerde entity türü (ajans vs marka direkt) cevap stratejisini tamamen değiştirir çünkü bütçe, karar verici ve motivasyon farklıdır.
>
> yt-signal skill'ine 'brand_deal_entity_classification' kuralı ekle: transkript'te 'agency reached out' / 'brand reached out' sinyali taranıp ilgili strateji template'i döndürülsün.
