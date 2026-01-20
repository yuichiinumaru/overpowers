---
name: frontend_ui_ux
description: Beautiful UI development with modern design patterns, responsive layouts, and accessibility best practices. Use for any frontend work requiring visual excellence.
---

# Frontend UI/UX Skill

Professional UI/UX development with pixel-perfect design replication capabilities.

## Model Selection

| Task Type | Use Alias | Model |
|-----------|-----------|-------|
| **Design replication** | `CREATIVE` | Claude Sonnet 4.5 |
| **Complex layouts** | `DEEP_REASONING` | Claude Opus 4.5 |
| **Quick styling** | `FAST` | Gemini 3 Flash |

---

# PART 0: VISUAL COLLABORATION WITH USER

## ⚠️ CRITICAL: Show Before You Code

**When the user suggests or requests a UI change, ALWAYS offer visual feedback BEFORE implementing.**

### When to Generate Visual Mockups

```markdown
GENERATE MOCKUPS FOR:
1. POSITIONING DECISIONS
   - "Where should I put the HUD?" → Show 2-3 position options
   - "The button is in the wrong place" → Generate layout options

2. COLOR CHOICES
   - "I don't like these colors" → Generate color palette variations
   - "Make it look more professional" → Show before/after color schemes

3. LAYOUT OPTIONS
   - "Rearrange this section" → Show grid/flex layout alternatives
   - "Make the sidebar smaller" → Show width comparison mockups

4. SIZING & SPACING
   - "The gap is too big" → Show variations with different values
   - "Make the text larger" → Show typography scale options

5. COMPONENT STYLING
   - "I want a different button style" → Show button variant mockups
   - "The card looks plain" → Show elevation/shadow options
```

### Visual Mockup Workflow

```markdown
1. USER REQUESTS CHANGE → "Move the HUD"

2. AI GENERATES OPTIONS
   - Option A: Top-left corner
   - Option B: Top-right corner
   - Option C: Bottom-center
   (Use generate_image tool or ASCII diagram)

3. USER CHOOSES → "I like B but smaller"

4. AI REFINES → Show adjusted version

5. USER APPROVES → "Yes, do that!"

6. AI IMPLEMENTS → Write the actual code
```

### How to Show Layout Options

**Option 1: ASCII Diagram (Fast)**
```
Layout A (Current):          Layout B (Proposed):
┌─────────────────┐         ┌─────────────────┐
│ [HUD]  [Score]  │         │ [Score]   [HUD] │
│                 │         │                 │
│      Game       │    vs   │      Game       │
│                 │         │                 │
│            [🌙] │         │ [🌙]            │
└─────────────────┘         └─────────────────┘
```

**Option 2: Generate Image (For complex layouts)**
Use the `generate_image` tool to create visual mockups showing:
- Multiple position options side by side
- Color palette comparisons
- Before/after layout changes

**Option 3: Browser Screenshot (For live comparison)**
- Make a quick change in code
- Take browser screenshot
- Show user for feedback before committing

### Positioning Decision Tree

```markdown
When user is unhappy with element position:

1. Ask: "Where would you like it?"
   - If they answer clearly → Implement directly
   - If they're unsure → Show options

2. Generate visual options:
   - Option A: [description + ASCII/image]
   - Option B: [description + ASCII/image]
   - Option C: [description + ASCII/image]

3. Get explicit approval before coding

4. After implementing, ALWAYS verify with screenshot
```

### Common User Frustrations & How to Avoid

```markdown
❌ BAD: Implement → User dislikes → Redo → User dislikes → Repeat
✅ GOOD: Show options → User picks → Implement once → Done

❌ BAD: "I'll put the HUD top-left" (assuming)
✅ GOOD: "Here are 3 HUD position options - which do you prefer?"

❌ BAD: Long back-and-forth text discussions about layout
✅ GOOD: Generate visual showing exactly what you're proposing
```

### Example Responses

**User: "The achievement popup is in the wrong place"**

```markdown
I can move it! Here are some options:

**Option A: Bottom-center** (won't block gameplay)
┌─────────────────────────────────────┐
│ Score: 0              Best: 633     │
├─────────────────────────────────────┤
│                                     │
│           (game area)               │
│                                     │
│    [🏅 Achievement Unlocked!]       │ ← Bottom
└─────────────────────────────────────┘

**Option B: Top-right corner** (corner notification style)
**Option C: Slide in from left edge** (toast style)

Which would you prefer?
```

---

# PART 1: DESIGN REPLICATION FROM SCREENSHOTS

## Critical: Screenshot Analysis Methodology

**When given a screenshot to replicate, follow this EXACT process:**

### Step 1: Visual Decomposition

```markdown
ANALYZE THE SCREENSHOT SYSTEMATICALLY:

1. LAYOUT STRUCTURE
   - Overall layout type (single column, sidebar, grid, etc.)
   - Major sections (header, content, footer, nav)
   - Container widths and max-widths
   - Alignment (centered, left, full-width)

2. SPACING MEASUREMENTS (estimate from proportions)
   - Padding: outer container, inner elements
   - Margins: between sections, between elements
   - Gap: between repeated items
   - Use 4px/8px base grid system

3. TYPOGRAPHY
   - Font families (identify or use similar)
   - Sizes: headlines, body, captions
   - Weights: regular, medium, semibold, bold
   - Line heights and letter spacing
   - Text colors (primary, secondary, muted)

4. COLORS
   - Background colors (page, cards, sections)
   - Text colors (primary, secondary, accent)
   - Border colors
   - Shadow colors
   - Gradient definitions

5. COMPONENTS
   - Buttons (size, radius, padding)
   - Inputs (height, border, focus states)
   - Cards (padding, radius, shadow)
   - Icons (size, stroke width, style)
   - Images (aspect ratio, object-fit)

6. EFFECTS
   - Border radius values
   - Box shadows (offset, blur, spread)
   - Opacity levels
   - Blur effects (backdrop-filter)
```

### Step 2: Create Design Tokens First

**ALWAYS extract design tokens before writing component CSS:**

```css
:root {
  /* Colors - extract exact values */
  --color-primary: #...;
  --color-secondary: #...;
  --color-background: #...;
  --color-surface: #...;
  --color-text-primary: #...;
  --color-text-secondary: #...;
  --color-border: #...;
  
  /* Typography */
  --font-family: 'Inter', -apple-system, sans-serif;
  --font-size-xs: 12px;
  --font-size-sm: 14px;
  --font-size-base: 16px;
  --font-size-lg: 18px;
  --font-size-xl: 20px;
  --font-size-2xl: 24px;
  --font-size-3xl: 30px;
  --font-size-4xl: 36px;
  
  /* Spacing - use 4px base */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);
}
```

### Step 3: Component-by-Component Replication

**For each component in the screenshot:**

```markdown
1. IDENTIFY exact dimensions (width, height, padding)
2. MEASURE spacing to adjacent elements
3. NOTE all visual properties (colors, borders, shadows)
4. IDENTIFY all states (hover, active, disabled)
5. CODE the component with ALL extracted values
6. VERIFY against screenshot before moving on
```

## Replication Checklist

```markdown
Before considering a design "complete":

LAYOUT
- [ ] Container widths match
- [ ] Section spacing matches
- [ ] Grid/flex gaps match
- [ ] Alignment matches (center, left, etc.)

TYPOGRAPHY  
- [ ] Font sizes match
- [ ] Font weights match
- [ ] Line heights match
- [ ] Text colors match
- [ ] Letter spacing matches

COLORS
- [ ] Background colors match
- [ ] Border colors match
- [ ] Text colors match
- [ ] Accent/brand colors match

SPACING
- [ ] Padding values match
- [ ] Margin values match
- [ ] Gap between items matches

COMPONENTS
- [ ] Button sizes and styles match
- [ ] Input field styles match
- [ ] Card styles match
- [ ] Icon sizes match

EFFECTS
- [ ] Border radius matches
- [ ] Shadows match
- [ ] Opacity/blur effects match
- [ ] Hover states implemented
```

---

# PART 2: PLATFORM-SPECIFIC PATTERNS

## Web Applications

### Header Pattern

```css
.header {
  position: sticky;
  top: 0;
  height: 64px;
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  padding: 0 var(--space-6);
  z-index: 100;
}

.header__logo {
  height: 32px;
}

.header__nav {
  display: flex;
  gap: var(--space-6);
  margin-left: var(--space-8);
}

.header__actions {
  margin-left: auto;
  display: flex;
  gap: var(--space-3);
}
```

### Sidebar Layout

```css
.layout {
  display: grid;
  grid-template-columns: 280px 1fr;
  min-height: 100vh;
}

.sidebar {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  background: var(--color-surface);
  border-right: 1px solid var(--color-border);
  padding: var(--space-6);
}

.main-content {
  padding: var(--space-8);
  max-width: 1200px;
}
```

## Mobile App (Web-based)

### Mobile Screen Structure

```css
.mobile-screen {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  max-width: 428px; /* iPhone 14 Pro Max */
  margin: 0 auto;
}

.mobile-header {
  position: sticky;
  top: 0;
  height: 56px;
  display: flex;
  align-items: center;
  padding: 0 var(--space-4);
  background: var(--color-surface);
}

.mobile-content {
  flex: 1;
  padding: var(--space-4);
  overflow-y: auto;
}

.mobile-tab-bar {
  position: sticky;
  bottom: 0;
  height: 56px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  /* Safe area for iPhone notch */
  padding-bottom: env(safe-area-inset-bottom);
}
```

### iOS-Style Components

```css
/* iOS Navigation Bar */
.ios-nav {
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.ios-nav__title {
  font-size: 17px;
  font-weight: 600;
}

.ios-nav__back {
  position: absolute;
  left: var(--space-4);
  color: var(--color-primary);
}

/* iOS List Item */
.ios-list-item {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  background: var(--color-surface);
  border-bottom: 0.5px solid var(--color-border);
}

.ios-list-item__chevron {
  margin-left: auto;
  color: #C7C7CC;
}

/* iOS Toggle */
.ios-toggle {
  width: 51px;
  height: 31px;
  border-radius: 16px;
  background: #E9E9EB;
  position: relative;
  transition: background 0.2s;
}

.ios-toggle.active {
  background: #34C759;
}

.ios-toggle__knob {
  width: 27px;
  height: 27px;
  border-radius: 50%;
  background: white;
  position: absolute;
  top: 2px;
  left: 2px;
  box-shadow: 0 3px 1px rgba(0,0,0,0.1);
  transition: transform 0.2s;
}

.ios-toggle.active .ios-toggle__knob {
  transform: translateX(20px);
}
```

### Android Material Design

```css
/* Material Button */
.md-button {
  height: 40px;
  padding: 0 24px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  background: var(--color-primary);
  color: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.md-button:active {
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

/* Material Card */
.md-card {
  background: var(--color-surface);
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  overflow: hidden;
}

/* Material FAB */
.md-fab {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 10px rgba(0,0,0,0.3);
  position: fixed;
  bottom: 24px;
  right: 24px;
}
```

## Browser Extension

### Extension Popup

```css
/* Extension popup dimensions */
.extension-popup {
  width: 350px;
  max-height: 500px;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-size: 13px;
}

.extension-header {
  padding: 12px 16px;
  background: var(--color-primary);
  color: white;
  display: flex;
  align-items: center;
  gap: 8px;
}

.extension-content {
  padding: 16px;
  max-height: 400px;
  overflow-y: auto;
}

.extension-footer {
  padding: 12px 16px;
  border-top: 1px solid var(--color-border);
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}
```

---

# PART 3: COMMON UI PATTERNS

## Button Variants

```css
/* Base button */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: 0 var(--space-4);
  height: 40px;
  font-size: var(--font-size-sm);
  font-weight: 500;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all 0.15s ease;
}

/* Primary */
.btn-primary {
  background: var(--color-primary);
  color: white;
}

.btn-primary:hover {
  filter: brightness(1.1);
}

/* Secondary */
.btn-secondary {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  color: var(--color-text-primary);
}

.btn-secondary:hover {
  background: var(--color-background);
}

/* Ghost */
.btn-ghost {
  background: transparent;
  color: var(--color-primary);
}

.btn-ghost:hover {
  background: rgba(var(--color-primary-rgb), 0.1);
}

/* Sizes */
.btn-sm { height: 32px; padding: 0 12px; font-size: 12px; }
.btn-lg { height: 48px; padding: 0 24px; font-size: 16px; }
```

## Input Fields

```css
.input {
  width: 100%;
  height: 40px;
  padding: 0 var(--space-3);
  font-size: var(--font-size-sm);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  transition: border-color 0.15s, box-shadow 0.15s;
}

.input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(var(--color-primary-rgb), 0.1);
}

.input::placeholder {
  color: var(--color-text-secondary);
}

/* With icon */
.input-group {
  position: relative;
}

.input-group .input {
  padding-left: 40px;
}

.input-group__icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--color-text-secondary);
}
```

## Cards

```css
.card {
  background: var(--color-surface);
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
  overflow: hidden;
}

.card--elevated {
  border: none;
  box-shadow: var(--shadow-lg);
}

.card__image {
  width: 100%;
  aspect-ratio: 16/9;
  object-fit: cover;
}

.card__content {
  padding: var(--space-5);
}

.card__title {
  font-size: var(--font-size-lg);
  font-weight: 600;
  margin-bottom: var(--space-2);
}

.card__description {
  color: var(--color-text-secondary);
  line-height: 1.5;
}

.card__footer {
  padding: var(--space-4) var(--space-5);
  border-top: 1px solid var(--color-border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

---

# PART 4: RESPONSIVE DESIGN

## Breakpoints

```css
/* Mobile First Breakpoints */
:root {
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
  --bp-2xl: 1536px;
}

/* Usage */
@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
```

## Responsive Grid

```css
.grid {
  display: grid;
  gap: var(--space-6);
}

/* 1 column mobile, 2 tablet, 3 desktop */
@media (max-width: 639px) {
  .grid { grid-template-columns: 1fr; }
}

@media (min-width: 640px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

---

# PART 5: QUALITY CHECKLIST

## ⚠️ CRITICAL: Element Overlap Prevention

**BEFORE adding any positioned elements (position: absolute, fixed), ALWAYS:**

```markdown
1. MAP EXISTING ELEMENTS
   - [ ] List ALL elements currently in the target container
   - [ ] Document their positions (top, bottom, left, right, center)
   - [ ] Identify "reserved zones" (headers, footers, corners)

2. CHOOSE NON-CONFLICTING POSITION
   - [ ] If top-left is used → use top-right or bottom
   - [ ] If header exists → position below header height
   - [ ] If footer exists → position above footer height
   - [ ] Consider z-index layering if overlap is intentional

3. VERIFY VISUALLY BEFORE COMMITTING
   - [ ] Run the app/page in browser
   - [ ] Check ALL screen states (start, running, paused, game over)
   - [ ] Resize window to test responsive behavior
   - [ ] Take screenshot and verify no overlap
```

### Position Zone Reference

```
┌─────────────────────────────────────────┐
│  TOP-LEFT      TOP-CENTER      TOP-RIGHT│  ← Check header conflicts
│                                         │
│                                         │
│  LEFT-CENTER              RIGHT-CENTER  │
│                                         │
│                                         │
│  BOTTOM-LEFT  BOTTOM-CENTER BOTTOM-RIGHT│  ← Check footer/nav conflicts
└─────────────────────────────────────────┘

Before using a zone, CHECK if it's already occupied!
```

## Before Submitting Any UI

```markdown
VISUAL ACCURACY
- [ ] Colors match reference exactly
- [ ] Typography matches reference exactly
- [ ] Spacing matches reference exactly
- [ ] Proportions match reference exactly
- [ ] Icons/images match reference

FUNCTIONALITY
- [ ] All hover states work
- [ ] All focus states work
- [ ] All active states work
- [ ] All disabled states work
- [ ] Transitions are smooth

RESPONSIVENESS
- [ ] Works on mobile (320px)
- [ ] Works on tablet (768px)
- [ ] Works on desktop (1280px+)
- [ ] No horizontal scroll
- [ ] No overlapping elements

ELEMENT OVERLAP CHECK (MANDATORY)
- [ ] All absolutely positioned elements verified for overlap
- [ ] Tested with content at maximum expected size
- [ ] Screenshot taken and visually inspected
- [ ] All app states tested (loading, active, error, etc.)

ACCESSIBILITY
- [ ] Color contrast passes WCAG AA
- [ ] Focusable elements have visible focus
- [ ] Images have alt text
- [ ] Form fields have labels
- [ ] Keyboard navigation works
```

## Common Mistakes to Avoid

```markdown
1. ELEMENT OVERLAP (CRITICAL)
   ❌ Adding position: absolute without checking existing elements
   ❌ Using same position (top-left) as existing UI
   ❌ Not testing all app states with the new element
   ✅ Map existing elements BEFORE choosing position
   ✅ Use opposite corner or different zone from existing UI
   ✅ Visually verify in browser with screenshot

2. WRONG SPACING
   ❌ Eyeballing margins/padding
   ✅ Use 4px/8px grid system, measure proportions

3. WRONG COLORS
   ❌ Using "close enough" colors
   ✅ Extract exact hex/rgb values from screenshot

4. MISSING STATES
   ❌ Only implementing default state
   ✅ Implement hover, focus, active, disabled

5. IGNORING TYPOGRAPHY
   ❌ Default browser fonts/sizes
   ✅ Match font family, size, weight, line-height

6. INCORRECT SHADOWS
   ❌ Generic box-shadow
   ✅ Match exact offset, blur, spread, color

7. BREAKING RESPONSIVENESS
   ❌ Fixed widths everywhere
   ✅ Use max-width, flex, grid
```

---

# PART 6: VISUAL VERIFICATION PROTOCOL

## Mandatory Browser Testing

**After ANY UI change:**

```markdown
1. Open in browser (not just code review)
2. Test ALL states the UI can be in
3. Take screenshot of each state
4. Compare to design intent
5. Fix any overlap or visual issues BEFORE committing
```

## Quick Overlap Detection Script

Use this in browser console to highlight positioned elements:

```javascript
// Highlight all positioned elements
document.querySelectorAll('*').forEach(el => {
  const pos = getComputedStyle(el).position;
  if (pos === 'absolute' || pos === 'fixed') {
    el.style.outline = '2px solid red';
    console.log('Positioned:', el.className, pos, el.getBoundingClientRect());
  }
});
```

