#!/bin/bash
QUERY=$1
NUM_RESULTS=${2:-10}

if [ -z "$EXA_API_KEY" ]; then
    echo "Error: EXA_API_KEY environment variable is not set."
    exit 1
fi

echo "Fetching code context for: $QUERY (results: $NUM_RESULTS)"
# curl command would go here
