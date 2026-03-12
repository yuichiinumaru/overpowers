#!/bin/bash
# Security Best Practices - Recommendation Helper

SKILL_DIR=$(dirname "$(dirname "$0")")
REF_DIR="$SKILL_DIR/references"

echo "--- Detecting Stack ---"
if [ -f package.json ]; then
    echo "Detected: Node.js/JavaScript environment"
    LANG="javascript"
elif [ -f requirements.txt ] || [ -f pyproject.toml ]; then
    echo "Detected: Python environment"
    LANG="python"
elif [ -f go.mod ]; then
    echo "Detected: Go environment"
    LANG="go"
fi

if [ -n "$LANG" ] && [ -d "$REF_DIR" ]; then
    echo "--- Recommended Guidance Files ---"
    ls "$REF_DIR" | grep "$LANG"
else
    echo "No specific guidance files found in $REF_DIR for detected language."
fi
