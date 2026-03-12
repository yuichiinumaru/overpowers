#!/bin/bash

# Fetch PR data for review using GitHub CLI (gh)

PR_NUMBER=$1

if [ -z "$PR_NUMBER" ]; then
    echo "Usage: $0 <PR_NUMBER_OR_URL>"
    exit 1
fi

# Extract number from URL if provided
if [[ "$PR_NUMBER" == http* ]]; then
    PR_NUMBER=$(echo "$PR_NUMBER" | grep -oE '[0-9]+$')
fi

echo "--- PR Metadata (#$PR_NUMBER) ---"
gh pr view "$PR_NUMBER" --json title,body,author,baseRefName,headRefName,additions,deletions

echo -e "\n--- Changed Files ---"
gh pr view "$PR_NUMBER" --json files --template '{{range .files}}{{.path}}{{"\n"}}{{end}}'

echo -e "\n--- Diff ---"
gh pr diff "$PR_NUMBER" > "pr_${PR_NUMBER}.diff"
echo "Diff saved to pr_${PR_NUMBER}.diff"

echo -e "\n--- Existing Comments ---"
gh pr view "$PR_NUMBER" --json comments,reviews
