# File Schemas

Output file format contracts for the SEO plugin. Commands and skills
reference these schemas to produce consistent, machine-readable output.

HTML reports are excluded — their format is defined by the reports
skill's reference HTML files, which ARE the schema.

---

## Site Profile (`./brand/site-profile.md`)

Central cache for domain-level data. Downstream commands read this before
making API calls — the more complete it is, the fewer redundant fetches.

### Frontmatter (blockquote line)

```
> date_fetched: {YYYY-MM-DD}
```

### Required Sections

| Section | Contents | Written by | Freshness |
|---------|----------|-----------|-----------|
| Domain | URL, average deal size | `/start-here` (user input) | Permanent |
| Company Overview | 2-3 sentence summary from homepage/about | `/start-here` (scraped) | Permanent |
| Domain Metrics | DR, organic traffic, organic keywords, organic traffic cost | `/start-here` or `/find-opportunities` (~~SEO data) | 7 days |
| Content Inventory | All URLs categorized by section (blog, services, landing, other) | `/start-here` (Firecrawl map) | Permanent |
| Top Pages | 20-50 pages by organic traffic: URL, traffic, top keyword, position | `/start-here` or `/find-opportunities` (~~SEO data) | 7 days |
| Striking Distance Keywords | Positions 6-20, volume ≥100: keyword, volume, position, traffic, KD | `/start-here` or `/find-opportunities` (~~SEO data) | 7 days |
| Top Keywords | 50 keywords by traffic: keyword, volume, position, traffic, KD | `/start-here` or `/find-opportunities` (~~SEO data) | 7 days |
| Notes | Notable observations (JS-rendered, subdomain blog, etc.) | `/start-here` | Permanent |

### Update Rules

- Only update data sections (Domain Metrics, Top Pages, Striking Distance, Top Keywords)
- Never overwrite user-authored sections (Domain, Company Overview, Notes)
- Set `date_fetched` to today after any update
- Sections without data use placeholder: `{Not yet fetched — will be populated on first /find-opportunities run}`

---

## Competitors (`./brand/competitors.md`)

Known competitors with positioning summaries. Keyword overlap data is
added by `/find-opportunities` when the user runs research.

### Frontmatter (blockquote line)

```
> date_fetched: {YYYY-MM-DD}
```

### Per-Competitor Entry (H2 per competitor)

| Field | Contents | Written by |
|-------|----------|-----------|
| URL | Competitor domain | `/start-here` (user input) |
| Overview | 1-2 sentence positioning summary | `/start-here` (scraped from homepage) |
| DR | Domain Rating | `/find-opportunities` (~~SEO data) |
| Common Keywords | Count of overlapping keywords | `/find-opportunities` (~~SEO data) |
| Competitor Traffic | Monthly organic traffic | `/find-opportunities` (~~SEO data) |
| Top Overlapping Keywords | Table: keyword, volume, your position, their position (top 10) | `/find-opportunities` (~~SEO data) |

### Update Rules

- `/start-here` creates entries with URL and Overview only
- `/find-opportunities` adds SEO metrics and keyword overlap
- Set `date_fetched` to today after any update
- Never remove a competitor the user added — only append data

---

## Opportunities (`./campaigns/opportunities.md`)

Append-only log of every opportunity surfaced. Each entry is an H2 section.
Commands update entries in place (status, brief path, article path) but
never delete or reorder them.

### Entry Format

| Field | Format | Set by |
|-------|--------|--------|
| `**Status:**` | `new` / `skipped` / `briefed` / `written` | All commands |
| `**Lead keyword:**` | `{keyword} ({volume}/mo)` | `/find-opportunities` |
| `**Cluster:**` | `{kw1} ({vol}/mo), {kw2} ({vol}/mo), ...` | `/find-opportunities` |
| `**Value:**` | `${modeled value}/mo` | `/find-opportunities` |
| `**Priority:**` | `DO FIRST` / `DO SECOND` / `QUICK WIN` / `LONG PLAY` / `BACKLOG` | `/find-opportunities` |
| `**AI visibility:**` | `gap` / `asset` / `greenfield` / `not checked` | `/find-opportunities` |
| `**Date found:**` | `YYYY-MM-DD` | `/find-opportunities` |
| `**Brief:**` | File path or empty | `/create-brief` |
| `**Article:**` | File path or empty | `/write-content` |

### Status Lifecycle

`new` → `briefed` → `written`
`new` → `skipped` (user explicitly passed)

### Dedup Rule

Before appending, check every existing entry's lead keyword and cluster
keywords (case-insensitive, trimmed). If any keyword in the new
opportunity already appears in any existing entry, skip it.

---

## Article (`./campaigns/{YYYY-MM-DD}/{slug}-article.md`)

Publication-ready article with YAML frontmatter and JSON-LD schema.

### Frontmatter

```yaml
---
title: ""
meta_description: ""
primary_keyword: ""
word_count:
date_created: ""
status: "draft"
schema: |
  {JSON-LD}
---
```

### Field Rules

| Field | Constraint |
|-------|-----------|
| `title` | Under 60 characters. Primary keyword front-loaded. Must differ from the H1 in the body. |
| `meta_description` | 150-160 characters. Summarizes the page's value proposition. Primary keyword included naturally. |
| `primary_keyword` | The main keyword target from the brief. |
| `word_count` | Actual word count of the body content (exclude frontmatter). |
| `date_created` | ISO 8601 date (YYYY-MM-DD). |
| `status` | One of: `draft`, `review`, `published`, `needs-refresh`. |
| `schema` | Valid JSON-LD. Article + FAQPage at minimum. Add HowTo for step-by-step content. Must match the body content structure. |

---

## Brand Voice (`./brand/brand-voice.md`)

Voice profile used by all content-producing commands. Built on the "voice
constant, tone flexes" model — voice is WHO the brand is (constant), tone
is HOW it speaks in a given context (flexes). Structure is defined by the
brand-voice skill — see `skills/brand-voice/SKILL.md` for the full
template and section definitions.

### Sections (for downstream consumers)

Downstream commands reading this file can expect these sections:
- **Voice Summary** — 2-3 sentence voice description
- **We Are / We Are Not** — identity anchor table (4-7 paired attributes defining brand personality and boundaries)
- **Tone Spectrum** — five dimension scores (formal↔casual, serious↔playful, reserved↔bold, simple↔sophisticated, warm↔direct)
- **Tone-by-Context Matrix** — how tone flexes (Formality, Energy, Technical Depth) per content type (blog, email, LinkedIn, Twitter/X, landing page)
- **Vocabulary** — preferred terms, avoided terms, jargon level
- **Rhythm & Structure** — sentence length patterns, paragraph structure, openings, formatting
- **POV & Address** — person, stance, reader address
- **Blog/SEO Calibration** — how the voice adapts specifically for long-form search content
- **Example Phrases** — on-brand and off-brand samples annotated with which voice attributes and boundaries apply
- **Do's and Don'ts** — quick reference guardrails
- **Confidence Notes** — which sections have strong evidence vs. inferred or assumed data
