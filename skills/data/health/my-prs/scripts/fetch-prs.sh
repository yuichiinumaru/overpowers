#!/bin/bash

# My PRs fetcher
# Usage: ./fetch-prs.sh [days]

DAYS=${1:-0}
REPO="airbytehq/airbyte"
MY_USER="@me"
TEAM="move-destinations"

if [ "$DAYS" -eq 0 ]; then
    DATE_FILTER=$(date +"%Y-%m-%d")
else
    DATE_FILTER=$(date -d "$DAYS days ago" +"%Y-%m-%d")
fi

echo "Fetching PRs since $DATE_FILTER for $MY_USER and team $TEAM in $REPO..."

# Fetch assigned directly
echo "--- Assigned to Me ---"
gh pr list --repo "$REPO" --assignee "$MY_USER" --search "created:>=$DATE_FILTER" --json number,title,author,url --template '{{range .}}#{{.number}} {{.title}} by {{.author.login}} ({{.url}}){{"\n"}}{{end}}'

# Fetch team review requested
echo "--- Team Review Requested ($TEAM) ---"
gh pr list --repo "$REPO" --search "created:>=$DATE_FILTER team-review-requested:$TEAM" --json number,title,author,url --template '{{range .}}#{{.number}} {{.title}} by {{.author.login}} ({{.url}}){{"\n"}}{{end}}'
