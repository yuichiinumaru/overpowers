#!/bin/bash
# hn.sh - Hacker News API CLI helper

COMMAND=$1
LIMIT=${2:-10}

BASE_URL="https://hacker-news.firebaseio.com/v0"

if [ "$COMMAND" == "top" ]; then
    ids=$(curl -s "$BASE_URL/topstories.json" | jq ".[0:$LIMIT][]")
    for id in $ids; do
        curl -s "$BASE_URL/item/$id.json" | jq -r '"\(.title) - \(.url)"'
    done
elif [ "$COMMAND" == "new" ]; then
    ids=$(curl -s "$BASE_URL/newstories.json" | jq ".[0:$LIMIT][]")
    for id in $ids; do
        curl -s "$BASE_URL/item/$id.json" | jq -r '"\(.title) - \(.url)"'
    done
else
    echo "Usage: $0 [top|new] <limit>"
fi
