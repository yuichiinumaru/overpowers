#!/usr/bin/env bash
# Search for feature flags in React codebase

echo "--- React Feature Flag Finder ---"
echo ""

FILES=(
    "packages/shared/ReactFeatureFlags.js"
    "packages/shared/forks/ReactFeatureFlags.www.js"
    "packages/shared/forks/ReactFeatureFlags.native-fb.js"
    "packages/shared/forks/ReactFeatureFlags.test-renderer.js"
)

if [ -z "$1" ]; then
    echo "Usage: flag_check.sh <flag_name>"
    echo "Scanning default files for all exports..."
    for f in "${FILES[@]}"; do
        if [ -f "$f" ]; then
            echo "--- $f ---"
            grep "export const" "$f" | head -n 10
        fi
    done
else
    FLAG=$1
    for f in "${FILES[@]}"; do
        if [ -f "$f" ]; then
            echo "Checking $f..."
            grep "$FLAG" "$f" || echo "  Not found."
        fi
    done
fi
