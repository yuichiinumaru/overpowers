#!/bin/bash
# pr-triage-workflow.sh - GitHub PR triage workflow helper

REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
echo "Triage starting for $REPO..."

# Fetch PRs using bundled script
./scripts/gh_fetch.py prs --output json > prs.json

echo "Fetched PRs. Ready for parallel analysis."
echo "Use 'npx claude-flow github review --pr <number>' for individual reviews."
