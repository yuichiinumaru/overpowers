#!/bin/bash
# Helper script to perform SearXNG queries easily and format the output

QUERY=$1
CATEGORY=${2:-general}
TIME_RANGE=${3:-}
LIMIT=${4:-5}
HOST="http://localhost:8888"

if [ -z "$QUERY" ]; then
    echo "Usage: $0 <query> [category] [time_range] [limit]"
    echo "Categories: general, images, videos, news, it, science, repos"
    echo "Time ranges: day, week, month, year"
    return 1 2>/dev/null || exit 1
fi

# URL encode the query
ENCODED_QUERY=$(python3 -c "import urllib.parse; print(urllib.parse.quote('''$QUERY'''))")

URL="$HOST/search?q=$ENCODED_QUERY&format=json"

if [ "$CATEGORY" != "general" ]; then
    URL="$URL&categories=$CATEGORY"
fi

if [ -n "$TIME_RANGE" ]; then
    URL="$URL&time_range=$TIME_RANGE"
fi

echo "Searching: $URL"

if ! command -v jq &> /dev/null; then
    echo "Warning: jq is not installed. Returning raw JSON."
    curl -s "$URL"
    return 0 2>/dev/null || true
fi

curl -s "$URL" | jq -r ".results[:$LIMIT] | .[] | \"## \(.title)\n[\(.url)](\(.url))\n\(.content)\n---\""
