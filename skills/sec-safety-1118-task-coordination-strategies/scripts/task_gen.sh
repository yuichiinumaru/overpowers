#!/bin/bash
# task_gen.sh
# Generates a task description file using the recommended template.

TASK_NAME=$1

if [ -z "$TASK_NAME" ]; then
    echo "Usage: ./task_gen.sh <task-name>"
    exit 1
fi

FILENAME="${TASK_NAME}.md"

cat <<EOF > "$FILENAME"
# Task: ${TASK_NAME}

## Objective
(1-2 sentences on what needs to be accomplished)

## Owned Files
- (List of files/directories this teammate may modify)

## Requirements
- (Specific deliverables or behaviors expected)

## Interface Contract
- (How this work connects to other teammates' work)

## Acceptance Criteria
- (How to verify the task is done correctly)

## Out of Scope
- (What is explicitly out of scope)
EOF

echo "Created task template at $FILENAME"
