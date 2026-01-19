#!/bin/bash
# run-subagent.sh - Run a single OpenCode subagent with auto-permissions
# Usage: ./run-subagent.sh "Your task prompt" [output_file.md] [model]
#
# Features:
# - Auto-fallback to GLM 4.7 on rate limit
# - Configurable timeout
# - Directory safety check

set -e

# Defaults
DEFAULT_MODEL="${SUBAGENT_MODEL:-google/antigravity-claude-sonnet-4-5-thinking}"
FALLBACK_MODEL="${SUBAGENT_FALLBACK:-google/opencode-glm-4-7-zen}"
DEFAULT_TIMEOUT="${SUBAGENT_TIMEOUT:-300}"
ENABLE_FALLBACK="${SUBAGENT_ENABLE_FALLBACK:-true}"

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
    echo ""
    echo "Environment variables:"
    echo "  SUBAGENT_MODEL       - Primary model (default: claude-sonnet-4-5)"
    echo "  SUBAGENT_FALLBACK    - Fallback model (default: glm-4-7-zen)"
    echo "  SUBAGENT_TIMEOUT     - Timeout in seconds (default: 300)"
    echo "  SUBAGENT_ENABLE_FALLBACK - Enable fallback (default: true)"
    exit 1
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
    local is_fallback="$2"
    
    echo "🚀 Launching subagent..."
    echo "📝 Task: ${TASK:0:60}..."
    echo "🤖 Model: $model"
    [ -n "$is_fallback" ] && echo "🔄 (Fallback attempt)"
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

# Try primary model
run_with_model "$MODEL"
EXIT_CODE=$?

# Handle rate limit with fallback
if [ $EXIT_CODE -eq 2 ] && [ "$ENABLE_FALLBACK" = "true" ] && [ "$MODEL" != "$FALLBACK_MODEL" ]; then
    echo ""
    echo "🔄 Attempting fallback to $FALLBACK_MODEL..."
    echo ""
    
    run_with_model "$FALLBACK_MODEL" "fallback"
    EXIT_CODE=$?
fi

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
    echo "❌ Rate limited on all models"
else
    echo "❌ Subagent failed with exit code $EXIT_CODE"
fi

exit $EXIT_CODE

