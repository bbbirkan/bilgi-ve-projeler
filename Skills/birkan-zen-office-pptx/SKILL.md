---
name: zen-office-pptx
description: Create professional PowerPoint presentations (.pptx) from JSON descriptors via the zenskill CLI. Triggers when the user asks to create, generate, or write a presentation, slide deck, pitch deck, or mentions .pptx, PowerPoint, slides, or keynote.
---

# Presentations (.pptx)

Create PowerPoint presentations (.pptx) from a JSON descriptor via the `zenskill` CLI.

## When to Use

- User asks to create, generate, or write a presentation, slide deck, or pitch deck
- User mentions .pptx, PowerPoint, slides, presentation, keynote, or deck
- You need to produce a downloadable/shareable presentation (not just markdown)

## Quick Start

```bash
# 1. Write a JSON descriptor to a temp file
cat > /tmp/descriptor.json << 'ENDJSON'
{
  "layout": "LAYOUT_WIDE",
  "slides": [
    {
      "background": { "color": "0F172A" },
      "elements": [
        { "type": "text", "options": { "x": 1, "y": 2.5, "w": 11, "h": 1.5, "text": "My Presentation", "fontSize": 40, "fontFace": "Arial", "color": "FFFFFF", "bold": true, "align": "center" } }
      ]
    }
  ]
}
ENDJSON

# 2. Generate the .pptx file
zenskill office presentation create --input /tmp/descriptor.json --output /tmp/deck.pptx
```

## Command

```
zenskill office presentation create --input <json> --output <path>
```

| Flag | Required | Description |
|------|----------|-------------|
| `--input` | Yes | Path to the JSON descriptor file |
| `--output` | Yes | Path for the generated .pptx file (parent dirs created automatically) |

The command reads the JSON descriptor, builds the file, writes the output, and returns a JSON envelope with the output path.

## Descriptor Format

The descriptor is a JSON object with this top-level structure:

```json
{
  "layout": "LAYOUT_WIDE",
  "author": "Author Name",
  "title": "Presentation Title",
  "subject": "Subject",
  "masters": [ ... ],
  "slides": [ ... ]
}
```

Only `slides` is required. Each slide contains an array of `elements`.

### Slide Layouts

| Layout | Width | Height | Aspect |
|--------|-------|--------|--------|
| `LAYOUT_WIDE` (default) | 13.33" | 7.5" | 16:9 |
| `LAYOUT_16x10` | 10" | 6.25" | 16:10 |
| `LAYOUT_4x3` | 10" | 7.5" | 4:3 |

### Slides

```json
{
  "slides": [{
    "background": { "color": "FFFFFF" },
    "masterName": "MY_MASTER",
    "elements": [ ... ],
    "notes": "Speaker notes for this slide",
    "slideNumber": { "x": "90%", "y": "95%", "fontSize": 10, "color": "94A3B8" }
  }]
}
```

### Slide Element Types

Each element has a `type` and an `options` object with positioning (`x`, `y`, `w`, `h` in inches).

#### Text

Simple text:
```json
{
  "type": "text",
  "options": {
    "x": 0.5, "y": 0.5, "w": 8, "h": 1,
    "text": "Hello World",
    "fontSize": 24, "fontFace": "Arial",
    "color": "334155", "bold": true,
    "align": "center", "valign": "middle"
  }
}
```

Multi-run rich text (use `items` for mixed formatting within one text box):
```json
{
  "type": "text",
  "options": { "x": 0.5, "y": 2, "w": 8, "h": 1, "isTextBox": true },
  "items": [
    { "text": "This is ", "fontSize": 18 },
    { "text": "bold", "bold": true, "fontSize": 18 },
    { "text": " and ", "fontSize": 18 },
    { "text": "red", "color": "EF4444", "fontSize": 18 }
  ]
}
```

**Text item properties:**

| Property | Type | Description |
|----------|------|-------------|
| `text` | string | Text content (required) |
| `fontSize` | number | Font size in points |
| `fontFace` | string | Font family name |
| `color` | string | Text color (6-char hex, no `#`) |
| `bold` | boolean | Bold |
| `italic` | boolean | Italic |
| `underline` | boolean | Underline |
| `strike` | boolean | Strikethrough |
| `breakLine` | boolean | Line break before this run |
| `bullet` | boolean/object | Enable bullets |
| `hyperlink` | object | `{ "url": "https://...", "tooltip": "..." }` |
| `subscript` | boolean | Subscript |
| `superscript` | boolean | Superscript |
| `align` | string | `left`, `center`, `right` |

#### Shape

```json
{
  "type": "shape",
  "options": {
    "x": 1, "y": 1, "w": 4, "h": 2,
    "type": "RECT",
    "fill": { "color": "3B82F6" },
    "line": { "color": "1D4ED8", "width": 2 },
    "rectRadius": 0.2,
    "shadow": { "type": "outer", "color": "000000", "blur": 6, "offset": 3, "angle": 45, "opacity": 0.4 }
  }
}
```

Shape types: `RECT`, `ROUNDRECT`, `OVAL`, `LINE`.

#### Image

From file path:
```json
{
  "type": "image",
  "options": { "x": 1, "y": 1, "w": 4, "h": 3, "path": "/path/to/image.png", "altText": "Photo" }
}
```

From base64:
```json
{
  "type": "image",
  "options": { "x": 1, "y": 1, "w": 4, "h": 3, "base64": "data:image/png;base64,iVBOR...", "altText": "Logo" }
}
```

#### Table

```json
{
  "type": "table",
  "options": {},
  "tableOptions": {
    "x": 0.5, "y": 1.5, "w": 9, "h": 3,
    "border": { "pt": 1, "color": "E2E8F0" },
    "colW": [3, 3, 3],
    "fontSize": 12, "fontFace": "Arial"
  },
  "rows": [
    [
      { "text": "Name", "bold": true, "fill": { "color": "3B82F6" }, "color": "FFFFFF" },
      { "text": "Role", "bold": true, "fill": { "color": "3B82F6" }, "color": "FFFFFF" },
      { "text": "Status", "bold": true, "fill": { "color": "3B82F6" }, "color": "FFFFFF" }
    ],
    [
      { "text": "Alice" },
      { "text": "Engineer" },
      { "text": "Active" }
    ]
  ]
}
```

**Table cell properties:**

| Property | Type | Description |
|----------|------|-------------|
| `text` | string or text items | Cell content |
| `fill` | object | `{ "color": "hex" }` background |
| `color` | string | Text color (hex, no `#`) |
| `bold` | boolean | Bold text |
| `fontSize` | number | Font size |
| `fontFace` | string | Font family |
| `align` | string | `left`, `center`, `right` |
| `valign` | string | `top`, `middle`, `bottom` |
| `border` | object/array | Border definition |
| `colspan` | number | Columns to span |
| `rowspan` | number | Rows to span |
| `margin` | number/array | Cell margins |

#### Chart

```json
{
  "type": "chart",
  "options": {
    "x": 0.5, "y": 1.5, "w": 9, "h": 5,
    "chartType": "BAR",
    "showTitle": true,
    "title": "Revenue by Quarter",
    "showLegend": true,
    "legendPos": "b",
    "chartColors": ["3B82F6", "F97316", "9CA3AF"],
    "barDir": "col",
    "showValAxisTitle": true,
    "valAxisTitle": "Revenue ($M)",
    "data": [
      { "name": "Product A", "labels": ["Q1", "Q2", "Q3", "Q4"], "values": [1.2, 1.5, 1.8, 2.1] },
      { "name": "Product B", "labels": ["Q1", "Q2", "Q3", "Q4"], "values": [0.8, 0.9, 1.1, 1.3] }
    ]
  }
}
```

Chart types: `BAR`, `LINE`, `PIE`, `DOUGHNUT`, `SCATTER`, `BUBBLE`, `RADAR`, `AREA`.

**Chart options:**

| Property | Type | Description |
|----------|------|-------------|
| `chartType` | string | Chart type (see above) |
| `data` | array | `[{ name, labels, values }]` series data |
| `showTitle` | boolean | Show chart title |
| `title` | string | Chart title text |
| `showLegend` | boolean | Show legend |
| `legendPos` | string | Legend position: `b`, `t`, `l`, `r` |
| `chartColors` | string[] | Colors for each series (hex, no `#`) |
| `barDir` | string | Bar direction: `bar` (horizontal), `col` (vertical) |
| `barGrouping` | string | `clustered`, `stacked`, `percentStacked` |
| `showValue` | boolean | Show data values on chart |
| `showPercent` | boolean | Show percentages (pie/doughnut) |
| `showCatAxisTitle` | boolean | Show category axis title |
| `catAxisTitle` | string | Category axis title |
| `showValAxisTitle` | boolean | Show value axis title |
| `valAxisTitle` | string | Value axis title |
| `lineSize` | number | Line width (line charts) |
| `lineSmooth` | boolean | Smooth lines |

### Slide Masters

Define reusable backgrounds and placeholders:

```json
{
  "masters": [{
    "title": "BRANDED",
    "background": { "color": "0F172A" },
    "objects": [{ "text": { "text": "Company", "options": { "x": 0.5, "y": 6.8, "w": 3, "h": 0.5, "fontSize": 10, "color": "FFFFFF" } } }]
  }],
  "slides": [{
    "masterName": "BRANDED",
    "elements": [{ "type": "text", "options": { "x": 1, "y": 2, "w": 10, "h": 2, "text": "Title Slide", "fontSize": 36, "color": "FFFFFF" } }]
  }]
}
```

## Complete Example

```json
{
  "layout": "LAYOUT_WIDE",
  "author": "Analytics Team",
  "title": "Q1 2025 Performance",
  "slides": [
    {
      "background": { "color": "0F172A" },
      "elements": [
        { "type": "text", "options": { "x": 1, "y": 2.5, "w": 11, "h": 1.5, "text": "Q1 2025 Performance", "fontSize": 40, "fontFace": "Arial", "color": "FFFFFF", "bold": true, "align": "center" } },
        { "type": "text", "options": { "x": 1, "y": 4.2, "w": 11, "h": 0.8, "text": "Prepared by the Analytics Team", "fontSize": 20, "fontFace": "Arial", "color": "94A3B8", "align": "center" } }
      ]
    },
    {
      "elements": [
        { "type": "text", "options": { "x": 0.5, "y": 0.3, "w": 12, "h": 0.8, "text": "Revenue by Quarter", "fontSize": 28, "fontFace": "Arial", "bold": true, "color": "0F172A" } },
        {
          "type": "chart",
          "options": {
            "x": 0.5, "y": 1.5, "w": 12, "h": 5.5,
            "chartType": "BAR",
            "barDir": "col",
            "showTitle": false,
            "showLegend": true,
            "legendPos": "b",
            "chartColors": ["3B82F6", "F97316"],
            "data": [
              { "name": "Product A", "labels": ["Q1", "Q2", "Q3", "Q4"], "values": [1.2, 1.5, 1.8, 2.1] },
              { "name": "Product B", "labels": ["Q1", "Q2", "Q3", "Q4"], "values": [0.8, 0.9, 1.1, 1.3] }
            ]
          }
        }
      ]
    },
    {
      "elements": [
        { "type": "text", "options": { "x": 0.5, "y": 0.3, "w": 12, "h": 0.8, "text": "Key Metrics", "fontSize": 28, "fontFace": "Arial", "bold": true, "color": "0F172A" } },
        {
          "type": "table",
          "options": {},
          "tableOptions": { "x": 0.5, "y": 1.5, "w": 12, "border": { "pt": 1, "color": "E2E8F0" }, "colW": [4, 4, 4], "fontSize": 14, "fontFace": "Arial" },
          "rows": [
            [
              { "text": "Metric", "bold": true, "fill": { "color": "0F172A" }, "color": "FFFFFF" },
              { "text": "Actual", "bold": true, "fill": { "color": "0F172A" }, "color": "FFFFFF" },
              { "text": "Target", "bold": true, "fill": { "color": "0F172A" }, "color": "FFFFFF" }
            ],
            [{ "text": "Revenue" }, { "text": "$1.2M" }, { "text": "$1.1M" }],
            [{ "text": "New Customers" }, { "text": "340" }, { "text": "300" }],
            [{ "text": "Retention" }, { "text": "94%" }, { "text": "90%" }]
          ]
        }
      ],
      "notes": "Highlight that all KPIs exceeded targets this quarter."
    }
  ]
}
```

## Critical Rules

1. **Always write JSON to a temp file first** -- do NOT pass JSON inline to the command. Write the descriptor to a file, then reference it with `--input`.
2. **Use straight quotes in JSON** -- never use smart/curly quotes. Standard JSON double quotes only.
3. **Image paths must be absolute** -- or relative to the working directory where the command runs.
4. **All coordinates and sizes are in inches** -- `x: 0.5` means half an inch from the left edge.
5. **Colors are 6-char hex WITHOUT the `#` prefix** -- use `3B82F6` not `#3B82F6`.
6. **Use `LAYOUT_WIDE` for 16:9 presentations** -- default slide is 13.33" x 7.5".
7. **Chart data series must have matching `labels` and `values` array lengths.**

## Tips

- All coordinates and sizes are in **inches** (e.g., `x: 0.5` = half an inch from the left)
- For `LAYOUT_WIDE` (default): slide is 13.33" wide x 7.5" tall
- Use `items` array for multi-run text with mixed formatting within a single text box
- Use `slideNumber` on slides to add automatic slide numbers
- Use `notes` for speaker notes
- For charts, each data series needs `name`, `labels`, and `values` arrays of equal length
- Use `barDir: "col"` for vertical bars (column chart) and `barDir: "bar"` for horizontal bars
