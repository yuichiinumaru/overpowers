#!/bin/bash
# Quick debug of recent agent activity using langsmith-fetch

# Check if required environment variables are set
if [ -z "$LANGSMITH_API_KEY" ]; then
    echo "Error: LANGSMITH_API_KEY environment variable not set."
    exit 1
fi

LIMIT=${1:-5}
MINUTES=${2:-5}

echo "🔍 Fetching $LIMIT traces from the last $MINUTES minutes..."

# Wrap the CLI command
langsmith-fetch traces --last-n-minutes "$MINUTES" --limit "$LIMIT" --format pretty
