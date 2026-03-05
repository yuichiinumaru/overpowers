#!/bin/bash
# Pre-review preflight checks

echo "--- Git Status ---"
git status

echo "--- Recent Diffs (staged) ---"
git diff --staged --stat

echo "--- Running Project Preflight (if applicable) ---"
if [ -f "package.json" ]; then
    if grep -q "preflight" package.json; then
        npm run preflight
    else
        echo "No 'preflight' script found in package.json. Running lint..."
        npm run lint
    fi
fi

echo "Preflight check complete."
