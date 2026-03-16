---
name: design-ux-frontend-design-pro
description: Frontend design quality improvement skill. Make AI-generated UIs more professional, adhere to design specifications, and avoid common design anti-patterns.
tags: [frontend, design, ux, ui, web]
version: 1.0.0
---

# Frontend Design Pro — Enhancing Frontend Design Quality

Inspiration: [impeccable](https://github.com/pbakaus/impeccable) ⭐ 3k

A professional frontend design language specification to free AI-generated UIs from "cookie-cutter template feel."

---

## Why is this skill needed?

LLMs learn from the same generic templates and, without guidance, produce predictable errors:
- Inter font + purple gradient
- Card within a card within a card
- Gray text on a colored background
- Bounce/elastic animations (look dated)

This skill actively guides AI to produce professional designs using design specifications and a list of anti-patterns.

---

## Design Specifications (Core Principles)

### Typography
- ✅ Choose distinctive fonts: Geist, Instrument Serif, DM Sans, Sora
- ✅ Establish a typographic scale system (modular scale: 1.25 or 1.333)
- ❌ Prohibited: Arial, Inter (too generic), system-ui (lacks personality)
- ❌ Prohibited: More than 2 font families on the same page

### Color & Contrast
- ✅ Define colors using the OKLCH color space (perceptually uniform)
- ✅ Neutrals always have a tint (warm gray / cool gray, never pure gray)
- ✅ Dark mode: Use #0f0f0f for backgrounds, not pure black #000000
- ❌ Prohibited: Gray text on colored backgrounds
- ❌ Prohibited: Pure black/gray (always with a slight tint)

### Spatial Design
- ✅ Establish a base spacing system of 4px or 8px
- ✅ Use whitespace to create breathing room, don't cram elements together
- ✅ Content width limits: Body text 65ch, wide containers 1280px
- ❌ Prohibited: Arbitrary padding values (13px, 22px)

### Motion Design
- ✅ Use `cubic-bezier(0.16, 1, 0.3, 1)` for easing (fast in, slow out)
- ✅ Micro-interaction duration: 100-200ms; Page transitions: 300-500ms
- ✅ Respect `prefers-reduced-motion`
- ❌ Prohibited: Bounce/elastic easing (looks cheap)
- ❌ Prohibited: Animations longer than 600ms (too slow)

### Interaction Design
- ✅ Focus states must be clearly visible (don't remove outlines)
- ✅ Loading states: Skeletons are preferred over spinners
- ✅ Error messages: Specific + actionable ("Invalid email format" vs "Input error")
- ❌ Prohibited: Disabled states without a reason

### UX Writing
- ✅ Button text: Start with a verb ("Save Changes" not "Confirm")
- ✅ Empty states: Explain the reason + provide next steps
- ✅ Error messages: Use plain language, avoid technical jargon
- ❌ Prohibited: "Please wait..." (explain what's happening)

---

## Command List

Use these commands in any UI/frontend-related conversation:

| Command | Function |
|------|------|
| `/audit [component_name]` | Check for accessibility, performance, and responsiveness issues |
| `/critique [component_name]` | UX design review: hierarchy, clarity |
| `/polish [component_name]` | Final polish before release |
| `/distill [component_name]` | Simplify and remove redundant elements |
| `/colorize [component_name]` | Introduce strategic color |
| `/animate [component_name]` | Add meaningful motion |
| `/bolder [component_name]` | Make understated designs bolder |
| `/quieter [component_name]` | Tone down overly flamboyant designs |
| `/delight [component_name]` | Add subtle, delightful details |
| `/normalize [component_name]` | Align with design system specifications |
| `/harden [component_name]` | Add error handling, edge cases, internationalization |

---

## Execution Rules

When the user makes a design-related request:

1. **Automatically Apply Design Specifications**: Actively follow the specifications above when generating or modifying UI code.
2. **When a Command is Received**:
   - `/audit`: Check and list 3-5 specific issues (with line numbers/component names).
   - `/polish`: Output the complete modified code + explain what was changed.
   - Other commands: First, explain what modifications will be made, then output the modified code.
3. **Proactively Warn About Anti-Patterns**: Briefly point out anti-patterns found in the user's code.
4. **Prioritize Code**: Design suggestions should be implemented in concrete CSS/code, not remain conceptual.

---

## Example

User says: "Help me write a login form"

**Output characteristics after automatically applying specifications:**
- Font uses Geist or DM Sans (not Arial/Inter).
- Input focus state uses `2px solid oklch(0.6 0.2 250)` (a tinted blue).
- Button text: "Log In" instead of "Confirm".
- Error message: "Invalid email format, please check the '@' symbol and surrounding characters" instead of "Input error".
- Loading state uses a skeleton, not a spinner.
- Spacing uses multiples of 8px (8/16/24/32px).
