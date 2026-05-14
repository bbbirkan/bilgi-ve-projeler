---
name: reports
description: >
  Render SEO research data as self-contained HTML reports. Two report
  types: opportunity dashboards and content briefs. Use when generating
  an HTML report from SEO data, rendering opportunity findings, or
  producing a visual content brief. Do NOT use for article writing or
  general frontend work.
---

# Reports

Render SEO data as single-file HTML reports. Two report types exist —
opportunity dashboards and content briefs. Each has a working HTML
reference file that defines the exact design system, layout, components,
and visual language.

---

## Opportunity Dashboard

Read `references/opportunity-report.html` for the template.

This report renders the output of a `/find-opportunities` run. The
reference file shows the complete structure:

- Header with brand name and date
- Executive summary card with narrative paragraph and metric row
  (total value, top opportunity, avg KD, opportunity count)
- Collapsible opportunity cards ranked by value — each card has a
  priority badge, competitor-framed headline, value pill, "why now"
  text, tags, and an expandable section with SERP assessment, action
  plan, and keyword cluster table with KD indicators

Match the reference file's design system exactly — colors, typography,
spacing, component patterns, layout. Populate with real data from the
research just completed.

---

## Content Brief

Read `references/brief-report.html` for the template.

This report renders the output of a brief-building run. The reference
file shows the complete structure:

- Header with primary keyword as the title, metadata row
- Metrics row (target word count, lead volume, avg KD, competitors)
- Keyword tables (primary with intent badges, long-tail)
- Question keywords table and People Also Ask table with format badges
- Autocomplete tag cloud with highlight variants
- Collapsible competitor cards (heading tree, word count bar chart,
  gap analysis)
- Recommended heading structure tree with color-coded H-tags
- Semantic keyword cloud
- Internal linking table
- Writing notes card (voice, differentiation, meta title, snippet
  targets, schema guidance, content hub strategy)

Match the reference file's design system exactly. Populate with real
data from the brief research just completed.

---

## How to Use the Reference Files

1. Read the reference HTML file for the report type being generated
2. Match the design system — CSS variables, font stack, spacing, component
   patterns, layout structure
3. Populate every element with real data from the research
4. Do not deviate from the visual language in the reference files

The reference file IS the spec.

---

## Data Integrity

Every number, keyword, headline, and paragraph in the report must come
directly from the research data. Never invent, interpolate, or estimate
any data point. The report is a rendering of what was found, not a
reinterpretation.

---

## Implementation

- Single self-contained `.html` file
- All CSS in `<style>` in `<head>`
- Interactivity (collapsible cards, toggles) in `<script>` at bottom
- Only external dependency: Google Fonts `<link>`
- Responsive: works from 600px to 1400px
- Print-friendly: `@media print` block that expands all collapsed
  sections and uses clean black-on-white
