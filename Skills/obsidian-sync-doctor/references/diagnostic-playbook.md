# Diagnostic Playbook

Use this decision tree when the Hermes + Obsidian loop is broken.

## 1. Confirm The Paths

Expected default:

```bash
/root/HermesVault
```

Check Hermes:

```bash
grep '^OBSIDIAN_VAULT_PATH=' ~/.hermes/.env
```

The value must match the path used for `ob sync-setup`.

## 2. Confirm The Folder

```bash
ls -la /root/HermesVault
ls -la /root/HermesVault/.obsidian
```

If `.obsidian` is in `/root/.obsidian` instead, setup was probably run from `/root`.

## 3. Confirm obsidian-headless

```bash
command -v ob
ob sync-list-remote
```

If `ob` is missing, fix `PATH`:

```bash
export PATH="$(npm prefix -g)/bin:$PATH"
echo 'export PATH="$(npm prefix -g)/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## 4. Confirm Continuous Sync

```bash
systemctl is-active obsidian-sync
systemctl is-enabled obsidian-sync
journalctl -u obsidian-sync -n 50 --no-pager
```

If inactive:

```bash
systemctl restart obsidian-sync
journalctl -u obsidian-sync -n 50 --no-pager
```

## 5. Run A One-Off Sync

```bash
ob sync --path /root/HermesVault
```

If this fails, fix `ob` auth or vault setup before debugging Hermes.

## 6. Test VPS To Mac

```bash
mkdir -p /root/HermesVault/_Hermes\ Sync\ Tests
date -u > /root/HermesVault/_Hermes\ Sync\ Tests/vps-to-mac-test.md
ob sync --path /root/HermesVault
```

Ask the user to open Obsidian on the Mac and look for the test file.

## 7. Test Mac To VPS

Ask the user to create a note on the Mac:

```text
mac-to-vps-test
```

Then check:

```bash
find /root/HermesVault -maxdepth 5 -iname '*mac-to-vps-test*'
```

## 8. Interpret Results

- VPS to Mac fails, one-off sync fails: fix obsidian-headless login or vault setup.
- VPS to Mac fails, one-off sync succeeds: check Mac account, remote vault, or local Obsidian Sync status.
- Mac to VPS fails: Mac is not connected to the same remote vault, or sync has not completed.
- Both directions pass but Hermes notes missing: fix `OBSIDIAN_VAULT_PATH` and restart Hermes.
