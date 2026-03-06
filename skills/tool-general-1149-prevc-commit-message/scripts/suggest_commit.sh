#!/bin/bash
# Conventional Commit Suggestion Helper

echo "--- Conventional Commit Suggestion ---"
DIFF=$(git diff --cached --name-only)

if [ -z "$DIFF" ]; then
    echo "No staged changes found. Please stage your changes first."
    exit 1
fi

echo "Staged files:"
echo "$DIFF"
echo ""

# Simple logic to suggest type
if echo "$DIFF" | grep -qE "test|spec"; then
    TYPE="test"
elif echo "$DIFF" | grep -qE "README|docs|SKILL.md"; then
    TYPE="docs"
elif echo "$DIFF" | grep -qE "scripts/|tools/"; then
    TYPE="ops"
else
    TYPE="feat"
fi

echo "Suggested commit message:"
echo "${TYPE}(scope): brief description"
echo ""
echo "Example: ${TYPE}(auth): add login validation"
