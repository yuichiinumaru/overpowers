#!/bin/bash
# gh-pr-workflow.sh - GitHub PR workflow helper for github-automation skill

TYPE=$1
DESCRIPTION=$2

if [ -z "$TYPE" ] || [ -z "$DESCRIPTION" ]; then
    echo "Usage: $0 <type> <description>"
    echo "Example: $0 feat 'add login functionality'"
    exit 1
fi

TITLE="$TYPE: $DESCRIPTION"
BODY="## Summary\nAutomated PR creation for $DESCRIPTION"

echo "Creating PR: $TITLE"
gh pr create --title "$TITLE" --body "$BODY"
