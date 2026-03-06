#!/bin/bash
# BirdNET-Go helper script
# Make sure ~/.clawdbot/credentials/birdnet/config.json exists with the url.

CONFIG_FILE="$HOME/.clawdbot/credentials/birdnet/config.json"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Configuration file not found at $CONFIG_FILE"
    echo "Please create it with the following format:"
    echo '{"url": "http://your-birdnet-ip:port"}'
    exit 1
fi

# Extract URL using grep and sed or jq if available
if command -v jq &> /dev/null; then
    BASE_URL=$(jq -r '.url' "$CONFIG_FILE")
else
    BASE_URL=$(grep '"url"' "$CONFIG_FILE" | sed -E 's/.*"url"[[:space:]]*:[[:space:]]*"([^"]+)".*/\1/')
fi

# Remove trailing slash if present
BASE_URL=${BASE_URL%/}

COMMAND=$1
shift

case "$COMMAND" in
    "recent")
        LIMIT=${1:-10}
        echo "Fetching $LIMIT recent BirdNet detections..."
        curl -s "$BASE_URL/api/v2/detections?limit=$LIMIT"
        ;;
    "search")
        if [ -z "$1" ]; then
            echo "Error: Missing species common name to search."
            exit 1
        fi
        echo "Searching BirdNet for: $1..."
        # Note: encoding the query parameter might be needed for proper API usage
        QUERY=$(echo "$1" | sed 's/ /%20/g')
        curl -s "$BASE_URL/api/v2/detections?common_name=$QUERY"
        ;;
    "detection")
        if [ -z "$1" ]; then
            echo "Error: Missing detection ID."
            exit 1
        fi
        echo "Fetching BirdNet detection details for ID: $1..."
        curl -s "$BASE_URL/api/v2/detections/$1"
        ;;
    "species")
        if [ -z "$1" ]; then
            echo "Error: Missing scientific name."
            exit 1
        fi
        echo "Fetching BirdNet species information for: $1..."
        QUERY=$(echo "$1" | sed 's/ /%20/g')
        curl -s "$BASE_URL/api/v2/species?scientific_name=$QUERY"
        ;;
    "today")
        echo "Fetching today's BirdNet detections..."
        # Pass a date filter for today
        TODAY=$(date +%Y-%m-%d)
        curl -s "$BASE_URL/api/v2/detections?date=$TODAY"
        ;;
    *)
        echo "Usage: $0 {recent|search|detection|species|today} [args...]"
        exit 1
        ;;
esac
