#!/bin/bash
# batch-analyze.sh - Analyze multiple repositories/directories
# Usage: ./batch-analyze.sh /path/to/repos/* output_dir/

set -e

OUTPUT_DIR="${2:-./analysis}"
MAX_PARALLEL="${3:-3}"
MODEL="${SUBAGENT_MODEL:-google/antigravity-claude-sonnet-4-5-thinking}"

# Collect directories from args
DIRS=()
for arg in "$@"; do
    if [ -d "$arg" ] && [[ "$arg" != "$OUTPUT_DIR" ]]; then
        DIRS+=("$arg")
    fi
done

if [ ${#DIRS[@]} -eq 0 ]; then
    echo "❌ Usage: $0 /path/to/dirs/* output_dir/ [max_parallel]"
    echo ""
    echo "Examples:"
    echo "  $0 ~/projects/* ./reports/"
    echo "  $0 /tmp/repos/repo1 /tmp/repos/repo2 ./out/ 5"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"
export OPENCODE_PERMISSION='"allow"'

# Analysis prompt template
PROMPT_TEMPLATE='Analyze the repository at %s.

1. List main files (ls -la)
2. Read README.md if exists
3. Identify the project type and purpose

OUTPUT (max 30 lines):
## Repository: %s
## Project Type
## Key Components  
## Notable Assets (skills, agents, scripts if any)
## Recommendation (USEFUL/SKIP with reason)'

echo "📁 Found ${#DIRS[@]} directories to analyze"
echo "📤 Output: $OUTPUT_DIR"
echo "⚡ Parallel: $MAX_PARALLEL"
echo ""

TASK_NUM=0
for DIR in "${DIRS[@]}"; do
    ((TASK_NUM++))
    BASENAME=$(basename "$DIR")
    OUTPUT_FILE="$OUTPUT_DIR/$(printf '%02d' $TASK_NUM)-$BASENAME.md"
    
    PROMPT=$(printf "$PROMPT_TEMPLATE" "$DIR" "$BASENAME")
    
    echo "[$TASK_NUM/${#DIRS[@]}] Analyzing: $BASENAME"
    
    (
        timeout 300 opencode run "$PROMPT" --model "$MODEL" 2>&1 > "$OUTPUT_FILE"
        echo "[$TASK_NUM] ✅ $BASENAME -> $OUTPUT_FILE"
    ) &
    
    while [ "$(jobs -r | wc -l)" -ge "$MAX_PARALLEL" ]; do
        sleep 1
    done
done

echo ""
echo "⏳ Waiting for analysis to complete..."
wait

echo ""
echo "========================================"
echo "📊 Analyzed ${#DIRS[@]} directories"
echo "📁 Reports: $OUTPUT_DIR/"
echo ""

# Summary
echo "📋 Quick Summary:"
for f in "$OUTPUT_DIR"/*.md; do
    if [ -f "$f" ]; then
        NAME=$(basename "$f" .md)
        REC=$(grep -i "Recommendation" "$f" 2>/dev/null | head -1 || echo "N/A")
        echo "  - $NAME: $REC"
    fi
done
