---
name: backtesting-python
description: |
  Python ile trading stratejisi backtesting rehberi. backtesting.py, VectorBT, Backtrader framework seçimi;
  walk-forward validasyon, slippage, survivorship bias; Polygon.io / Tiingo / Alpaca data kaynakları;
  Alpaca deploy; AI destekli 140K backtest metodolojisi.

  TRIGGER: backtesting, strateji test, walk-forward, vectorbt, backtrader, slippage, sharpe, drawdown
---

# Python Backtesting — Strateji Test Rehberi

## Ne Zaman Kullan
- Bir trading stratejisi yazmadan önce neyle backtest yapacağını seçerken
- VectorBT, Backtrader, backtesting.py arasında karar verirken
- Walk-forward, slippage, bias gibi kavramları uygulamaya dökerken
- Tarihsel data kaynağı seçerken (yfinance değil!)

---

## Framework Seçimi

| | backtesting.py | Backtrader | VectorBT | Zipline-Reloaded |
|--|----------------|------------|----------|---------|
| **Hız** | Orta | Yavaş | **Çok hızlı** | Orta |
| **Kolaylık** | ⭐ En kolay | Kolay | Zor API | Orta |
| **Gerçekçilik** | Orta | **Yüksek** (tick-by-tick) | Düşük | Orta |
| **Parametre tarama** | Grid search var | Yavaş | 1M sim / 20s | Hayır |
| **Geliştirme durumu** | Aktif (geç 2025) | Durmuş (2018) | **Açık kaynak aktif** (v0.28.5, Mart 2026) | **Aktif** (v3.1.1, Temmuz 2025) |
| **Ne zaman kullan** | Hızlı prototip | Final validasyon | Parametre tarama | Kurumsal portföy |

> **Düzeltme:** VectorBT Community sürümü terk edilmemiştir. Kurucu hata düzeltmelerini ve yeni Python uyumunu sürdürüyor; opsiyonel Rust motoru (vectorbt[rust]) da açık kaynak. PRO ücretli ama Community production-ready.

**Kural:** VectorBT ile parametreleri tara → Backtrader ile validasyon yap → Alpaca ile deploy et.

### RustyBT — Yeni Nesil Zipline
Zipline-Reloaded üzerine kurulan fork: Polars ile işleme, Parquet depolama, Decimal tipi (finansal kesinlik). Zipline'dan 5-10x hız kazandırır. Büyük ölçekli backtest için düşün.

---

## Data Kaynakları

| Kaynak | Fiyat | Neden |
|--------|-------|-------|
| **Polygon.io** | $29/mo | En iyi genel; REST + WebSocket, tick seviye, büyük backtest için flat file indir |
| **Tiingo** | Ücretsiz tier var | Temiz EOD data, fundamentals, akademik backtest için ideal |
| **Alpaca Market Data** | Ücretsiz (IEX) | Research → execution aynı stack; crypto + hisse + options |
| **Alpha Vantage** | 25/gün ücretsiz | Prototip/öğrenme; prodda kullanma |
| **yfinance** | Ücretsiz | **KULLANMA** — Yahoo resmi API'yi 2017'de kapattı, hâlâ web scraping; IP ban riski, SLA yok |

> Polygon.io artık "Massive.com" markası altında da biliniyor — aynı servis.

---

## backtesting.py — Hızlı Başlangıç

```python
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas_ta as ta
import pandas as pd

class SMACross(Strategy):
    n1 = 10   # optimize edilecek parametre
    n2 = 20

    def init(self):
        self.sma1 = self.I(ta.sma, self.data.Close, self.n1)
        self.sma2 = self.I(ta.sma, self.data.Close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.position.close()

# data: OHLCV pandas DataFrame (Open, High, Low, Close, Volume)
bt = Backtest(
    data, SMACross,
    cash=10_000,
    commission=0.001,   # %0.1 komisyon
    slippage=0.001,     # %0.1 slippage — MUTLAKA ekle
)
stats = bt.run()
print(stats)

# Parametre optimizasyonu
stats_opt = bt.optimize(
    n1=range(5, 30, 5),
    n2=range(20, 60, 10),
    maximize='Sharpe Ratio',
    constraint=lambda p: p.n1 < p.n2,   # mantıksal kısıt
)
```

---

## VectorBT — 1M Simülasyon

```python
import vectorbt as vbt
import numpy as np

# Polygon.io veya Alpaca'dan data al (yfinance KULLANMA)
# price = pd.read_parquet("spy_daily.parquet")["close"]

# Tüm SMA kombinasyonlarını test et — vektörize
fast_vals = np.arange(5, 50, 5)
slow_vals = np.arange(20, 100, 10)

fast_ma = vbt.MA.run(price, fast_vals, short_name='fast')
slow_ma = vbt.MA.run(price, slow_vals, short_name='slow')

entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

pf = vbt.Portfolio.from_signals(
    price, entries, exits,
    init_cash=10_000,
    fees=0.001,
    slippage=0.001,
)

# Hangi kombinasyon en iyi?
best_idx = pf.sharpe_ratio().idxmax()
print(f"En iyi: fast={best_idx[0]}, slow={best_idx[1]}")

# Isı haritası
pf.sharpe_ratio().vbt.heatmap(
    x_level='fast_window',
    y_level='slow_window'
)
```

---

## Walk-Forward Validation (Zorunlu)

Sadece in-sample backtest = overfitting garantisi. **Her zaman out-of-sample doğrula:**

```python
import numpy as np
from typing import Callable

def walk_forward(
    data: pd.DataFrame,
    strategy_fn: Callable,   # (train_data) -> params dict
    backtest_fn: Callable,   # (test_data, params) -> metrics dict
    n_splits: int = 5,
    train_ratio: float = 0.7
) -> list[dict]:
    """
    Her split'te:
    - Train bölümünde parametre optimize et
    - Test bölümünde (görülmemiş data) doğrula
    """
    results = []
    split_size = len(data) // n_splits

    for i in range(n_splits):
        start = i * split_size
        mid = start + int(split_size * train_ratio)
        end = start + split_size

        train = data.iloc[start:mid]
        test = data.iloc[mid:end]

        params = strategy_fn(train)          # in-sample optimize
        metrics = backtest_fn(test, params)  # out-of-sample doğrula
        metrics['split'] = i
        results.append(metrics)

    return results

# Kullanım
results = walk_forward(ohlcv_data, optimize_params, run_backtest)
avg_sharpe = np.mean([r['sharpe'] for r in results])
print(f"Out-of-sample ortalama Sharpe: {avg_sharpe:.2f}")
```

---

## Metrik Hesaplama

```python
import numpy as np

def sharpe_ratio(returns: np.ndarray, periods: int = 252) -> float:
    """Günlük return serisi → annualized Sharpe"""
    if returns.std() == 0:
        return 0.0
    return np.sqrt(periods) * returns.mean() / returns.std()

def sortino_ratio(returns: np.ndarray, periods: int = 252) -> float:
    """Sadece downside volatility kullanır"""
    downside = returns[returns < 0]
    if len(downside) == 0 or downside.std() == 0:
        return float('inf')
    return np.sqrt(periods) * returns.mean() / downside.std()

def max_drawdown(equity_curve: np.ndarray) -> float:
    """Equity curve'den max drawdown (negatif, örn. -0.25 = %25)"""
    cummax = np.maximum.accumulate(equity_curve)
    return ((equity_curve - cummax) / cummax).min()

def calmar_ratio(returns: np.ndarray, periods: int = 252) -> float:
    """Annualized return / max drawdown"""
    equity = (1 + returns).cumprod()
    ann_return = (equity[-1]) ** (periods / len(returns)) - 1
    mdd = abs(max_drawdown(equity))
    return ann_return / mdd if mdd > 0 else 0.0
```

---

## Reel Getiri Hesabı (M2 Deflasyonu)

Backtest sonuçları nominal gösterir. Reel satın alma gücünü ayrıca hesapla:

```python
def real_return(nominal: float, m2_growth: float = 0.068) -> float:
    """Nominal getiriyi M2 büyümesine göre reel getiriye çevir."""
    return (1 + nominal) / (1 + m2_growth) - 1

def purchasing_power_change(nominal: float, years: int, m2_growth: float = 0.068) -> float:
    """N yıl sonunda satın alma gücündeki değişim."""
    r = real_return(nominal, m2_growth)
    return (1 + r) ** years - 1

# Örnek: S&P 500 beklenen nominal ~%4.3, M2 ~%6.8
print(real_return(0.043))          # → -0.024 (-%2.4/yıl reel)
print(purchasing_power_change(0.043, 17))  # → ~-34% (17 yılda reel kayıp)
```

> M2 büyümesi tarihsel ~%6.8/yıl. Backtest dönem seçiminde bunu göz önünde bulundur.

---

## Shiller PE Rejim Filtresi

Backtest dönem seçimi ve beklenti kalibrasyonu için:

```python
# Shiller PE (CAPE) eşikleri ve tarihsel 17-yıllık getiri beklentisi:
# CAPE < 15  → yüksek beklenti dönemi (tarihin dip seviyeleri)
# CAPE 15-25 → nötr
# CAPE > 30  → düşük beklenti dönemi (dot-com: ~44, 2024: ~34-36)

# 17 yıllık return auto-correlation: R²≈0.88 (negatif)
# Güçlü geçmiş 17 yıl → zayıf gelecek 17 yıl beklentisi (ve tersi)
# 2009-2024 güçlü dönem → 2025-2042 için beklentiyi düşür

# Backtest'e etkisi:
# "Son 15 yılı test et" = anormal dönemi test etmek
# Farklı CAPE rejimlerini (yüksek/düşük PE dönemleri) ayrı ayrı test et
# Kaynak: multpl.com/shiller-pe
```

---

## Kritik Hatalar (Bunları Yapma)

| Hata | Sonuç | Çözüm |
|------|-------|-------|
| **yfinance prodda kullanmak** | Beklenmedik ani arızalar | Polygon.io veya Alpaca kullan |
| **Slippage eklememek** | Gerçekçi olmayan getiri | `commission=0.001, slippage=0.001` ekle |
| **Survivorship bias** | Şişirilmiş backtest | Delisted hisseleri de dahil et |
| **Look-ahead bias** | Geleceği geçmişte kullanmak | `signal = data.shift(1)` ile önceki çubuk |
| **Sadece in-sample test** | Overfitting | Walk-forward zorunlu |
| **Parametre overfitting** | Noise fit etmek | Diversity filter + out-of-sample doğrula |
| **Backtesting.py'nin hızlı sonucu** | "Bu harika çalışıyor" yanılsaması | Backtrader'la da doğrula |
| **0DTE options Greeks = NaN hatası** | "Bu bir API bug" yanılgısı | **Bug değil:** Black-Scholes'ta vade=0 → sıfıra bölme → tanımsız. NaN beklenen matematiksel davranış. Exception handling ekle. |

---

## AI Destekli Backtest Metodolojisi

Austin Starks'ın 140.000 backtest'i analiz ettiği yaklaşım:

```
1. Strateji bileşenlerini parçala
   → strateji setleri, entry/exit koşulları, indikatörler

2. Her bileşen için istatistiksel analiz yap
   → annualized return, Sharpe, Calmar, Sortino

3. Çeşitlilik filtresi uygula (TF-IDF + cosine similarity)
   → Top Sharpe'ı seç, ama birbirine çok benzer kombinasyonları çıkar

4. "Elite tier" oluştur
   → Tüm metrikler açısından top %20'ye giren bileşenler

5. Bunları sistem prompt'una enjekte et
   → LLM, "momentum + güçlü fundamentals" gibi kanıtlanmış kombinasyonları önerir

6. Öneriyi walk-forward ile test et
   → 2020-2024 train, 2025 blind test

Sonuç: 36.94% vs SPY 16.0%, Sharpe 1.39 vs 0.61
```

---

## Alpaca ile Deploy

```python
import alpaca_trade_api as tradeapi
api = tradeapi.REST(
    key_id='KEY',
    secret_key='SECRET',
    base_url='https://api.alpaca.markets'   # paper için: paper-api.alpaca.markets
)

# Backtest'ten gelen sinyale göre order
def place_signal(symbol: str, signal: int, qty: int = 1):
    side = 'buy' if signal == 1 else 'sell'
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type='market',
        time_in_force='day'
    )

# Gecelik/extended hours data için BOATS feed
from alpaca_trade_api import DataFeed
bars = api.get_bars(
    'AAPL', '1Hour',
    feed=DataFeed.BOATS   # overnight data
).df

# Crypto → /v1beta3 endpoint (otomatik)
crypto_bars = api.get_crypto_bars('BTC/USD', '1Day').df

# Options → /v1beta1 endpoint (Feb 2024+, otomatik)
options_chain = api.get_option_chain('AAPL')
```

---

## Kaynaklar
- backtesting.py: kernc.github.io/backtesting.py
- VectorBT PRO: vectorbt.pro
- Polygon.io: polygon.io (data)
- Tiingo: tiingo.com (clean EOD + fundamentals)
- Alpaca: alpaca.markets (execution + data)
- NexusTrade metodoloji gist: gist.github.com/austin-starks/b1fff758f0c59c3fc2865927ffb6310b
