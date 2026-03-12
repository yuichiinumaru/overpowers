#!/bin/bash
# generate-handoff.sh - Handoff document generator helper

HANDOFF_FILE="HANDOFF.md"

if [ -f "$HANDOFF_FILE" ]; then
    echo "Updating existing $HANDOFF_FILE..."
else
    echo "Creating new $HANDOFF_FILE..."
fi

cat <<EOF > "$HANDOFF_FILE"
# Handoff Document

**Generated:** $(date)

## Goal
- [Enter the primary objective here]

## Current Progress
- [List completed tasks here]

## What Worked
- [List successful approaches here]

## What Didn't Work
- [List failed approaches here]

## Next Steps
- [List clear action items here]
EOF

echo "Handoff document ready at $HANDOFF_FILE"
