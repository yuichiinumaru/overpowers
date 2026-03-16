#!/bin/bash
# Accessibility Audit Checklist Generator

TARGET_URL=${1:-"http://localhost:3000"}
FILENAME="accessibility_audit_$(echo $TARGET_URL | sed 's/[^a-zA-Z0-9]/_/g').md"

cat <<EOF > "$FILENAME"
# Accessibility Audit: ${TARGET_URL}

## 1. Automated Scans
- [ ] Run Lighthouse / Axe / Pa11y
- [ ] Record critical violations

## 2. Keyboard Navigation
- [ ] Focus visible on all elements
- [ ] Logical tab order
- [ ] No keyboard traps
- [ ] Interactive elements reachable

## 3. Screen Reader Testing
- [ ] Semantic HTML (landmarks, headings)
- [ ] Alt text for images
- [ ] Form labels and error messages
- [ ] ARIA attributes where needed

## 4. Visual Analysis
- [ ] Color contrast (WCAG AA/AAA)
- [ ] Text scaling (up to 200%)
- [ ] No reliance on color alone

## 5. Remediation Plan
- **Priority 1 (Critical):**
- **Priority 2 (High):**
- **Priority 3 (Medium):**
EOF

echo "Scaffolded accessibility audit checklist: $FILENAME"
