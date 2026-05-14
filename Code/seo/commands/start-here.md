---
description: Set up the SEO plugin and learn the workflow — brand voice, site profile, competitor context, and a guided tour of every command.
argument-hint: "<your website URL>"
---

# /start-here

> Your starting point. Run this once to set up the plugin, or again any time for help.

## Iteration Detection

Check whether `./brand/` exists and contains files.

### If brand/ has content → Dashboard + Help

Don't re-run setup. Instead:

1. **Show setup status** — read `./brand/` and `./campaigns/` to build a dashboard:
   - Brand voice: exists / missing
   - Site profile: exists / stale (>7 days) / fresh
   - Competitors: exists / stale (>14 days) / fresh
   - Opportunities found: count from `./campaigns/opportunities.md`
   - Briefs created: count entries with a `**Brief:**` path
   - Articles written: count entries with an `**Article:**` path
2. **Connection check** — test which MCP servers respond and report status (see Connection Check below)
3. **Show the Workflow Guide** (bottom of this file)
4. Ask if they want to **re-run setup** (rebuild voice, update competitors, re-scrape) or **jump to a command**

### If brand/ is empty or missing → Onboarding

Run the full setup below.

---

## Onboarding

### Three Questions

Ask all three in a single conversational message — not a numbered form. If the user provided their URL as the command argument, acknowledge it and only ask the remaining two.

1. **What's your website URL?** — the primary domain the plugin will optimize for
2. **What's your average deal size?** — a dollar figure used to model the revenue value of keyword opportunities (e.g., "$100K", "$5,000", "$75"). For e-commerce this is average order value. For SaaS this is annual contract value. For services this is average project value. If the user isn't sure, ask what a typical customer is worth over their first year
3. **Who are your 2–5 main competitors?** — URLs preferred, company names accepted. These are the sites you compete with in search results, not necessarily direct business competitors

Wait for all three answers before proceeding. Do not start scraping until the user has responded.

### Setup Process

#### Step 1 — Create directories and project instructions

Create `./brand/` and `./campaigns/` if they don't exist.

Copy the plugin's `CLAUDE.md.example` to `./CLAUDE.md` at the root of the current working directory. This gives Claude project context when the user opens this folder in future sessions. If a `./CLAUDE.md` already exists, do not overwrite it — the user may have customized it.

#### Step 2 — Scrape the primary URL

Use ~~web scraper to gather content from the user's site. The goal is enough text for voice extraction and enough structure for a site profile.

**If Firecrawl is connected:**

1. Run `firecrawl_map` on the domain (limit: 500) to discover all URLs
2. Categorize **every** URL by section (blog, services/products, about, landing pages, other). Keep this categorized list — it becomes the Content Inventory in the site profile. Do not truncate or abbreviate; save every URL returned by the map
3. Scrape key pages with `firecrawl_scrape` (formats: `["markdown"]`, onlyMainContent varies by page type):
   - Homepage (onlyMainContent: false — need full page structure)
   - About page (onlyMainContent: true)
   - 2–3 recent blog posts (onlyMainContent: true)
   - Primary services/product page (onlyMainContent: true)

**If Firecrawl is not connected:**

Use WebFetch on the homepage, about page, and any blog posts discoverable from homepage links. Note that JS-rendered sites may return incomplete content — flag this to the user if the content looks thin.

Report what was found and approximate word count before proceeding to voice extraction.

#### Step 3 — Build brand voice (streamlined)

Feed the scraped content into the brand-voice skill using **Auto-Scrape mode**, with these onboarding modifications:

- **Skip the supplementary questions** — onboarding should be fast. The user can refine voice later by running the brand-voice skill directly
- **Skip the voice test loop** — save the initial profile without the 3-sample feedback cycle
- **Do generate the full voice profile** — all sections from the brand-voice template (summary, traits, tone spectrum, vocabulary, rhythm, POV, blog calibration, examples, do's and don'ts)

Save to `./brand/brand-voice.md`.

Tell the user the voice profile is a starting point — they can refine it any time by asking to update their brand voice (the brand-voice skill has full iteration detection and will offer Update mode).

#### Step 4 — Build site profile

Create `./brand/site-profile.md`. This file is the central cache that downstream commands read before making API calls. The more complete it is now, the fewer redundant fetches later.

**Phase A — Site structure (always runs, uses scrape data from Step 2):**

Populate Domain, Company Overview, and Content Inventory from the scraped content and Firecrawl map.

**Phase B — SEO metrics (runs only if ~~SEO data is connected):**

If ~~SEO data is available, fetch domain-level data now and save it to the site profile. This is the same data `/find-opportunities` would fetch later — doing it here means the first research run uses cache instead of re-fetching. Read the MCP reference file for the connected provider before making calls (see `skills/seo-analysis/SKILL.md` → MCP Tool Usage).

Fetch:
1. **Domain overview** — DR, organic traffic, organic keywords count, organic traffic cost
2. **Top pages** — 20–50 pages ordered by organic traffic descending
3. **Striking distance keywords** — organic keywords with position 6–20, volume ≥ 100, ordered by traffic potential descending (limit 50)
4. **Top keywords** — 50 keywords ordered by traffic descending

If ~~SEO data is not connected, leave the Domain Metrics, Top Pages, Striking Distance Keywords, and Top Keywords sections empty with a note: `{Not yet fetched — will be populated on first /find-opportunities run}`. Do not skip these sections entirely; include them as empty placeholders so downstream commands know where to write.

**Site profile template** (canonical schema: `${CLAUDE_PLUGIN_ROOT}/FILE-SCHEMAS.md` → Site Profile):

```markdown
# Site Profile

> date_fetched: {YYYY-MM-DD}

## Domain
- **URL:** {primary URL}
- **Average deal size:** {dollar value from question 2}

## Company Overview
{2-3 sentence summary extracted from homepage and about page copy}

## Domain Metrics
{From ~~SEO data domain overview. Leave placeholder if not connected.}

| Metric | Value |
|--------|-------|
| Domain Rating (DR) | {dr} |
| Organic Traffic | {organic_traffic}/mo |
| Organic Keywords | {organic_keywords} |
| Organic Traffic Cost | ${organic_cost_usd}/mo |

## Content Inventory
{From Firecrawl map. Include EVERY URL returned — do not truncate or summarize.}

### Blog ({count} posts)
- {url} — {title or slug}
{... list every blog URL from the map}

### Services/Products ({count} pages)
- {url} — {title or slug}
{... list every service/product URL from the map}

### Landing Pages ({count})
- {url} — {title or slug}
{... list every landing page URL from the map}

### Other Pages ({count})
- {url} — {title or slug}
{... list every remaining URL from the map}

## Top Pages
{From ~~SEO data, 20-50 pages by organic traffic. Leave placeholder if not connected.}

| URL | Organic Traffic | Top Keyword | Position |
|-----|----------------|-------------|----------|
| {url} | {traffic}/mo | {keyword} | {pos} |

## Striking Distance Keywords
{From ~~SEO data, positions 6-20, volume ≥ 100. Leave placeholder if not connected.}

| Keyword | Volume | Position | Traffic | KD |
|---------|--------|----------|---------|-----|
| {keyword} | {vol}/mo | {pos} | {traffic}/mo | {kd} |

## Top Keywords
{From ~~SEO data, top 50 by traffic. Leave placeholder if not connected.}

| Keyword | Volume | Position | Traffic | KD |
|---------|--------|----------|---------|-----|
| {keyword} | {vol}/mo | {pos} | {traffic}/mo | {kd} |

## Notes
{Anything notable: site is JS-rendered, blog is on a subdomain, no about page found, etc.}
```

If no Firecrawl map was available, include what was discovered via manual link following and note that the inventory is partial.

#### Step 5 — Build competitor file

Create `./brand/competitors.md` (canonical schema: `${CLAUDE_PLUGIN_ROOT}/FILE-SCHEMAS.md` → Competitors):

```markdown
# Competitors

> date_fetched: {YYYY-MM-DD}

## {Competitor 1 Name}
- **URL:** {url}
- **Overview:** {1-2 sentences from homepage scrape if available}

## {Competitor 2 Name}
- **URL:** {url}
- **Overview:** {1-2 sentences from homepage scrape if available}

...
```

If ~~web scraper is available, scrape each competitor's homepage (onlyMainContent: true) to extract a brief positioning summary. If not, just list the URLs — `/find-opportunities` will pull competitor data from ~~SEO data later.

Competitor keyword overlap and competitive analysis data is fetched by `/find-opportunities` when the user is ready — do not pull competitor keywords during onboarding. Domain-level data for the **user's own site** (metrics, top pages, ranking keywords) is fetched in Step 4 if ~~SEO data is connected.

#### Step 6 — Connection check

Test which tool categories are available and report status. See Connection Check below.

### After Setup

Show a summary of everything that was created, then display the **Workflow Guide** and **Connection Check** sections below.

Point the user to `/find-opportunities` as their next step.

---

## Connection Check

Test each connector category and report clearly:

| Tool | Status | What it means |
|------|--------|---------------|
| ~~SEO data | Connected / Not connected | **Required** for `/find-opportunities` and `/create-brief`. Without this the plugin can still set up and write content, but can't do keyword research or data-backed briefs |
| ~~web scraper | Firecrawl / WebFetch fallback | Firecrawl gives JS rendering and site mapping. WebFetch works for most sites but may miss JS-rendered content |
| ~~browser | Connected / Not available | Optional. Enables live SERP screenshots during briefs |

If any providers are not connected, show the relevant setup steps from the **MCP Setup Guide** below. Don't make this a blocker for onboarding — voice and site profile don't need SEO data or Firecrawl.

---

## MCP Setup Guide

When the connection check shows missing providers, walk the user through setup using these instructions.

### Editing the MCP Configuration

The plugin's MCP servers are configured in `.mcp.json` inside the plugin directory.

**In Claude Code (CLI):**
Open the plugin's `.mcp.json` in your editor and update the relevant fields below.

**In Cowork (Desktop App):**
Click the **Customise** button → find **SEO** under Plugins → click **Connectors** → **Edit**. This opens the config in VS Code or your default text editor.

After editing, restart the session for changes to take effect.

### Firecrawl (~~web scraper)

Firecrawl provides JS rendering and full site mapping. Without it the plugin falls back to WebFetch, which works for most sites but can't map all URLs or render JavaScript-heavy pages.

**Setup steps:**

1. Sign up for an account at [firecrawl.dev](https://www.firecrawl.dev)
2. Get your API key from the [Firecrawl dashboard](https://www.firecrawl.dev/app/api-keys)
3. Open `.mcp.json` and replace `{FIRECRAWL_API_KEY}` with your actual key:

```json
"firecrawl": {
  "type": "http",
  "url": "https://mcp.firecrawl.dev/fc-YOUR-API-KEY-HERE/v2/mcp"
}
```

### DataForSEO (~~SEO data)

DataForSEO is an SEO data provider that runs locally via Node.js.

**Prerequisites:** [Node.js](https://nodejs.org) must be installed on your machine (the MCP server runs via `npx`).

**Setup steps:**

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

### Ahrefs (~~SEO data)

Ahrefs is the recommended primary SEO data provider. An active Ahrefs subscription is required. The MCP server authenticates through the Ahrefs platform — no API key is needed in the config file. When Claude connects for the first time, follow the authentication prompt.

### SEMrush (~~SEO data)

SEMrush is an alternative SEO data provider. An active SEMrush subscription is required. The MCP server authenticates through the SEMrush platform — no API key is needed in the config file. When Claude connects for the first time, follow the authentication prompt.

### Which providers do I need?

| What you want to do | Minimum required |
|---------------------|-----------------|
| Set up brand voice and site profile | Nothing — WebFetch is built in |
| Full site mapping and JS rendering | Firecrawl |
| Keyword research and opportunity finding | Any one ~~SEO data provider (Ahrefs, DataForSEO, or SEMrush) |
| The complete pipeline | Firecrawl + one ~~SEO data provider |

Only one ~~SEO data provider needs to be connected. The plugin auto-detects which one is available.

---

## Workflow Guide

```
/find-opportunities  →  /create-brief  →  /write-content
    Find keywords         Build brief        Write article
```

### `/find-opportunities`

Give it a keyword, topic, or your domain. It finds three types of opportunities:

- **Striking distance** — keywords where you already rank 6–20 (fastest wins)
- **Competitive gaps** — keywords where no one ranks well (weakest competition)
- **Unowned topics** — high-intent keywords with no clear winner

Every opportunity comes with a modeled dollar value so you know what's worth your time. Results are saved to `./campaigns/opportunities.md` and an HTML dashboard is generated in `./campaigns/{YYYY-MM-DD}/daily-opportunities.html`.

**Requires ~~SEO data (Ahrefs, DataForSEO, or SEMrush).**

### `/create-brief`

Pick an opportunity (or give it any keyword) and it builds a complete content brief:

- Primary, long-tail, and question keywords with volume
- People Also Ask questions with answer format recommendations
- Competitor content analysis (headings, word count, ranking keywords)
- Recommended heading structure and word count
- Semantic keywords and internal linking suggestions
- Writing notes tailored to your brand voice

The brief is saved as an HTML report in `./campaigns/{YYYY-MM-DD}/{slug}-brief.html`.

**Requires ~~SEO data.**

### `/write-content`

Writes the article from a brief. It:

- Writes in your brand voice (from `./brand/brand-voice.md`)
- Follows the brief's heading structure and keyword targets
- Runs a 4-level humanization check (word, phrase, structure, voice)
- Sends the draft through an independent quality review before saving
- Adds YAML frontmatter and JSON-LD schema markup

The result is a publication-ready article saved to `./campaigns/{YYYY-MM-DD}/{slug}-article.md`.

**No ~~SEO data required** — works from the brief alone.

### Tips

- **Start with `/find-opportunities`** — the pipeline flows from there
- **The plugin caches data** in `./brand/` to avoid redundant API calls (7-day site data, 14-day competitor data)
- **Run `/start-here` again** any time to check your setup status and see this guide
- **Brand voice evolves** — ask to update your brand voice when your writing style changes or the profile doesn't sound right
- **Opportunities are tracked** — the plugin won't resurface keywords you've already seen, so you always get fresh results
