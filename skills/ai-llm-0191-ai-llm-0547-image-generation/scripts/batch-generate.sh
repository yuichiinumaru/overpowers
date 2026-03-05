#!/bin/bash
# batch-generate.sh - Batch image generation helper

PROMPTS_FILE=$1
OUTPUT_DIR=${2:-"./outputs"}

if [ -z "$PROMPTS_FILE" ]; then
    echo "Usage: $0 <prompts_file> [output_dir]"
    echo "Example: $0 prompts.txt ./images"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

while IFS= read -r line; do
    if [ -n "$line" ]; then
        filename=$(echo "$line" | tr ' ' '_' | cut -c1-50).png
        echo "Generating: $line"
        python3 scripts/generate.py --prompt "$line" --output "$OUTPUT_DIR/$filename"
    fi
done < "$PROMPTS_FILE"
