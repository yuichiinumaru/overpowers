#!/usr/bin/env bash
# Helper for goplaces with JSON output

if [ -z "$1" ]; then
    echo "Usage: goplaces_query.sh <query>"
    exit 1
fi

QUERY=$1

echo "Searching for '$QUERY'..."
goplaces search "$QUERY" --json --limit 5 | jq .
