#!/bin/bash
# Fetch the 'foryou' feed from daily.dev

if [ -z "$DAILY_DEV_TOKEN" ]; then
    echo "Error: DAILY_DEV_TOKEN environment variable not set."
    exit 1
fi

echo "Fetching daily.dev 'foryou' feed..."
curl -s -X GET "https://api.daily.dev/public/v1/feeds/foryou" \
     -H "Authorization: Bearer $DAILY_DEV_TOKEN" | jq '.'
