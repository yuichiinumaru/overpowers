#!/bin/bash
# Find top 20 largest files in a directory

if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

TARGET_DIR="$1"

echo "Top 20 largest files in $TARGET_DIR:"
du -ah "$TARGET_DIR" | sort -rh | head -n 20
