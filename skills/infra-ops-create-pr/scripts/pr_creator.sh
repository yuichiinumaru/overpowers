#!/usr/bin/env bash
# Create PR Helper Script
# Usage: ./pr_creator.sh <type> <scope> <summary>
# Example: ./pr_creator.sh feat editor "Add new button"

set -e

TYPE=$1
SCOPE=$2
SUMMARY=$3

if [ -z "$TYPE" ] || [ -z "$SUMMARY" ]; then
    echo "Usage: $0 <type> <scope> <summary>"
    echo "Types: feat, fix, perf, test, docs, refactor, build, ci, chore"
    echo "Scope can be empty string '' if not needed."
    exit 1
fi

TITLE=""
if [ -n "$SCOPE" ]; then
    TITLE="${TYPE}(${SCOPE}): ${SUMMARY}"
else
    TITLE="${TYPE}: ${SUMMARY}"
fi

echo "Generated Title: $TITLE"

# Simple validation (capital letter start, no period end)
if [[ ! "$SUMMARY" =~ ^[A-Z] ]]; then
    echo "Warning: Summary should start with a capital letter."
fi

if [[ "$SUMMARY" == *\. ]]; then
    echo "Warning: Summary should not end with a period."
fi

echo "To create the PR, run the following gh command:"
cat <<EOF
gh pr create --draft --title "$TITLE" --body "## Summary

<Describe what the PR does and how to test. Photos and videos are recommended.>

## Related Linear tickets, Github issues, and Community forum posts

<!-- Link to Linear ticket: https://linear.app/n8n/issue/[TICKET-ID] -->
<!-- Use \"closes #<issue-number>\", \"fixes #<issue-number>\", or \"resolves #<issue-number>\" to automatically close issues -->

## Review / Merge checklist

- [ ] PR title and summary are descriptive.
- [ ] Docs updated or follow-up ticket created.
- [ ] Tests included.
"
EOF
