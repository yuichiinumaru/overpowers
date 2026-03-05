#!/bin/bash
TOPIC=$1
if [ -z "$TOPIC" ]; then
    echo "Usage: $0 <topic>"
    exit 1
fi

FILE=".agents/scratch/${TOPIC}-research.md"
mkdir -p .agents/scratch

cat <<EOF > "$FILE"
# ${TOPIC} Research

## Summary

Brief overview of findings and recommendations.

## pdf.js Approach

- How it works
- Key files: 
- Pros/cons

## pdf-lib Approach

- How it works
- Key files: 
- Pros/cons

## PDFBox Approach

- How it works
- Key files: 
- Pros/cons

## Recommendations for @libpdf/core

- What approach to take
- Key considerations
- Edge cases to handle
EOF

echo "Research document initialized: $FILE"
