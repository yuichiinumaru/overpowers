#!/bin/bash

# Helper to initialize a code review swarm for a GitHub PR.

PR_NUM=$1
AGENTS=${2:-"security,performance,style,architecture"}

if [ -z "$PR_NUM" ]; then
    echo "Usage: $0 <pr_number> [agents]"
    echo "Example: $0 123 'security,performance'"
    exit 1
fi

echo "🔍 Fetching data for PR #$PR_NUM..."
PR_DATA=$(gh pr view "$PR_NUM" --json files,additions,deletions,title,body)
PR_DIFF=$(gh pr diff "$PR_NUM")

echo "🚀 Initializing code review swarm with agents: $AGENTS"
npx ruv-swarm github review-init \
  --pr "$PR_NUM" \
  --pr-data "$PR_DATA" \
  --diff "$PR_DIFF" \
  --agents "$AGENTS" \
  --depth comprehensive

gh pr comment "$PR_NUM" --body "🔍 Multi-agent code review initiated via review-swarm helper script."
