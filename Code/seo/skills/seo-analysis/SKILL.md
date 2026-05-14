---
name: seo-analysis
description: >
  SEO research and competitive analysis. SERP pattern recognition, intent
  classification, keyword difficulty assessment, competitive landscape reading,
  seed generation, 6 Circles keyword expansion, validation and clustering,
  prioritization, trend detection, content gap interpretation, and topical
  authority mapping. Use when interpreting SERP data, finding keyword
  opportunities, or assessing competitive positioning.
---

# SEO Analysis

Consolidated knowledge base for reading SERPs, discovering keywords, and
optimizing content for search.

---

## Brand Context Integration

On every invocation, check for existing brand context in `./brand/` before
performing any analysis. Prior knowledge about the site, its competitors,
and its voice makes every downstream step more accurate.

### Reads (if they exist)

| File | What it provides | How it informs analysis |
|------|-----------------|----------------------|
| `site-profile.md` | Domain overview, business summary, top pages, content map, technical notes | Grounds the audit in what the site actually does — avoids misclassifying intent, misidentifying competitors, or flagging intentional technical choices as issues |
| `competitors.md` | Known competitors with DR, keyword overlap, traffic | Use these as the primary competitor list instead of auto-detection. Auto-detected competitors are often wrong (government sites, news outlets, unrelated domains). Only supplement with auto-detection if fewer than 2 competitors are listed |
| `brand-voice.md` | Voice profile, tone, vocabulary, style conventions | Informs content quality assessment — evaluate whether existing content matches the brand's stated voice, not a generic quality bar |

### Context Loading

1. Check whether `./brand/` exists
2. If it exists, read all files present. Briefly note what was found and how
   it will shape the analysis (e.g., "Found site profile and 3 known
   competitors — using these instead of auto-detection")
3. If `./brand/` is empty or doesn't exist, proceed without brand context.
   All analysis works standalone — brand context makes it more accurate,
   not possible

### Competitor Source Priority

When competitors are needed (audit, research, gap analysis):

1. **User-provided competitors** (from command input) — always first
2. **`./brand/competitors.md`** — user-provided or user-approved competitors
3. **~~SEO data auto-detection** — last resort only, validate results with user before using

`./brand/competitors.md` is the reliable source because users provide
their competitors directly. Auto-detection frequently returns
irrelevant domains (news sites, government pages, unrelated industries) —
discard these rather than polluting the analysis with bad comparisons.

---

## Data Persistence

~~SEO data API calls are expensive. Never re-fetch data that's already saved
locally.

### Cache-Check Rule

Before calling any ~~SEO data domain-level tool, check `./brand/` first:

| File | Fresh If | Caches |
|------|----------|--------|
| `site-profile.md` | `date_fetched` within 7 days | Domain metrics, top pages, striking-distance keywords, top keywords by traffic |
| `competitors.md` | `date_fetched` within 14 days | Competitor domains with DR, keyword overlap, top shared keywords |

- **Fresh** → use cached data, skip the API call
- **Stale or missing** → fetch from ~~SEO data, then save back to the file
- **User says "refresh"** → force-fetch regardless of freshness

### What to Save

Update `./brand/site-profile.md` and `./brand/competitors.md` per the
field definitions in `${CLAUDE_PLUGIN_ROOT}/FILE-SCHEMAS.md`. Only update
data sections — never overwrite user-authored sections.

### Save-Back Rule

After any command fetches domain-level ~~SEO data, update the
corresponding `./brand/` file and set `date_fetched` to today. Create
`./brand/` if it doesn't exist. Never overwrite user-authored sections
(like business description in site-profile) — only update the data
sections.

### Brief as Cache

The brief HTML file (path tracked in the `**Brief:**` field of
`./campaigns/opportunities.md`) already stores keyword metrics, SERP
data, and competitor analysis. Downstream commands (like `/write-content`)
should read the brief instead of re-fetching the same data. A brief
younger than 14 days is fresh enough for a SERP check.

---

## MCP Tool Usage (Mandatory)

Before making any calls to an MCP tool, read the corresponding reference file:

- **Ahrefs** → [Ahrefs MCP Reference](references/ahrefs-mcp.md)
- **DataForSEO** → [DataForSEO MCP Reference](references/dataforseo-mcp.md)
- **Firecrawl** → [Firecrawl MCP Reference](references/firecrawl-mcp.md)

These references contain the exact tool names, parameter schemas, cost
guidance, and required pre-call steps. Each ~~SEO data provider has
different conventions (column names, filter syntax, parameter shapes).
The reference files include equivalent recipes so the same operations
work regardless of which provider is connected.

---

## SERP Analysis

How to read search engine results pages and make decisions from what you see.

### SERP Pattern Recognition

Classify every SERP before making strategy decisions. Pull 10 results via
~~SEO data's SERP overview tool and categorize:

**Content type distribution** — what formats dominate?

| Dominant Format | Signal | Action |
|-----------------|--------|--------|
| Long-form guides (70%+) | Google rewards depth | Write comprehensive guide |
| Listicles (70%+) | Searchers want scannable options | Write a better list |
| Mixed formats | No single format wins | Match the top performer or fill the format gap |
| Tools / calculators | Searchers want to DO, not read | Consider interactive content or skip |
| Video results in top 5 | Visual intent | Include video or reconsider keyword |
| Reddit / forums in top 5 | No good article exists | Major content gap — high opportunity |
| E-commerce / product pages | Transactional intent | Blog content won't rank here |

**DR range reading** — who ranks and what that means:

| DR Range of Top 5 | Interpretation | Your Move |
|--------------------|----------------|-----------|
| All 80+ | Authority-gated — big brands only | Target long-tail variations instead |
| 60-80 mix | Competitive but winnable with strong content | Requires excellent content + some links |
| 30-60 mix | Content-driven SERP | Win on quality and depth |
| Under 30 present | Low barrier to entry | Fast win opportunity |
| Wide spread (20-90) | Google testing — no clear authority signal | Quality content can break in |

**Freshness signals** — how old are the top results?

| Age Pattern | Meaning |
|-------------|---------|
| All results < 6 months | Google values freshness for this query |
| Top results 1-2 years old | Stable SERP — content needs to be significantly better to displace |
| Top results 2+ years old | Freshness opportunity — update advantage |
| Mix of old and new | Not freshness-sensitive — focus on quality |

### Intent Classification

Determine intent from what Google shows, not from the keyword alone.

**Primary intent signals from SERP results:**

| SERP Signal | Intent | Content Approach |
|-------------|--------|------------------|
| Knowledge panels, definitions, explainer articles | Informational | Educate thoroughly, answer directly |
| Product listings, pricing pages, "best of" lists | Commercial | Help them compare and decide |
| Shopping results, buy buttons, specific product pages | Transactional | Remove friction, enable purchase |
| Brand homepages, login pages, specific site results | Navigational | You can't compete here — skip |
| Featured Snippet present | Informational (answerable) | Structure content to win the snippet |
| PAA boxes extensive | Informational with depth | Cover sub-questions as sections |
| Video carousel | Visual / how-to | Consider video or include visual aids |

**Mixed intent handling:**

Many keywords carry multiple intents. When the SERP shows a mix (e.g.,
informational guides alongside product pages), look at positions 1-3
specifically — Google puts the dominant intent there. Positions 4-10
often serve the secondary intent.

**Intent-to-content-type mapping:**

| Intent | Keyword Signals | Content Type | CTA Style |
|--------|-----------------|--------------|-----------|
| Informational | what, how, why, guide, tutorial | Pillar guide, how-to | Newsletter, resource |
| Commercial | best, vs, review, compare, top | Comparison, listicle | Free trial, demo |
| Transactional | buy, pricing, get, hire, cost | Landing page, product | Purchase, contact |
| Mixed | Broad terms with varied SERP | Match top performer | Context-dependent |

### Keyword Difficulty Assessment

KD is a starting point, not a verdict. Factor in what the number hides.

**When low KD is actually hard:**
- Strong brands ranking casually (DR 80+ sites with thin content — they
  rank on authority, not content quality)
- Product or navigational intent disguised as informational
- YMYL topics where Google requires E-E-A-T signals regardless of KD
- Keywords with low volume and low competition because nobody wants them

**When high KD is actually winnable:**
- Top results are outdated (2+ years, pre-AI content)
- Top results are thin (under 1,000 words for topics that need depth)
- No result matches the actual search intent well
- SERP has forums/Reddit — signals content gap despite high KD
- You have genuine topical authority in the space

**KD interpretation by range:**

| KD Range | General Assessment | Nuance |
|----------|-------------------|--------|
| 0-15 | Easy — content quality wins | Verify there's actual search demand |
| 16-30 | Moderate — good content + some authority | Sweet spot for growing sites |
| 31-50 | Competitive — need strong content + links | Check DR of top results first |
| 51-70 | Hard — authority matters significantly | Only pursue with strong domain or unique angle |
| 71+ | Very hard — established players dominate | Long-term play, needs link building |

Always cross-reference KD with actual SERP composition. A KD 25 keyword
where all top results are DR 70+ sites is harder than the number suggests.

### Competitive Landscape Reading

Framework for understanding who ranks, why, and where the openings are.

**Identifying the weak link in a SERP:**

Pull SERP results for the target keyword via ~~SEO data and evaluate each result:

1. **Content quality** — Is it comprehensive, or thin and generic?
2. **Freshness** — Published date and last update
3. **Domain authority** — DR relative to others in the SERP
4. **Backlink profile** — Referring domains to that specific page
5. **Content-intent match** — Does it actually answer what the searcher wants?

The weak link is the result with the lowest combination of these. That's
the position you can realistically take.

**Competitive moat assessment:**

| Moat Type | Signal | How to Compete |
|-----------|--------|----------------|
| Backlink-driven | High DR, many referring domains, mediocre content | Win on content quality — their content is beatable, their links aren't (yet) |
| Content-driven | Lower DR but exceptional depth and freshness | Match or exceed their content quality, build links over time |
| Brand-driven | Household name ranking on brand recognition | Target long-tail variations they won't bother with |
| Technical | Fast site, strong schema, excellent UX | Match their technical baseline, differentiate on content |

When a competitor advantage is **structural** (DR, backlinks), it requires
long-term authority building. When it's **actionable** (content quality,
freshness, coverage gaps), you can compete immediately with better content.

---

## Keyword Research

How to find keyword opportunities and decide which ones are worth pursuing.

### Seed Generation

Generate 20-30 seed keywords covering four categories:

**Direct terms** — what the business sells or offers
> Products, services, solutions. The obvious starting point.

**Problem terms** — what pain the target audience has
> Challenges, frustrations, obstacles. How people search before they
> know a solution exists.

**Outcome terms** — what results people want to achieve
> Transformations, metrics, end states. The "after" picture.

**Category terms** — broader industry or niche terms
> Market categories, industry labels. Captures people exploring the space.

**Extracting seeds from existing data:**

If `./campaigns/opportunities.md` or `./brand/site-profile.md` exists,
extract additional seeds from:
- Striking-distance keywords (rank 6-20) — already close, push to top 5
- Topics competitors cover that the site doesn't — gap-derived seeds
- Underperforming pages with ranking potential — keyword targets to optimize

### Expansion Methodology (6 Circles)

Expand seeds using six lenses that cover the full search landscape.

**Circle 1: What You Sell** — Products, services, solutions offered directly.

**Circle 2: Problems You Solve** — Pain points and challenges the audience faces.

**Circle 3: Outcomes You Deliver** — Results and transformations customers achieve.

**Circle 4: What Makes You Different** — Unique positioning, methodology,
approach. If `./brand/brand-voice.md` or site profile exists, use the
stated differentiators to populate this circle.

**Circle 5: Adjacent Topics** — Related areas where the target audience
spends time. Industry trends, complementary tools, community interests.

**Circle 6: Entities to Associate With** — People, tools, frameworks,
competing products the brand wants to be connected to. Comparison and
"alternative to" keywords live here.

**Expansion techniques per circle:**

Apply three pattern types to each seed:

- **Question patterns**: what is, how to, why, best, vs, examples, for [audience]
- **Modifier patterns**: tools, templates, guide, strategy, [year], for beginners, for [industry]
- **Comparison patterns**: A vs B, best [category], [tool] alternatives, [tool] review

**Target**: 100-200 expanded keywords from the seed list.

### Validation Framework

Before finalizing any pillar, run four checks. A pillar that fails 2+
checks is not a pillar — demote to a single article or remove it.

**1. Search Volume Check**
Does this pillar have >1,000 monthly searches across its cluster?

With ~~SEO data: pull keyword overview data for the cluster
keywords and sum volume. Without: use autocomplete richness (more
suggestions = more interest) and SERP competitiveness as demand proxies.

**2. Market-Centric Check**
Does the MARKET search for this, or is it just what you WANT to talk about?

| Product-Centric (Fail) | Market-Centric (Pass) |
|--------------------------|------------------------|
| "Our methodology" | "Marketing automation" |
| "[Your product] tutorials" | "[Category] tutorials" |
| "Why we're different" | "[Problem] solutions" |
| Features of your product | Outcomes people search for |

The brand's positioning angle informs HOW to write about market topics,
not WHAT topics to target.

**3. Competitive Reality Check**
Can you realistically rank on page 1?

Pull SERP results for the pillar keyword. If all top results are DR 80+
with comprehensive content and strong backlinks, this pillar needs
a different entry point — long-tail variations, a sub-topic cluster,
or a differentiated format.

**4. Proprietary Advantage Check**
Do you have unique content, data, or expertise for this pillar?

| Advantage | Priority Impact |
|-----------|----------------|
| Proprietary data others don't have | Prioritize highly |
| Unique methodology or framework | Prioritize highly |
| Practitioner experience (done it, not read about it) | Prioritize |
| Same information everyone else has | Deprioritize |

### Clustering Methodology

Group keywords into pillars using the hub-and-spoke model:

```
                [PILLAR]
             Main Topic Area
                  |
    +-------------+-------------+
    |             |             |
[CLUSTER 1]  [CLUSTER 2]  [CLUSTER 3]
 Subtopic      Subtopic      Subtopic
    |             |             |
 Keywords     Keywords      Keywords
```

**Identifying pillars (5-10 per business):**

A pillar is a major topic area that supports one comprehensive guide,
3-7 supporting articles, and ongoing content expansion. Ask: "Could
this be a complete guide that thoroughly covers the topic?"

**Clustering process:**

1. **Group by semantic similarity** — keywords that mean similar things
2. **Group by search intent** — keywords with the same user goal
3. **Identify the pillar keyword** — broadest term in each group
4. **Identify supporting keywords** — more specific variations
5. **Attach PAA questions** — map People Also Ask data to the cluster
   it belongs to
6. **Note competitor coverage** — mark which competitors cover each cluster

### Prioritization Matrix

Score each cluster on three dimensions and map to a priority tier.

**Business Value** (High / Medium / Low):
- **High**: Direct path to revenue — commercial intent, core offering
- **Medium**: Indirect path — trust building, lead capture, education
- **Low**: Brand awareness only — top of funnel, tangential

**Opportunity** (High / Medium / Low):
- **High**: No good content exists, results are outdated or thin,
  forums ranking, you have a unique angle, growing trend
- **Low**: Dominated by DR 80+ sites with strong content, excellent
  coverage already exists, declining interest

**Speed to Win** (Fast / Medium / Long):
- **Fast (3mo)**: Low competition, unique expertise, confirmed content gap
- **Medium (6mo)**: Moderate competition, needs comprehensive content
- **Long (9-12mo)**: High competition, requires authority building + links

**Priority tiers:**

| Business Value | Opportunity | Speed | Priority |
|---------------|-------------|-------|----------|
| High | High | Fast | DO FIRST |
| High | High | Medium | DO SECOND |
| High | Medium | Fast | DO THIRD |
| Medium | High | Fast | QUICK WIN |
| High | Low | Any | LONG PLAY |
| Low | Any | Any | BACKLOG |

### Trend Detection

Identify whether a keyword opportunity is growing, stable, or dying
before investing in content.

**Using ~~SEO data for validation:**

Pull keyword volume history for candidate keywords. Compare
volume quarter-over-quarter:
- **Rising**: Volume increasing 2+ consecutive quarters → real trend
- **Stable**: Flat volume with minor fluctuation → evergreen topic
- **Declining**: Volume dropping quarter-over-quarter → avoid investing
- **Seasonal**: Predictable annual spikes → time content to pre-season

**Using ~~web research for discovery:**

Search for emerging topics in the niche — recent developments, new
tools, shifting practices. Then validate with volume history above.
If volume history isn't available, use autocomplete expansion rate
(more suggestions = growing interest) and news coverage density
as proxies.

### Content Gap Interpretation

Not all gaps are worth filling. Filter noise from signal.

For the full tactical methodology — how to find gaps across four lenses
(striking distance, competitive gaps, unowned topics, AI visibility), revenue modeling,
SERP weakness scanning, content feature auditing, competitor pattern
detection, opportunity clustering, and narrative framing — see
[Opportunity Finding Reference](references/opportunity-finding.md).

**Gap types worth pursuing:**

| Gap Type | Signal | Action |
|----------|--------|--------|
| Catch-up gap | All competitors cover this, you don't | Create content — table-stakes topic |
| Blue ocean | Nobody covers this well (forums ranking, thin results) | Create content — first-mover advantage |
| Improvement gap | Competitors cover it but content is weak/outdated | Create better content — outclass them |
| Depth gap | Topic covered superficially everywhere | Write the definitive resource |

**Gaps to skip:**

- Keywords with no measurable demand (no autocomplete, no volume)
- Topics outside your domain expertise (no E-E-A-T signals)
- Keywords where the gap exists because the topic is declining
- Extremely niche variations that fragment effort

### Topical Authority Mapping

Map a domain's authority footprint to identify where to invest.

**Using ~~SEO data:**

Pull organic keyword rankings via ~~SEO data and group by topic cluster.
For each cluster, evaluate:

- **Keyword count** — how many keywords does the site rank for in this topic?
- **Average position** — clustered near top 10 (strong) or scattered 20-50 (weak)?
- **Traffic contribution** — what percentage of total organic traffic comes from this cluster?
- **Content depth** — how many pages cover this topic?

**Authority assessment:**

| Pattern | Assessment | Strategy |
|---------|-----------|----------|
| Many keywords, strong positions, high traffic | Core authority cluster | Protect and expand |
| Few keywords, weak positions, low traffic | Emerging or neglected cluster | Invest if strategically important |
| Many keywords, declining positions | Eroding authority | Refresh content urgently |
| No keywords in topic | No authority footprint | Build from scratch — start with low-KD entries |

**Investment prioritization:**

Invest where the return is highest:
1. Clusters where you already rank 6-20 (push to top 5 — fastest ROI)
2. Clusters adjacent to existing authority (topical proximity helps)
3. High-value clusters with zero coverage (strategic gap fill)
4. Low-priority clusters with existing weak content (lowest priority)

### Overlap Checking

Before recommending any opportunity, deduplicate against everything
already tracked.

**Check sequence:**

1. **`./campaigns/opportunities.md`** — read every entry. Collect all
   keywords (lead + cluster) into a dead-keyword set. If a candidate
   opportunity's keywords overlap with any dead keyword, skip it —
   regardless of the existing entry's status
2. **Existing briefs** — check `**Brief:**` fields in opportunities.md
   entries. If a brief path exists for a keyword, flag as "brief exists"
3. **Produced articles** — check `**Article:**` fields in
   opportunities.md entries. If an article path exists, flag as
   "already produced"

**How to match:** compare lowercase, trimmed keyword strings. "Low-Code
Automation Platform" matches "low-code automation platform". Ignore
volume numbers in parentheses when comparing.

**Overlap labels:**

| Label | Meaning | Action |
|-------|---------|--------|
| Create new | No existing content targets this keyword | New opportunity |
| Optimize existing | Page exists but underperforms | Optimize opportunity |
| Brief exists | Brief created, not yet written | Skip to `/write-content` |
| Already produced | Article written | Skip unless refresh needed |

---

## References

For detailed frameworks, load these when needed:

- [Opportunity Finding](references/opportunity-finding.md) — Revenue modeling, striking-distance extraction, competitive gap methodology, SERP weakness scanning, content feature auditing, opportunity clustering, narrative framing
- [Ahrefs MCP Reference](references/ahrefs-mcp.md) — Ahrefs endpoint map, conventions, and query patterns
- [DataForSEO MCP Reference](references/dataforseo-mcp.md) — DataForSEO endpoint map, conventions, and query patterns
- [Firecrawl MCP Reference](references/firecrawl-mcp.md) — Firecrawl tool inventory, cost guidance, and preferred workflows (scrape + map over crawl, never default to agent)