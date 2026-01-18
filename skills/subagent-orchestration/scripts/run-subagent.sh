#!/bin/bash
# run-subagent.sh - Run a single OpenCode subagent with auto-permissions
# Usage: ./run-subagent.sh "Your task prompt" [output_file.md] [model]

set -e

# Defaults
DEFAULT_MODEL="${SUBAGENT_MODEL:-google/antigravity-claude-sonnet-4-5-thinking}"
DEFAULT_TIMEOUT="${SUBAGENT_TIMEOUT:-300}"

# Args
TASK="$1"
OUTPUT_FILE="${2:-/dev/stdout}"
MODEL="${3:-$DEFAULT_MODEL}"

if [ -z "$TASK" ]; then
    echo "❌ Usage: $0 'task prompt' [output.md] [model]"
    echo ""
    echo "Examples:"
    echo "  $0 'Analyze this codebase for security issues'"
    echo "  $0 'Refactor auth module' result.md"
    echo "  $0 'Review code' out.md google/antigravity-claude-opus-4-5-thinking"
    exit 1
fi

# Check we're not in .config/opencode
if [[ "$PWD" == *".config/opencode"* ]]; then
    echo "⚠️  WARNING: Running from .config/opencode may cause permission issues"
    echo "   Consider running from a different directory"
fi

# Set permission for non-interactive mode
export OPENCODE_PERMISSION='"allow"'

echo "🚀 Launching subagent..."
echo "📝 Task: ${TASK:0:50}..."
echo "🤖 Model: $MODEL"
echo "📄 Output: $OUTPUT_FILE"
echo ""

# Run with timeout
timeout "$DEFAULT_TIMEOUT" opencode run "$TASK" \
    --model "$MODEL" \
    2>&1 | tee "$OUTPUT_FILE"

EXIT_CODE=$?

if [ $EXIT_CODE -eq 124 ]; then
    echo ""
    echo "⏰ Task timed out after ${DEFAULT_TIMEOUT}s"
elif [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo "✅ Subagent completed successfully"
else
    echo ""
    echo "❌ Subagent failed with exit code $EXIT_CODE"
fi

exit $EXIT_CODE
