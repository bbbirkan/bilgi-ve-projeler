---
name: zen-office-docx
description: Create professional Word documents (.docx) from JSON descriptors via the zenskill CLI. Triggers when the user asks to create, generate, or write a Word document, .docx file, report, proposal, letter, memo, invoice, contract, resume, or any formatted document.
---

# Word Documents (.docx)

Create Word documents (.docx) from a JSON descriptor via the `zenskill` CLI.

## When to Use

- User asks to create, generate, or write a Word document
- User mentions .docx, Word, report, proposal, letter, memo, contract, resume, invoice, or any formatted document
- User wants a professional document with headings, tables, lists, images, or custom formatting
- You need to produce a downloadable/shareable document (not just markdown)

## Quick Start

```bash
# 1. Write a JSON descriptor to a temp file
cat > /tmp/descriptor.json << 'ENDJSON'
{
  "sections": [{
    "children": [
      { "text": "Quarterly Report", "heading": "HEADING_1" },
      { "text": "This report summarizes Q1 performance metrics." },
      {
        "type": "table",
        "rows": [
          { "cells": [{ "text": "Metric", "bold": true, "shading": "DBEAFE" }, { "text": "Value", "bold": true, "shading": "DBEAFE" }], "tableHeader": true },
          { "cells": [{ "text": "Revenue" }, { "text": "$1.2M" }] },
          { "cells": [{ "text": "Growth" }, { "text": "15%" }] }
        ]
      }
    ]
  }]
}
ENDJSON

# 2. Generate the .docx file
zenskill office document create --input /tmp/descriptor.json --output /tmp/report.docx
```

## Command

```
zenskill office document create --input <json> --output <path>
```

| Flag | Required | Description |
|------|----------|-------------|
| `--input` | Yes | Path to the JSON descriptor file |
| `--output` | Yes | Path for the generated .docx file (parent dirs created automatically) |

The command reads the JSON descriptor, builds the file, writes the output, and returns a JSON envelope with the output path.

## Descriptor Format

The descriptor is a JSON object with this top-level structure:

```json
{
  "sections": [ ... ],
  "styles": { ... },
  "numbering": [ ... ]
}
```

Only `sections` is required. Each section contains an array of `children` elements.

### Sections

```json
{
  "sections": [{
    "properties": {
      "page": {
        "size": { "width": 12240, "height": 15840, "orientation": "portrait" },
        "margin": { "top": 1440, "right": 1440, "bottom": 1440, "left": 1440 }
      }
    },
    "headers": { "default": [{ "text": "Company Name", "alignment": "right", "size": 18, "color": "94A3B8" }] },
    "footers": { "default": [{ "text": "Confidential", "alignment": "center", "size": 16, "color": "94A3B8" }] },
    "children": [ ... ]
  }]
}
```

Headers and footers contain arrays of paragraph objects.

### Document Elements

The `children` array accepts four element types: paragraphs, tables, images, and page breaks.

#### Paragraphs

The default element type. Use `text` for simple content or `runs` for mixed formatting.

**Simple paragraph:**
```json
{ "text": "Hello world" }
```

**With heading:**
```json
{ "text": "Chapter 1: Introduction", "heading": "HEADING_1" }
```

Heading values: `TITLE`, `HEADING_1`, `HEADING_2`, `HEADING_3`, `HEADING_4`, `HEADING_5`, `HEADING_6`.

**With formatting (shorthand):**
```json
{ "text": "Important notice", "bold": true, "italic": true, "size": 28, "color": "DC2626", "font": "Georgia" }
```

**With alignment and spacing:**
```json
{
  "text": "Centered paragraph with spacing",
  "alignment": "center",
  "spacing": { "before": 240, "after": 240, "line": 360 },
  "indent": { "left": 720, "firstLine": 360 }
}
```

Alignment values: `left`, `center`, `right`, `justified`.

**Rich text with multiple runs:**
```json
{
  "runs": [
    { "text": "This is " },
    { "text": "bold", "bold": true },
    { "text": " and " },
    { "text": "red italic", "italic": true, "color": "EF4444" },
    { "text": "." }
  ]
}
```

**Page break before paragraph:**
```json
{ "text": "This starts on a new page", "heading": "HEADING_1", "pageBreakBefore": true }
```

#### Text Run Properties

| Property | Type | Description |
|----------|------|-------------|
| `text` | string | The text content (required) |
| `bold` | boolean | Bold formatting |
| `italic` | boolean | Italic formatting |
| `underline` | boolean | Underline formatting |
| `strike` | boolean | Strikethrough |
| `size` | number | Font size in half-points (24 = 12pt) |
| `color` | string | Text color as 6-char hex without `#` (e.g., `FF0000`) |
| `font` | string | Font family name (e.g., `Arial`) |
| `highlight` | string | Highlight color name |
| `superScript` | boolean | Superscript |
| `subScript` | boolean | Subscript |
| `allCaps` | boolean | All capitals |
| `smallCaps` | boolean | Small capitals |

#### Bullet Lists

```json
{ "text": "First bullet item", "bullet": { "level": 0 } },
{ "text": "Nested bullet", "bullet": { "level": 1 } },
{ "text": "Second bullet item", "bullet": { "level": 0 } }
```

#### Numbered Lists

Numbered lists require a `numbering` config at the top level and a `reference` on each paragraph.

```json
{
  "numbering": [{
    "reference": "my-numbers",
    "levels": [
      { "level": 0, "format": "DECIMAL", "text": "%1.", "alignment": "left" },
      { "level": 1, "format": "LOWER_LETTER", "text": "%2)", "alignment": "left" }
    ]
  }],
  "sections": [{
    "children": [
      { "text": "First item", "numbering": { "reference": "my-numbers", "level": 0 } },
      { "text": "Sub-item a", "numbering": { "reference": "my-numbers", "level": 1 } },
      { "text": "Second item", "numbering": { "reference": "my-numbers", "level": 0 } }
    ]
  }]
}
```

Format values: `DECIMAL`, `UPPER_ROMAN`, `LOWER_ROMAN`, `UPPER_LETTER`, `LOWER_LETTER`, `BULLET`.

#### Tables

```json
{
  "type": "table",
  "width": 9360,
  "widthType": "DXA",
  "borders": true,
  "rows": [
    {
      "tableHeader": true,
      "cells": [
        { "text": "Name", "bold": true, "shading": "DBEAFE", "width": 4680, "widthType": "DXA" },
        { "text": "Role", "bold": true, "shading": "DBEAFE", "width": 4680, "widthType": "DXA" }
      ]
    },
    {
      "cells": [
        { "text": "Alice", "width": 4680, "widthType": "DXA" },
        { "text": "Engineer", "width": 4680, "widthType": "DXA" }
      ]
    }
  ]
}
```

**Cell properties:**

| Property | Type | Description |
|----------|------|-------------|
| `text` | string | Simple text content |
| `paragraphs` | array | Rich content (array of paragraph objects) |
| `bold` | boolean | Bold text (shorthand, applies when using `text`) |
| `shading` | string | Background fill color (6-char hex, no `#`) |
| `width` | number | Cell width in DXA |
| `widthType` | string | Width unit: `DXA`, `PCT`, or `AUTO` |
| `verticalAlign` | string | Vertical alignment: `top`, `center`, `bottom` |
| `columnSpan` | number | Number of columns to span |
| `rowSpan` | number | Number of rows to span |
| `borders` | object | Per-cell border overrides (`top`, `bottom`, `left`, `right`) |

**Border definition:**
```json
{ "style": "SINGLE", "size": 1, "color": "000000" }
```

Border styles: `SINGLE`, `DOUBLE`, `DASHED`, `DOTTED`, `THICK`, `NONE`.

#### Images

From a file path:
```json
{ "type": "image", "path": "/absolute/path/to/image.png", "width": 300, "height": 200, "altText": "Company logo" }
```

From base64 data:
```json
{ "type": "image", "base64": "iVBORw0KGgo...", "width": 300, "height": 200, "imageType": "png" }
```

Image dimensions are in **pixels**. Supported types: `png`, `jpg`, `gif`, `bmp`.

#### Page Breaks

```json
{ "type": "page-break" }
```

### Document Styles

Set default font, size, and color for the entire document:

```json
{
  "styles": {
    "default": {
      "document": {
        "run": {
          "font": "Arial",
          "size": 24,
          "color": "334155"
        }
      }
    }
  }
}
```

## Page Layout

### Common Page Sizes

| Paper | Width (DXA) | Height (DXA) | Content Width (1" margins) |
|-------|-------------|--------------|---------------------------|
| US Letter | 12240 | 15840 | 9360 |
| A4 | 11906 | 16838 | 9026 |

### Landscape Orientation

```json
{
  "properties": {
    "page": {
      "size": { "width": 15840, "height": 12240, "orientation": "landscape" },
      "margin": { "top": 1440, "right": 1440, "bottom": 1440, "left": 1440 }
    }
  }
}
```

### Common Margins

| Margin | DXA Value |
|--------|-----------|
| 1 inch (standard) | 1440 |
| 0.75 inch (narrow) | 1080 |
| 0.5 inch (tight) | 720 |

## Units Reference

| Unit | Conversion |
|------|-----------|
| DXA (twips) | 1440 DXA = 1 inch = 2.54 cm |
| Font size | Half-points: 24 = 12pt, 20 = 10pt, 28 = 14pt, 32 = 16pt, 48 = 24pt |
| Image dimensions | Pixels |
| Spacing/indent | DXA (240 DXA ~ 1/6 inch) |

## Critical Rules

1. **Always write JSON to a temp file first** -- do NOT pass JSON inline to the command. Write the descriptor to a file, then reference it with `--input`.
2. **Use straight quotes in JSON** -- never use smart/curly quotes. Standard JSON double quotes only.
3. **Image paths must be absolute** -- or relative to the working directory where the command runs.
4. **Table cell widths must sum to content width** -- for US Letter with 1-inch margins, the content width is 9360 DXA. Cell widths in each row must sum to the table width.
5. **Color values are 6-character hex WITHOUT the `#` prefix** -- use `FF0000` not `#FF0000`.
6. **Font sizes are in half-points** -- 24 = 12pt, not 24pt.
7. **One section is usually sufficient** -- use multiple sections only when you need different page layouts (e.g., portrait then landscape).
8. **Prefer `DXA` for table widths** -- it gives the most predictable results across Word and Google Docs.

## Complete Examples

### Professional Report

```json
{
  "styles": {
    "default": { "document": { "run": { "font": "Arial", "size": 22, "color": "334155" } } }
  },
  "sections": [{
    "properties": {
      "page": {
        "size": { "width": 12240, "height": 15840 },
        "margin": { "top": 1440, "right": 1440, "bottom": 1440, "left": 1440 }
      }
    },
    "headers": { "default": [{ "text": "Acme Corp", "alignment": "right", "size": 18, "color": "94A3B8" }] },
    "footers": { "default": [{ "text": "Confidential", "alignment": "center", "size": 16, "color": "94A3B8" }] },
    "children": [
      { "text": "Q1 2025 Performance Report", "heading": "TITLE", "alignment": "center" },
      { "text": "Prepared by the Analytics Team", "alignment": "center", "size": 20, "color": "64748B", "spacing": { "after": 480 } },
      { "text": "Executive Summary", "heading": "HEADING_1" },
      { "text": "Revenue grew 15% year-over-year, exceeding our target of 12%. Key drivers include expansion into the European market and the launch of our premium tier." },
      { "text": "Key Metrics", "heading": "HEADING_1", "pageBreakBefore": true },
      {
        "type": "table",
        "width": 9360,
        "widthType": "DXA",
        "borders": true,
        "rows": [
          {
            "tableHeader": true,
            "cells": [
              { "text": "Metric", "bold": true, "shading": "2563EB", "width": 3120, "widthType": "DXA" },
              { "text": "Q1 Actual", "bold": true, "shading": "2563EB", "width": 3120, "widthType": "DXA" },
              { "text": "Q1 Target", "bold": true, "shading": "2563EB", "width": 3120, "widthType": "DXA" }
            ]
          },
          {
            "cells": [
              { "text": "Revenue", "width": 3120, "widthType": "DXA" },
              { "text": "$1.2M", "width": 3120, "widthType": "DXA" },
              { "text": "$1.1M", "width": 3120, "widthType": "DXA" }
            ]
          },
          {
            "cells": [
              { "text": "New Customers", "width": 3120, "widthType": "DXA" },
              { "text": "340", "width": 3120, "widthType": "DXA" },
              { "text": "300", "width": 3120, "widthType": "DXA" }
            ]
          }
        ]
      },
      { "text": "Next Steps", "heading": "HEADING_1" },
      { "text": "Expand sales team in EMEA region", "bullet": { "level": 0 } },
      { "text": "Launch premium tier marketing campaign", "bullet": { "level": 0 } },
      { "text": "Target 20% growth in Q2", "bullet": { "level": 0 } }
    ]
  }]
}
```

### Business Letter

```json
{
  "styles": {
    "default": { "document": { "run": { "font": "Times New Roman", "size": 24 } } }
  },
  "sections": [{
    "properties": {
      "page": {
        "size": { "width": 12240, "height": 15840 },
        "margin": { "top": 1440, "right": 1440, "bottom": 1440, "left": 1440 }
      }
    },
    "children": [
      { "text": "Acme Corporation", "bold": true, "size": 28 },
      { "text": "123 Business Ave, Suite 100", "size": 20, "color": "64748B" },
      { "text": "San Francisco, CA 94102", "size": 20, "color": "64748B", "spacing": { "after": 480 } },
      { "text": "March 30, 2025", "spacing": { "after": 480 } },
      { "text": "Dear Ms. Johnson,", "spacing": { "after": 240 } },
      { "text": "Thank you for your interest in our services. We are pleased to present our proposal for the upcoming project. Our team has extensive experience in delivering high-quality solutions that meet our clients' needs." },
      { "text": "We look forward to the opportunity to work with your organization. Please do not hesitate to reach out if you have any questions.", "spacing": { "after": 240 } },
      { "text": "Sincerely,", "spacing": { "before": 480 } },
      { "text": "John Smith", "spacing": { "before": 480 }, "bold": true },
      { "text": "Vice President, Sales" }
    ]
  }]
}
```

### Table-Heavy Document

```json
{
  "styles": {
    "default": { "document": { "run": { "font": "Calibri", "size": 20 } } }
  },
  "sections": [{
    "properties": {
      "page": {
        "size": { "width": 15840, "height": 12240, "orientation": "landscape" },
        "margin": { "top": 720, "right": 720, "bottom": 720, "left": 720 }
      }
    },
    "children": [
      { "text": "Project Timeline", "heading": "HEADING_1" },
      {
        "type": "table",
        "width": 14400,
        "widthType": "DXA",
        "borders": true,
        "rows": [
          {
            "tableHeader": true,
            "cells": [
              { "text": "Phase", "bold": true, "shading": "1E293B", "width": 3600, "widthType": "DXA" },
              { "text": "Task", "bold": true, "shading": "1E293B", "width": 4800, "widthType": "DXA" },
              { "text": "Owner", "bold": true, "shading": "1E293B", "width": 3000, "widthType": "DXA" },
              { "text": "Status", "bold": true, "shading": "1E293B", "width": 3000, "widthType": "DXA" }
            ]
          },
          {
            "cells": [
              { "text": "Planning", "width": 3600, "widthType": "DXA", "rowSpan": 2 },
              { "text": "Requirements gathering", "width": 4800, "widthType": "DXA" },
              { "text": "Alice", "width": 3000, "widthType": "DXA" },
              { "text": "Complete", "width": 3000, "widthType": "DXA", "shading": "DCFCE7" }
            ]
          },
          {
            "cells": [
              { "text": "Architecture review", "width": 4800, "widthType": "DXA" },
              { "text": "Bob", "width": 3000, "widthType": "DXA" },
              { "text": "In Progress", "width": 3000, "widthType": "DXA", "shading": "FEF9C3" }
            ]
          },
          {
            "cells": [
              { "text": "Development", "width": 3600, "widthType": "DXA" },
              { "text": "Core implementation", "width": 4800, "widthType": "DXA" },
              { "text": "Team", "width": 3000, "widthType": "DXA" },
              { "text": "Not Started", "width": 3000, "widthType": "DXA", "shading": "FEE2E2" }
            ]
          }
        ]
      }
    ]
  }]
}
```

### Tips

- For simple documents, omit `properties`, `styles`, and `numbering` -- defaults work well
- Use `pageBreakBefore: true` on headings to start new chapters/sections on a fresh page
- Mark the first table row with `"tableHeader": true` so it repeats on subsequent pages when the table spans multiple pages
- For rich cell content (multiple paragraphs, mixed formatting), use `paragraphs` instead of `text` in table cells
- When the user does not specify a font, use `Arial` (universally supported) as the default
- When the user does not specify page size, use US Letter (12240 x 15840 DXA)
