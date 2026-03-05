#!/bin/bash
# Initialize a new Market Research Report project structure

TOPIC="$1"
if [ -z "$TOPIC" ]; then
    echo "Usage: $0 <report_topic>"
    exit 1
fi

DATE_STR=$(date +%Y%m%d_%H%M%S)
SAFE_TOPIC=$(echo "$TOPIC" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
PROJECT_DIR="writing_outputs/${DATE_STR}_market_report_${SAFE_TOPIC}"

echo "🏗️ Initializing project: $PROJECT_DIR"

# Create directory structure
mkdir -p "$PROJECT_DIR"/{drafts,references,figures,sources,final}

# Create progress.md
cat > "$PROJECT_DIR/progress.md" << EOF
# Market Research: $TOPIC
Started: $(date)

## Status
- [ ] Phase 1: Research & Data Gathering
- [ ] Phase 2: Analysis & Framework Application
- [ ] Phase 3: Visual Generation
- [ ] Phase 4: Report Writing
- [ ] Phase 5: Compilation & Review
EOF

# Note: In a real scenario, we would copy the .sty and .tex templates
# from the skill's assets directory.
echo "✅ Project initialized. Ready for research phase."
echo "Location: $PROJECT_DIR"
