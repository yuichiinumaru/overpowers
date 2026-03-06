#!/bin/bash

# Prepare screenshots for analysis

if [ -z "$1" ]; then
    echo "Usage: $0 <directory_with_screenshots>"
    exit 1
fi

DIR=$1

echo "Screenshots found in $DIR:"
FILES=$(ls "$DIR"/*.{png,jpg,jpeg} 2>/dev/null)

if [ -z "$FILES" ]; then
    echo "No screenshots found."
    exit 1
fi

for f in $FILES; do
    echo "- $f"
done

echo -e "\nStarter Prompt for Coordinator Agent:"
echo "--------------------------------------"
echo "I have screenshots in $DIR. Please start the multi-agent analysis pipeline for these files:"
for f in $FILES; do
    echo "Screenshot: $f"
done
echo "--------------------------------------"
