#!/bin/bash
# Initialize a findings.md file from the template in SKILL.md

if [ -z "$1" ]; then
    TARGET_DIR="."
else
    TARGET_DIR="$1"
fi

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE_FILE="$SKILL_DIR/SKILL.md"
OUTPUT_FILE="$TARGET_DIR/findings.md"

if [ -f "$OUTPUT_FILE" ]; then
    echo "Error: $OUTPUT_FILE already exists."
    exit 1
fi

# Extract content after the first markdown header
sed -n '/^# Findings & Decisions/,$p' "$TEMPLATE_FILE" > "$OUTPUT_FILE"

echo "Initialized $OUTPUT_FILE"
