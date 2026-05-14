# DataForSEO MCP Reference

Tool inventory, query patterns, and conventions for the DataForSEO MCP server.

All tools follow the naming pattern `mcp__dataforseo__{tool-name}`.

---

## No Schema Pre-Call Needed

Unlike Ahrefs, DataForSEO tools are self-documenting through their parameter
schemas. There is no `doc` pre-call. All fields are always returned — there
is no `select` parameter to specify columns.

---

## Conventions

### Monetary values
CPC and cost values are returned in **USD dollars** (not cents).

### Domain input
Specify domains without `https://` or `www.`. For page-level analysis,
use the full URL including protocol.

Use `include_subdomains: true` where available to get full domain data
(equivalent to Ahrefs' `mode: "subdomains"`).

### Location
Use the full country name: `"United States"`, `"United Kingdom"`,
`"Australia"`, `"Canada"`. Not country codes.

### Language
Use ISO two-letter code: `"en"`, `"fr"`, `"de"`, etc.

### Filtering
Filters use an array syntax with operators between conditions:

```json
[["field_name", ">=", 100], "and", ["other_field", "<", 50]]
```

Simple filter:
```json
[["ranked_serp_element.serp_item.rank_group", "<=", 10]]
```

Supported operators: `=`, `<>`, `<`, `<=`, `>`, `>=`, `in`, `not_in`,
`like`, `not_like`, `ilike`, `not_ilike`, `regex`, `not_regex`,
`match`, `not_match`.

Use `%` with `like`/`not_like` as wildcards.

### Sorting (order_by parameter)
Array of strings with field name and direction separated by comma:
```json
["keyword_data.keyword_info.search_volume,desc"]
```

Multiple sorting rules:
```json
["keyword_data.keyword_info.search_volume,desc", "keyword_data.keyword_info.cpc,desc"]
```

Maximum 3 sorting rules per request.

### Limits
Default limit varies by endpoint (usually 10). Set `limit` explicitly.
Maximum is typically 1,000 rows per request. Use `offset` for pagination.

### Response structure
All responses include `keyword_info` (volume, CPC, competition,
monthly_searches), `keyword_properties` (keyword_difficulty, core_keyword,
detected_language), and `search_intent_info` (main_intent, probability,
secondary intents). This means **search intent and KD are built into
most keyword responses** — no separate call needed.

### Monthly searches
Returned as an object keyed by `"YYYY-MM"`:
```json
{"2025-12": 9900, "2025-11": 9900, "2025-10": 9900}
```

### Search volume trend
Includes percentage changes: `monthly`, `quarterly`, `yearly`.
Positive = growth, negative = decline. Use for trend detection.

### ETV (Estimated Traffic Value)
DataForSEO's traffic estimate metric. Equivalent to Ahrefs' organic
traffic estimate. Represents estimated monthly organic traffic based
on keyword positions and search volumes.

### Rank
DataForSEO uses a 0–1,000 scale domain authority metric from its
backlinks index (higher = more authoritative). This is **not** directly
comparable to Ahrefs Domain Rating (0–100 scale). When comparing
domains, use relative rank rather than absolute thresholds.

### Subscription tiers
DataForSEO has separate subscriptions for different API sections.
The Backlinks API may not be available if only the Labs subscription
is active. Check tool availability before relying on backlink data.
The Labs and SERP APIs cover the majority of SEO research needs.

---

## Tool Inventory by Operation

### Domain Overview

**Get domain ranking distribution and traffic estimate**
Tool: `dataforseo_labs_google_domain_rank_overview`
Required: `target`
Optional: `location_name`, `language_code`, `ignore_synonyms`
Returns organic keyword count by position bucket (pos_1, pos_2_3,
pos_4_10, pos_11_20, etc.), ETV, and keyword count.

```
target: "example.com"
location_name: "United States"
```

**Get historical domain ranking and traffic**
Tool: `dataforseo_labs_google_historical_rank_overview`
Required: `target`
Optional: `location_name`, `language_code`
Returns monthly snapshots of ranking distribution and traffic over time.
Use for trend analysis — traffic growth/decline.

**Get subdomains with ranking data**
Tool: `dataforseo_labs_google_subdomains`
Required: `target`
Optional: `location_name`, `language_code`, `limit`, `order_by`, `filters`
Returns subdomain list with ranking distribution and estimated traffic.

---

### Top Pages

**Get pages ranked by traffic or keyword count**
Tool: `dataforseo_labs_google_relevant_pages`
Required: `target`
Optional: `location_name`, `language_code`, `limit`, `order_by`, `filters`

Order by `["metrics.organic.etv,desc"]` for top pages by traffic.
Order by `["metrics.organic.count,desc"]` for top pages by keyword count.

Returns per-page: URL, ranking distribution, ETV, keyword count.

---

### Keyword Rankings

**Get organic keywords a domain/URL ranks for**
Tool: `dataforseo_labs_google_ranked_keywords`
Required: `target`
Optional: `location_name`, `language_code`, `limit`, `order_by`,
`filters`, `include_subdomains`, `item_types`

`target` accepts both domains and full URLs. For a specific page,
use the full URL with protocol (e.g., `https://example.com/page`).
For domains, specify without protocol.

Returns per keyword: volume, CPC, competition, KD, search intent,
monthly_searches, position, URL, title, ETV, rank changes.

Key filter patterns:

Striking distance keywords (positions 6-20):
```json
[["ranked_serp_element.serp_item.rank_group", ">=", 6],
 "and",
 ["ranked_serp_element.serp_item.rank_group", "<=", 20]]
```

High-volume keywords only:
```json
[["keyword_data.keyword_info.search_volume", ">", 100]]
```

Order by volume descending:
```json
["keyword_data.keyword_info.search_volume,desc"]
```

**Get keywords relevant to a domain (keyword ideas)**
Tool: `dataforseo_labs_google_keywords_for_site`
Required: `target`
Optional: `location_name`, `language_code`, `limit`, `order_by`,
`filters`, `include_subdomains`

Unlike `ranked_keywords` (what the site ranks for), this returns
keywords relevant to the domain's topic — useful for discovering
new opportunities the site doesn't yet target.

---

### Competitor Discovery

**Find organic competitors by keyword overlap**
Tool: `dataforseo_labs_google_competitors_domain`
Required: `target`
Optional: `location_name`, `language_code`, `limit`, `order_by`,
`filters`, `exclude_top_domains`, `item_types`

Set `exclude_top_domains: true` to filter out mega-sites (Wikipedia,
Amazon, etc.) and get more relevant competitors.

Returns per competitor: domain, intersection count, avg_position,
full_domain_metrics (ranking distribution + ETV), and the shared
keyword metrics.

Order by `["intersections,desc"]` for highest keyword overlap.

**Find SERP competitors for specific keywords**
Tool: `dataforseo_labs_google_serp_competitors`
Required: `keywords` (array)
Optional: `location_name`, `language_code`, `limit`, `order_by`, `filters`

Provide an array of target keywords to find which domains appear
most frequently across those SERPs. Returns domain, median_position,
rating, ETV, and visibility score.

**Find shared keywords between two domains**
Tool: `dataforseo_labs_google_domain_intersection`
Required: `target1`, `target2`
Optional: `location_name`, `language_code`, `limit`, `order_by`,
`filters`, `intersections`

Set `intersections: true` (default) to get keywords both domains rank for.
Set `intersections: false` to get keywords target1 ranks for but target2
doesn't — useful for gap analysis.

Returns keyword data with SERP elements for both domains side-by-side.

**Find shared keywords between specific pages**
Tool: `dataforseo_labs_google_page_intersection`
Same as domain_intersection but for specific URLs.
Use for page-level competitive analysis.

---

### SERP Analysis

**Get live SERP results for a keyword**
Tool: `serp_organic_live_advanced`
Required: `keyword`, `language_code`
Optional: `location_name`, `depth`, `device`, `search_engine`,
`people_also_ask_click_depth`, `max_crawl_pages`

Returns real-time Google SERP including organic results, AI overview,
People Also Ask (with expansion depth), related searches, knowledge
panels, images, and videos.

Each organic result includes: domain, title, url, description,
rank_group, rank_absolute, rating (if present).

Set `people_also_ask_click_depth: 2-4` to expand PAA questions
and capture deeper question chains.

Set `depth: 10` for top 10, `depth: 20` for top 20, etc.

**Note:** This is a **live** API call — it fetches fresh SERP data
in real time. More expensive than database endpoints but gives the
most current results.

**Get historical SERP data for a keyword**
Tool: `dataforseo_labs_google_historical_serp`
Required: `keyword`
Optional: `location_name`, `language_code`
Returns how the SERP for a keyword has changed over time, including
featured snippets and extra elements.

---

### Keyword Research

**Get keyword metrics (volume, KD, CPC, intent)**
Tool: `dataforseo_labs_google_keyword_overview`
Required: `keywords` (array, max 700)
Optional: `location_name`, `language_code`

Returns per keyword: search_volume, CPC, competition,
competition_level, monthly_searches (12 months), search_volume_trend,
keyword_difficulty, search_intent (main + secondary).

This is the primary keyword validation tool. Supports batch lookups
of up to 700 keywords in one call.

**Expand keywords — long-tail suggestions**
Tool: `dataforseo_labs_google_keyword_suggestions`
Required: `keyword` (single string)
Optional: `location_name`, `language_code`, `limit`, `order_by`, `filters`

Returns keywords containing the seed keyword with additional words.
Similar to Ahrefs' matching-terms / search-suggestions.

**Expand keywords — related terms (from "related searches")**
Tool: `dataforseo_labs_google_related_keywords`
Required: `keyword` (single string)
Optional: `location_name`, `language_code`, `limit`, `order_by`,
`filters`, `depth` (1-4)

Returns keywords from Google's "searches related to" SERP element.
The `depth` parameter controls how many levels deep to search
(depth 1 = 8 results, depth 2 = ~72, depth 4 = ~4,680).

Each result includes the keyword data AND a `related_keywords`
array listing further expansions at that depth level.

Use depth 1-2 for focused expansion, depth 3-4 for comprehensive
keyword discovery.

**Keyword ideas by topic category**
Tool: `dataforseo_labs_google_keyword_ideas`
Required: `keywords` (array, max 200)
Optional: `location_name`, `language_code`, `limit`, `order_by`, `filters`

Returns keywords that fall into the same product/service categories
as the seed keywords. Broader than suggestions — finds semantically
related keywords that may not contain the seed phrase.

Use for "also talk about" / topical coverage discovery (similar to
Ahrefs' `terms: "also_talk_about"`).

**Bulk keyword difficulty**
Tool: `dataforseo_labs_bulk_keyword_difficulty`
Required: `keywords` (array, max 1,000)
Optional: `location_name`, `language_code`

Returns KD score (0-100, logarithmic) for each keyword. Use for
batch scoring after keyword expansion to quickly filter by difficulty.

**Search intent classification**
Tool: `dataforseo_labs_search_intent`
Required: `keywords` (array, max 1,000)
Optional: `language_code`

Returns primary intent (informational, navigational, commercial,
transactional) with probability score, plus secondary intents.

Note: intent is also included in `keyword_overview` and
`ranked_keywords` responses — use this endpoint only when you need
intent for keywords you haven't already pulled via those tools.

**Get historical keyword data (trend detection)**
Tool: `dataforseo_labs_google_historical_keyword_data`
Required: `keywords` (array, max 700)
Optional: `location_name`, `language_code`

Returns monthly volume, CPC, and competition data since August 2021.
Use to identify rising, stable, declining, or seasonal keywords.

**Warning:** This endpoint returns large responses. Limit to 5-10
keywords per call to avoid oversized results.

---

### Backlink Data (Requires Backlinks Subscription)

These tools require the Backlinks API subscription. If not available,
skip backlink analysis or use the bulk endpoints from Labs.

**Get backlink overview**
Tool: `backlinks_summary`
Required: `target`
Optional: `include_subdomains`, `exclude_internal_backlinks`
Returns aggregate stats: total backlinks, dofollow, referring domains,
referring main domains, rank, broken pages/backlinks.

**Get referring domains**
Tool: `backlinks_referring_domains`
Required: `target`
Optional: `limit`, `order_by`, `filters`

**Get all backlinks (detailed)**
Tool: `backlinks_backlinks`
Required: `target`
Optional: `limit`, `order_by`, `filters`

**Get anchor text distribution**
Tool: `backlinks_anchors`
Required: `target`
Optional: `limit`, `order_by`, `filters`

**Get backlink competitors**
Tool: `backlinks_competitors`
Required: `target`
Optional: `limit`, `order_by`, `filters`
Returns domains sharing backlink profile — useful for link gap analysis.

**Domain link intersection (Link Gap)**
Tool: `backlinks_domain_intersection`
Required: `targets` (array, max 20)
Optional: `limit`, `order_by`, `filters`
Find domains linking to competitors but not to you.

**Backlink time-series**
Tool: `backlinks_timeseries_summary`
Required: `target`
Optional: `date_from`, `date_to`, `group_range`
Track backlink growth over time.

**Bulk backlink counts**
Tool: `backlinks_bulk_backlinks`
Required: `targets` (array, max 1,000)
Compare backlink counts across multiple domains at once.

**Bulk referring domain counts**
Tool: `backlinks_bulk_referring_domains`
Required: `targets` (array, max 1,000)

**Bulk rank scores**
Tool: `backlinks_bulk_ranks`
Required: `targets` (array, max 1,000)
Returns rank (0-1000) for each target — use for comparing domain
authority across multiple domains in one call.

**Bulk spam scores**
Tool: `backlinks_bulk_spam_score`
Required: `targets` (array, max 1,000)

---

### On-Page Analysis

**Parse page content**
Tool: `on_page_content_parsing`
Required: `url`
Optional: `enable_javascript`, `custom_user_agent`, `accept_language`

Returns structured content: headings, links, anchors, text content.
Useful for competitor content analysis (heading structure, word count,
internal/external links).

Set `enable_javascript: true` for JS-rendered pages.

**On-page SEO analysis**
Tool: `on_page_instant_pages`
Required: `url`
Returns page-level SEO optimization data: meta tags, headings,
content quality signals, and technical SEO factors.

**Lighthouse audit**
Tool: `on_page_lighthouse`
Required: `url`
Optional: `result` (audits | categories | configSettings | timing)
Returns Google Lighthouse scores for performance, accessibility,
SEO, and best practices. Use `result: "categories"` for summary
scores, `result: "audits"` for detailed audit results.

---

### Keyword Trends

**DataForSEO Trends (Google Search, News, Shopping)**
Tool: `kw_data_dfs_trends_explore`
Required: `keywords` (array, max 5)
Optional: `location_name`, `date_from`, `date_to`, `time_range`, `type`

Returns popularity data over time. Use `time_range: "past_12_months"`
or `"past_5_years"` for historical trends.

**Google Trends Explore**
Tool: `kw_data_google_trends_explore`
Required: `keywords` (array, max 5)
Optional: `location_name`, `language_code`, `date_from`, `date_to`,
`time_range`, `type`, `item_types`, `category_code`

Returns Google Trends data including graph, map, related topics,
and related queries. Set `item_types` to control what's returned.

**Trends by demographics**
Tool: `kw_data_dfs_trends_demography`
Required: `keywords` (array, max 5)
Returns age/gender breakdown of keyword interest.

**Trends by region**
Tool: `kw_data_dfs_trends_subregion_interests`
Required: `keywords` (array, max 5)
Returns location-specific keyword popularity.

---

### Content Analysis

**Citation search**
Tool: `content_analysis_search`
Required: `keyword`
Optional: `limit`, `order_by`, `filters`, `page_type`, `search_mode`
Returns detailed citation data: where a keyword is mentioned across
the web, with sentiment analysis, domain rank, and content info.

**Citation summary**
Tool: `content_analysis_summary`
Required: `keyword`
Returns aggregate citation metrics: mention count, sentiment
distribution, top domains, top categories.

**Citation trends**
Tool: `content_analysis_phrase_trends`
Required: `keyword`, `date_from`
Optional: `date_to`, `date_group`
Returns citation volume over time. Use for tracking brand mentions
or topic coverage trends.

---

### Domain Analytics

**WHOIS data with SEO metrics**
Tool: `domain_analytics_whois_overview`
Optional: `filters`, `limit`, `order_by`
Returns WHOIS data enriched with backlink stats and traffic info.

**Technology detection**
Tool: `domain_analytics_technologies_domain_technologies`
Returns technologies used by a domain (CMS, analytics, frameworks).

---

### Google Ads Keyword Data

**Search volume from Google Ads**
Tool: `kw_data_google_ads_search_volume`
Required: `keywords` (array)
Optional: `location_name`, `language_code`
Returns Google Ads data: search volume, CPC, competition.
More granular than Labs data for some keywords.

---

### AI Optimization

**Get LLM response for a keyword**
Tool: `ai_optimization_llm_response`
Required: `llm_type`, `user_prompt`, `model_name`
Optional: `temperature`, `top_p`, `web_search`

Sends a prompt to the specified LLM and returns the structured response.
Use this to check whether a brand or its competitors appear in AI
answers for a given query.

`llm_type` values: `"chat_gpt"`, `"claude"`, `"gemini"`, `"perplexity"`

`model_name` must match the LLM type. Call `ai_optimization_llm_models`
with your target `llm_type` to get available model names if unsure.

`user_prompt` is capped at 500 characters. Phrase keywords as natural
questions to get realistic answer-style responses (e.g., "What is the
best workforce management software in Australia?" rather than
"workforce management software").

Set `web_search: true` to let the LLM pull current information — this
produces responses closer to what real users see in chat interfaces
with web access.

**Cost guidance:** Each call queries one LLM. Checking four LLMs for
one keyword = 4 calls. Limit to top 3–5 priority keywords and only
the LLMs that matter for the target audience. ChatGPT and Perplexity
are the highest-traffic AI answer channels for most markets.

**Get AI search volume**
Tool: `ai_opt_kw_data_search_volume`
Required: `keywords` (array), `location_name`, `language_code`

Returns monthly AI-specific search volume with 12-month history per
keyword. This is the volume of queries made through AI chat interfaces
(ChatGPT, Perplexity, etc.) — separate from traditional Google search
volume.

Response includes `search_volume` (current monthly), and a monthly
history array for trend detection. AI search volume is typically
4–20% of traditional volume and growing rapidly.

**Cost guidance:** Cheap. Supports batch lookups. Safe to include
alongside traditional keyword validation calls.

---

## Common Recipes

These recipes describe the sequence of tools to call. They map 1:1
to the Ahrefs recipes in ahrefs-mcp.md — use whichever provider is
connected.

### Full domain audit data pull
1. `dataforseo_labs_google_domain_rank_overview` — ranking distribution, ETV, keyword count
2. `backlinks_summary` or `backlinks_bulk_ranks` — domain authority score
3. `dataforseo_labs_google_relevant_pages` (limit 50, order by ETV desc) — top content
4. `dataforseo_labs_google_ranked_keywords` (limit 100, order by volume desc) — keyword portfolio
5. `backlinks_summary` — backlink profile (if subscribed)
6. `backlinks_referring_domains` (limit 20) — top linkers (if subscribed)
7. `dataforseo_labs_google_competitors_domain` (limit 5, exclude_top_domains: true) — competitive landscape

### Keyword opportunity discovery
1. `dataforseo_labs_google_keyword_overview` — validate seed keywords (volume, KD, intent)
2. `dataforseo_labs_google_keyword_suggestions` — expand seeds into long-tail
3. `dataforseo_labs_google_related_keywords` (depth: 2) — semantic expansion via related searches
4. `dataforseo_labs_google_keyword_ideas` — category-based expansion (topical coverage)
5. `dataforseo_labs_google_historical_keyword_data` — trend validation on top picks (limit to 5-10 keywords)
6. `serp_organic_live_advanced` — competitive analysis on priority keywords

### Brief data collection
1. `dataforseo_labs_google_keyword_overview` — primary keyword metrics
2. `dataforseo_labs_google_keyword_suggestions` — long-tail and question variants
3. `dataforseo_labs_google_keyword_ideas` — semantic/topical keywords ("also talk about")
4. `dataforseo_labs_google_keyword_suggestions` — autocomplete-style suggestions
5. `serp_organic_live_advanced` (depth: 10) — top competitors + PAA questions
6. `dataforseo_labs_google_ranked_keywords` (target: competitor URL) — competitor ranking keywords

### Competitor gap analysis
1. `dataforseo_labs_google_competitors_domain` — find competitors by overlap
2. `dataforseo_labs_google_domain_intersection` (intersections: false) — keywords you're missing
3. `dataforseo_labs_google_ranked_keywords` on competitor — their keyword portfolio
4. `dataforseo_labs_google_keyword_overview` on gap keywords — validate opportunity
5. `serp_organic_live_advanced` on priority gaps — assess winnability

### AI visibility check (for opportunity clusters)
1. `ai_opt_kw_data_search_volume` on lead keywords — AI search volume alongside traditional volume
2. For top 3–5 commercial-intent clusters: rephrase lead keyword as a natural question
3. `ai_optimization_llm_response` across all four LLMs (ChatGPT, Claude, Gemini, Perplexity) — scan each response for brand and competitor mentions
4. Score each cluster: brand absent + competitor present = AI visibility gap; brand present = AI visibility asset; both absent = greenfield

This is 4 calls per keyword. Limit to top 3–5 clusters to control cost.

### Content refresh analysis
1. `dataforseo_labs_google_ranked_keywords` (target: page URL) — current rankings
2. `dataforseo_labs_google_historical_rank_overview` — traffic trend over time
3. `serp_organic_live_advanced` for the primary keyword — current SERP state
4. Compare against original brief data — what changed

---

## Error Handling

### Common errors

**Access denied (40204)**
The tool requires a subscription tier you haven't activated. Most common
with Backlinks API. Check your plan at app.dataforseo.com. Labs and SERP
tools are available on most plans.

**No data returned (empty items)**
The domain/keyword may be too new, too niche, or misspelled. Check:
- Domain spelling (no protocol prefix for domains)
- Location name is a valid full country name
- Language code is valid two-letter ISO

**Oversized response**
Some endpoints (especially `historical_keyword_data`) return very large
responses. Limit to 5-10 keywords per call or use filters to reduce
result size.

**Filter syntax errors**
Filters must be valid JSON arrays. Each condition is `["field", "operator", value]`.
Boolean operators (`"and"`, `"or"`) are strings between condition arrays.
Maximum 8 filters per request.

### Differences from Ahrefs to watch for

| Aspect | Ahrefs | DataForSEO |
|--------|--------|------------|
| Pre-call schema check | Required (`doc` call) | Not needed |
| Column selection | `select` parameter | All fields returned |
| Subdomain mode | `mode: "subdomains"` | `include_subdomains: true` |
| Monetary values | USD cents (divide by 100) | USD dollars |
| Location format | Country code (`us`) | Full name (`"United States"`) |
| Domain authority | DR (0-100) | Rank (0-1000) |
| Filter syntax | JSON object with `and`/`or` keys | Array with string operators |
| Order by syntax | Comma-separated string `"field:desc"` | Array `["field,desc"]` |
| Keyword input | Comma-separated string or array | Array (most endpoints) |
| Search intent | Separate inference needed | Built into keyword responses |
| Monthly volume | Separate history call | Included in keyword_info |
