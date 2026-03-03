#!/bin/bash

# Refactor Preview Helper
# Use this to find all occurrences of a string across the project before refactoring.

SEARCH_PATTERN="$1"
FILE_PATTERN="${2:-*}"

if [ -z "$SEARCH_PATTERN" ]; then
    echo "Usage: $0 [search_pattern] [file_pattern (optional, default: *)]"
    exit 1
fi

echo "Searching for '$SEARCH_PATTERN' in files matching '$FILE_PATTERN'..."
echo "----------------------------------------------------------------"

# Use grep to find matches with line numbers and context
grep -rnE --include="$FILE_PATTERN" "$SEARCH_PATTERN" . | grep -v "node_modules" | grep -v "\.git"

echo "----------------------------------------------------------------"
COUNT=$(grep -rE --include="$FILE_PATTERN" "$SEARCH_PATTERN" . | grep -v "node_modules" | grep -v "\.git" | wc -l)
echo "Total occurrences found: $COUNT"
