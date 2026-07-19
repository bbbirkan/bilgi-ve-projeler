# ORKESTRA ÇALIŞMA MODLARI

> Servis: Orchester | Port: 8006 | CLI: `/root/2026-orchester/terminal_orchester.py`
> Modları listele: `python3 /root/2026-orchester/terminal_orchester.py --list-modes`

---

## 3 ANA MOD

### ★ KORO — 5 model paralel
```
Claude · DeepSeek · Kimi · GLM · AGY  →  aynı anda  →  Claude sentezler
```
Ne zaman: Farklı bakış açısı, yaratıcı fikir, strateji lazımsa
Süre: ~60-90 sn

```bash
python3 /root/2026-orchester/terminal_orchester.py --mode koro "görev"
```

---

### ★ KOLEKTİF — sıralı zincir [CLI varsayılan]
```
Kimi(Thinker) → DeepSeek(Worker) → GLM(Challenger) → AGY(Verifier) → Claude(Sentez)
```
Ne zaman: Derin analiz, hata olmaması kritik, itiraz/doğrulama lazımsa
Özellik: safe_abort — Verifier hata görürse pipeline durur
Süre: ~2-3 dk

```bash
python3 /root/2026-orchester/terminal_orchester.py --mode kolektif "görev"
# veya sadece (CLI varsayılanı):
python3 /root/2026-orchester/terminal_orchester.py "görev"
```

---

### ★ AKILLI — otomatik seçim [API varsayılan]
```
Claude görevi ölçer:
  basit → Claude tek (~5 sn)
  orta  → Claude + OpenCode paralel (~30 sn)
  zor   → 3 tur konsey (~90 sn)
```
Ne zaman: Ne kullanacağını bilmiyorsan, API çağrısında

```bash
python3 /root/2026-orchester/terminal_orchester.py --mode akilli "görev"
```

---

## Birkan Tetikleyicileri
| Birkan ne derse | Ne çalışır |
|-----------------|-----------|
| "koro modu" | `--mode koro` |
| "kolektif mod" | `--mode kolektif` |
| "akıllı mod" | `--mode akilli` |
| "orkestra ile çöz" | varsayılan: kolektif (CLI) |

## Kural
Yeni mod eklenince → bu dosyayı güncelle + CLAUDE.md tetikleyici ekle.
"Yeni yetenek = keşfedilebilir olmadan bitmiş sayılmaz."
