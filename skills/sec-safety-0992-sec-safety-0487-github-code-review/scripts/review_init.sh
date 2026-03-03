#!/bin/bash

# Simple wrapper to initialize a multi-agent review swarm for a GitHub PR

if [ -z "$1" ]; then
  echo "Usage: review_init.sh <pr_number> [agents]"
  echo "Example: review_init.sh 123 \"security,performance,style\""
  exit 1
fi

PR_NUMBER=$1
AGENTS=${2:-"security,performance,style,architecture"}

echo "🔍 Getting PR context for #$PR_NUMBER..."
PR_DATA=$(gh pr view "$PR_NUMBER" --json files,additions,deletions,title,body)
PR_DIFF=$(gh pr diff "$PR_NUMBER")

if [ -z "$PR_DATA" ]; then
  echo "❌ Error: Could not retrieve data for PR #$PR_NUMBER"
  exit 1
fi

echo "🚀 Initializing comprehensive review swarm with agents: $AGENTS"
npx ruv-swarm github review-init \
  --pr "$PR_NUMBER" \
  --pr-data "$PR_DATA" \
  --diff "$PR_DIFF" \
  --agents "$AGENTS" \
  --depth comprehensive

echo "💬 Posting status comment to PR #$PR_NUMBER..."
gh pr comment "$PR_NUMBER" --body "🔍 Multi-agent code review initiated with agents: $AGENTS"

echo "✅ Review swarm initialized successfully."
