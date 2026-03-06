#!/usr/bin/env bash
# Helper script to initialize the Stitch Build Loop files

echo "Bootstrapping Stitch Build Loop..."

if [ ! -f "SITE.md" ]; then
  cat << 'SITE' > SITE.md
# Site Vision
Describe the site here.

## 4. Sitemap
- [ ] index

## 5. Roadmap
- Create index page
SITE
  echo "Created SITE.md"
fi

if [ ! -f "DESIGN.md" ]; then
  cat << 'DESIGN' > DESIGN.md
# Design System
**DESIGN SYSTEM (REQUIRED):**
- Modern, clean, minimalist.
- Primary color: #000000
DESIGN
  echo "Created DESIGN.md"
fi

if [ ! -f "next-prompt.md" ]; then
  cat << 'PROMPT' > next-prompt.md
---
page: index
---
A modern landing page.

**DESIGN SYSTEM (REQUIRED):**
- Modern, clean, minimalist.
- Primary color: #000000

**Page Structure:**
1. Hero section
2. Features
PROMPT
  echo "Created next-prompt.md"
fi

mkdir -p queue site/public
echo "Stitch Build Loop initialized. You can now dispatch the agent."
