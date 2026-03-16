#!/bin/bash

CONFIG_FILE="$HOME/.clawdbot/credentials/birdnet/config.json"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Configuration file not found at $CONFIG_FILE"
    echo "Please create it with your BirdNET-Go URL."
    exit 1
fi

BIRDNET_URL=$(grep -o '"url": *"[^"]*"' "$CONFIG_FILE" | grep -o '"[^"]*"$' | sed 's/"//g')

if [ -z "$BIRDNET_URL" ]; then
    echo "Error: URL not found in config file."
    exit 1
fi

COMMAND=$1
ARG1=$2

case "$COMMAND" in
    recent)
        LIMIT=${ARG1:-10}
        curl -s "${BIRDNET_URL}/api/v2/detections?limit=${LIMIT}" | jq '.[] | "\(.common_name) (\(.scientific_name)) - \(.confidence) - \(.date) \(.time)"'
        ;;
    search)
        SPECIES="$ARG1"
        if [ -z "$SPECIES" ]; then
            echo "Usage: $0 search \"Species Name\""
            exit 1
        fi
        curl -s "${BIRDNET_URL}/api/v2/detections?species=${SPECIES}" | jq '.[] | "\(.common_name) (\(.scientific_name)) - \(.confidence) - \(.date) \(.time)"'
        ;;
    detection)
        ID="$ARG1"
        if [ -z "$ID" ]; then
            echo "Usage: $0 detection <id>"
            exit 1
        fi
        curl -s "${BIRDNET_URL}/api/v2/detections/${ID}" | jq '.'
        ;;
    species)
        SPECIES="$ARG1"
        if [ -z "$SPECIES" ]; then
            echo "Usage: $0 species \"Scientific Name\""
            exit 1
        fi
        curl -s "${BIRDNET_URL}/api/v2/species?name=${SPECIES}" | jq '.'
        ;;
    today)
        curl -s "${BIRDNET_URL}/api/v2/detections?date=today" | jq '.[] | "\(.common_name) (\(.scientific_name)) - \(.confidence) - \(.time)"'
        ;;
    *)
        echo "Usage: $0 {recent|search|detection|species|today} [args]"
        exit 1
        ;;
esac
