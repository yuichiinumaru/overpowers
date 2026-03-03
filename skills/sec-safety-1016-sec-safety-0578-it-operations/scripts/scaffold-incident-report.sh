#!/bin/bash
# Script to scaffold a post-mortem incident report

if [ -z "$1" ]; then
    echo "Usage: $0 <incident-name>"
    exit 1
fi

NAME=$1
DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="incident-${DATE}-${NAME}.md"

cat <<EOF > "$OUTPUT_FILE"
# Post-Incident Review: ${NAME}

## Date
${DATE}

## Status
DRAFT

## Incident Summary
- **Start Time**: 
- **End Time**: 
- **Duration**: 
- **Impact**: 
- **Severity**: [P1/P2/P3/P4]

## Timeline of Events
- [HH:MM] - 
- [HH:MM] - 

## Root Cause Analysis
- **Primary Cause**: 
- **Trigger**: 
- **5 Whys**:
  1. 
  2. 
  3. 
  4. 
  5. 

## What Went Well
- 

## What Could Be Improved
- 

## Action Items
| Task | Owner | Due Date | Status |
|------|-------|----------|--------|
| | | | TODO |

## Lessons Learned
- 

EOF

echo "Scaffolded incident report to $OUTPUT_FILE"
