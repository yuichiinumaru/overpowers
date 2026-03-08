#!/bin/bash
set -e

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <runbook.md>"
    exit 1
fi

RUNBOOK="$1"
if [ ! -f "$RUNBOOK" ]; then
    echo "Error: File $RUNBOOK not found."
    exit 1
fi

echo "Validating structure of $RUNBOOK..."

SECTIONS=(
  "Overview"
  "Detection"
  "Triage"
  "Mitigation"
  "Escalation"
)

missing=0
for section in "${SECTIONS[@]}"; do
    if ! grep -qi "^#.*$section" "$RUNBOOK"; then
        echo "Warning: Missing or improperly formatted '$section' section."
        missing=$((missing + 1))
    fi
done

if [ $missing -gt 0 ]; then
    echo "Validation failed. $missing required sections are missing."
    exit 1
else
    echo "Runbook validation passed."
fi
