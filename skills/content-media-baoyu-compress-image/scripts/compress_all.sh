#!/usr/bin/env bash
# Batch compress images in a directory

if [ -z "$1" ]; then
    echo "Usage: compress_all.sh <directory>"
    exit 1
fi

DIR=$1

find "$1" -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) | while read img; do
    bun "$(dirname "$0")/main.ts" "$img"
done
