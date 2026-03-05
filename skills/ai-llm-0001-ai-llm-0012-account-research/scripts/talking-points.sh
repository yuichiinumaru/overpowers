#!/bin/bash

# Script to extract talking points from research data.
# Usage: ./talking-points.sh research_file.md

RESEARCH_FILE=$1

if [ -z "$RESEARCH_FILE" ] || [ ! -f "$RESEARCH_FILE" ]; then
  echo "Usage: $0 research_file.md"
  exit 1
fi

echo "Extracting Talking Points from $RESEARCH_FILE..."
echo "--------------------------------"

grep -A 5 "Talking Points:" "$RESEARCH_FILE" | grep -v "\-\-" | grep -v "Talking Points:" | sed 's/^[[:space:]]*//' | sed 's/^- //' | grep .
