# Ahrefs MCP Reference

Tool inventory, query patterns, and conventions for the Ahrefs MCP server.

All tools follow the naming pattern `mcp__ahrefs__{tool-name}`.

---

## Schema Verification (Mandatory)

**Before using any Ahrefs tool for the first time in a session**, call:

```
mcp__ahrefs__doc(tool: "{tool-name}")
```

This returns the full input/output schema including every valid column name,
parameter enum, and data type. It is **free** — no API units consumed.

**Why this is mandatory:** Column names differ between tools (e.g., keyword
difficulty is `difficulty` in Keywords Explorer but `keyword_difficulty` in
Site Explorer). Parameter names can also be misleading (`terms` and `view_for`
have different meanings across tools). Using the wrong name causes a failed
call, an error, a retry, and wasted API units.

**Workflow:**
1. Before your first call to a tool, call `doc` for that tool
2. Read the outputSchema to identify valid `select` columns
3. Read the inputSchema to identify valid filter fields for `where`
4. Use the verified names in your actual call

You only need to call `doc` once per tool per session. Cache the column
names mentally after the first call.

---

## Conventions

### Monetary values
All monetary fields (`org_cost`, `paid_cost`, `value`, `cpc`) are returned
in **USD cents**. Divide by 100 to display in dollars.

### Domain mode
When analyzing a domain name, always use `mode: "subdomains"`. Using
`mode: "domain"` excludes www and other subdomains, which underreports data.

### Dates
All date parameters use `YYYY-MM-DD` format. Use today's date unless
comparing against a historical period.

### Select parameter
Most tools require a `select` parameter listing which columns to return.
Only request columns you need — each column may consume API units.
Column names with `_merged` suffixes are optimized for sorting.
Column names with `_prev` suffixes are comparison-date values.

**Always verify column names via `doc` before constructing `select`.**

### Filtering (where parameter)
Filters use a JSON object with `and`/`or`/`not` boolean operators and
field-level conditions: `eq`, `neq`, `gt`, `gte`, `lt`, `lte`,
`substring`, `prefix`, `suffix`, `regex`.

**Important:** Filter field names sometimes differ from `select` column names.
The `doc` tool lists filter fields separately from output columns. Check both.

Example structure:
```json
{"and": [
  {"field": "{volume_field}", "is": ["gte", 1000]},
  {"field": "{difficulty_field}", "is": ["lt", 40]}
]}
```

### Sorting (order_by parameter)
Comma-separated column names with `:asc` or `:desc` suffix.
Example: `"{traffic_field}:desc,{difficulty_field}:asc"`

### Limits
Default limit is 1000 rows. Set `limit` explicitly when you need fewer
(saves API units) or up to the maximum.

---

## Tool Inventory by Operation

### Domain Overview

**Get domain metrics (DR, traffic, keywords)**
Tool: `site-explorer-metrics`
Required: `target`, `date`
Optional: `country`, `mode` (default: subdomains), `volume_mode`
Returns organic keyword count, traffic, cost, and paid equivalents.
No `select` parameter needed — returns all fields.

```
target: "example.com"
date: "2026-02-22"
mode: "subdomains"
```

**Get domain rating**
Tool: `site-explorer-domain-rating`
Required: `target`, `date`
Returns domain rating score and rank.

**Get metrics broken down by country**
Tool: `site-explorer-metrics-by-country`
Required: `target`, `date`
Optional: `mode`, `select`
Use when you need to see which countries drive traffic.

**Get historical traffic and keyword trends**
Tool: `site-explorer-metrics-history`
Required: `target`, `date_from`
Optional: `date_to`, `country`, `mode`, `history_grouping`, `select`
Use for trend analysis — traffic growth/decline over time.

---

### Top Pages

**Get top pages by traffic**
Tool: `site-explorer-top-pages`
Required: `target`, `date`, `select`
Optional: `country`, `mode`, `limit`, `order_by`, `where`, `date_compared`

Select columns for: URL, traffic, keyword count, top keyword + position + volume,
URL rating, referring domains. Call `doc` to verify exact names.
Order by the traffic field descending, limit to 20-50.

**Get pages by traffic bucket distribution**
Tool: `site-explorer-pages-by-traffic`
Required: `target`
Returns count of pages in each traffic bucket (0, 1-10, 11-100, etc.)

---

### Keyword Rankings

**Get organic keywords a domain/URL ranks for**
Tool: `site-explorer-organic-keywords`
Required: `target`, `date`, `select`
Optional: `country`, `mode`, `limit`, `order_by`, `where`, `date_compared`

Select columns for: keyword, position, volume, difficulty, traffic, ranking URL,
SERP features, intent flags. Call `doc` to verify exact names.

Key filter patterns (verify field names via `doc`):

Striking distance keywords (positions 6-20):
```json
{"and": [
  {"field": "{position_field}", "is": ["gte", 6]},
  {"field": "{position_field}", "is": ["lte", 20]}
]}
```

Cannibalization detection — keywords where multiple pages rank:
```json
{"field": "serp_target_main_positions_count", "is": ["gte", 2]}
```

**Get historical keyword count by position range**
Tool: `site-explorer-keywords-history`
Required: `target`, `date_from`
Optional: `date_to`, `country`, `mode`, `history_grouping`, `select`
Use to see if keyword footprint is growing or shrinking.

---

### Competitor Discovery

**Find organic competitors by keyword overlap**
Tool: `site-explorer-organic-competitors`
Required: `target`, `country`, `date`, `select`
Optional: `mode`, `limit`, `order_by`, `where`

Select columns for: competitor domain, common keywords, competitor traffic,
domain rating. Call `doc` to verify exact names — this tool uses distinct
column names for competitor vs target metrics.

Order by common keywords descending, limit to 5-10.

---

### SERP Analysis

**Get top results for a keyword**
Tool: `serp-overview`
Required: `keyword`, `country`, `select`
Optional: `date`, `top_positions`

Select columns for: URL, title, position, domain rating, backlinks,
referring domains, traffic, keywords, result type. Call `doc` for exact names.
Set `top_positions: 10` for top 10 results.

Returns the actual SERP: who ranks, their DR, backlinks, and traffic.
Use this for competitive analysis on a specific keyword.

---

### Keyword Research

**Get keyword metrics (volume, KD, CPC, intent)**
Tool: `keywords-explorer-overview`
Required: `country`, `select`
Optional: `keywords` (comma-separated), `keyword_list_id`, `target`,
`target_mode`, `where`, `limit`

Select columns for: keyword, volume, difficulty, CPC, traffic potential,
parent topic, SERP features. Call `doc` for exact names — note that the
difficulty column name differs from Site Explorer tools.

Note: `traffic_potential` shows the estimated traffic of the #1 result,
which is more useful than raw volume for prioritization.

**Expand keywords — matching terms**
Tool: `keywords-explorer-matching-terms`
Required: `country`, `select`
Optional: `keywords`, `terms`, `match_mode`, `limit`, `where`, `order_by`

`terms` parameter: `"all"` (default) or `"questions"` (question-form only).
`match_mode`: `"terms"` (words in any order) or `"phrase"` (exact order).

Use for expanding a seed keyword into related terms that contain
the seed phrase. Good for long-tail discovery.

**Expand keywords — related terms (also rank for / also talk about)**
Tool: `keywords-explorer-related-terms`
Required: `country`, `select`
Optional: `keywords`, `terms`, `view_for`, `limit`, `where`, `order_by`

**Critical parameter distinction** — this tool has TWO parameters that
control different things. Call `doc` to verify:
- `terms` — selects the relationship type: `"also_rank_for"`,
  `"also_talk_about"`, or `"all"`
- `view_for` — selects the scope: `"top_10"` or `"top_100"`

Use `terms: "also_rank_for"` for semantic keyword expansion.
Use `terms: "also_talk_about"` for topical coverage / semantic keywords.

**Search suggestions (autocomplete-style)**
Tool: `keywords-explorer-search-suggestions`
Required: `country`, `select`
Optional: `keywords`, `limit`, `where`, `order_by`

Returns Google autocomplete-style suggestions. Useful for finding
question-format keywords and long-tail variants.

**Get keyword volume history (trend detection)**
Tool: `keywords-explorer-volume-history`
Required: `country`, `keyword`
Optional: `date_from`, `date_to`

Returns monthly volume over time. Use to identify:
- Rising keywords (volume increasing quarter-over-quarter)
- Seasonal keywords (predictable spikes)
- Declining keywords (avoid investing in)

**Get keyword volume by country**
Tool: `keywords-explorer-volume-by-country`
Required: `keyword`
Returns volume broken down by country. Useful when targeting
multiple markets.

---

### Backlink Data

**Get backlink statistics**
Tool: `site-explorer-backlinks-stats`
Required: `target`, `date`
Optional: `mode`
Returns aggregate backlink counts: total, dofollow, referring domains.

**Get referring domains**
Tool: `site-explorer-referring-domains`
Required: `target`, `select`
Optional: `mode`, `limit`, `order_by`, `where`, `history`

**Get all backlinks (detailed)**
Tool: `site-explorer-all-backlinks`
Required: `target`, `select`
Optional: `mode`, `limit`, `order_by`, `where`, `aggregation`, `history`

**Get anchor text distribution**
Tool: `site-explorer-anchors`
Required: `target`, `select`
Optional: `mode`, `limit`, `order_by`, `where`, `history`

**Get broken backlinks**
Tool: `site-explorer-broken-backlinks`
Required: `target`, `select`
Optional: `mode`, `limit`, `order_by`, `where`, `aggregation`

**Get referring domain history**
Tool: `site-explorer-refdomains-history`
Required: `target`, `date_from`
Optional: `date_to`, `mode`, `history_grouping`

---

### Internal Link Analysis

**Best pages by internal links**
Tool: `site-explorer-best-by-internal-links`
Required: `target`, `select`
Optional: `mode`, `limit`, `order_by`, `where`

**Best pages by external links**
Tool: `site-explorer-best-by-external-links`
Required: `target`, `select`
Optional: `mode`, `limit`, `order_by`, `where`

**External linked domains**
Tool: `site-explorer-linked-domains`
Required: `target`, `select`
Optional: `mode`, `limit`, `order_by`, `where`

---

### Batch Operations

**Analyze multiple URLs/domains at once**
Tool: `batch-analysis`
Required: `select`, `targets`
Optional: `country`, `volume_mode`, `order_by`

`targets` is an array of objects, each with `url`, `mode`, `protocol`:
```json
[
  {"url": "example.com", "mode": "subdomains", "protocol": "both"},
  {"url": "competitor.com", "mode": "subdomains", "protocol": "both"}
]
```

Use for comparing your domain against competitors in a single call.
More efficient than multiple `site-explorer-metrics` calls.

---

### Site Audit (if project exists)

**Get site audit projects**
Tool: `site-audit-projects`
Optional: `project_id`, `date`

**Get audit issues**
Tool: `site-audit-issues`
Required: `project_id`
Optional: `date`, `date_compared`

**Explore crawled pages**
Tool: `site-audit-page-explorer`
Required: `project_id`
Optional: `select`, `where`, `limit`, `order_by`, `date`

**Get page content from crawl**
Tool: `site-audit-page-content`
Required: `target_url`, `project_id`, `select`
Optional: `date`

---

### Rank Tracker (if project exists)

**Overview of tracked keywords**
Tool: `rank-tracker-overview`
Required: `project_id`, `date`, `device`, `select`

**Competitor overview**
Tool: `rank-tracker-competitors-overview`
Required: `project_id`, `date`, `device`, `select`

**Competitor stats**
Tool: `rank-tracker-competitors-stats`
Required: `project_id`, `date`, `device`, `select`

---

### Account Info

**Check API usage and limits**
Tool: `subscription-info-limits-and-usage`
Free — does not consume API units. Call this to check remaining
quota before large operations.

---

## Common Recipes

These recipes describe the sequence of tools to call and what data to
pull at each step. Always call `doc` for each tool before first use
to get the correct column names.

### Full domain audit data pull
1. `site-explorer-metrics` — organic traffic, keyword count, costs
2. `site-explorer-domain-rating` — domain rating detail
3. `site-explorer-top-pages` (limit 50, order by traffic) — top content
4. `site-explorer-organic-keywords` (limit 100, order by traffic) — keyword portfolio
5. `site-explorer-backlinks-stats` — backlink profile summary
6. `site-explorer-referring-domains` (limit 20, order by domain rating) — top linkers
7. `site-explorer-organic-competitors` (limit 5) — competitive landscape

### Keyword opportunity discovery
1. `keywords-explorer-overview` — validate seed keywords (volume, difficulty, intent)
2. `keywords-explorer-matching-terms` — expand seeds into long-tail
3. `keywords-explorer-related-terms` (`terms: "also_rank_for"`) — semantic expansion
4. `keywords-explorer-search-suggestions` — autocomplete-style discovery
5. `keywords-explorer-volume-history` — trend validation on top picks
6. `serp-overview` — competitive analysis on priority keywords

### Brief data collection
1. `keywords-explorer-overview` — primary keyword metrics
2. `keywords-explorer-matching-terms` — long-tail and question variants
3. `keywords-explorer-related-terms` (`terms: "also_talk_about"`) — semantic keywords
4. `keywords-explorer-search-suggestions` — autocomplete suggestions
5. `serp-overview` — top 5 competitors for the primary keyword
6. `site-explorer-organic-keywords` (target: each competitor URL, `mode: "exact"`) — competitor ranking keywords

### Competitor gap analysis
1. `site-explorer-organic-competitors` — find competitors by overlap
2. `site-explorer-organic-keywords` on competitor — their keyword portfolio
3. Compare against our `site-explorer-organic-keywords` — find gaps
4. `keywords-explorer-overview` on gap keywords — validate opportunity
5. `serp-overview` on priority gaps — assess winnability

### Content refresh analysis
1. `site-explorer-organic-keywords` for the URL — current rankings
2. `site-explorer-metrics-history` for the URL — traffic trend over time
3. `serp-overview` for the primary keyword — current SERP state
4. Compare against original brief data — what changed

---

## Error Handling

### Common errors

**Invalid column name in select**
The `select` parameter contains a column name the tool doesn't recognize.
This is the most common error. Fix: call `doc` for the tool and use only
columns listed in the outputSchema.

**No data returned**
The domain/keyword may be too new, too niche, or misspelled. Check:
- Domain spelling (no protocol prefix needed)
- Country code is valid two-letter ISO
- Date is not in the future

**Rate limiting**
If a request fails with a rate limit error:
- Check `subscription-info-limits-and-usage` for remaining quota
- Reduce `limit` parameter to pull fewer rows
- Space out requests (avoid parallel MCP calls)

**Mode mismatch**
If a domain shows unexpectedly low metrics, check `mode`. Using
`mode: "domain"` instead of `mode: "subdomains"` excludes www traffic.
