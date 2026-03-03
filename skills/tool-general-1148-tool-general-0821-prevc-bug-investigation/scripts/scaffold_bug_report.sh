#!/bin/bash
# PREVC Bug Investigation Scaffolding

BUG_NAME=${1:-"new_bug"}
FILENAME="bug_investigation_${BUG_NAME}.md"

cat <<EOF > "$FILENAME"
# Bug Investigation: ${BUG_NAME}

## 1. Plan (P)
- Objective:
- Hypothesis:
- Reproduction Steps:

## 2. Reproduction (R)
- Evidence:
- Logs:

## 3. Evaluation (E)
- Root Cause Analysis:
- Impact:

## 4. Verification (V)
- Fix Strategy:
- Test Cases:

## 5. Completion (C)
- Final Resolution:
- Lessons Learned:
EOF

echo "Scaffolded bug investigation report: $FILENAME"
