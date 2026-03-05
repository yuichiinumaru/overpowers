#!/bin/bash

# Release Note Generation Helper - Dump PRs
# Requires gh CLI

REPO=${1:-"microsoft/PowerToys"}
MILESTONE=$2
SINCE=$3 # Optional tag or commit

if [ -z "$MILESTONE" ]; then
  echo "Usage: $0 <repo> <milestone> [since_commit]"
  exit 1
fi

echo "Fetching PRs for milestone '$MILESTONE' in $REPO..."

if [ -n "$SINCE" ]; then
  # Fetch PRs merged since a certain commit/tag that are in the milestone
  gh pr list --repo "$REPO" --milestone "$MILESTONE" --state merged --json number,title,author,labels,url,closedAt --limit 1000 > milestone_prs.json
else
  gh pr list --repo "$REPO" --milestone "$MILESTONE" --state merged --json number,title,author,labels,url,closedAt --limit 1000 > milestone_prs.json
fi

echo "Saved to milestone_prs.json"
