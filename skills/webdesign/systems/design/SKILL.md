---
name: component-api-design
description: "Designs reusable React/Vue component APIs and file structure for clarity, flexibility, and maintainability. Use when designing components, component APIs, encapsulating components, component design, or defining props/slots/events."
metadata:
  openclaw:
    category: "design"
    tags: ['design', 'creative', 'graphics']
    version: "1.0.0"
---

# Component & API Design

Design easy-to-use, scalable, and maintainable component APIs and file structures to improve future development efficiency.

## Trigger Scenarios

- User says "Design this component," "How to encapsulate components," "How to define APIs," "How to design props."
- When creating new general components, business components, or upgrading existing component APIs.

## Design Dimensions

### 1. Single Responsibility

- A component should do one type of thing (display / form / layout / feedback).
- If it handles "data fetching + display + complex interaction" simultaneously, consider splitting into a container + display component or splitting into sub-components.

### 2. Props Design

| Principle | Description |
|------|------|
| Add only when necessary | Don't turn what can be expressed by `children`/composition into a prop. |
| Consistent Naming | Use project conventions: `value`/`onChange`, `open`/`onOpenChange`, `disabled`, etc. |
| Clear Types | Define TypeScript clearly, specify required/optional, and union types. |
| Controlled vs. Uncontrolled | If supporting controlled components, `value` + `onChange` should be paired; provide `defaultValue` for uncontrolled. |
| Avoid Redundancy | Don't provide props that can be inferred from existing props (e.g., `disabled` can be handled internally when loading). |

### 3. Extension Methods

- **`children`**: Default content area; use **slots/render props** for complex layouts (e.g., `header`, `footer`, `itemRenderer`).
- **`className` / `style`**: Allow external control of layout and themes.
- **Pass-through**: Form components should pass through `aria-*`, `data-*`, and remaining HTML attributes for accessibility and testing.
- **Themes/Variants**: Use enums like `variant`/`size` instead of a bunch of boolean props (e.g., `type="primary" size="md"`).

### 4. Events & Callbacks

- Naming: `on` + verb or `on` + noun + verb (e.g., `onChange`, `onSubmit`, `onOpenChange`).
- Parameters: Pass "data strongly related to the event" first, then the native `event` (if needed).
- Avoid stuffing too much business logic into callbacks; keep components "neutral."

### 5. Files & Directories

- Single components can be in single files; for components with styles, types, and multiple sub-components, use a directory:
  - `ComponentName/index.tsx` (entry point)
  - `ComponentName/ComponentName.tsx` (implementation)
  - `ComponentName/types.ts`
  - `ComponentName/styles.module.scss`
  - `ComponentName/SubPart.tsx` (internal sub-component)
- Types, constants, and utility functions that can be shared should be placed in the upper layer or `shared`.

## Output Template

```markdown
## Component Design: {Component Name}

### Responsibility
- A one-sentence description of the component's purpose and use cases.

### API (Props)
| Property | Type | Required | Default | Description |
|------|------|------|------|------|
| … | … | … | … | … |

### Events/Callbacks
| Event | Parameters | Description |
|------|------|------|
| … | … | … |

### Slots/Extensions
- default: …
- Other named slots: …

### Usage Example
\`\`\`tsx
<ComponentName ... />
\`\`\`

### File Structure
- Path and description of main files.
```

## Consistency with Project

- If the project uses Radix/shadcn: Align with its "composition + controlled" style and naming.
- If the project uses Tailwind: The component's root node should support `className`, and `cn()` should be used internally for merging.
- Form components should maintain consistency with existing form libraries (like `react-hook-form`) regarding `value`/`onChange` conventions.
