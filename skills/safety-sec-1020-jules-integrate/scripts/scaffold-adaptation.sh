#!/bin/bash
# Script to scaffold an adaptation plan for a Jules branch

if [ -z "$1" ]; then
    echo "Usage: $0 <branch-name>"
    exit 1
fi

BRANCH=$1
OUTPUT_FILE="adaptation-${BRANCH}.md"

cat <<EOF > "$OUTPUT_FILE"
# Adaptation Process: ${BRANCH}

## Source
Branch: jules/${BRANCH}

## What to Extract
1. 
2. 

## Adaptation Needed
- Align with project conventions: [Style/Imports/Logging]
- Integration points: 
- Modifications: 

## Resulting Files
- src/... (new/modified)

## Tests
- tests/...

## Attribution
Source: jules/${BRANCH} branch
Original work by Jules AI
Integrated/adapted by: [Name]

Co-authored-by: Jules <jules@google.com>
EOF

echo "Scaffolded adaptation plan to $OUTPUT_FILE"
