#!/bin/bash
# Script to scaffold a new incident runbook from templates

TEMPLATE_DIR="$(dirname "$0")/../"
SKILL_MD="$TEMPLATE_DIR/SKILL.md"

if [ -z "$1" ]; then
    echo "Usage: $0 <runbook-name> [template-type]"
    echo "Templates: service (default), database"
    exit 1
fi

NAME=$1
TYPE=${2:-service}
OUTPUT_FILE="${NAME}.md"

if [ -f "$OUTPUT_FILE" ]; then
    echo "Error: $OUTPUT_FILE already exists."
    exit 1
fi

echo "Scaffolding $TYPE runbook to $OUTPUT_FILE..."

if [ "$TYPE" == "database" ]; then
    # Extract Template 2
    sed -n '/### Template 2: Database/,/###/p' "$SKILL_MD" | sed '1d;$d' | sed '/^```markdown/d;/^```$/d' > "$OUTPUT_FILE"
else
    # Extract Template 1
    sed -n '/### Template 1: Service/,/###/p' "$SKILL_MD" | sed '1d;$d' | sed '/^```markdown/d;/^```$/d' > "$OUTPUT_FILE"
fi

echo "Done. Please edit $OUTPUT_FILE with your service-specific details."
