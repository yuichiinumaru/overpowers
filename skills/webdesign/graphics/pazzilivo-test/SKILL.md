---
name: pazzilivo-test
description: "Generate Pencil design file components (.pen format) from UI screenshots"
metadata:
  openclaw:
    category: "testing"
    tags: ['testing', 'development', 'quality']
    version: "1.0.0"
---

# Pencil Component Generator

Identify design elements from UI screenshots and generate editable Pencil component files.

## Workflow Overview

```
Screenshot → ASCII Structure Analysis → Extract Design Tokens → Generate .pen File
```

## Detailed Steps

### 1. Analyze Screenshot
Identify the following in the UI screenshot:
- Hierarchy (containers, child elements)
- Text content
- Icon types
- Visual properties like color, spacing, and corner radius

### 2. Generate ASCII Structure Diagram
Describe the component hierarchy using ASCII text:

```
Card (Card Container)
├── Header Row (Title Row)
│   ├── Icon (Icon)
│   └── Title (Title Text)
├── Divider (Separator Line)
└── Content Row (Content Area)
    ├── Item 1
    ├── Item 2
    └── Item 3
```

### 3. Extract Design Tokens
Analyze the screenshot to extract precise design parameters:

| Token | Description | Example Value |
|-------|-------------|---------------|
| Color | Background, text, icon, border | `#ffffff`, `#333333` |
| FontSize | Title, label, value | `15px`, `13px`, `30px` |
| FontWeight | normal, 500, 700 | `"500"`, `"700"` |
| FontFamily | Chinese, numeric fonts | `PingFang SC`, `DIN Alternate` |
| CornerRadius | Card corner radius | `8px` |
| Spacing | padding, gap | `[20, 24]`, `8` |

### 4. Generate .pen File

#### File Structure
```json
{
  "version": "2.6",
  "children": [...],
  "variables": {...}
}
```

#### Key Rules

1. **Variables are only for colors**
   ```json
   "fill": "$--card-bg"        // ✅ Correct
   "fontSize": "$--title-size" // ❌ Incorrect
   "fontSize": 15              // ✅ Correct
   ```

2. **Dimensions use hardcoded numbers**
   ```json
   "width": 560,
   "height": 48,
   "cornerRadius": 8,
   "gap": 8,
   "padding": [20, 24]
   ```

3. **Basic structure of a frame node**
   ```json
   {
     "type": "frame",
     "id": "unique-id",
     "name": "Component Name",
     "reusable": true,          // Set to true for reusable components
     "width": 560,
     "fill": "$--card-bg",
     "cornerRadius": 8,
     "layout": "vertical",      // vertical | horizontal | none
     "gap": 8,
     "padding": [top, right, bottom, left] // Or a single value
   }
   ```

4. **Structure of a text node**
   ```json
   {
     "type": "text",
     "id": "title",
     "name": "Title",
     "fill": "$--title-color",
     "content": "Title Text",
     "lineHeight": 1.5,
     "fontFamily": "PingFang SC",
     "fontSize": 15,
     "fontWeight": "500"
   }
   ```

5. **Structure of an icon_font node**
   ```json
   {
     "type": "icon_font",
     "id": "icon",
     "width": 20,
     "height": 20,
     "iconFontName": "chevrons-right",  // lucide icon name
     "iconFontFamily": "lucide",
     "fill": "$--icon-color"
   }
   ```

6. **Layout properties**
   - `layout`: `"vertical"` | `"horizontal"` | `"none"`
   - `justifyContent`: `"space_between"` | `"center"` | `"flex_start"` | `"flex_end"`
   - `alignItems`: `"center"` | `"flex_start"` | `"flex_end"`
   - `width`: number | `"fill_container"`

7. **Variable definition**
   ```json
   "variables": {
     "--card-bg": {
       "type": "color",
       "value": "#ffffff"
     }
   }
   ```

## Common Design Token Templates

```json
"variables": {
  "--card-bg": { "type": "color", "value": "#ffffff" },
  "--header-bg": { "type": "color", "value": "#fafbfc" },
  "--divider-color": { "type": "color", "value": "#f0f0f0" },
  "--icon-color": { "type": "color", "value": "#4285f4" },
  "--title-color": { "type": "color", "value": "#333333" },
  "--label-color": { "type": "color", "value": "#8c8c8c" },
  "--value-color": { "type": "color", "value": "#333333" },
  "--value-danger": { "type": "color", "value": "#fa5151" }
}
```

## Reference Files

- Target File: `pencil-new.pen`

## Verification Checklist

- [ ] Hierarchy structure consistent with the original image
- [ ] Variables are only used for color properties
- [ ] Dimension values are hardcoded numbers
- [ ] Color values precisely match the original image
- [ ] Font family, size, and weight are correct
- [ ] Spacing and corner radius are correct
- [ ] Component displays correctly in Pencil
