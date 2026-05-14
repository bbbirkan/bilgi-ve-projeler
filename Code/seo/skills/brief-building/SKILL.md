---
name: brief-building
description: >
  Assemble SEO research data into an execution-ready content brief.
  Defines the 12-section brief structure, content type selection,
  heading structure synthesis from competitor and PAA data, word count
  calculation, keyword placement rules, internal linking strategy,
  featured snippet targeting, schema selection, and quality checklist.
  Use when building a content brief from keyword research data,
  structuring an SEO brief, or planning article outlines.
---

# Brief Writing

The brief is the research product. Agencies charge $300-500 per brief
because the research, structure, and competitive analysis inside it is
what separates content that ranks from content that doesn't. A good brief
means the writer (human or AI) can execute without guessing.

This skill defines how to assemble that brief from research data
collected by the seo-analysis skill and ~~SEO data tools.

---

## Brief Sections

Every brief contains these sections. Each is backed by real data, not
assumptions. The order below is the order they appear in the output file.

| # | Section | Data Source | Purpose |
|---|---------|-------------|---------|
| 1 | Metadata | User input + ~~SEO data | Client, topic, country, date |
| 2 | Primary Keywords | ~~SEO data keyword overview | Head terms with volume + KD |
| 3 | Long-Tail Keywords | ~~SEO data keyword suggestions | Variations with volume + KD |
| 4 | Question Keywords | ~~SEO data keyword suggestions | Question-form queries with volume + KD |
| 5 | People Also Ask | ~~SEO data SERP overview (~~browser fallback) | PAA questions with answer format guidance |
| 6 | Google Autocomplete | ~~SEO data keyword suggestions | Related searches users actually type |
| 7 | Competitor Analysis | ~~SEO data SERP + WebFetch | Top 3-5 URLs: headings, word count, ranking keywords |
| 8 | Recommended Word Count | Competitor analysis | Calculated from competitor average |
| 9 | Recommended Headings | Synthesis | H1-H3 structure from competitor + PAA + keyword data |
| 10 | Semantic Keywords | ~~SEO data related/idea terms | "Also talk about" terms to weave in naturally |
| 11 | Internal Linking | Site audit / existing content | Pages on the site to link to and from |
| 12 | Content Writing Notes | Brand voice + SEO guidelines | Voice guidance, keyword integration rules |

---

## Data Requirements

Before building the brief, the following data must be collected. The
seo-analysis skill and MCP reference files define HOW to collect each
item — this section defines WHAT the brief needs.

| Brief Section | Required Data | Minimum |
|--------------|---------------|---------|
| Primary Keywords | Head terms (≤3 words, volume >100) with volume, KD, intent, SERP features | 5 keywords |
| Long-Tail Keywords | Specific variations (4+ words or question-form) with volume, KD | 10 keywords |
| Question Keywords | Question-form queries with volume, KD | 3 keywords |
| People Also Ask | PAA questions from SERP with answer format (paragraph/list/table) per question | 3 questions |
| Google Autocomplete | Related search suggestions | 20 suggestions |
| Competitor Analysis | Top 3-5 organic URLs: heading structure, word count, top 10 ranking keywords, DR | 3 competitors |
| Semantic Keywords | "Also talk about" terms from co-occurrence data, ordered by volume | 15 terms |
| Internal Linking | Existing site pages related to the target topic (from site-profile.md or prior research) | Best effort |

### PAA answer format classification

When PAA data is collected, classify each question's expected answer format:

| SERP Signal | Recommended Format |
|-------------|-------------------|
| Short text snippet displayed | Paragraph (2-4 sentences) |
| Numbered list displayed | Step-by-step list |
| Bulleted list displayed | Unordered list |
| Table displayed | Comparison table |
| Image alongside text | Paragraph + image |

### PAA placement rules

- High-volume PAA questions with complex answers → recommend as H2 sections
- Low-volume PAA questions with simple factual answers → recommend for FAQ section
- PAA questions that align with existing heading recommendations → note as sub-questions within that section

### Competitor analysis detail

For each competitor URL, the brief needs:

1. **Heading structure** — all H1/H2/H3 tags in order (reveals topic coverage and gaps)
2. **Word count** — main content body only (exclude nav/footer/sidebar)
3. **Top ranking keywords** — keywords the page ranks for, ordered by volume (top 10)
4. **Domain Rating** — authority signal for competitive assessment

---

## Calculations

### Recommended Word Count

Do not use default word counts. Calculate from competitor data:

1. Take the word counts from the 3-4 competitor pages analyzed.
2. Calculate the average.
3. Multiply by 1.2 (aim to be 20% more comprehensive).
4. Round to the nearest 100.

If competitor word counts vary wildly (e.g., 800 vs 3,000), note this
and recommend based on the top-performing competitor's length rather
than the average.

**Fallback defaults** (when no competitor data is available):
- Pillar guide: 2,500-4,000 words
- How-to tutorial: 1,500-2,500 words
- Comparison/review: 2,000-3,000 words
- Listicle: 1,500-2,500 words
- News/opinion: 1,000-1,500 words

### Content Type Selection

Determine the right format from SERP signals:

| Signal | Content Type |
|--------|-------------|
| Top results are all long-form guides | Pillar guide |
| "How to" queries dominate | How-to tutorial |
| "Best" / "top" queries, list-style results | Listicle |
| "vs" / comparison queries | Comparison |
| News-style results, recent dates | News/opinion article |
| Mixed results | Match the top-performing format or fill a gap |

See [Content Type Selection](references/content-type-selection.md) for
detailed outline templates per content type.

---

## Recommended Heading Structure

This is the synthesis step — the part that requires judgment, not just
data. Build the recommended H1-H3 structure from:

**1. Competitor heading patterns**
- Identify headings that appear across multiple competitors (shared
  sub-topics that users and Google expect)
- Note headings unique to the top-performing competitor (differentiators
  that may contribute to their ranking)
- Identify topics covered by competitors that the current heading plan
  misses (gaps)

**2. PAA questions**
- High-volume PAA questions → promote to H2 sections
- The question phrasing itself can be used as the heading (matches
  how people search)
- Lower-volume questions → address within relevant sections or in FAQ

**3. Keyword targets**
- Primary keyword in the H1
- Secondary keywords distributed across H2 headings
- Long-tail variations in H3 headings where natural

**4. Search intent flow**
Structure headings to match how a reader moves through the topic:
- Start with the core answer (what they searched for)
- Expand into context and depth
- Address related questions and concerns
- Close with actionable next steps or CTA

**Heading construction rules:**
- H1: One per article. Primary keyword front-loaded. Under 60 chars.
- H2: Major topic sections. 4-8 per article. Use keyword variations
  and PAA questions where natural.
- H3: Sub-sections within an H2. 2-4 per H2 maximum. Use long-tail
  keywords.
- Every heading should pass the scan test: a reader who only reads
  headings should understand the article's full scope.

**Heading density guidelines:**

| Content Length | Minimum H2s | H3s per H2 |
|---------------|-------------|------------|
| Under 1,000 words | 2-3 | 0-1 |
| 1,000-2,000 words | 3-5 | 1-2 |
| 2,000-4,000 words | 5-8 | 1-3 |
| 4,000+ words | 8+ | 2-3 |

---

## Internal Linking Recommendations

If existing site content is available (from `./brand/site-profile.md`
or prior research), identify:

- **Pages to link TO from this article** — existing pages on related
  topics that provide depth on sub-topics mentioned in the article.
- **Pages to link FROM to this article** — existing pages that mention
  the target topic but link out to external sources instead of internal
  content.

For each internal link recommendation:
- The keyword phrase to use as anchor text
- The target URL
- Where in the article the link should appear (which section)

If no existing site content data is available, leave this section as
"Populate after publishing — identify related pages to cross-link."

**Contextual linking rules:**
- Place links within body content where they add value (not just navigation)
- Use descriptive anchor text — never "click here"
- Vary anchor text — don't repeat the same phrase for every link to the same page
- Hub-and-spoke: pillar pages link to cluster pages and vice versa

---

## Content Writing Notes

These notes accompany the brief to guide the writer (human or AI) on
how to use the research effectively.

### Keyword Integration

The goal is to capture primary, long-tail, and semantic keywords
naturally. Well-written and natural is the priority — keyword placement
is secondary.

- Primary keyword in the H1, first paragraph, and at least one H2.
- Long-tail keywords distributed across H2 and H3 headings.
- Semantic keywords woven into body paragraphs naturally. If a semantic
  keyword doesn't fit the flow, skip it.
- Image alt text — use primary or secondary keywords where contextually
  relevant to the image. Don't keyword-stuff decorative images.
- Never force a keyword. If it reads awkwardly, rephrase.

**Mandatory keyword placements (primary keyword):**
1. Title tag — front-loaded when possible
2. H1
3. First 100 words of body content
4. At least one H2
5. URL slug
6. Meta description

**Over-optimization signals to avoid:**

| Signal | What It Looks Like |
|--------|-------------------|
| Keyword stuffing | Same keyword in every heading and every paragraph |
| Unnatural density | Primary keyword appears more than 3% of word count |
| Forced phrasing | Awkward sentence structure to fit exact-match keyword |
| Every heading keyworded | Primary keyword in H1, H2, H3 — too aggressive |

### PAA Question Handling

Answer PAA questions naturally inside the article body. They don't
need to be in question-and-answer format — the answer can be woven
into a paragraph under a relevant heading. Google can extract the
answer from natural prose.

Questions that can't be covered naturally in the main body go into
an FAQ section at the bottom. These can use Q&A format and be marked
up with FAQ schema for rich results.

### Featured Snippet Targeting

| Snippet Format | How to Win It |
|---------------|--------------|
| Paragraph | Answer the query in 40-60 words directly under an H2 that matches the query |
| List (ordered) | Use a numbered list immediately after a "how to" heading |
| List (unordered) | Use bullet points immediately after a "types of" or "best" heading |
| Table | Use a comparison or data table immediately after a relevant heading |

**FAQ section structure:**
- H3 question headings (exact question phrasing)
- Direct answer paragraphs (2-4 sentences, no fluff)
- Schema-ready format that maps directly to JSON-LD

### Schema Selection

| Content Type | Schema to Generate |
|-------------|-------------------|
| Blog / article | `Article` + `FAQPage` (if FAQ section present) |
| How-to tutorial | `Article` + `HowTo` + `FAQPage` |
| Comparison / review | `Article` + `FAQPage` |

Article and FAQ schema are the baseline for every piece — add HowTo
for step-by-step content. See `${CLAUDE_PLUGIN_ROOT}/FILE-SCHEMAS.md`
for the article output format contract.

### The Single Source of Truth Standard

The article should aim to be the best single resource on this topic.
Use the competitor analysis as the benchmark of what to beat — then
layer on top with:
- Additional keyword research coverage
- PAA questions competitors missed
- Deeper analysis or more recent information
- Better structure and readability

### Meta Title

Under 60 characters. Primary keyword front-loaded. The title should
fully describe the page well enough that someone scanning search
results immediately understands what they'll find.

### On-Page Links

Anchor text should be descriptive. "Click here" is never acceptable
in body content. The linked text should explain what the reader will
find at the destination.

### Voice

If `./brand/brand-voice.md` exists, the brief should include a short
voice guidance section referencing the key points: tone, vocabulary
preferences, rhythm, and POV. Apply the Blog/SEO Calibration from the
voice profile.

If no voice profile exists, note: "No brand voice profile found.
Write in a direct, conversational, specific tone."

---

## Quality Checklist

Before delivering a brief, verify:

- [ ] At least 5 primary + long-tail keywords with volume and KD
- [ ] At least 3 question keywords captured
- [ ] PAA questions listed with answer format for each
- [ ] Autocomplete / related searches captured
- [ ] 3-4 competitors analyzed with heading structures
- [ ] Word count calculated from competitor data (not defaulted)
- [ ] Recommended heading structure covers all major sub-topics
- [ ] Heading structure incorporates PAA questions
- [ ] Semantic keyword list included
- [ ] Internal linking section present (even if "populate later")
- [ ] Content writing notes included
- [ ] PAA data captured via ~~SEO data (or ~~browser fallback if unavailable)
- [ ] Screenshots saved if ~~browser was used as fallback
- [ ] Differentiation angle articulated — what makes this article
  worth ranking over what already exists

---

## References

For detailed frameworks, load when needed:

- [Content Type Selection](references/content-type-selection.md) — Decision tree for content types, outline templates per format, when to match vs differentiate from SERP
