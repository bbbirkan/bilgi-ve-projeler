#!/usr/bin/env bash
set -u

vault="/root/HermesVault"
service="obsidian-sync"
write_test=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --vault)
      vault="${2:-}"
      shift 2
      ;;
    --service)
      service="${2:-}"
      shift 2
      ;;
    --write-test)
      write_test=1
      shift
      ;;
    -h|--help)
      echo "Usage: $0 [--vault /root/HermesVault] [--service obsidian-sync] [--write-test]"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

failures=0

ok() { echo "[ok] $*"; }
warn() { echo "[warn] $*"; }
fail() { echo "[fail] $*"; failures=$((failures + 1)); }

echo "Hermes + Obsidian sync loop verification"
echo "Vault: $vault"
echo "Service: $service"
echo

if [ -d "$vault" ]; then
  ok "vault directory exists"
else
  fail "vault directory missing"
fi

if [ -d "$vault/.obsidian" ]; then
  ok "vault has .obsidian config"
else
  warn "vault does not show .obsidian config; confirm ob sync-setup was run from this folder"
fi

if [ -f "$HOME/.hermes/.env" ]; then
  ok "Hermes env file exists"
  hermes_vault="$(grep '^OBSIDIAN_VAULT_PATH=' "$HOME/.hermes/.env" | tail -n1 | cut -d= -f2- || true)"
  if [ -n "$hermes_vault" ]; then
    echo "[info] Hermes OBSIDIAN_VAULT_PATH=$hermes_vault"
    if [ "$hermes_vault" = "$vault" ]; then
      ok "Hermes vault path matches"
    else
      fail "Hermes vault path does not match expected vault"
    fi
  else
    fail "OBSIDIAN_VAULT_PATH not set in Hermes env"
  fi
else
  warn "Hermes env file not found"
fi

if command -v ob >/dev/null 2>&1; then
  ok "ob CLI found: $(command -v ob)"
else
  fail "ob CLI not found"
fi

if command -v systemctl >/dev/null 2>&1; then
  if systemctl is-active "$service" >/dev/null 2>&1; then
    ok "$service is active"
  else
    fail "$service is not active"
  fi
  if systemctl is-enabled "$service" >/dev/null 2>&1; then
    ok "$service is enabled"
  else
    warn "$service is not enabled"
  fi
else
  warn "systemctl not found"
fi

if command -v ob >/dev/null 2>&1 && [ -d "$vault" ]; then
  echo
  echo "Running one-off sync check..."
  if ob sync --path "$vault"; then
    ok "one-off ob sync completed"
  else
    fail "one-off ob sync failed"
  fi
fi

if [ "$write_test" -eq 1 ]; then
  test_dir="$vault/_Hermes Sync Tests"
  timestamp="$(date -u +%Y%m%d-%H%M%S)"
  test_file="$test_dir/vps-to-mac-$timestamp.md"
  mkdir -p "$test_dir"
  {
    echo "---"
    echo "type: sync-test"
    echo "created: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "tags:"
    echo "  - sync-test"
    echo "---"
    echo
    echo "# VPS To Mac Sync Test $timestamp"
    echo
    echo "If this appears on the Mac, the VPS to Obsidian Sync direction works."
  } > "$test_file"
  ok "created test note: $test_file"
  if command -v ob >/dev/null 2>&1; then
    ob sync --path "$vault" && ok "synced test note" || fail "failed to sync test note"
  fi
fi

echo
if [ "$failures" -eq 0 ]; then
  echo "Result: no blocking failures found. Confirm visibility on the Mac to finish the proof."
  exit 0
else
  echo "Result: $failures blocking issue(s) found."
  exit 1
fi
