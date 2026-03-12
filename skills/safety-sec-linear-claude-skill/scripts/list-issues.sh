#!/bin/bash
set -e

# Requires LINEAR_API_KEY environment variable.
if [ -z "$LINEAR_API_KEY" ]; then
    echo "Error: LINEAR_API_KEY is not set."
    exit 1
fi

echo "Fetching recent active issues from Linear..."

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: $LINEAR_API_KEY" \
  --data '{ "query": "{ issues(first: 10, filter: { state: { type: { in: [\"unstarted\", \"started\"] } } }) { nodes { identifier title state { name } assignee { name } } } }" }' \
  https://api.linear.app/graphql | jq '.data.issues.nodes[] | "[\(.identifier)] \(.title) (State: \(.state.name), Assignee: \(.assignee.name // "Unassigned"))"'
