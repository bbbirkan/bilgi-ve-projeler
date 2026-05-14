---
description: Write a publication-ready SEO article from a content brief with human voice and schema markup.
argument-hint: "[brief path or keyword]"
---

# /write-content

## Input

- A brief path, a keyword, or nothing
- If nothing: auto-detect the top briefed-but-unwritten opportunity in `./campaigns/`
- If no briefs exist: tell the user to run `/create-brief` first, or give a keyword

## Process

1. **Brand context** — read `./brand/` if it exists. If `brand-voice.md` is found, write in that voice. If not, default to: direct, conversational, specific, opinionated
2. **Load brief** — look up the opportunity's `**Brief:**` field in `./campaigns/opportunities.md` to find the brief path. Read the HTML file but **skip the `<head>` section entirely** — it's only CSS, fonts, and JavaScript. Jump straight to the `<body>` tag and extract data from there. The body contains keyword tables, heading structure, competitor analysis, and writing notes as semantic HTML. Extract: keywords, headings, word count target, competitors, PAA questions, semantic keywords, internal links, writing notes
3. **Existing article check** — look up the opportunity's `**Article:**` field in `./campaigns/opportunities.md`. If a path exists and the file is there, offer: **Refresh**, **Rewrite**, or **Expand**
4. **SERP check** — if the brief's date is less than 14 days old, use its competitor analysis and SERP data as-is (skip the ~~SEO data call). If the brief is older than 14 days, do a quick SERP check via ~~SEO data to verify the SERP hasn't shifted. Flag significant changes to the user
5. **Write** — follow the brief's structure. The humanizer skill defines voice standards — every article must pass its detection checklist. The brief's Content Writing Notes section defines keyword placement, snippet targeting, and schema requirements. Before saving, run the pre-save check:
   - H1 contains primary keyword, under 60 chars, differs from title tag
   - Primary keyword in first 100 words and at least one H2
   - Heading density meets the brief's guidelines for the target word count
   - No orphan H3s (every H3 has a parent H2)
   - Internal links included (or marked "populate after publishing")
   - Anchor text is descriptive (never "click here")
   - Featured snippet opportunity addressed if identified in brief
   - FAQ section has schema-ready structure (if applicable)
   - JSON-LD schema in frontmatter (see FILE-SCHEMAS.md for format)
   - Meta description 150-160 chars with primary keyword
   - No over-optimization signals (density, stuffing, forced phrasing)
6. **Quality gate** — use a Task tool subagent to independently review the article against the brief. Check: content completeness, humanization, SEO, and E-E-A-T. Fix issues before saving
7. **Save** — write to `./campaigns/{YYYY-MM-DD}/{opportunity-slug}-article.md` with YAML frontmatter per `${CLAUDE_PLUGIN_ROOT}/FILE-SCHEMAS.md` → Article schema. Create the date folder if it doesn't exist. In `./campaigns/opportunities.md`, update the entry:
   - Change `**Status:**` from `briefed` to `written`
   - Set `**Article:**` to the file path