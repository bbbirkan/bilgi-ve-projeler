---
description: Compile keyword research, competitor analysis, and heading structure into a content brief for a target keyword.
argument-hint: "<keyword or opportunity from /find-opportunities>"
---

# /create-brief

> ~~SEO data is **required** for full briefs. See `${CLAUDE_PLUGIN_ROOT}/CONNECTORS.md`.

## Input

A keyword or an SEO opportunity the user picked from. If no input, check `./campaigns/opportunities.md` and offer the top 3 highest priority unbriefed ones.

## Process

1. **Brand context + cached data** — read `./brand/` if it exists. Competitor metrics and keyword overlap from `competitors.md` can replace ~~SEO data calls if `date_fetched` is within 14 days. Domain data from `site-profile.md` is fresh within 7 days
2. **Resolve target** — figure out the primary keyword from the input. If the user gave an opportunity by name or slug, look it up in `./campaigns/opportunities.md`. The slug is the H2 heading of each entry
3. **Existing brief check** — look up the opportunity's `**Brief:**` field in `./campaigns/opportunities.md`. If a path exists and the file is there, show a summary and offer: **Update** or **Rebuild**
4. **Build the brief** — the brief-building skill defines every section, data requirement, and quality standard. Follow it. Use cached data from `./brand/` wherever fresh enough — only call ~~SEO data for keyword-specific data not already saved
5. **Save** — generate an HTML content brief report:
   - Use the reports skill — read its brief report reference for the template
   - Save to `./campaigns/{YYYY-MM-DD}/{opportunity-slug}-brief.html`
   - Create the date folder if it doesn't exist
   - In `./campaigns/opportunities.md`, update the entry:
     - Change `**Status:**` from `new` to `briefed`
     - Set `**Brief:**` to the file path

## Next

Point the user to `/write-content` to produce the article from this brief.