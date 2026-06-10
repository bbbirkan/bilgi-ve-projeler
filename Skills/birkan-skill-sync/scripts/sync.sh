#!/usr/bin/env bash
# Sistem bağlamı senkronizasyon scripti
# Kullanım: bash ~/.hermes/skills/birkan-skill-sync/scripts/sync.sh

set -e

SOURCE="/root/CLAUDE.md"
HERMES_SKILL="$HOME/.hermes/skills/birkan-system-context/SKILL.md"
GIT_SKILL="/root/bilgi-ve-projeler/Skills/birkan-system-context/SKILL.md"
TODAY=$(date +%Y-%m-%d)

FRONTMATTER='---
name: birkan-system-context
description: "Birkan Kalyon'"'"'un Contabo VDS sunucusundaki AI otomasyon ekosisteminin tam bağlamı. Bu dosyayı oku: sunucu durumu, kurulu sistemler, aktif projeler, port haritası, GitHub/SSH kuralları, skill indeksi ve geçmiş kararlar. '"'"'sistemi tanı'"'"', '"'"'bağlamı anla'"'"', '"'"'projeler neler'"'"', '"'"'ne kurulu'"'"', '"'"'skill indeksi'"'"' gibi sorgularda kullan."
---

'

echo "==> Kaynak: $SOURCE"
echo "==> Hedef 1: $HERMES_SKILL"
echo "==> Hedef 2: $GIT_SKILL"
echo ""

# Tarih satırını bugün olarak güncelle
UPDATED_SOURCE=$(sed "s/Son güncelleme: [0-9-]*/Son güncelleme: $TODAY/" "$SOURCE")

# Frontmatter + içerik → Hermes skill
printf "%s%s" "$FRONTMATTER" "$UPDATED_SOURCE" > "$HERMES_SKILL"
echo "[OK] Hermes skill güncellendi"

# bilgi-ve-projeler kopyası
cp "$HERMES_SKILL" "$GIT_SKILL"
echo "[OK] bilgi-ve-projeler kopyası güncellendi"

# Git push
echo ""
echo "==> Git push..."
eval $(ssh-agent -s) > /dev/null 2>&1
ssh-add ~/.ssh/trade_push > /dev/null 2>&1

cd /root/bilgi-ve-projeler
git add Skills/birkan-system-context/SKILL.md
git commit -m "sync: birkan-system-context $TODAY" || echo "[INFO] Değişiklik yok, commit atlanıyor"
GIT_SSH_COMMAND="ssh -i /root/.ssh/trade_push -o StrictHostKeyChecking=no" \
  git push origin master 2>&1 || echo "[WARN] Git push başarısız - manuel kontrol gerekiyor"

echo ""
echo "✓ Senkronizasyon tamamlandı ($TODAY)"
