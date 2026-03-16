#!/bin/bash
# Find files not modified in the last N days

if [ -z "$2" ]; then
    echo "Usage: $0 <directory> <days>"
    exit 1
fi

TARGET_DIR="$1"
DAYS="$2"

echo "Files in $TARGET_DIR not modified in the last $DAYS days:"
find "$TARGET_DIR" -type f -mtime +"$DAYS" -ls
