#!/bin/bash

# Script to capture and prepare inspiration analysis report.
# Usage: ./capture-inspiration.sh "URL" "Name"

URL=$1
NAME=${2:-"Inspiration"}
DATE=$(date +"%Y-%m-%d")
OUTPUT_DIR="docs/assets"
REPORT_FILE="$OUTPUT_DIR/inspiration-$(echo $NAME | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md"

if [[ -z "$URL" ]]; then
    echo "Usage: $0 <URL> [Name]"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

# Note: This script assumes the agent will use its 'chrome-devtools' skill 
# to capture the actual screenshot. This script generates the report template.

echo "Creating inspiration report: $REPORT_FILE"

cat <<EOF > "$REPORT_FILE"
# Inspiration Analysis: $NAME

**URL**: $URL
**Captured**: $DATE
**Status**: 📥 Captured / 🔍 Analyzing

---

## Visual Analysis (to be completed by AI)

### 🎨 Design Style
- [ ] Minimalism
- [ ] Glassmorphism
- [ ] Neo-brutalism
- [ ] Other: __________

### 📐 Layout & Grid
- [ ] Responsive
- [ ] Bento Grid
- [ ] Masonry
- [ ] Fixed width

### 🔡 Typography
- **Heading Font**: 
- **Body Font**: 
- **Hierarchy Notes**: 

### 🌈 Color Palette
- Primary: 
- Secondary: 
- Accent: 
- Background: 

### ✨ Micro-Interactions
- Hover effects: 
- Loading states: 
- Transitions: 

---

## 📈 Quality Rating
**Score**: /10

---

## 🚀 Key Takeaways for Project
1. 
2. 
3. 

EOF

echo "Report template created. Please use 'chrome-devtools' to capture screenshot and 'ai-multimodal' to analyze."
