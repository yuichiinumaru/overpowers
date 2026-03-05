#!/bin/bash
# Script to prepare a Jules dispatch task

if [ -z "$1" ]; then
    echo "Usage: $0 <task-name> <title> <objective>"
    exit 1
fi

TASK_NAME=$1
TITLE=$2
OBJECTIVE=$3
DATE=$(date +%Y-%m-%d)
TASK_ID="${DATE}-${TASK_NAME}"

JULES_DIR=".jules"
PENDING_DIR="$JULES_DIR/pending"
PROMPTS_DIR="$JULES_DIR/prompts"

mkdir -p "$PENDING_DIR" "$PROMPTS_DIR"

PROMPT_FILE="$PROMPTS_DIR/${TASK_ID}.md"
RECORD_FILE="$PENDING_DIR/${TASK_ID}.json"

# Generate Prompt
cat <<EOF > "$PROMPT_FILE"
# Task: ${TITLE}

## Context
Project: Overpowers
Stage: Development
Context: Cloud-based toolkit expansion

## Objective
${OBJECTIVE}

## Constraints
- Write modular code that doesn't require integration
- Place output in a new directory: \`jules-output/${TASK_NAME}/\`
- Do NOT modify existing project files
- Include comprehensive README explaining your work
- Include tests for any code produced

## Deliverables
1. Code in jules-output/${TASK_NAME}/
2. README.md explaining approach and usage
3. Tests (if applicable)

## Success Criteria
- [ ] Output is self-contained in jules-output/
- [ ] README explains what was done
- [ ] Code is clean and documented
- [ ] Tests pass (if applicable)
EOF

# Generate Record
cat <<EOF > "$RECORD_FILE"
{
  "id": "${TASK_ID}",
  "title": "${TITLE}",
  "prompt_file": "${PROMPT_FILE}",
  "dispatched_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "session_id": null,
  "status": "pending",
  "account": null,
  "repo": "user/project",
  "branch_pattern": "jules/${TASK_NAME}-*",
  "expected_completion": null,
  "tags": []
}
EOF

echo "✅ Prepared dispatch for task: ${TASK_ID}"
echo "Prompt: ${PROMPT_FILE}"
echo "Record: ${RECORD_FILE}"
