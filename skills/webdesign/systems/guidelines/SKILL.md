---
name: guidelines
description: "Guidelines - This skill can automatically generate HTML preview interfaces that comply with FTdesign design specifications based on the user's natural language description. It supports three main page types: list pages, form pages, and detail pages. The generated pages can be previewed directly in the browser."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# FTdesign HTML Generator Skill

## Skill Overview

This skill can automatically generate HTML preview interfaces that comply with FTdesign design specifications based on user descriptions in natural language. It supports three main page types: list pages, form pages, and detail pages. The generated pages can be previewed directly in a browser.

## Trigger Conditions

This skill will be automatically loaded when the user's request meets any of the following conditions:

1. The user explicitly requests "generate HTML page" or "generate preview interface".
2. The user's description includes page type keywords:
   - List page/Table page/Query page (keywords: list, table, query, manage, browse)
   - Form page/Edit page/New page (keywords: form, edit, new, add, create)
   - Detail page/View page (keywords: detail, view, detail page, view page)
3. The user mentions FTdesign related design specifications.

## Skill Workflow

### Step 1: Page Type Identification

Determine the page type through keyword matching:

- **List Page**: Contains keywords like "list", "table", "query", "manage".
- **Form Page**: Contains keywords like "form", "edit", "new", "add", "create".
- **Detail Page**: Contains keywords like "detail", "view", "detail page", "view page".

### Step 2: Template Selection

Select the corresponding template file based on the page type:

- List Page → `assets/templates/list-page.html`
- Form Page → `assets/templates/form-page.html`
- Detail Page → `assets/templates/detail-page.html`

### Step 3: Data Population

Parse user requirements and extract the following information:

1. **Page Title**: e.g., "User Management", "Article List".
2. **Field Information**: Field name, field type, whether it's required.
3. **Operation Buttons**: Query, New, Edit, Delete, Save, Cancel, etc.
4. **Data Examples**: Used to generate sample data.

### Step 4: Generate HTML

Generate a complete HTML file, including:
1. Basic Layout (Sidebar + Main Content Area)
2. Header (Breadcrumbs + Title)
3. Content Area (Generated based on page type)
4. Style Definitions (Complete CSS variable system)
5. Icon Resources (Remix Icon CDN)

### Step 5: Output Result

Generate the HTML file and open it in the IDE preview window.

## Design System Specifications

### Layout Specifications

#### Fixed Sidebar Mode
- Sidebar: `position: fixed`, width 240px
- Main Content Area: `margin-left: 240px`
- Do not use `display: flex` on the root element of React components or `#root`.

#### Page Structure
- Header Module: Breadcrumbs + Title, white background.
- Content Area: White card, 24px margin, 2px border-radius.
- Filter Area and Operation Area: `flex-direction: column`, `gap: 16px`.

### Component Specifications

#### Button Component (Uniform height 32px)
- Primary Button (`ft-btn-primary`): Brand color background.
- Default Button (`ft-btn-default`): White background.
- Dashed Button (`ft-btn-dashed`): Dashed border.
- Link Button (`ft-btn-link`): No background.

#### Form Components
- Input Field (`ft-input`): Height 32px, brand color border on focus.
- Select Field (`ft-select`): Height 32px, arrow positioned at `right: 12px`.
- Textarea (`ft-textarea`): Minimum height 120px.
- Radio/Checkbox: 16px size.

#### Table Component
- Table Header Background: `var(--ft-grey-1)`.
- Row Hover: `var(--ft-grey-1)` background color.
- Cell Padding: 12px 16px.

#### Tag Component
- Height: 22px.
- Status: Success (green), Warning (orange), Error (red).

### Sidebar Specifications

#### Light Style (Must adhere to)
- Background Color: `#FFFFFF` (`var(--ft-grey-0)`)
- Right Border: `#E6E8EC` (`var(--ft-grey-3)`)
- Text Color: `#39485E` (`var(--ft-grey-7)`)
- Active State Background: `#EFF0FA` (`var(--ft-brand-color-bg)`)
- Active State Highlight: 2px left border `#005DEB` "matchstick".

#### Icon Completeness
- All menu items must include an icon.
- Common Icon Mapping:
  - Dashboard: `ri-dashboard-line`
  - User Management: `ri-user-line`
  - Role Management: `ri-team-line`
  - Permission Management: `ri-shield-check-line`
  - System Settings: `ri-settings-3-line`
  - List Management: `ri-file-list-3-line`

### CSS Variable System

```css
:root {
    /* Brand Color */
    --ft-brand-color: #005DEB;
    --ft-brand-color-hover: #267DFF;
    --ft-brand-color-active: #004BBF;
    --ft-brand-color-bg: #EFF0FA;

    /* Neutral Colors (10-level grayscale) */
    --ft-grey-0: #FFFFFF;
    --ft-grey-1: #F7F8FA;
    --ft-grey-2: #F2F3F5;
    --ft-grey-3: #E6E8EC;
    --ft-grey-4: #D1D5DB;
    --ft-grey-5: #9CA3AF;
    --ft-grey-6: #6B7280;
    --ft-grey-7: #39485E;
    --ft-grey-8: #1F2937;
    --ft-grey-9: #111827;

    /* Functional Colors */
    --ft-success-color: #10B981;
    --ft-warning-color: #F59E0B;
    --ft-error-color: #EF4444;

    /* Shadows and Radii */
    --ft-shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --ft-shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --ft-radius-sm: 2px;
    --ft-radius-md: 4px;

    /* Layout Dimensions */
    --ft-sidebar-width: 240px;
    --ft-header-height: 64px;
}
```

## Skill File Structure

```
.codebuddy/skills/ftdesign-html-generator/
├── SKILL.md                    # This file - Skill core instructions
├── README.md                   # Usage Guide
├── references/
│   ├── design-system.md       # Complete FTdesign Design System Specification
│   ├── components-api.md      # Component Usage Guide and API
│   └── examples.md           # Code Example Library
├── assets/
│   ├── templates/
│   │   ├── base-layout.html   # Base Layout Template
│   │   ├── list-page.html     # List Page Template
│   │   ├── form-page.html     # Form Page Template
│   │   └── detail-page.html   # Detail Page Template
│   └── css/
│       └── ftdesign-vars.css  # CSS Variable Definition File
└── scripts/
    └── generate-html.py       # HTML Generation Script (Python, optional)
```

## Generation Rules

### List Page Generation Rules

1. **Must Include**:
   - Query filter area (at least one query condition).
   - Query/Reset buttons.
   - Data table.
   - Pagination component.
   - New button.

2. **Table Column Structure**:
   - ID column (width 60px).
   - Business field columns.
   - Operation column (width 180px).

3. **Operation Buttons**: View, Edit, Delete.

### Form Page Generation Rules

1. **Must Include**:
   - Form fields (at least 3).
   - Form operation buttons (Save, Cancel).
   - Required field indicators.

2. **Form Layout**:
   - Single column layout: Wide forms.
   - Two-column layout: Two fields side-by-side.

3. **Field Type Support**:
   - Text input.
   - Dropdown select.
   - Textarea.
   - Radio button.
   - Checkbox.
   - Date selection.

### Detail Page Generation Rules

1. **Must Include**:
   - Title and metadata area.
   - Information grid display.
   - Operation buttons (Edit, Return).

2. **Information Structure**:
   - Title: 28px, 600 font weight.
   - Metadata: Author, Time, Views, Status.
   - Information Grid: Two-column layout of label + value.

## Generation Examples

### Example 1: User Management List Page

**User Input**:
```
Generate a user management list page, including fields for username, email, role, and status, supporting query and new operations.
```

**Skill Output**:
- Identified as a list page.
- Applied list page template.
- Generated query form (username input, status dropdown).
- Generated data table (ID, Username, Email, Role, Status, Operation columns).
- Generated pagination component.
- Activated the "User Management" menu item in the sidebar.

### Example 2: Article Edit Form

**User Input**:
```
Generate an article edit form, including fields for title (required), category (required), author, abstract, and content.
```

**Skill Output**:
- Identified as a form page.
- Applied form page template.
- Generated form fields (Title, Category, Author, Abstract, Rich Text Editor).
- Marked required fields.
- Generated operation buttons (Save, Preview, Cancel).

### Example 3: Order Detail Page

**User Input**:
```
Generate an order detail page, displaying information such as order number, product details, amount, and status.
```

**Skill Output**:
- Identified as a detail page.
- Applied detail page template.
- Generated title and metadata area.
- Generated information grid (Order Number, Amount, Status, etc.).
- Generated product list area.
- Generated operation buttons (Edit, Return to List).

## Notes

1. **Style Consistency**: All components must use the unified CSS variable system.
2. **Responsive Design**: Generated pages should support basic responsive adaptation.
3. **Interaction States**: Buttons, input fields, and other components must include hover, focus, and active states.
4. **Icon Completeness**: Sidebar menu items must include icons and cannot be missing.
5. **Prohibited Usage**: Absolutely prohibit the use of Emoji symbols; use Remix Icon uniformly.

## Extended Features

### Custom Templates

Users can modify the template files in the `assets/templates/` directory to customize their page styles.

### Custom Styles

By modifying `assets/css/ftdesign-vars.css`, users can customize CSS variables to override design specifications.

### Python Script Assistance

`scripts/generate-html.py` provides a command-line method for generating HTML, facilitating batch processing.

## Troubleshooting

### Issue 1: Incorrectly Generated Page Styles

**Solution**: Check if CSS variables are correctly imported and ensure the complete variable system is used.

### Issue 2: Missing Sidebar Icons

**Solution**: Ensure all sidebar menu items include icons and use standard Remix Icon class names.

### Issue 3: Inconsistent Table Column Widths

**Solution**: Refer to the column width settings in the template; ID column is 60px, operation column is 180px.

## Version Information

- Version: 1.0.0
- Last Updated: 2024-02-26
- Applicable FTdesign Version: Full Version
