#!/bin/bash
# run-subagent.sh - Run a single OpenCode subagent with auto-permissions
# Usage: ./run-subagent.sh "Your task prompt" [output_file.md] [model] [complexity]
#
# Features:
# - Auto-fallback chain based on complexity (Opus -> Sonnet -> Flash -> GLM)
# - Configurable timeout
# - Directory safety check
# - Stateful Health Monitor integration

set -e

# Args
TASK="$1"
OUTPUT_FILE="${2:-/dev/stdout}"
MODEL_INPUT="$3"
COMPLEXITY="${4:-medium}"

if [ -z "$TASK" ]; then
    echo "❌ Usage: $0 'task prompt' [output.md] [model] [complexity]"
    echo ""
    echo "Examples:"
    echo "  $0 'Analyze this codebase for security issues' result.md auto high"
    echo "  $0 'Refactor auth module' result.md"
    echo "  $0 'Review code' out.md google/antigravity-claude-opus-4-5-thinking"
    echo ""
    echo "Environment variables:"
    echo "  SUBAGENT_TIMEOUT     - Timeout in seconds (default: 300)"
    echo "  SUBAGENT_ENABLE_FALLBACK - Enable fallback (default: true)"
    exit 1
fi

DEFAULT_TIMEOUT="${SUBAGENT_TIMEOUT:-300}"
ENABLE_FALLBACK="${SUBAGENT_ENABLE_FALLBACK:-true}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
MODEL_SELECTOR="${REPO_ROOT}/scripts/utils/model_selector.py"

# Resolve Initial Model
if [ -z "$MODEL_INPUT" ] || [ "$MODEL_INPUT" == "auto" ]; then
    MODEL=$($MODEL_SELECTOR --get-model "$COMPLEXITY")
else
    MODEL="$MODEL_INPUT"
fi

# Check we're not in .config/opencode
if [[ "$PWD" == *".config/opencode"* ]]; then
    echo "⚠️  WARNING: Running from .config/opencode may cause permission issues"
    echo "   Consider running from a different directory"
fi

# Set permission for non-interactive mode
export OPENCODE_PERMISSION='"allow"'

# Temp file for output (for rate limit detection)
TEMP_OUTPUT=$(mktemp)
trap "rm -f $TEMP_OUTPUT" EXIT

run_with_model() {
    local model="$1"
    local attempt="$2"
    
    echo "🚀 Launching subagent (Attempt $attempt)..."
    echo "📝 Task: ${TASK:0:60}..."
    echo "🤖 Model: $model"
    echo ""
    
    # Run with timeout
    set +e
    timeout "$DEFAULT_TIMEOUT" opencode run "$TASK" \
        --model "$model" \
        2>&1 | tee "$TEMP_OUTPUT"
    
    local exit_code=$?
    set -e
    
    # Check for rate limiting
    if grep -qiE "rate.?limit|quota|429|exceeded|too.?many" "$TEMP_OUTPUT" 2>/dev/null; then
        echo ""
        echo "⚠️  Rate limit detected on $model"
        return 2  # Special code for rate limit
    fi
    
    return $exit_code
}

ATTEMPT=1
run_with_model "$MODEL" "$ATTEMPT"
EXIT_CODE=$?

SKIPPED_MODELS=("$MODEL")

# Handle rate limit with fallback chain
while [ $EXIT_CODE -eq 2 ] && [ "$ENABLE_FALLBACK" = "true" ] && [ $ATTEMPT -lt 4 ]; do
    # Report failure to health monitor
    $MODEL_SELECTOR --report-failure "$MODEL" > /dev/null
    
    # Get next available fallback model, skipping the ones we already tried
    NEXT_MODEL=$($MODEL_SELECTOR --get-model "$COMPLEXITY" --skip "${SKIPPED_MODELS[@]}")
    
    if [ "$NEXT_MODEL" == "$MODEL" ]; then
        echo "❌ No more fallback models available."
        break
    fi
    
    MODEL="$NEXT_MODEL"
    SKIPPED_MODELS+=("$MODEL")
    ATTEMPT=$((ATTEMPT + 1))
    
    echo ""
    echo "🔄 Attempting fallback chain -> $MODEL..."
    echo ""
    
    run_with_model "$MODEL" "$ATTEMPT"
    EXIT_CODE=$?
done

# Copy temp to final output
if [ "$OUTPUT_FILE" != "/dev/stdout" ]; then
    cp "$TEMP_OUTPUT" "$OUTPUT_FILE"
fi

# Final status
echo ""
if [ $EXIT_CODE -eq 124 ]; then
    echo "⏰ Task timed out after ${DEFAULT_TIMEOUT}s"
elif [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Subagent completed successfully"
elif [ $EXIT_CODE -eq 2 ]; then
    echo "❌ Rate limited on all models in the fallback chain."
else
    echo "❌ Subagent failed with exit code $EXIT_CODE"
fi

exit $EXIT_CODE
