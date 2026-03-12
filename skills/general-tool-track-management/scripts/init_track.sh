#!/bin/bash
# Conductor Track Initialization Helper

NUM=$1
NAME=$2

if [ -z "$NUM" ] || [ -z "$NAME" ]; then
    echo "Usage: $0 <nnnn> <track-name>"
    exit 1
fi

FILENAME="docs/tasks/${NUM}-track-${NAME}.md"

cat <<EOF > "$FILENAME"
# Track ${NUM}: ${NAME}

**Status**: [ ]
**Priority**: MEDIUM
**Type**: feature

## Objective
[Describe objective]

## Exit Conditions
- [ ] Condition 1
- [ ] Condition 2

## Sub-tasks
- [ ] Task 1
- [ ] Task 2
EOF

echo "Track initialized: $FILENAME"
