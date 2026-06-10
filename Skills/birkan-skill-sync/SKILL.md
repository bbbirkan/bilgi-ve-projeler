---
name: birkan-skill-sync
description: "Sistem bağlamını (CLAUDE.md) üç lokasyonda senkronize tutar: /root/CLAUDE.md (kaynak), ~/.hermes/skills/birkan-system-context/SKILL.md (Hermes için) ve /root/bilgi-ve-projeler/Skills/birkan-system-context/SKILL.md (GitHub backup). 'sistem bağlamını güncelle', 'senkronize et', 'skill sync', 'CLAUDE.md değişti', 'birkan-system-context güncelle' gibi isteklerde kullan. Sync script'i de içerir."
---

# Skill Sync — Sistem Bağlamı Senkronizasyonu

Bu skill, `/root/CLAUDE.md` değiştiğinde üç lokasyonun hepsinin güncel kalmasını sağlar.

## Üç Lokasyon

| # | Konum | Kim Okur |
|---|-------|----------|
| 1 | `/root/CLAUDE.md` | Claude Code (kaynak gerçek) |
| 2 | `~/.hermes/skills/birkan-system-context/SKILL.md` | Hermes Agent |
| 3 | `/root/bilgi-ve-projeler/Skills/birkan-system-context/SKILL.md` | GitHub backup |

## Hızlı Sync (Tek Komut)

```bash
bash ~/.hermes/skills/birkan-skill-sync/scripts/sync.sh
```

Bu script:
1. `/root/CLAUDE.md` içeriğini okur
2. Hermes frontmatter ekler
3. 2. ve 3. lokasyona yazar
4. bilgi-ve-projeler'e git commit + push atar

## Manuel Sync (Adım Adım)

### Adım 1 — Hermes skill'ini güncelle
```bash
# CLAUDE.md başına frontmatter ekleyip skill'e yaz
python3 ~/.hermes/skills/birkan-skill-sync/scripts/inject_frontmatter.py
```

### Adım 2 — bilgi-ve-projeler'e kopyala
```bash
cp ~/.hermes/skills/birkan-system-context/SKILL.md \
   /root/bilgi-ve-projeler/Skills/birkan-system-context/SKILL.md
```

### Adım 3 — Git push
```bash
eval $(ssh-agent -s) && ssh-add ~/.ssh/trade_push

cd /root/bilgi-ve-projeler
git add Skills/birkan-system-context/SKILL.md
git commit -m "sync: birkan-system-context güncel hale getirildi"
GIT_SSH_COMMAND="ssh -i /root/.ssh/trade_push -o StrictHostKeyChecking=no" \
git push origin main
```

## Senkronizasyon Gerektiren Durumlar

CLAUDE.md şunlar değiştiğinde mutlaka sync yap:
- Yeni proje eklendi / bir proje tamamlandı
- Sistem kurulumu değişti (yeni araç kuruldu, versiyon güncellendi)
- Port haritası değişti
- Skill indeksine yeni skill eklendi
- Kritik karar/seçim yapıldı

## Sync Durumu Kontrol

```bash
# İki dosya aynı mı?
diff <(tail -n +7 ~/.hermes/skills/birkan-system-context/SKILL.md) /root/CLAUDE.md
# Çıktı yoksa: senkronize
# Fark varsa: sync gerekiyor
```

## Frontmatter Format

`birkan-system-context/SKILL.md` dosyasının başında her zaman bu frontmatter olmalı:

```yaml
---
name: birkan-system-context
description: "Birkan Kalyon'un Contabo VDS sunucusundaki AI otomasyon ekosisteminin tam bağlamı. ..."
---
```

CLAUDE.md'de frontmatter yoktur — sync script bunu otomatik ekler.
