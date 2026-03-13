#!/usr/bin/env bash
# Helper for SearXNG searches

if [ -z "$SEARXNG_URL" ]; then
    echo "Error: SEARXNG_URL environment variable not set."
    exit 1
fi

if [ -z "$1" ]; then
    echo "Usage: searxng_query.sh <query> [limit] [format]"
    exit 1
fi

QUERY=$1
LIMIT=${2:-5}
FORMAT=${3:-text}

echo "Searching for '$QUERY' via SearXNG..."
curl -s "${SEARXNG_URL}/search?q=${QUERY}&format=json" | jq ".results | .[:$LIMIT]"
