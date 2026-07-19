# Algo Trading Stack — Birkan İçin Geleneksel Piyasalar

## Ne Zaman Kullan
- Alpaca API ile hisse/ETF botu geliştirirken
- Backtest, walk-forward optimizasyon, strateji validasyonu yaparken
- Coinbase (kripto) → geleneksel piyasalar geçişi planlarken
- Portföy risk yönetimi hesaplamalarında

---

## Alpaca API — Hızlı Başlangıç

```python
import alpaca_trade_api as tradeapi

# Paper trading
api = tradeapi.REST(
    key_id='APCA-API-KEY-ID',
    secret_key='APCA-API-SECRET-KEY',
    base_url='https://paper-api.alpaca.markets'
)

# Live'a geçmek için SADECE bu satırı değiştir:
# base_url='https://api.alpaca.markets'
```

**Kritik fark:** Coinbase 7/24, Alpaca NYSE saatleri (09:30–16:00 ET). Zamanlama mantığını ayrı tut.

```python
from datetime import datetime
import pytz

def is_market_open():
    et = pytz.timezone('US/Eastern')
    now = datetime.now(et)
    # Sadece hafta içi 09:30–16:00
    return (now.weekday() < 5 and
            now.hour >= 9 and (now.hour < 16 or (now.hour == 9 and now.minute >= 30)))
```

---

## Market Data — yfinance KULLANMA

```python
# ❌ YAPMA — IP ban riski, SLA yok, Yahoo API 2017'de kapandı
# import yfinance as yf

# ✅ YAP — Alpaca kendi market data API'si (aynı key)
bars = api.get_bars('AAPL', '1Day', limit=100).df

# Gecelik/extended hours → BOATS feed
from alpaca_trade_api import DataFeed
bars = api.get_bars('AAPL', '1Hour', feed=DataFeed.BOATS).df

# Kripto data → /v1beta3 endpoint (otomatik)
crypto = api.get_crypto_bars('BTC/USD', '1Day').df

# Options data → /v1beta1 endpoint (Feb 2024+, otomatik)
chain = api.get_option_chain('AAPL')
```

### API Karşılaştırma

| API | Fiyat | Güçlü olduğu yer |
|-----|-------|-----------------|
| **Alpaca Market Data** | Ücretsiz (IEX) | Research → execution tek stack |
| **Polygon.io** | $29/mo | En iyi genel; tick data, flat files büyük backtest |
| **Tiingo** | Ücretsiz tier | Temiz EOD + fundamentals, akademik |
| **Tradier** | $10/mo | Options için en iyi: Greeks dahil full chain, REST |
| **yfinance** | Ücretsiz | **KULLANMA** — resmi API 2017'de kapandı, IP ban riski |

> Backtesting framework seçimi için: `~/.claude/skills/backtesting-python/SKILL.md`

---

## Walk-Forward Optimization (Zorunlu)

Sadece in-sample backtest overfitting'e yol açar. Her zaman out-of-sample doğrula:

```python
def walk_forward_test(data, strategy_fn, train_ratio=0.7, n_splits=5):
    """
    data: tüm fiyat serisi
    strategy_fn: (train_data) -> params döndürür
    Her split'te: train ile optimize et, test ile doğrula
    """
    results = []
    split_size = len(data) // n_splits
    
    for i in range(n_splits):
        start = i * split_size
        mid = start + int(split_size * train_ratio)
        end = start + split_size
        
        train = data[start:mid]
        test = data[mid:end]
        
        params = strategy_fn(train)           # in-sample optimizasyon
        perf = backtest(test, params)         # out-of-sample doğrulama
        results.append(perf)
    
    return results
```

---

## Kelly Criterion + Max Drawdown

```python
def kelly_fraction(win_rate, avg_win, avg_loss):
    """
    win_rate: kazanma oranı (0–1)
    avg_win: ortalama kazanç (mutlak değer)
    avg_loss: ortalama kayıp (mutlak değer)
    
    Genellikle yarı-Kelly kullan (0.5 * kelly) — gerçek dünya için daha güvenli
    """
    b = avg_win / avg_loss       # kazanç/kayıp oranı
    q = 1 - win_rate
    kelly = (win_rate * b - q) / b
    return max(0, kelly * 0.5)   # half-Kelly, negatif → pozisyon alma

def max_drawdown(equity_curve):
    """Equity curve listesinden max drawdown hesapla (0–1 arası)"""
    peak = equity_curve[0]
    max_dd = 0
    for value in equity_curve:
        if value > peak:
            peak = value
        dd = (peak - value) / peak
        max_dd = max(max_dd, dd)
    return max_dd
```

---

## ETF Rotasyon Stratejisi (Pseudokod)

```
Her Ay Başında:
1. Universe: SPY, QQQ, GLD, TLT, IWM gibi ETF'ler
2. Her ETF için momentum skoru hesapla (12-1 ay getirisi)
3. En yüksek momentum'a sahip N ETF'i seç
4. Eşit ağırlıkla pozisyon aç
5. Stop-loss: %15 drawdown'da tümünü çık
6. Momentum negatifse tümünü cash'e al (Bear filter)
```

---

## Gizli Tuzaklar

| Tuzak | Açıklama | Çözüm |
|-------|----------|-------|
| **Survivorship Bias** | Sadece hayatta kalan hisseleri test etmek başarıyı şişirir | Delisted hisseleri de dahil et |
| **Slippage** | Gerçek dolum fiyatı backtest fiyatından farklı | %0.1–0.5 slippage ekle |
| **Look-Ahead Bias** | Gelecek veriyi geçmiş kararda kullanmak | Sadece `shift(1)` ile önceki çubuk verisi kullan |
| **Split Adjustment** | Hisse bölünmeleri fiyatı yapay düşürür | Adjusted close kullan |
| **Survivorship** | Endeks bileşeni değişikliklerini yoksaymak | Point-in-time endeks verileri al |

---

## LLM Destekli Analiz (Genel)

NexusTrade metodolojisi (140.000 backtest'ten çıkarılmış):
1. Geçmiş backtest'leri bileşenlerine ayır (strateji, entry/exit, indikatör)
2. Her bileşen için Sharpe/Calmar/Sortino hesapla
3. **TF-IDF + cosine similarity ile diversity filter uygula** — LLM binlerce benzer momentum stratejisi üretir; bu filtre aynı varyasyonları çıkarır, çeşitli kombinasyon seçtirir
4. "Elite tier" bileşenlerini LLM system prompt'una enjekte et
5. LLM → portföy önerisi → walk-forward validasyon
6. n8n üzerinden günlük 07:00 raporu → Telegram

**Kanıtlanmış sonuç:** 36.94% vs SPY 16.0%, Sharpe 1.39 vs 0.61, 0.3% slippage dahil.

**Uyarı:** Herhangi bir platform "backtest sonuçları yüksek" diye iddia ediyorsa şüpheyle yaklaş.

---

## Makro Rejim Sinyalleri (Valuation-Based)

### Shiller PE Rejim Filtresi
Shiller PE (CAPE), piyasanın uzun vadeli beklenen getirisini tahmin etmek için en güçlü tek indikatörlerden biri:

```python
# Shiller PE > 30 → tarihi olarak sonraki 10-17 yılda düşük getiri beklentisi
# Dot-com zirvesinde ~44, 2024 seviyesi ~34-36

# Strateji seçimini etkiler:
# - Yüksek PE (>30): momentum stratejileri daha riskli, değer/temettü öne çıkar
# - Düşük PE (<15): momentum ve büyüme stratejileri tarihsel olarak daha iyi çalışır
# - Orta PE (15-25): nötr

# Kaynak: multpl.com/shiller-pe (güncel CAPE)
```

### 17 Yıllık Return Auto-Correlation (R²≈0.88)
Akademik araştırma bulgusu: ~17 yıl geriye ve ileriye bakıldığında **güçlü negatif korelasyon**:

```python
# Yüksek geçmiş 17 yıllık getiri → düşük ileriki 17 yıllık getiri (ve tersi)
# R² ≈ 0.88 — finansal tahmin için alışılmadık derecede yüksek

# Pratik anlamı:
# 2009-2024 dönemi = çok güçlü getiri dönemi
# → 2025-2042 dönemi için beklenti düşürmek matematiksel olarak destekli

# Backtest dönem seçimine etkisi:
# "En iyi 15 yılı backtest et" → overfit riski çünkü o dönem anormal
# Mutlaka farklı rejim dönemlerini (düşük getiri dönemleri de dahil) test et
```

### Nominal vs Reel Getiri (M2 Deflasyonu)
Backtest sonuçlarını reel satın alma gücüyle değerlendirme:

```python
import numpy as np

def real_return(nominal_return: float, m2_growth: float = 0.068) -> float:
    """
    nominal_return: yıllık nominal getiri (örn. 0.043 = %4.3)
    m2_growth: M2 büyüme hızı (tarihsel ~%6.8/yıl, varsayılan)
    
    S&P 500 beklenen nominal getiri (2025-2042): ~%4.3 (valuation modelleri)
    M2 büyümesi tarihsel: ~%6.8/yıl
    → Reel getiri: ~%4.3 - %6.8 = -%2.5/yıl (satın alma gücünde kayıp)
    """
    return (1 + nominal_return) / (1 + m2_growth) - 1

# Örnek
nominal = 0.043   # %4.3 nominal
real = real_return(nominal)
print(f"Nominal: {nominal*100:.1f}% → Reel: {real*100:.1f}%")
# Output: Nominal: 4.3% → Reel: -2.4%

# 17 yıl bileşik etki
years = 17
purchasing_power_change = (1 + real) ** years - 1
print(f"17 yılda satın alma gücü değişimi: {purchasing_power_change*100:.1f}%")
# Output: ~-34% (nominal kazanırken reel güç kaybı)
```

> **Uyarı:** M2 büyüme hızı dönemsel değişir. Bu hesaplama tahmindir, kesin değil. Portföy değerlendirmesinde reel getiriyi **ek bilgi** olarak kullan, tek kriter olarak değil.

---

## M2 Likidite ve Piyasa Korelasyonu

> **Kritik Düzeltme — LLM Hallüsinasyon Riski Yüksek:**
> - "M2 ile %94 korelasyon" → **Bitcoin ile Küresel M2 arasında** (Lyn Alden, Mayıs 2013–Temmuz 2024)
> - **SPY ile M2 korelasyonu bu değil.** SPY kurumsal geri alım ve temettü beklentilerinden etkilenir
> - Rolling 12-aylık pencerede Bitcoin-M2 korelasyonu 0.51'e düşer — kesin sinyal değil
> - "M2 Divergence SPY" aratırken lazer fiziğindeki M2 (beam quality factor) literatürüyle karışır → LLM hallüsinasyonu tetikler; source doğrula

```python
# M2 Divergence Stratejisi (kavramsal):
# SPY fiyatı Küresel M2'nin yukarısında sapıyorsa (divergence)
# → uzun vadede kapanma beklentisiyle pozisyon
# Ama: rolling 12m korelasyon 0.51 — sinyali tek başına kullanma
# Bitcoin için daha güçlü barometrik sinyal
```

---

## Kripto — Gerçek Edge Nerede?

Candlestick pattern → fiyat hareketi zayıf bir edge. Gerçek edge:

```python
# Funding rate + Open Interest takibi
# Yüksek pozitif funding = long ağır = squeeze riski
# OI aniden düşüyor + fiyat yükseliyor = güçlü trend sinyali

# Corvino ensemble yaklaşımı (DOĞRULANMIŞ production sistemi, ~%60 TP hit rate):
# XGBoost + LightGBM + LSTM + Transformer
# → Her model kendi signal üretir, voting/averaging ile nihai karar
# → GİRİŞ sinyalleri: ML ensemble
# → ÇIKIŞ yönetimi (TP/SL): ATR (Average True Range) — Deep Learning değil!
#   Neden: Deep Learning TP/SL'de overfitting yapar; ATR dinamik volatilite bazlı,
#   daha yüksek isabet oranı sağlar.
# Özellikler: funding rate, OI delta, liquidation data, CVD
```

### Kripto Fonlama Arbitrajı (Delta-Nötr)
Perpetual futures'ta long+short arbitraj — piyasa yönünden bağımsız fonlama getirisi:
```python
# Temel mantık:
# 1. Spot piyasada kripto al (long)
# 2. Aynı miktarı futures'ta aç (short)
# 3. Delta = 0 → piyasa yönü önemsiz
# 4. Gelir: 8 saatlik fonlama ödemeleri
# Çapraz borsa için: Binance, Bybit, OKX'i eşzamanlı izle
# MCP: github.com/kukapay/funding-rates-mcp — anlık fonlama verileri
```

---

## Kanıtlanmış Stratejiler (Backtest Verisinden)

1. **"All-Weather" Momentum**: S&P500 + güçlü fundamentals + 15 en yüksek aylık değişim hissesi → SPY'ı her dönemde geçti
2. **"Bear Market Specialist"**: Pozitif net gelir + rating 2 + en düşük 14-gün RSI → bear markette parlar
3. **"Capital Protection"**: SPY > 200-gün SMA → momentum; altında → temettü + cash
4. **Funding Rate Edge**: Kripto'da yüksek pozitif funding = short squeeze potansiyeli
5. **ETF Rotasyon**: Aylık momentum rebalans (SPY, QQQ, GLD, TLT, IWM)

---

## Kaynaklar
- Alpaca Docs: docs.alpaca.markets
- vectorbt: vectorbt.pro
- Repo: github.com/alpacahq/alpaca-trade-api-python
