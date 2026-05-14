# Opportunity Finding

Tactical methodology for surfacing revenue-ranked SEO opportunities.
Everything flows through four lenses: striking distance, competitive
gaps, unowned topics, and AI visibility. Each opportunity gets a dollar value, a
competitive narrative, and a clear action.

---

## Revenue Modeling

Every opportunity is valued in dollars, not abstract scores. Use this
model to estimate what winning a keyword is worth per month.

### Formula

```
Monthly value = volume × CTR at target position × conversion rate × deal value
```

This is the primary model. Every opportunity gets valued with it.

**CTR curve by organic position** (approximate):

| Position | CTR |
|----------|-----|
| 1 | 28% |
| 2 | 15% |
| 3 | 11% |
| 4 | 8% |
| 5 | 6% |
| 6-10 | 2-4% |
| 11-20 | 0.5-1.5% |

### Where deal value and conversion rate come from

**Best case:** `./brand/site-profile.md` has an `Average deal size`
field (set during `/start-here`). Use it directly.

**If no deal size is available:** Infer the business model from the site
content and competitors, then use the defaults below.

### Industry defaults

Use these when the user hasn't provided their own numbers. Pick the
row that best matches the business model — not the industry label.

| Business Model | Default Deal Value | Default Conversion Rate | Rationale |
|---------------|-------------------|------------------------|-----------|
| B2B SaaS (enterprise) | $50,000 | 0.5% | Long sales cycles, high ACV, organic drives pipeline not direct sales |
| B2B SaaS (mid-market) | $15,000 | 1.0% | Shorter cycles, demo/trial driven |
| B2B SaaS (SMB/self-serve) | $3,000 | 2.0% | Higher velocity, lower touch |
| B2B Services (consulting, agency) | $25,000 | 0.5% | Project-based, relationship-driven |
| E-commerce (high-ticket) | $500 | 2.5% | Direct purchase, higher AOV |
| E-commerce (general) | $75 | 3.5% | High volume, low friction |
| SaaS (PLG / freemium) | $1,200 | 3.0% | Annual value, signup-driven |
| Local services | $2,000 | 5.0% | High intent searchers, booking-driven |
| Marketplace / platform | $200 | 2.0% | GMV per transaction |
| Media / content (ad-supported) | RPM $25 | 100% (every visitor = revenue) | Use `volume × CTR × $0.025` — RPM model, not conversion model |

**"Conversion rate" here means:** visitor-to-revenue event. For B2B
this is visitor → lead → closed deal (the full funnel, not just form
fills). For e-commerce it's visitor → purchase. The rates above
account for the full funnel.

### Showing your math

Always state the assumptions in the output so the user can correct them:

```
590/mo × 11% CTR (position 3) × 0.5% conversion × $50,000 deal = $16,225/mo
```

If the user says the numbers look wrong, adjust the deal value or
conversion rate and remodel — don't switch to CPC proxy.

### CPC proxy (last resort)

```
Monthly value = volume × CTR at target position × CPC / 100
```

CPC values may be in USD cents (Ahrefs) or USD dollars (DataForSEO) —
check the provider reference. This model estimates the cost of buying
the same traffic via paid search. **Only use this when:**
- No deal size in `site-profile.md`
- Business model can't be inferred from the site
- User explicitly asks for a CPC-based model

The CPC proxy systematically undervalues B2B keywords (where CPC
is low but deal sizes are high) and overvalues competitive
e-commerce keywords (where CPC is inflated by bidding wars). Prefer
the deal-value model in all cases where you have any basis for
estimating deal size.

### Cluster-level value

Sum the modeled value of all keywords in a cluster. This is the
headline number on each opportunity.

### Traffic potential as a sanity check

Some providers include a traffic potential metric (Ahrefs:
`traffic_potential`, DataForSEO: `etv`) showing the estimated monthly
traffic of the current #1 result. Compare your modeled traffic
(volume × CTR) against this — if your estimate is 3x+ higher, your
CTR assumption may be too aggressive. Adjust position target or note
the discrepancy.

---

## Lens 1: Striking Distance

Keywords where the site already ranks 6–20. These are the fastest ROI
because the content exists and Google already considers it relevant.

### How to find them

1. Pull organic keyword rankings via ~~SEO data with position filter
   6–20, volume >= 100, ordered by traffic potential descending
2. Group results by topic cluster (keywords sharing the same ranking URL
   or semantically related keywords ranking on different pages)
3. For each cluster, identify the lead keyword (highest volume)

### How to assess winnability

For each striking-distance cluster, pull SERP results on the lead
keyword via ~~SEO data and evaluate:

| Signal | What to check | Winnable if... |
|--------|--------------|----------------|
| Content quality gap | Scrape the top 3 results via ~~web scraper | Their content is thinner, older, or less comprehensive than yours |
| DR gap | Compare your DR to positions 1-5 | The DR range of top 5 includes sites at or below your DR |
| Backlink gap | Compare referring domains to your page vs theirs | Gap is < 3x (closeable with content improvement alone) |
| Format match | Is your content the same type as the top results? | Yes — or the SERP is mixed enough that your format has a slot |
| Freshness | When were top results last updated? | Top results are 12+ months old in a fast-moving topic |

### Value calculation for striking distance

Model the traffic delta from current position to realistic target:

```
Current traffic = volume × CTR at current position
Target traffic = volume × CTR at target position (usually position 3-5)
Monthly value uplift = (target traffic - current traffic) × CPC / 100
```

This is the incremental value — what you gain by improving position.

### Action framing

Striking-distance opportunities are always "Optimize existing" — the
content exists, it needs improvement or refresh. Specify what's needed:
update content, add missing sections, improve heading structure, add
internal links, refresh data/examples.

---

## Lens 2: Competitive Gaps

Keywords competitors rank for that you don't. These are the
opportunities hiding in your competitors' keyword portfolios.

### How to find them

1. **Identify competitors** — check `./brand/competitors.md` first
   (user-confirmed). Fall back to ~~SEO data competitor discovery tool
   only if no brand context exists. Limit to 3-5 real competitors
2. **Pull competitor keywords** — organic keyword rankings on each
   competitor domain via ~~SEO data, filtered to top 100 by traffic,
   volume >= 200
3. **Pull your keywords** — organic keyword rankings on the user's
   domain, same filters
4. **Find the gaps** — keywords where at least one competitor ranks in
   the top 10 AND you either don't rank at all or rank 20+
5. **Validate gaps** — keyword overview on the gap keywords to get
   volume, KD, intent, and traffic potential
6. **Assess winnability** — SERP overview on priority gap keywords

### Competitor pattern detection

When analyzing competitor keyword portfolios, look for signals of
strategic moves — not just static snapshots:

**Content velocity:** If a competitor has multiple new pages ranking in
the same topic cluster (published within 3 months), they're making a
deliberate push. This is the "coordinated expansion" signal — it means
the window to compete is closing.

**Position momentum:** Use the ~~SEO data ranked keywords tool with
date comparison to see position changes over time. Competitors gaining
positions across a cluster = active investment. Competitors losing
positions = weakening grip, your opening.

**Multi-competitor convergence:** When 2+ competitors are independently
investing in the same topic cluster, it validates the opportunity AND
increases urgency. If UiPath, Blue Prism, and Gartner are all publishing
about RPA software, that cluster has real commercial value.

### Gap type assessment

Once you have the gap keywords, classify each cluster:

| Pattern | Gap Type | Evidence | Urgency |
|---------|----------|----------|---------|
| All competitors cover it, you don't | Catch-up | Table-stakes topic | High — you're losing ground every day |
| One competitor dominates, others don't | Land grab | First-mover advantage available | Medium — window exists until others follow |
| All competitors cover it, all poorly | Improvement | Weak content across the board | Medium — quality wins but no rush |
| Nobody covers it well | Blue ocean | Forums, Reddit, thin results ranking | High — first good content wins |

---

## Lens 3: Unowned Topics

Keywords where no one has strong content — the SERP is weak and waiting
for someone to claim it.

### SERP weakness signals

Pull SERP results for candidate keywords via ~~SEO data and scan for these patterns:

| Signal | How to detect | What it means |
|--------|--------------|---------------|
| Forums in top 5 | Reddit, Quora, Stack Exchange ranking | No authoritative article exists — major gap |
| Thin content ranking | Scrape top results, check word count < 800 for informational queries | Depth gap — comprehensive content wins |
| Outdated results | Top results published 2+ years ago, no recent updates | Freshness opportunity — updated content has edge |
| Aggregators ranking | Yelp, G2, Capterra, directory sites in top 5 | No direct-answer content exists |
| Low DR in top 3 | Sites with DR < 30 holding top positions | Content-quality SERP — anyone with good content can rank |
| Wide DR spread | Top 10 has DR ranging from 20 to 90 | Google is testing — no authority signal locked in |
| AI Overview present | Check SERP features for AI overview | Google is synthesizing because no single result answers well |
| Format mismatch | Top results are all listicles for a "how to" query | Wrong format dominates — correct format has an opening |

### Content feature audit ("What's Working")

For priority opportunities, go deeper. Scrape the top 3-5 results via
~~web scraper and evaluate what content features the winners use:

| Feature | Check for | Opportunity if missing |
|---------|-----------|----------------------|
| FAQ section | Dedicated FAQ with 5+ questions | Add FAQ with schema markup |
| Table of contents | Anchor-linked navigation | Add TOC for scannability |
| Freshness signals | Year references, "updated" dates | Publish with current date + year in content |
| Quantified outcomes | Specific metrics, case study data | Add real numbers and results |
| Visual aids | Charts, diagrams, screenshots, embedded tools | Add visuals competitors lack |
| Multi-use-case coverage | Multiple industries or scenarios covered | Cover breadth competitors skip |
| Interactive elements | Calculators, quizzes, downloadable templates | Add engagement layer |
| Schema markup | FAQ, HowTo, Article structured data | Add schema for rich results |
| Internal linking depth | Links to related content on same site | Advantage for sites with topical authority |

**This produces the "Gaps to Exploit" section** of each opportunity.
Identify 2-4 specific content angles that NONE of the current top
results cover. These are the differentiation plays — not "write better
content" but "cover X angle that nobody else does."

### Demand validation

Before promoting an unowned topic to an opportunity:

1. **Volume check** — does it have measurable search demand? Pull
   keyword overview via ~~SEO data. If volume is 0 and no autocomplete
   suggestions exist, skip it
2. **Trend direction** — is demand growing or dying? Pull keyword
   volume history via ~~SEO data. Declining topics are gaps for a reason
3. **E-E-A-T fit** — does the brand have credible authority here? A
   fintech company writing about gardening won't rank regardless of the
   gap

---

## Lens 4: AI Visibility

Whether the brand appears — or is absent — in AI-generated answers for
the opportunity's lead keywords. This is a scoring signal on
opportunities already identified by Lenses 1–3, not a standalone
discovery method.

### When to run

Only on the top 3–5 commercial-intent opportunity clusters after
clustering and valuation. AI visibility checks are expensive — do not
run them across all expanded keywords.

If the connected ~~SEO data provider does not support AI optimization
endpoints, skip this lens. Mark opportunities as "AI visibility: not
checked." The opportunity still stands on its organic merits.

### How to check

1. Take the lead keyword from each priority cluster
2. Rephrase it as a natural question a buyer would type into a chat
   interface ("What's the best workforce management software in
   Australia?" not "workforce management software")
3. Query all four AI answer channels — ChatGPT, Claude, Gemini, and
   Perplexity — via ~~SEO data
4. Scan each response for mentions of the user's brand and known
   competitors (from `./brand/competitors.md` or earlier research)

### How to score

| Pattern | Label | What it means |
|---------|-------|---------------|
| Brand absent, competitor(s) present | **AI visibility gap** | Competitors are capturing AI answer traffic you're missing. Priority boost |
| Brand present | **AI visibility asset** | Existing content is earning AI citations. Note it, protect it |
| Brand and competitors both absent | **AI greenfield** | No one owns this in AI answers yet. First-mover signal |

### AI search volume

Pull AI-specific search volume for lead keywords alongside traditional
volume via ~~SEO data. AI volume is typically 4–20% of traditional
volume but growing fast. Include it in the opportunity presentation
when available — it adds a second demand signal beyond Google organic.

### Cost guardrails

- Run AI visibility checks last, after opportunities are already
  clustered and valued
- Limit to the top 3–5 clusters by modeled value
- Check all four LLMs per keyword (4 calls per keyword)
- Do not scan all keywords in a cluster — only the lead keyword

### What it adds to opportunities

Add an **AI visibility** line to each checked opportunity:

- `AI visibility: gap` — "{Competitor} appears in ChatGPT and Perplexity
  answers; you don't"
- `AI visibility: asset` — "Your brand is cited in ChatGPT answers for
  this topic"
- `AI visibility: greenfield` — "No brands cited in AI answers — first
  mover advantage"
- `AI visibility: not checked` — AI optimization data not available

An AI visibility gap is a "Why Now" signal — competitors are building
presence in a channel that's growing while you're absent.

---

## Opportunity Clustering

Individual keywords aren't opportunities — clusters are. Group related
keywords into a single narrative opportunity with a headline dollar
value.

### How to cluster

1. **Semantic grouping** — keywords that mean roughly the same thing or
   share significant SERP overlap (same URLs ranking for multiple
   keywords in the group)
2. **Identify the lead keyword** — highest volume keyword in the cluster.
   This anchors the opportunity
3. **Sum cluster value** — add the modeled monthly value of all keywords
   in the cluster. This is the headline number
4. **Determine the action** — based on the dominant lens:
   - Mostly striking distance → Optimize existing
   - Mostly competitor gaps → Create new
   - Mostly unowned → Create new

### Narrative framing

Frame each opportunity as a competitive story, not a data row. The
framing depends on what the data shows:

**Competitor dominance threat:**
> "{Competitor} dominates {topic} searches while your visibility declines"
> Use when: a named competitor holds top positions and you're losing ground

**Uncontested gap:**
> "No dominant player in {topic} — {volume}/mo with rising demand"
> Use when: the SERP is weak and nobody owns it

**Erosion alert:**
> "Your {topic} rankings are losing ground to {Competitor A} and {Competitor B}"
> Use when: position data shows you're declining in a cluster

**Emerging trend:**
> "{Topic} search demand up {X}% — no established content leader yet"
> Use when: volume history shows growth and the SERP is immature

### Evidence strength

Rate each opportunity by how strong the evidence is:

| Rating | Criteria |
|--------|----------|
| **Strong evidence** | 3+ signals confirm the opportunity (volume, weak SERP, competitor gap, trend data, content audit all align) |
| **Growing evidence** | 2 signals confirm, others are neutral or unavailable |
| **Emerging signal** | 1 strong signal (e.g., volume spike) but limited supporting data |

Include this in the opportunity presentation so the user can gauge
confidence.

---

## The "Why Now" Test

Every opportunity needs a timing rationale. If you can't answer "why
should they act on this now instead of next quarter?" it's not urgent
enough to lead the list.

**Strong "Why Now" signals:**

| Signal | Source | Example |
|--------|--------|---------|
| Volume trending up | ~~SEO data keyword volume history | "Search volume up 74% over 6 months" |
| Competitor just published | Competitor content freshness check | "UiPath published a new guide last month — window closing" |
| SERP in flux | ~~SEO data SERP overview position changes | "Top 3 positions changed in the last 90 days — Google is re-evaluating" |
| Low KD + high value | ~~SEO data keyword overview | "KD 8 with $5,900/mo value — low-competition window" |
| Seasonal peak approaching | Volume history seasonality | "Peak search month is 6 weeks away — publish now to index in time" |
| Top result just went stale | Content freshness of #1 | "The #1 result hasn't been updated since 2024" |

**Weak "Why Now" signals (don't lead with these):**

- "It's a good keyword" — that's always true, not a timing argument
- "Competitors rank and you don't" — true but static; needs a momentum signal
- "High volume" — volume alone isn't urgency
