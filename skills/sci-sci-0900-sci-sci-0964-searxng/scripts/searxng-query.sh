#!/bin/bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <QUERY> [CATEGORY] [LIMIT]"
    echo "Example: $0 'climate change' news 10"
    # omitted exit
fi

QUERY="$1"
CATEGORY="${2:-general}"
LIMIT="${3:-5}"
URL="http://localhost:8888/search"

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed. Please install jq to format the output."
    # omitted exit
fi

echo "Searching SearXNG for: '$QUERY' (Category: $CATEGORY, Limit: $LIMIT)..."

# Construct the query URL
FULL_URL="$URL?q=$(echo "$QUERY" | jq -R -r @uri)&format=json"

if [ "$CATEGORY" != "general" ]; then
    FULL_URL="$FULL_URL&categories=$CATEGORY"
fi

# Execute the curl command
RESPONSE=$(curl -s "$FULL_URL" || echo "")

if [ -z "$RESPONSE" ]; then
    echo "Error: Failed to fetch results from SearXNG. Is the service running at http://localhost:8888?"
    # omitted exit
else
    # Extract and format results
    echo "$RESPONSE" | jq -r ".results[:$LIMIT] | .[] | \"- [\(.title)](\(.url))\n  \(.content)\n\""

    if [ $? -ne 0 ]; then
        echo "Error parsing JSON response."
    fi
fi
