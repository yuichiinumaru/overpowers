---
name: design-ux-frontend-slides
description: Create stunning, animated HTML presentations from scratch or by converting PowerPoint files. Use when users want to build presentations, convert PPT/PPTX to web format, or create slides for talks/pitches. Help non-designers discover their aesthetic through visual exploration rather than abstract choices.
tags: [design, ux, slides, presentation, html]
version: 1.0.0
---

# Frontend Slideshow

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.

Inspired by the visual exploration methods showcased in the work of zarazhangrui (cc: @zarazhangrui).

## When to Enable

* When creating lecture, pitch, workshop, or internal presentations
* When converting `.ppt` or `.pptx` slides to an HTML presentation
* When improving the layout, animations, or typography of existing HTML presentations
* When exploring presentation styles with users who are unsure of their design preferences

## Uncompromising Principles

1. **Zero Dependencies**: A self-contained HTML file with inline CSS and JS by default.
2. **Must Fit Viewport**: Each slide must fit a viewport with no internal scrolling.
3. **Show, Don't Tell**: Use visual previews, not abstract style questionnaires.
4. **Unique Design**: Avoid generic purple gradients, white-background-with-Inter-font, or templated document looks.
5. **Production Quality**: Keep code clear, accessible, responsive, and performant.

Before generating, read `STYLE_PRESETS.md` for viewport-safe CSS foundations, density constraints, preset directories, and CSS gotchas.

## Workflow

### 1. Detect Mode

Choose a path:

* **New Presentation**: User has a topic, notes, or full draft
* **PPT Conversion**: User has `.ppt` or `.pptx`
* **Enhancement**: User already has HTML slides and wants to improve them

### 2. Discover Content

Ask only for the minimum necessary:

* Purpose: Pitch, educational, conference talk, internal update
* Length: Short (5-10 slides), Medium (10-20 slides), Long (20+ slides)
* Content Status: Final copy, rough notes, topic only

If the user has content, have them paste it before proceeding with styling.

### 3. Discover Style

Default to visual exploration.

If the user already knows the desired preset, skip previews and use it directly.

Otherwise:

1. Ask what feeling the presentation should evoke: Impressive, Energetic, Focused, Inspiring.
2. Generate **3 single-slide preview files** in `.ecc-design/slide-previews/`.
3. Each preview must be self-contained, clearly showcase typography/colors/animations, and keep slide content to roughly 100 lines.
4. Ask the user which preview to keep or which elements to mix.

Use the preset guidelines in `STYLE_PRESETS.md` when mapping feelings to styles.

### 4. Build Presentation

Output one of:

* `presentation.html`
* `[presentation-name].html`

Only use an `assets/` folder if the presentation includes extracted or user-provided images.

Required structure:

* Semantic slide sections
* Viewport-safe CSS foundations from `STYLE_PRESETS.md`
* CSS custom properties for theme values
* Presentation controller classes for keyboard, wheel, and touch navigation
* Intersection Observer for entrance animations
* Support for reduced motion

### 5. Enforce Viewport Fit

Treat this as a hard requirement.

Rules:

* Each `.slide` must use `height: 100vh; height: 100dvh; overflow: hidden;`
* All fonts and spacing must scale with `clamp()`
* Split content into multiple slides when it doesn't fit
* Never solve overflow by shrinking text below readability
* Never allow scrollbars within a slide

Use density constraints and mandatory CSS code blocks from `STYLE_PRESETS.md`.

### 6. Validate

Check the completed presentation at these dimensions:

* 1920x1080
* 1280x720
* 768x1024
* 375x667
* 667x375

If browser automation is available, use it to verify no slides overflow and keyboard navigation works.

### 7. Deliver

Upon delivery:

* Remove temporary preview files unless the user wishes to keep them
* Open the presentation with an appropriate open-source tool for the current platform, when useful
* Summarize file paths, preset used, slide count, and simple theme customization points

Use the correct open-source tool for the current OS:

* macOS: `open file.html`
* Linux: `xdg-open file.html`
* Windows: `start "" file.html`

## PPT / PPTX Conversion

For PowerPoint conversions:

1. Prioritize `python3` and `python-pptx` to extract text, images, and notes.
2. If `python-pptx` is unavailable, ask whether to install it or fall back to a manual/export-based workflow.
3. Preserve slide order, speaker notes, and extracted assets.
4. After extraction, run the same style discovery workflow as for new presentations.

Keep conversions cross-platform. Do not rely on macOS-only tools when Python can accomplish the task.

## Implementation Requirements

### HTML / CSS

* Use inline CSS and JS unless the user explicitly requests a multi-file project.
* Fonts may come from Google Fonts or Fontshare.
* Prioritize atmospheric backgrounds, strong typographic hierarchy, and clear visual direction.
* Use abstract shapes, gradients, grids, noise, and geometry, not illustrations.

### JavaScript

Include:

* Keyboard navigation
* Touch/swipe navigation
* Mouse wheel navigation
* Progress indicator or slide index
* Entrance animations triggered on view

### Accessibility

* Use semantic structure (`main`, `section`, `nav`)
* Maintain readable contrast
* Support keyboard-only navigation
* Respect `prefers-reduced-motion`

## Content Density Constraints

Unless the user explicitly requests denser slides and readability is maintained, use the following maximums:

| Slide Type    | Constraint                     |
|---------------|--------------------------------|
| Title         | 1 heading + 1 sub-heading + optional tagline |
| Content       | 1 heading + 4-6 bullet points or 2 short paragraphs |
| Feature Grid  | Max 6 cards                    |
| Code          | Max 8-10 lines                 |
| Quote         | 1 quote + attribution          |
| Image         | 1 viewport-constrained image   |

## Anti-Patterns

* Generic startup gradients with no visual identity
* System font documents, unless adopting an editorial style intentionally
* Lengthy bulleted lists
* Code blocks requiring scrolling
* Fixed-height content boxes that break on short screens
* Invalid negation CSS functions like `-clamp(...)`

## Related ECC Skills

* `frontend-patterns` for components and interaction patterns surrounding the presentation
* `liquid-glass-design` when the presentation intentionally borrows from Apple's glass aesthetic
* `e2e-testing` if you need automated browser validation for the final presentation

## Delivery Checklist

* Presentation runs locally in a browser from a file
* Each slide fits the viewport without scrolling
* Style is unique and intentional
* Animations are meaningful, not gratuitous
* Reduced motion setting is respected
* File paths and customization points are explained upon delivery
