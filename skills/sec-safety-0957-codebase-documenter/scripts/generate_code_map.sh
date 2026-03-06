#!/bin/bash
# Generate a directory map for documentation

OUTPUT_FILE=${1:-"docs/CODE_MAP.md"}

echo "# Codebase Directory Map" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "\`\`\`" >> "$OUTPUT_FILE"
tree -L 3 --dirsfirst -I "node_modules|.git|.jj|.serena|.genkit|dist|build" >> "$OUTPUT_FILE"
echo "\`\`\`" >> "$OUTPUT_FILE"

echo "Code map generated at $OUTPUT_FILE"
