## 2024-05-22 - [Tamagui Button as Next.js Link]
**Learning:** Tamagui `Button` components can be made accessible router links by wrapping them in `next/link` (with `legacyBehavior` and `passHref`) and adding `tag="a"` to the `Button`. This preserves styling while ensuring semantic HTML and accessibility.
**Action:** When encountering Tamagui buttons used for navigation, always wrap them in `Link` and use `tag="a"` to enable standard link behavior and accessibility features like `aria-current`.
## 2026-02-24 - [Add loading state to Button]
**Learning:** Standardizing loading states in `Button` components improves UX consistency and prevents double-submissions without requiring custom implementations in every form.
**Action:** Always check if core UI components support `loading` states before implementing custom spinners in feature code.
