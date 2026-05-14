---
description: Surface revenue-ranked SEO opportunities — striking-distance keywords, competitive gaps, topics nobody owns yet, and AI visibility gaps across LLMs.
argument-hint: "<keyword, domain, or topic>"
---

# /find-opportunities

> ~~SEO data is **required**. Hard stop without it. See `${CLAUDE_PLUGIN_ROOT}/CONNECTORS.md`.

## Input

Whatever the user gives — a seed keyword, domain, competitor, topic, or nothing. If nothing, ask.

Ask for **country** if not obvious (needed for accurate volume data).

If the user provides their domain, start with striking-distance keywords (positions 6–20) — these are the fastest wins and should lead the opportunity list.

## Process

1. **Brand context + cached data** — read `./brand/` if it exists. If `site-profile.md` has a `date_fetched` within 7 days, use its domain metrics, top pages, and keyword snapshot instead of re-fetching from ~~SEO data. If `competitors.md` has a `date_fetched` within 14 days, use its competitor data. Only call ~~SEO data domain-level tools for data that's missing or stale. **Read `Average deal size` from `site-profile.md`** — this is the primary input for revenue modeling (see step 4)
2. **Previous opportunities** — read `./campaigns/opportunities.md` if it exists. Collect every keyword that appears in any entry (lead keyword + cluster keywords). These are **dead keywords** — do not surface any opportunity whose lead keyword or cluster keywords overlap with a dead keyword. This is the dedup gate
3. **Research** — the seo-analysis skill has the methodology: seed generation, 6 Circles expansion, SERP analysis, validation, clustering, prioritization. Follow it, but filter everything through four lenses:
   - **Striking distance** — keywords where the site already ranks 6–20. Fastest ROI, action these first
   - **Competitive gaps** — keywords where no result is strong (forums ranking, thin content, outdated pages)
   - **Unowned topics** — high-intent keywords with no clear winner in the SERP
   - **AI visibility** — after clustering, check whether the brand appears in LLM answers for top 3–5 priority clusters. See `skills/seo-analysis/references/opportunity-finding.md` Lens 4. Skip if ~~SEO data provider doesn't support AI optimization
4. **Value each opportunity** — use the deal-value revenue model from `skills/seo-analysis/references/opportunity-finding.md`. Read `Average deal size` from `site-profile.md` if available. If not, infer the business model and use the industry defaults table. Never silently fall back to CPC proxy — it undervalues B2B. Show your math: state the deal value, conversion rate, and CTR assumption for each opportunity so the user can correct them
5. **Identify who owns what** — for each opportunity cluster, name the competitors holding top positions and assess their content strength. Frame opportunities relative to the competitive landscape, not in a vacuum

## Output

### Executive Summary

A narrative paragraph — not a bulleted list. Tell the competitive story:
- Who is pressuring the user's rankings and where
- What patterns you see across competitors (coordinated expansion, content gaps, declining positions)
- The single biggest gap worth acting on immediately and why the window exists
- Total modeled upside across all opportunities

This should read like a strategic briefing, not a data dump.

### Opportunity List

Each opportunity is a cluster of related keywords, framed as a competitive threat or gap. Rank by modeled dollar value, highest first.

For each opportunity:

```
### {Competitor}-framed headline describing the threat or gap
**${modeled value}/mo** · {evidence strength}

**Why now:** {1-2 sentences — what changed, why the window exists, what happens if you wait}

**Gaps to exploit:** {2-3 specific content angles that nobody in the top results covers}

**AI visibility:** {gap | asset | greenfield | not checked} — {brief narrative if checked}

**Action:** {Create new | Optimize existing} · {keyword cluster with volumes}
```

Example:

```
### Gartner dominates low-code automation searches you're missing entirely
**$5,981/mo** · Growing evidence

**Why now:** Search volume for "low-code automation platform" surged 74% in 6 months.
Gartner holds #1 across all variants. Average KD is 2% — this is a low-competition
window closing as more vendors publish.

**Gaps to exploit:**
- Head-to-head comparison with real user ROI vs. Gartner rankings
- Selection checklist mapped to specific use cases (finance ops, HR workflows)
- Migration guide for when your current vendor drops in rankings

**AI visibility:** gap — Gartner and UiPath cited across all four LLMs; you appear in none

**Action:** Create new · low-code automation platform (590/mo), low code automation
platforms (480/mo), low-code automation (370/mo)
```

Ask the user which opportunities to action.

### Save

Append new opportunities to `./campaigns/opportunities.md`. Create the file and directory if needed. Do not overwrite existing entries.

**Entry format** (canonical schema: `${CLAUDE_PLUGIN_ROOT}/FILE-SCHEMAS.md` → Opportunities) — each opportunity is an H2 section using the slug as the heading:

```markdown
## {opportunity-slug}
- **Status:** new
- **Lead keyword:** {keyword} ({volume}/mo)
- **Cluster:** {kw1} ({vol}/mo), {kw2} ({vol}/mo), ...
- **Value:** ${modeled value}/mo
- **Priority:** {DO FIRST | DO SECOND | QUICK WIN | LONG PLAY | BACKLOG}
- **AI visibility:** {gap | asset | greenfield | not checked}
- **Date found:** {YYYY-MM-DD}
- **Brief:**
- **Article:**
```

**Status lifecycle:**

| Status | Set by | Meaning |
|--------|--------|---------|
| `new` | `/find-opportunities` | Surfaced, not yet actioned |
| `skipped` | `/find-opportunities` | User explicitly passed |
| `briefed` | `/create-brief` | Brief created |
| `written` | `/write-content` | Article published |

Commands update status in place — change the `Status:` line, don't duplicate the entry.

**Dedup rule:** before appending, check every existing entry's lead keyword and cluster keywords. If any keyword in the new opportunity already appears in any existing entry, skip it — it's already tracked.

Update `./brand/site-profile.md` and `./brand/competitors.md` with any domain-level data fetched during this run (metrics, keyword snapshot, competitor overlap). Set `date_fetched` to today. Create `./brand/` if needed. Preserve any user-authored sections.

### Report

Generate an HTML opportunity dashboard for this run's findings.

1. Use the reports skill — read its opportunity report reference for the template
2. Save to `./campaigns/{YYYY-MM-DD}/daily-opportunities.html`
3. Create the date folder if it doesn't exist
4. The report renders the same data just saved to `opportunities.md` — the executive summary, opportunity cards, keyword clusters, and metrics

## Next

Point the user to `/create-brief` for whichever opportunity they want to action.
