#!/bin/bash
# Search X/Twitter for recent discussions using bird CLI

TOPIC="$1"
LIMIT=${2:-10}

if [ -z "$TOPIC" ]; then
    echo "Usage: $0 <topic> [limit]"
    exit 1
fi

echo "🐦 Searching X for: '$TOPIC'..."

# Wrap the bird CLI command
bird search "$TOPIC" -n "$LIMIT" --plain
