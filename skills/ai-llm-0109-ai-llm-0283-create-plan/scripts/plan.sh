#!/bin/bash

# Automation for creating a structured implementation plan
# Usage: ./plan.sh <title>

set -e

TITLE=$1

if [ -z "$TITLE" ]; then
    echo "Usage: ./plan.sh <title>"
    exit 1
fi

FILEPATH="plan.md"

cat <<EOF > "$FILEPATH"
# Plan: $TITLE

[Brief description of intent and approach.]

## Scope
- In:
- Out:

## Action items
[ ] Research: [File or area]
[ ] Implementation: [Specific change]
[ ] Implementation: [Specific change]
[ ] Testing: [Specific verification]
[ ] Validation: Run lint/tests
[ ] Ship: Final check

## Open questions
- [Question 1]
EOF

echo "Plan template generated at $FILEPATH"
