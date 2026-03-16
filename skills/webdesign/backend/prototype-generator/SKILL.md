---
name: prototype-generator
description: "Generates admin/list prototypes from requirements. Supports mountListPage-style frameworks (e.g. kfk-mock-ui), standalone HTML, or project-specific setups. Use when user wants to create a prototype..."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# Automatic Prototype Generation Based on User Requirements

Automatically generates backend list prototypes based on user-input requirements. Supports multiple output modes to adapt to different project structures.

## Trigger Conditions

- User requests "Generate prototype based on requirements", "Automatically generate a set of prototypes", or "Create prototype".
- User describes a business scenario and wishes to obtain a runnable prototype page.
- User requests to add a new list page or management page.

## Step 1: Detect Project Context

Scan the project before generation to determine the output mode:

| Detected | Output Mode | Description |
|---|---|---|
| `kfk-mock-ui.js` or `KFK.mountListPage` | **List Framework Mode** | Generates `menu.js`, `view_*.html`, and adds mock data branches to the existing `mock-ui`. |
| `kfk-admin.css` or parent UI library directory | **Sub-project Mode** | Same as above, with resource paths like `../parent_directory/`. |
| No such dependencies detected | **Standalone Mode** | Generates self-contained HTML (inline styles + scripts) with no external dependencies. |

If the user explicitly specifies (e.g., "Use existing framework", "Standalone page", "Pure HTML"), prioritize that specification.

## Step 2: Parse Requirements

Extract or infer from the user's description:

| Item | Description | Default if Missing |
|---|---|---|
| Project/Module Name | Brand or module name | Ask or use the keyword from the first sentence |
| Target Directory | Output location | Project root or a subdirectory of the same name |
| Menu Group | Group by business domain | e.g., "Core Business", "Basic Data", "System Configuration" |
| Page List | Per page: title, table columns, query conditions, row actions | Corresponds to requirements one by one |

**Field Inference Rules:**
- Name/Title/Code fields → Fuzzy search `mode: 'like'`
- Yes/No, Status, Enum → Dropdown `type: 'select'`, `options: [{value:'',label:'All'},...]`
- Year/Month/Date → `type: 'month'` or placeholder `e.g., 2025-10`
- Enum options are extracted from requirements or examples.

## Step 3: Generate Files (by Mode)

### List Framework Mode (if `kfk-mock-ui` or similar `mountListPage` framework exists)

1. **`menu.js`**: `{ group, items: [{ id, title, href }] }`, `id` uses kebab-case.
2. **`view_xxx.html`**: References CSS/JS, calls `mountListPage(app, config)` (e.g., KFK.mountListPage).
3. **`mock-ui.js`**: Adds `generateXxxRow`, and a branch in `generateRows`.
4. **`sql/*.sql`** (Optional): Table creation statements corresponding to business fields.

**Resource Path Convention**: If the project has a parent UI library directory (e.g., a parent prototype directory), use `../parent_directory/css/`, `../parent_directory/js/`; otherwise, use `./css/`, `./js/` within the project.

### Standalone Mode (no framework dependencies)

Generates a single-page HTML file including:
- Query form (based on `queryFields`)
- Data table (based on `columns`)
- Simple pagination
- Row action buttons (view/edit/delete, etc.)
- Inline styles and scripts, can be opened directly in a browser.

Structure: `query-form` + `data-table` + `pager`, with inline CSS and scripts. See [references/standalone-template.md](references/standalone-template.md) for details.

### Multi-page Standalone Mode

When there are multiple list pages and the user requires menu navigation, it can generate:
- `index.html`: Left-side menu + iframe display.
- `view_xxx.html`: Individual list pages (standalone HTML).
- `menu.js` or inline menu data.

## Step 4: Checklist Verification

- [ ] `menu` item's `id` matches `pageId` / page identifier.
- [ ] `columns` `key` matches the mock data object `key`.
- [ ] Dropdown-type `queryFields` use `type: 'select'` and `options`.
- [ ] Styles and scripts function correctly in standalone mode.

## Template Configuration (List Framework Mode)

### `queryFields`

```javascript
{ key: 'name', label: 'Name', placeholder: 'Please enter', mode: 'like' }
{ key: 'status', label: 'Status', type: 'select', mode: 'eq', options: [
  { value: '', label: 'All' }, { value: 'Yes', label: 'Yes' }, { value: 'No', label: 'No' }
]}
{ key: 'summaryMonth', label: 'Month', type: 'month', mode: 'eq' }
```

### `columns`

```javascript
{ key: 'serialNo', title: 'Serial No.' }
{ key: 'code', title: 'Code', mono: true }
{ key: 'name', title: 'Name', align: 'left', required: true }
{ key: 'remark', title: 'Remark', align: 'left' }
{ key: 'createTime', title: 'Create Time', mono: true }
```

### `rowActions` + `onRowAction`

```javascript
rowActions: [
  { act: 'view', label: 'View' },
  { act: 'edit', label: 'Edit' },
  { act: 'delete', label: 'Delete', danger: true }
]
```

## Requirement Examples

| User Input | Output |
|---|---|
| "Create a supplier management system with fields for name, entity, and remarks." | 1 supplier list page, 3 columns + `remark`/`createTime`. |
| "Query the invoice pool by seller, buyer, and whether it has been pushed." | `queryFields`: Seller/Buyer/Pushed (dropdown). |
| "The list should have 'Scrap' and 'Reset' buttons." | Add custom operations to `rowActions`, implement logic in `onRowAction`. |
| "Standalone prototype, no dependencies." | Single HTML file with inline styles and scripts. |

## Optional References

If the project has the following conventions, they will also be followed:
- `.cursor/rules/prototype-menu.mdc`: Menu and list page structure.
- If the project has conventions for list page configs or CRUD, they will be followed.

## References

- Detailed template for standalone mode: [references/standalone-template.md](references/standalone-template.md)
