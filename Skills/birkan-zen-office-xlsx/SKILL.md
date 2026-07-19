---
name: zen-office-xlsx
description: Create professional Excel spreadsheets (.xlsx) from JSON descriptors via the zenskill CLI. Triggers when the user asks to create, generate, or write a spreadsheet, workbook, data table, or mentions .xlsx, Excel, or tabular data export.
---

# Spreadsheets (.xlsx)

Create Excel spreadsheets (.xlsx) from a JSON descriptor via the `zenskill` CLI.

## When to Use

- User asks to create, generate, or write a spreadsheet, workbook, or data table
- User mentions .xlsx, Excel, spreadsheet, workbook, or tabular data export
- You need to produce a downloadable/shareable spreadsheet (not just markdown or CSV)

## Quick Start

```bash
# 1. Write a JSON descriptor to a temp file
cat > /tmp/descriptor.json << 'ENDJSON'
{
  "sheets": [{
    "name": "Sales Data",
    "columns": [
      { "header": "Product", "key": "product", "width": 25 },
      { "header": "Revenue", "key": "revenue", "width": 15, "style": { "numFmt": "$#,##0.00" } }
    ],
    "rows": [
      ["Widget A", 4498.50],
      ["Widget B", 11497.70],
      ["Total", { "formula": "SUM(B2:B3)" }]
    ],
    "autoFilter": true,
    "freezeRow": 1
  }]
}
ENDJSON

# 2. Generate the .xlsx file
zenskill office spreadsheet create --input /tmp/descriptor.json --output /tmp/report.xlsx
```

## Command

```
zenskill office spreadsheet create --input <json> --output <path>
```

| Flag | Required | Description |
|------|----------|-------------|
| `--input` | Yes | Path to the JSON descriptor file |
| `--output` | Yes | Path for the generated .xlsx file (parent dirs created automatically) |

The command reads the JSON descriptor, builds the file, writes the output, and returns a JSON envelope with the output path.

## Descriptor Format

The descriptor is a JSON object with this top-level structure:

```json
{
  "creator": "Author Name",
  "title": "Workbook Title",
  "subject": "Subject",
  "sheets": [ ... ]
}
```

Only `sheets` is required. Each sheet has a `name` and an array of `rows`.

### Sheets

```json
{
  "sheets": [{
    "name": "Sales Data",
    "tabColor": "FF3B82F6",
    "columns": [
      { "header": "Product", "key": "product", "width": 25 },
      { "header": "Revenue", "key": "revenue", "width": 15, "style": { "numFmt": "$#,##0.00" } }
    ],
    "rows": [ ... ],
    "merges": ["A1:C1"],
    "autoFilter": true,
    "freezeRow": 1,
    "styles": { "headerStyle": { "font": { "bold": true, "color": "FFFFFF" }, "fill": { "fgColor": "FF3B82F6" } } }
  }]
}
```

### Row Formats

**Simple array rows** (values by position):
```json
{ "rows": [
  ["Product A", 1200, 15.5, true],
  ["Product B", 800, 10.2, false]
] }
```

**Array rows with formulas:**
```json
{ "rows": [
  ["Product A", 1200, 800, { "formula": "B2-C2" }],
  ["Product A", 1500, 900, { "formula": "B3-C3" }],
  ["Total", { "formula": "SUM(B2:B3)" }, { "formula": "SUM(C2:C3)" }, { "formula": "SUM(D2:D3)" }]
] }
```

**Rich row objects** (with height, visibility, styles):
```json
{
  "values": ["Product A", 1200, 15.5],
  "height": 25,
  "style": { "font": { "bold": true } }
}
```

**Rich cell objects** (cell-level control):
```json
{
  "cells": {
    "A": { "value": "Product A", "style": { "font": { "bold": true } } },
    "B": { "value": 1200, "style": { "numFmt": "$#,##0.00" } },
    "C": { "formula": "B1*1.1", "style": { "numFmt": "$#,##0.00" } },
    "D": { "value": "Click here", "hyperlink": "https://example.com" }
  }
}
```

### Cell Styles

```json
{
  "font": {
    "name": "Arial",
    "size": 12,
    "bold": true,
    "italic": false,
    "underline": false,
    "strike": false,
    "color": "FF334155"
  },
  "fill": {
    "type": "pattern",
    "pattern": "solid",
    "fgColor": "FFDBEAFE"
  },
  "alignment": {
    "horizontal": "center",
    "vertical": "middle",
    "wrapText": true,
    "textRotation": 0,
    "indent": 0
  },
  "border": {
    "top": { "style": "thin", "color": "FF000000" },
    "bottom": { "style": "thin", "color": "FF000000" },
    "left": { "style": "thin", "color": "FF000000" },
    "right": { "style": "thin", "color": "FF000000" }
  },
  "numFmt": "$#,##0.00"
}
```

**Colors** use ARGB format (8-char hex): `FF3B82F6` where `FF` is the alpha channel.

**Border styles:** `thin`, `medium`, `thick`, `dotted`, `dashed`, `double`.

**Number formats:**

| Format String | Example Output |
|---------------|----------------|
| `$#,##0.00` | $1,234.56 |
| `#,##0` | 1,235 |
| `0.00%` | 15.50% |
| `yyyy-mm-dd` | 2025-03-30 |
| `mm/dd/yyyy` | 03/30/2025 |
| `0.00` | 15.50 |

### Sheet Features

**Auto-filter:**
```json
{ "autoFilter": true }
```
Or specify a range: `{ "autoFilter": "A1:D10" }`

**Freeze panes:**
```json
{ "freezeRow": 1 }
```
Or: `{ "freezePane": { "row": 1, "column": 1 } }`

**Page setup:**
```json
{
  "pageSetup": {
    "orientation": "landscape",
    "paperSize": 9,
    "fitToPage": true,
    "fitToWidth": 1,
    "fitToHeight": 0,
    "margins": { "top": 0.75, "bottom": 0.75, "left": 0.7, "right": 0.7 }
  }
}
```

Paper sizes: 9 = A4, 1 = Letter.

**Header/footer:**
```json
{ "headerFooter": { "oddHeader": "&C&\"Arial,Bold\"Monthly Report", "oddFooter": "&CPage &P of &N" } }
```

**Conditional formatting:**
```json
{
  "conditionalFormatting": [{
    "ref": "B2:B100",
    "rules": [{
      "type": "cellIs",
      "operator": "greaterThan",
      "formulae": ["1000"],
      "style": { "font": { "color": "FF15803D" }, "fill": { "fgColor": "FFDCFCE7" } },
      "priority": 1
    }]
  }]
}
```

**Data validations:**
```json
{
  "dataValidations": [{
    "ref": "C2:C100",
    "type": "list",
    "formulae": ["\"Active,Inactive,Pending\""],
    "showErrorMessage": true,
    "errorTitle": "Invalid",
    "error": "Please select from the list"
  }]
}
```

**Sheet protection:**
```json
{ "protection": { "password": "secret", "sheet": true } }
```

## Complete Example

```json
{
  "creator": "Sales Team",
  "title": "Q1 Sales Report",
  "sheets": [
    {
      "name": "Sales Data",
      "tabColor": "FF3B82F6",
      "columns": [
        { "header": "Product", "key": "product", "width": 25 },
        { "header": "Units Sold", "key": "units", "width": 15 },
        { "header": "Unit Price", "key": "price", "width": 15, "style": { "numFmt": "$#,##0.00" } },
        { "header": "Revenue", "key": "revenue", "width": 18, "style": { "numFmt": "$#,##0.00" } }
      ],
      "rows": [
        ["Widget A", 150, 29.99, { "formula": "B2*C2" }],
        ["Widget B", 230, 49.99, { "formula": "B3*C3" }],
        ["Widget C", 89, 99.99, { "formula": "B4*C4" }],
        ["Total", { "formula": "SUM(B2:B4)" }, null, { "formula": "SUM(D2:D4)" }]
      ],
      "autoFilter": "A1:D1",
      "freezeRow": 1,
      "styles": {
        "headerStyle": {
          "font": { "bold": true, "color": "FFFFFFFF" },
          "fill": { "fgColor": "FF3B82F6" },
          "alignment": { "horizontal": "center" }
        }
      },
      "conditionalFormatting": [{
        "ref": "D2:D4",
        "rules": [{
          "type": "cellIs",
          "operator": "greaterThan",
          "formulae": ["5000"],
          "style": { "font": { "color": "FF15803D" }, "fill": { "fgColor": "FFDCFCE7" } },
          "priority": 1
        }]
      }]
    },
    {
      "name": "Summary",
      "rows": [
        [{ "value": "Q1 2025 Sales Summary", "formula": null }],
        [],
        ["Total Products", 3],
        ["Total Revenue", { "formula": "'Sales Data'!D5" }]
      ]
    }
  ]
}
```

## Critical Rules

1. **Always write JSON to a temp file first** -- do NOT pass JSON inline to the command. Write the descriptor to a file, then reference it with `--input`.
2. **Use straight quotes in JSON** -- never use smart/curly quotes. Standard JSON double quotes only.
3. **Colors use ARGB format (8-char hex)** -- use `FF3B82F6` where `FF` is the alpha channel (always `FF` for opaque).
4. **Formulas do NOT start with `=`** -- use `"formula": "SUM(A1:A10)"` not `"formula": "=SUM(A1:A10)"`.
5. **Sheet names must be unique and <=31 characters.**
6. **`autoFilter: true` auto-calculates the range** -- or pass an explicit range string like `"A1:D10"`.

## Tips

- Use `columns` with `header` to define column headers and widths -- the first data row added will be headers
- Use `{ "formula": "..." }` in array rows for Excel formulas; formulas do NOT start with `=`
- Use `autoFilter: true` for automatic filter on all columns, or a range string for specific columns
- `freezeRow: 1` freezes the header row so it stays visible when scrolling
- Use `numFmt` in cell/column styles for number formatting (currency, percentage, dates)
- For cross-sheet references in formulas, use `'Sheet Name'!A1` syntax
