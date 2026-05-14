# Evrim Geçiren Trade Bot — Konsept Notları

> **Kaynak İlham:** [karpathy/autoresearch](https://github.com/karpathy/autoresearch)
> autoresearch'ün temel döngüsünü (Mutasyon → Değerlendir → Koru/At) 
> trading stratejilerine uyarlayan otonom bir araştırma sistemi.

---

## Temel Konsept

AI ajan gece boyunca `strategy.py`'yi düzenler, backtest yapar, sonucu ölçer.
İyi sonuç → tutulur. Kötü sonuç → geri alınır. Sabah en iyi strateji hayatta.

```
Mevcut Strateji
     ↓
  AI Ajan (Claude/Gemini)
     ↓ strategy.py'yi düzenle
  Backtest (geçmiş data)
     ↓
  Sharpe Ratio / PnL / Win Rate
     ↓
  İyileştiyse → GIT COMMIT (tut)
  Kötüleştiyse → GIT REVERT (at)
     ↓
  Tekrar (gecelik ~100 deney)
```

---

## autoresearch → Trade Bot Mapping

| autoresearch | Trade Bot Karşılığı |
|---|---|
| `train.py` | `strategy.py` — ajan bu dosyayı düzenler |
| 5 dakika eğitim | Backtest süresi (örn. 1 yıllık data) |
| `val_bpb` metriği | **Sharpe Ratio** (veya PnL, Win Rate, Max Drawdown) |
| `program.md` | `research.md` — trading araştırma talimatları |
| Git commit/revert | Strateji versiyonlama mekanizması |
| Gecelik 100 deney | Gecelik N strateji mutasyonu |
| `prepare.py` (dokunulmaz) | `backtest_engine.py` (dokunulmaz) |

---

## Proje Dosya Yapısı (Hedef)

```
evolving-trade-bot/
├── backtest_engine.py   ← DOKUNULMAZ (hazır backtest altyapısı)
├── strategy.py          ← AI AJAN BURASI DÜZENLEYECEk
├── research.md          ← Ajan talimatları (sen yazıyorsun)
├── data/                ← OHLCV fiyat verileri
├── results/             ← Her deneyin sonuçları (JSON/CSV)
└── pyproject.toml       ← Bağımlılıklar
```

---

## Değerlendirme Metrikleri (Ne Ölçülecek)

```python
# Backtest sonrası hesaplanacak metrikler
metrics = {
    "sharpe_ratio":    ...,   # Ana metrik (>1.5 hedef)
    "total_pnl":       ...,   # Toplam kar/zarar
    "win_rate":        ...,   # Kazanma oranı (>55% hedef)
    "max_drawdown":    ...,   # Maksimum düşüş (<%15 hedef)
    "profit_factor":   ...,   # Gross profit / Gross loss
}
```

**Tek ana metrik önce:** Sharpe Ratio (autoresearch'teki val_bpb gibi)

---

## research.md İçeriği (Ajan Talimatları)

```markdown
# Trading Research Program

## Görev
strategy.py dosyasını düzenle. Backtest çalıştır. 
Sharpe Ratio > önceki denemeden iyiyse tut, değilse geri al.

## Kural
- backtest_engine.py dosyasına DOKUNMA
- Her denemede tek bir değişiklik yap (A/B test mantığı)
- Değişiklik türleri: indikatör ekleme, parametre ayarı, 
  giriş/çıkış koşulu, position sizing, risk yönetimi

## Mevcut En İyi Sonuç
Sharpe: X.XX | PnL: $X | Win Rate: X%
```

---

## Teknik Stack (Planlama)

### Backtest Engine
- **Backtrader** veya **vectorbt** (Python)
- Veri: Binance/Yahoo Finance OHLCV
- Sembol: BTC/USDT (başlangıç için)

### AI Ajan
- **Claude Code CLI** (Anthropic API key)
- veya **Aider** (herhangi bir LLM ile)
- Ajan `strategy.py`'yi düzenler, terminalde backtest çalıştırır

### Versiyonlama
- Git — her deney otomatik commit
- Kötü deney → `git revert` ile geri al

### Veri Kaynakları
- `ccxt` kütüphanesi (Binance, Coinbase vb.)
- Yahoo Finance (hisse senedi için `yfinance`)

---

## Geliştirme Yol Haritası

### Faz 1 — Temel Altyapı
- [ ] `backtest_engine.py` yaz (veri yükleme + simülasyon)
- [ ] `strategy.py` basit bir SMA crossover ile başlat
- [ ] Metrik hesaplama sistemi (Sharpe, PnL, Win Rate)
- [ ] Git entegrasyonu (auto-commit/revert)

### Faz 2 — Ajan Entegrasyonu  
- [ ] `research.md` talimat dosyası yaz
- [ ] Claude Code / Aider ile test et
- [ ] Ajan döngüsünü otomatize et (cron veya script)

### Faz 3 — Gelişmiş Özellikler
- [ ] Çoklu sembol desteği
- [ ] Portföy optimizasyonu
- [ ] Paper trading (gerçek zamanlı, parasız)
- [ ] Dashboard (sonuçları görselleştir)

### Faz 4 — Canlı İşlem (isteğe bağlı)
- [ ] Exchange API entegrasyonu
- [ ] Risk limitleri ve kill switch
- [ ] Gerçek para ile küçük pozisyonlar

---

## Önemli Notlar & Riskler

> **NOT:** autoresearch H100 GPU gerektirir ama trade bot için GPU gerekmez.
> Backtest CPU'da çalışır, Mac'te sorunsuz.

### Teknik Riskler
- **Overfitting:** Ajan geçmişe çok iyi uyar, gelecekte başarısız olabilir
  - Çözüm: Walk-forward testing (farklı dönemler)
- **Lookahead Bias:** Backtest geleceği görüyorsa sonuçlar yanıltıcıdır
  - Çözüm: Backtest engine'i dikkatli yaz, sadece geçmiş veri kullan
- **Token Maliyeti:** Gece 100 deney = çok API çağrısı = maliyet
  - Çözüm: Denemeleri sınırla veya local model (Ollama) kullan

### Finansal Riskler
- Otonom bir bot real money ile çalıştırılmadan önce:
  - En az 3 ay paper trading
  - Kill switch mekanizması
  - Maksimum günlük kayıp limiti

---

## Bağlantılı Kaynaklar

- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — İlham kaynağı
- [miolini/autoresearch-macos](https://github.com/miolini/autoresearch-macos) — Mac fork
- [vectorbt](https://vectorbt.dev/) — Python backtest kütüphanesi
- [ccxt](https://github.com/ccxt/ccxt) — Exchange API kütüphanesi
- [Aider](https://aider.chat/) — Terminal AI coding agent
