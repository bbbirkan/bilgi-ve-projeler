# Connectors

This plugin uses `~~category` placeholders in its workflows. These refer to
*categories* of tools, not specific products. The actual tool depends on what
you've connected.

| Category | Placeholder | Included Servers | Other Options |
|----------|-------------|-----------------|---------------|
| SEO Data | `~~SEO data` | Ahrefs, DataForSEO | SEMrush |
| Web Scraping | `~~web scraper` | Firecrawl | WebFetch (built-in) |
| Web Research | `~~web research` | WebSearch (built-in) | — |
| Browser | `~~browser` | Claude in Chrome | None |

## How connectors work

Commands reference the category, not the tool. Each command includes
conditional logic for when a connector is or isn't available.

### ~~SEO data

This is the primary data source. The plugin is built around real SEO
metrics — not estimates from web search. When `~~SEO data` is not
connected there is no silent fallback. If real data is required and the
MCP is not connected, the command stops and says so.

Provider reference files:

- **Ahrefs** → `skills/seo-analysis/references/ahrefs-mcp.md`
- **DataForSEO** → `skills/seo-analysis/references/dataforseo-mcp.md`

### ~~web scraper

Falls back to built-in `WebFetch` if Firecrawl MCP is not configured.

### ~~web research

Uses the built-in `WebSearch` tool. No external MCP required.

### ~~browser

Available via Claude in Chrome. Lets Claude open a real browser, navigate
to Google, perform searches, and take screenshots — capturing exactly
what users see in search results.

When `~~browser` is not available there is no fallback. Skills that use
it note what to skip when it's unavailable.

## Configuration

Add the MCP server to your Claude Code configuration with the actual
endpoint URL for whichever providers you use. Only one `~~SEO data`
provider needs to be connected.

See `.mcp.json` for the server definitions.
