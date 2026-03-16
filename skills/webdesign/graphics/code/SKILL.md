---
name: design-to-code
description: "Implements UI from design mockups (Figma, Sketch, or image) with pixel-accurate layout, responsive behavior, and design tokens. Use when restoring design drafts, implementing designs, slicing images, design drafts to code, or converting mocku..."
metadata:
  openclaw:
    category: "development"
    tags: ['development', 'coding', 'programming']
    version: "1.0.0"
---

# Design to Code

High-fidelity restoration of design drafts (Figma/Sketch/images) into front-end code, ensuring consistency in layout, spacing, typography, color, and interaction.

## Trigger Scenarios

- User says "Restore design draft," "Implement according to design," "Slice assets," or "Design to code."
- Providing a Figma/Sketch link, a screenshot of the design, or annotations.
- Need to implement the UI for a specific page/component.

## Execution Flow

### 1. Design Draft Analysis

- **Annotations**: Dimensions, spacing (padding/margin/gap), font size and line height, color (including transparency), border-radius, shadows, borders.
- **Hierarchy**: Component breakdown, nesting relationships, reusable modules.
- **States**: Default / hover / focus / disabled / loading / empty / error.
- **Responsiveness**: Breakpoints, layout changes at different widths (grid, wrapping, hiding).

### 2. Design Token Alignment

- Map colors, font sizes, and spacing to existing CSS variables or Tailwind configurations in the project as much as possible.
- If no existing tokens are available, use variable naming during implementation (e.g., `--color-primary`) for future unification.

### 3. Implementation Priority

1. **Layout**: Use Flex/Grid to build the skeleton first, ensuring alignment and spacing.
2. **Typography**: Font, font size, font weight, line height, color.
3. **Visuals**: Background, borders, border-radius, shadows.
4. **Interaction States**: hover/focus/disabled, etc.
5. **Responsiveness**: Breakpoints and flexible layouts.
6. **Animations**: Implement transitions/animations only if specified in the design.

### 4. Fidelity Self-Check

- [ ] Key dimensions consistent with the design draft (1–2px difference acceptable).
- [ ] Fonts and colors consistent with the design.
- [ ] Layout reasonable and without misalignment at major breakpoints.
- [ ] Interactive elements have clear state feedback.

## Output Conventions

- Use the project's existing tech stack (e.g., Next.js, Tailwind, SCSS, component library).
- Componentization: Extract reusable parts into components with clear naming.
- Semantic HTML + appropriate ARIA (buttons, links, forms).
- Note when necessary: Differences from the design draft and reasons (e.g., compatibility, accessibility).

## Common Mappings

| Design Draft | Implementation Method |
|--------------|-----------------------|
| 8px Grid     | Use multiples of 8 for spacing (8/16/24/32). |
| Font Hierarchy | Map to semantic classes like heading/body/caption or design tokens. |
| Blur/Frosted Glass | `backdrop-filter` + semi-transparent background. |
| Multi-line Truncation | `line-clamp` or `-webkit-line-clamp`. |
| Safe Area    | `padding` combined with `env(safe-area-inset-*)`. |
