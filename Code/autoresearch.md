# autoresearch

**Kaynak**: https://github.com/karpathy/autoresearch  
**Yazar**: Andrej Karpathy  
**Lisans**: MIT  
**Yıldız**: ~78k+ ⭐ | **Fork**: ~11k+

---

## Ne İşe Yarar?

`autoresearch`, bir yapay zeka ajanının **tek başına derin öğrenme araştırması** yapmasını sağlayan minimalist bir framework'tür.

Temel fikir şu:
- Ajana küçük ama gerçek bir **LLM eğitim altyapısı** verilir
- Ajan gecelik olarak özerk şekilde deneyler yapar
- `train.py` dosyasını değiştirir → 5 dakika eğitir → sonuç iyileştiyse değişikliği saklar, kötüleştiyse atar → tekrar eder
- Sabah uyandığında bir deney günlüğü ve (umarız ki) daha iyi bir model bulursun

Bu, insanın doğrudan Python kodu yazmadığı; bunun yerine **`program.md` dosyasını düzenleyerek** ajana araştırma yönelimi verdiği bir yaklaşımdır.

---

## Nasıl Çalışır?

Repoda yalnızca 3 önemli dosya vardır:

| Dosya | Açıklama |
|-------|----------|
| `prepare.py` | Sabit değerler, veri hazırlığı (eğitim verisi indir, BPE tokenizer eğit), çalışma zamanı araçları. **Değiştirilmez.** |
| `train.py` | GPT modeli, optimizer (Muon + AdamW) ve eğitim döngüsü. **Ajan bu dosyayı düzenler.** |
| `program.md` | Ajana verilen baseline talimatlar. **İnsan bu dosyayı düzenler.** |

**Metrik**: `val_bpb` (validation bits per byte) — düşük olması daha iyidir.  
**Süre**: Her deney tam olarak 5 dakika sürer (wall clock, başlatma/derleme hariç).

---

## Kurulum ve Kullanım

### Gereksinimler
- Tek bir NVIDIA GPU (H100 ile test edilmiş)
- Python 3.10+
- `uv` paket yöneticisi

```bash
# 1. uv kurulumu (yoksa)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Bağımlılıkları yükle
uv sync

# 3. Veriyi indir ve tokenizer'ı eğit (bir kere yapılır, ~2 dk)
uv run prepare.py

# 4. Tek bir eğitim deneyi çalıştır (~5 dk)
uv run train.py
```

### Ajan Modunda Çalıştırma

Claude, Codex veya başka bir AI ajanını repo dizininde başlat (izinleri kısıtla), ardından şunu söyle:

> *"Hi, have a look at program.md and let's kick off a new experiment! Let's do the setup first."*

Ajan `program.md` dosyasını okur ve araştırmaya başlar.

---

## Tasarım Kararları

- **Tek dosya değişikliği**: Ajan yalnızca `train.py` dosyasına dokunur. Kapsam yönetilebilir kalır, diff'ler incelenebilir.
- **Sabit zaman bütçesi**: Her deney her zaman tam 5 dakika sürer. Bu, farklı mimari/hiperparametre değişikliklerini adil karşılaştırmayı sağlar. Yaklaşık 12 deney/saat, uyurken ~100 deney yapılır.
- **Bağımsız yapı**: Yalnızca PyTorch ve birkaç küçük paket gerektirir. Dağıtık eğitim yok, karmaşık konfigürasyon yok.

---

## Daha Küçük Donanımlar İçin (MacBook vb.)

| Ayar | Öneri |
|------|-------|
| Dataset | TinyStories gibi daha düşük entropili bir set kullan |
| `vocab_size` | 8192'den 1024 veya byte-level 256'ya indir |
| `MAX_SEQ_LEN` | 256'ya kadar düşür |
| `DEPTH` | Default 8'den 4'e indir |
| `WINDOW_PATTERN` | `"SSSL"` yerine `"L"` kullan |
| `TOTAL_BATCH_SIZE` | 2^14 (~16K) düzeyine indir |

### Dikkat Çekici Fork'lar

- [miolini/autoresearch-macos](https://github.com/miolini/autoresearch-macos) — macOS
- [trevin-creator/autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx) — macOS MLX
- [jsegov/autoresearch-win-rtx](https://github.com/jsegov/autoresearch-win-rtx) — Windows RTX
- [andyluo7/autoresearch](https://github.com/andyluo7/autoresearch) — AMD GPU

---

## Proje Yapısı (İndirildi)

```
autoresearch/
├── prepare.py        # Veri hazırlığı ve runtime araçları (değiştirme)
├── train.py          # Model + optimizer + eğitim döngüsü (ajan bu dosyayı düzenler)
├── program.md        # Ajan talimatları (sen bunu düzenlersin)
├── analysis.ipynb    # Deney sonuçlarını analiz etmek için Jupyter notebook
├── pyproject.toml    # Bağımlılıklar
└── uv.lock           # Kilitlenmiş bağımlılık versiyonları
```

---

## Özet

> **autoresearch** = Gece boyunca uyurken AI ajanının senin adına LLM araştırması yapması.  
> Sen `program.md` dosyasını yazarsın, ajan `train.py` üzerinde deneyler yapar, sabah sonuçlara bakarsın.
