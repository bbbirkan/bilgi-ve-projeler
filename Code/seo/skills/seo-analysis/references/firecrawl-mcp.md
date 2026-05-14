# Firecrawl MCP Reference

Tool inventory, query patterns, and cost guidance for the Firecrawl MCP server.

All tools follow the naming pattern `mcp__firecrawl__{tool-name}`.

---

## Cost Awareness

Firecrawl charges credits per operation. Some tools are significantly more
expensive than others.

**Preferred tools (low cost):**
- `firecrawl_scrape` — single page, predictable cost
- `firecrawl_map` — URL discovery, lightweight
- `firecrawl_crawl` — multiple pages, cost scales with `limit`

**Use with caution (moderate cost):**
- `firecrawl_search` — web search + optional scraping
- `firecrawl_extract` — LLM-powered, costs per URL

**Avoid unless necessary (high cost):**
- `firecrawl_agent` — autonomous browsing, unpredictable cost, runs its
  own LLM. Never use agent mode when scrape + map can accomplish the task.

**Rule: prefer scrape + map over crawl. Prefer crawl over agent. Never
default to agent mode.**

### Credit Thresholds

The MCP server supports credit monitoring via environment variables:
- `FIRECRAWL_CREDIT_WARNING_THRESHOLD` — default 1,000 credits
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD` — default 100 credits

If a warning or critical threshold is hit, note it to the user and reduce
scope (fewer pages, skip optional scrapes).

---

## Tools

### firecrawl_scrape

Extract content from a single URL. **This is the primary tool for most
SEO workflows** — page analysis, content extraction, competitor research.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | yes | Target URL |
| `formats` | array | no | Output formats — use `["markdown"]` for SEO analysis |
| `onlyMainContent` | boolean | no | Strip nav, footer, sidebar.
| `waitFor` | number | no | Milliseconds to wait before scraping (for JS-rendered sites) |
| `mobile` | boolean | no | Use mobile user agent |
| `includeTags` | array | no | HTML tags to prioritize |
| `excludeTags` | array | no | HTML tags to ignore |
| `skipTlsVerification` | boolean | no | Skip SSL cert validation |

**When to use:**
- Scraping a specific page for audit or competitor analysis
- Extracting article content for brand voice analysis
- Pulling heading structure, word count, meta tags from a known URL
- Any time you know the exact URL you need

**SEO recipes:**

Scrape a page for on-page audit:
```
firecrawl_scrape(url: "https://example.com/page", formats: ["markdown"], onlyMainContent: false)
```
Use `onlyMainContent: false` here because you need nav, footer, schema,
and meta tags for technical evaluation.

Scrape a page for content analysis:
```
firecrawl_scrape(url: "https://example.com/blog/post", formats: ["markdown"], onlyMainContent: true)
```
Use `onlyMainContent: true` to get clean body text for word count,
heading structure, and voice analysis.

Scrape a JS-rendered page (Framer, React SPA, Next.js):
```
firecrawl_scrape(url: "https://example.com", formats: ["markdown"], waitFor: 3000)
```
Firecrawl handles JS rendering — this is its main advantage over WebFetch.

---

### firecrawl_map

Discover all indexed URLs on a website. **Use this before scraping to know
what exists** — site inventory, content audit scoping, blog discovery.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | yes | Base website URL |
| `search` | string | no | Keyword filter for URLs |
| `sitemap` | string | no | `"include"` (default), `"skip"`, or `"only"` |
| `includeSubdomains` | boolean | no | Include subdomains |
| `limit` | number | no | Max URLs to return |
| `ignoreQueryParameters` | boolean | no | Treat `?page=1` and `?page=2` as same URL |

**When to use:**
- During `/seo-setup` to build the content inventory
- Before an audit to discover all pages on a site
- To find all blog posts, landing pages, or product pages
- To scope a crawl (map first, then scrape specific URLs)

**SEO recipes:**

Discover all pages on a site:
```
firecrawl_map(url: "https://example.com", limit: 500)
```

Find only blog content:
```
firecrawl_map(url: "https://example.com", search: "blog")
```

Find product or service pages:
```
firecrawl_map(url: "https://example.com", search: "services")
```

**Map → Scrape pattern (preferred workflow):**
1. Map the site to get all URLs
2. Filter URLs by path pattern (e.g., all `/blog/` URLs)
3. Scrape individual URLs that matter

This is cheaper and more targeted than crawling the entire site.

---

### firecrawl_crawl

Crawl multiple pages starting from a URL. Runs asynchronously — returns
a job ID, poll with `firecrawl_check_crawl_status`.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | yes | Starting URL |
| `maxDiscoveryDepth` | number | no | How many links deep to follow |
| `limit` | number | no | Max pages to crawl |
| `allowExternalLinks` | boolean | no | Follow links to other domains |
| `deduplicateSimilarURLs` | boolean | no | Consolidate near-identical pages |

**When to use:**
- When you need content from many pages and don't know exact URLs
- Full site audit requiring all page content (not just URLs from map)
- When map + selective scrape would require too many individual scrapes

**When NOT to use:**
- When you only need 5-10 specific pages — use map + scrape instead
- When you only need URLs, not content — use map instead
- For competitor research — scrape specific competitor pages instead

**Cost control:** Always set `limit` to the minimum needed. A crawl with
`limit: 500` costs far more than mapping 500 URLs and scraping 15.


### firecrawl_search

Search the web and optionally scrape result pages.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | yes | Search query |
| `limit` | number | no | Max results |
| `location` | string | no | Geographic region |
| `tbs` | string | no | Time filter: `qdr:d` (day), `qdr:w` (week), `qdr:m` (month) |
| `sources` | array | no | `["web"]`, `["news"]`, `["images"]` |
| `scrapeOptions` | object | no | Nested scrape parameters for result pages |

**When to use:**
- Finding competitor pages for a specific keyword
- Discovering trending content in a niche
- PAA and SERP feature research when ~~browser is unavailable

**SEO recipe:**

Find competitor content for a keyword:
```
firecrawl_search(query: "best family lawyer sydney", limit: 5, scrapeOptions: { formats: ["markdown"], onlyMainContent: true })
```

---

### firecrawl_extract

LLM-powered structured data extraction. Sends page content through an LLM
with a prompt and optional JSON schema.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `urls` | array | yes | Target URLs |
| `prompt` | string | yes | Extraction instructions (max 10,000 chars) |
| `schema` | object | no | JSON schema defining output structure |
| `allowExternalLinks` | boolean | no | Follow external links |
| `enableWebSearch` | boolean | no | Supplement with web search |

**When to use:**
- Extracting structured data from competitor pages (pricing, features)
- Pulling specific data points from many pages at once
- When you need structured JSON output, not raw markdown

**When NOT to use:**
- When you just need page content — use scrape instead (cheaper)
- When Claude can parse the markdown itself — scrape + Claude is free,
  extract costs credits per URL plus LLM usage

---

### firecrawl_agent (avoid)

Autonomous research agent that browses the web independently.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | yes | Research task (max 10,000 chars) |
| `urls` | array | no | Optional starting URLs |
| `schema` | object | no | JSON schema for output |

Returns a job ID. Poll with `firecrawl_agent_status` every 15-30 seconds.

**Do not use this tool unless explicitly requested by the user.** It is
the most expensive Firecrawl operation — it runs its own LLM, browses
autonomously, and the cost is unpredictable. Every task the agent can do
can be accomplished more cheaply with map + scrape + Claude's own analysis.

---

## Error Handling

The MCP server includes automatic retry with exponential backoff:
- Max attempts: 3 (configurable via `FIRECRAWL_RETRY_MAX_ATTEMPTS`)
- Initial delay: 1,000ms
- Max delay: 10,000ms
- Backoff factor: 2x

If a scrape fails after retries, fall back to WebFetch for that URL and
note the limitation.