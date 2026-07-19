---
name: zen-discovery
description: Discover available integrations and their connection status. Use when the user asks what integrations are available, wants to check connection status across providers, or needs to connect a provider but no provider-specific skill is loaded.
---

# Integration Discovery

## How Connection Status Works

Provider skills (e.g., `zen-jira`, `zen-google-calendar`) are automatically installed when a provider is connected and removed when disconnected. This means:

- **If a provider skill is loaded** → the provider is connected. Just use it directly.
- **If a provider skill is NOT loaded** → the provider is not connected. Emit a connect block to prompt the user.

You do NOT need to call `zenskill providers list` to check connection status. Only call it when the user explicitly asks for connection details (status, scopes, auth type).

## Available Providers

- `amplitude` — Amplitude analytics
- `gmail` — Gmail
- `google-calendar` — Google Calendar
- `google-drive-docs` — Google Drive & Docs
- `hubspot` — HubSpot CRM (contacts, companies, deals, tickets)
- `jira` — Jira issue tracking
- `linear` — Linear issue tracking
- `miro` — Miro collaborative whiteboard
- `notion` — Notion
- `office` — Microsoft Office document generation (Word, PowerPoint, Excel, PDF)
- `sentry` — Sentry error tracking
- `slack_bot` — Slack Bot
- `telegram_bot` — Telegram Bot

## Connecting a Provider

If the user asks to use a provider that has no loaded skill, emit a connect block.
**NEVER** call provider APIs directly via `curl` or HTTP requests — always use `zenskill` commands.

**Read-only** requests (listing, searching, checking status, reading content):
```
<integration-connect>PROVIDER_ID</integration-connect>
```

**Read-write** requests (creating, updating, deleting, sending, commenting):
```
<integration-connect mode="readwrite">PROVIDER_ID</integration-connect>
```

Replace `PROVIDER_ID` with the actual provider id (e.g., `jira`, `google-calendar`).

## Check Integration Status

Run `zenskill providers list` only when the user explicitly asks about integration status, connected scopes, or auth details.

Each provider returns:
- `status` — `connected`, `not_connected`, or `expired`
- `connected_mode` — current access level (e.g., `readonly`, `readwrite`), or `null`
- `connection_modes` — available access levels with their scopes
