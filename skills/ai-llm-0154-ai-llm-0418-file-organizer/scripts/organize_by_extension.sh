#!/bin/bash
# Organize files into subdirectories based on their extension

if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

TARGET_DIR="$1"
cd "$TARGET_DIR" || exit

for file in *; do
    if [ -f "$file" ]; then
        ext="${file##*.}"
        if [ "$file" = "$ext" ]; then
            ext="no_extension"
        fi
        mkdir -p "$ext"
        mv "$file" "$ext/"
        echo "Moved $file to $ext/"
    fi
done
