#!/bin/bash
# Find duplicate files based on MD5 hash

if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

TARGET_DIR="$1"

echo "Searching for duplicates in $TARGET_DIR..."
find "$TARGET_DIR" -type f -exec md5sum {} + | sort | uniq -w32 -dD
