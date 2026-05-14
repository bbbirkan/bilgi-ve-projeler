# SEO Plugin (v2)

Four commands. Set up, find opportunities, brief them, write them.

| Command | What it does | Needs ~~SEO data? |
|---------|-------------|-------------------|
| `/start-here` | One-time setup + workflow guide. Builds brand voice, site profile, competitor context | No |
| `/find-opportunities` | Discover and prioritise keyword opportunities | Yes — hard stop |
| `/create-brief` | Build a data-backed content brief for an opportunity | Yes |
| `/write-content` | Write a publication-ready article from a brief | No |

## Output Structure

```
brand/                              Context + cached ~~SEO data (auto-updated by commands)
├── brand-voice.md                  Voice profile for content production
├── competitors.md                  Competitor profiles + keyword overlap (date_fetched, 14-day cache)
└── site-profile.md                 Domain metrics + keyword snapshot (date_fetched, 7-day cache)

campaigns/
├── opportunities.md                Running list of all discovered opportunities (append-only tracker)
└── {YYYY-MM-DD}/                   Date folder, created on first output that day
    ├── daily-opportunities.html    Opportunity report from /find-opportunities
    ├── {slug}-brief.html           Content brief report from /create-brief
    ├── {slug}-article.md           Written article from /write-content (markdown for CMS)
    └── screenshots/                SERP and PAA screenshots from /create-brief
```

## Philosophy

**Built on what works.** The methodologies in this plugin combine original frameworks with the best publicly available SEO techniques — adapted, extended, and wired into a data-backed pipeline. What ties it together is the system: MCP data integration, connector abstraction, command orchestration, and file contracts that turn isolated techniques into a repeatable, data-first workflow.

## Skills

Loaded automatically based on context — commands reference them, you don't invoke them directly.

| Skill | What it covers |
|-------|---------------|
| seo-analysis | Keyword research, SERP analysis, opportunity finding |
| brief-building | Brief assembly, heading structure, keyword placement, schema selection |
| humanizer | Making AI content sound human |
| brand-voice | Voice extraction, profile building |
| reports | Rendering SEO data as self-contained HTML reports |

## Setup

### What you need

| What you want to do | Minimum required |
|---------------------|-----------------|
| Set up brand voice and site profile | Nothing — WebFetch is built in |
| Full site mapping and JS rendering | Firecrawl |
| Keyword research and opportunity finding | Any one SEO data provider (Ahrefs, DataForSEO, or SEMrush) |
| The complete pipeline | Firecrawl + one SEO data provider |

Only one SEO data provider needs to be connected. The plugin auto-detects which one is available.

### Editing the MCP config

MCP servers are configured in `.mcp.json` inside the plugin directory.

**In Claude Code (CLI):** Open the plugin's `.mcp.json` in your editor.

**In Cowork (Desktop App):** Click the **Customise** button → find **SEO** under Plugins → click **Connectors** → **Edit**. This opens the config in VS Code or your default text editor.

Restart the session after making changes.

### Firecrawl (web scraper)

Firecrawl provides JS rendering and full site mapping. Without it the plugin falls back to the built-in WebFetch tool.

1. Sign up at [firecrawl.dev](https://www.firecrawl.dev)
2. Get your API key from the [Firecrawl dashboard](https://www.firecrawl.dev/app/api-keys)
3. Open `.mcp.json` and replace `{FIRECRAWL_API_KEY}` with your key:

```json
"firecrawl": {
  "type": "http",
  "url": "https://mcp.firecrawl.dev/fc-YOUR-API-KEY-HERE/v2/mcp"
}
```

### DataForSEO (SEO data)

**Prerequisites:** [Node.js](https://nodejs.org) must be installed (the MCP server runs via `npx`).

1. Sign up at [dataforseo.com](https://dataforseo.com)
2. Go to [API Access](https://app.dataforseo.com/api-access) to get your **API login email** and **API password**
   - Your API password is **different** from your regular DataForSEO login password — copy it from the API Access page
3. Open `.mcp.json` and add your credentials:

```json
"dataforseo": {
  "type": "stdio",
  "command": "npx",
  "args": ["dataforseo-mcp-server"],
  "env": {
    "DATAFORSEO_USERNAME": "your-email@example.com",
    "DATAFORSEO_PASSWORD": "your-api-password-from-api-access-page"
  }
}
```

### Ahrefs (SEO data)

An active Ahrefs subscription is required. The MCP server authenticates through the Ahrefs platform — no API key is needed in the config. Follow the authentication prompt on first connection.

### SEMrush (SEO data)

An active SEMrush subscription is required. The MCP server authenticates through the SEMrush platform — no API key is needed in the config. Follow the authentication prompt on first connection.

### Optional: Claude in Chrome

Connect Claude in Chrome for live SERP screenshots during briefs. No configuration needed — the plugin detects it automatically.

### Get started

Run `/start-here` — it builds your brand voice, site profile, and competitor context, then walks you through the workflow.
