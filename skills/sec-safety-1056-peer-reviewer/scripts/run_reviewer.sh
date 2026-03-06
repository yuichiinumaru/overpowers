#!/bin/bash

# Configuration: Update this path to where peer-reviewer is installed
REVIEWER_PATH="/Users/sschepis/Development/peer-reviewer"

if [ ! -d "$REVIEWER_PATH" ]; then
    echo "Error: Peer Reviewer directory not found at $REVIEWER_PATH"
    echo "Please update the REVIEWER_PATH in this script."
    exit 1
fi

INPUT="$1"

if [ -z "$INPUT" ]; then
    echo "Usage: $0 <path_to_paper_or_raw_text>"
    exit 1
fi

cd "$REVIEWER_PATH" || exit 1
node dist/index.js "$INPUT"
