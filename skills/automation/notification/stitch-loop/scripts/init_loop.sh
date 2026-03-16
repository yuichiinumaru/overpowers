#!/bin/bash
set -e

echo "Initializing Stitch Build Loop..."

mkdir -p queue site/public

if [ ! -f "next-prompt.md" ]; then
  cat > next-prompt.md << 'EOF'
---
page: index
---
A landing page for our new project.

**DESIGN SYSTEM (REQUIRED):**
[Replace this with your design system block from DESIGN.md]

**Page Structure:**
1. Hero section with call to action
2. Features grid
3. Footer
EOF
  echo "Created next-prompt.md"
fi

if [ ! -f "SITE.md" ]; then
  cat > SITE.md << 'EOF'
# Site Vision
A modern, responsive website built autonomously.

## Sitemap
- [ ] index

## Roadmap
- [ ] index
- [ ] about
- [ ] contact

## Creative Freedom
- Add a blog section
- Add an interactive pricing calculator
EOF
  echo "Created SITE.md"
fi

if [ ! -f "DESIGN.md" ]; then
  cat > DESIGN.md << 'EOF'
# Design System

**Section 6 (For Stitch Generation):**
Use a clean, modern aesthetic with ample whitespace. Primary color: #2563eb. Font: Inter.
EOF
  echo "Created DESIGN.md"
fi

echo "Initialization complete. Ready for the first loop iteration."
