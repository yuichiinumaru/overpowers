#!/bin/bash
# Quick security scan for common issues

echo "--- Searching for Hardcoded Secrets ---"
grep -rE "password|api_key|secret|token" . --exclude-dir={node_modules,.git,.jj} | head -n 20

echo "--- Checking Dependencies (npm) ---"
if [ -f "package.json" ]; then
    npm audit --audit-level=high
fi

echo "--- Checking Dependencies (python) ---"
if [ -f "requirements.txt" ]; then
    # Requires safety package: pip install safety
    if command -v safety &> /dev/null; then
        safety check -r requirements.txt
    else
        echo "Safety package not found. Skipping python vulnerability check."
    fi
fi

echo "Scan complete."
