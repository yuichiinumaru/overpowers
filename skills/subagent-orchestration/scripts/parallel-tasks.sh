#!/bin/bash
# parallel-tasks.sh - Run multiple subagents in parallel
# Usage: ./parallel-tasks.sh tasks.txt output_dir/ [max_parallel]

set -e

TASKS_FILE="$1"
OUTPUT_DIR="${2:-.}"
MAX_PARALLEL="${3:-3}"
MODEL="${SUBAGENT_MODEL:-google/antigravity-gemini-3-flash}"

if [ -z "$TASKS_FILE" ] || [ ! -f "$TASKS_FILE" ]; then
    echo "❌ Usage: $0 tasks.txt [output_dir/] [max_parallel]"
    echo ""
    echo "tasks.txt should contain one task per line"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Set permission for non-interactive mode
export OPENCODE_PERMISSION='"allow"'

echo "📋 Tasks file: $TASKS_FILE"
echo "📁 Output dir: $OUTPUT_DIR"
echo "⚡ Max parallel: $MAX_PARALLEL"
echo "🤖 Model: $MODEL"
echo ""

# Count tasks
TOTAL=$(wc -l < "$TASKS_FILE")
echo "🚀 Launching $TOTAL subagents (max $MAX_PARALLEL parallel)..."
echo ""

# Run tasks in parallel
TASK_NUM=0
while IFS= read -r TASK || [ -n "$TASK" ]; do
    # Skip empty lines and comments
    [[ -z "$TASK" || "$TASK" =~ ^# ]] && continue
    
    ((TASK_NUM++))
    OUTPUT_FILE="$OUTPUT_DIR/$(printf '%02d' $TASK_NUM)-result.md"
    
    echo "[$TASK_NUM/$TOTAL] Starting: ${TASK:0:40}..."
    
    # Run in background
    (
        timeout 300 opencode run "$TASK" --model "$MODEL" 2>&1 > "$OUTPUT_FILE"
        echo "[$TASK_NUM] ✅ Completed -> $OUTPUT_FILE"
    ) &
    
    # Limit parallel jobs
    while [ "$(jobs -r | wc -l)" -ge "$MAX_PARALLEL" ]; do
        sleep 1
    done
    
done < "$TASKS_FILE"

# Wait for all to complete
echo ""
echo "⏳ Waiting for all subagents to complete..."
wait

echo ""
echo "========================================"
echo "📊 All $TASK_NUM tasks completed!"
echo "📁 Results in: $OUTPUT_DIR/"
ls -la "$OUTPUT_DIR"/*.md 2>/dev/null || echo "No output files found"
