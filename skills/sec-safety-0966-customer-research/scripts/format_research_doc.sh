#!/bin/bash
# Format a research finding into a knowledge base entry

TOPIC=${1:-"Topic"}
DATE=$(date +%Y-%m-%d)
FILENAME="docs/research/$(echo $TOPIC | tr ' ' '-').md"

mkdir -p docs/research

cat > "$FILENAME" <<EOF
## $TOPIC

**Last Verified:** $DATE
**Confidence:** [High / Medium / Low]

### Answer
[Clear, direct answer]

### Details
[Supporting detail, context, and nuance]

### Sources
[Where this information came from]

### Related Questions
[Other questions this might help answer]

### Review Notes
[When to re-verify, what might change this answer]
EOF

echo "Research entry template created at $FILENAME"
