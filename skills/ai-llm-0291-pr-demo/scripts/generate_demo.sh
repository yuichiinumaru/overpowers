#!/bin/bash

# PR Demo Helper Script
# This script helps record and convert a terminal demo using asciinema and agg.

set -e

DEMO_NAME=${1:-"demo"}
CAST_FILE="${DEMO_NAME}.cast"
GIF_FILE="${DEMO_NAME}.gif"

echo "=== PR Demo Recorder ==="
echo "1. Script your demo first (20-30s recommended)."
echo "2. Terminal will be set to 100x24."
echo "3. Press ENTER to start recording."
echo "4. Press Ctrl+D or type 'exit' to stop."
read -p "Ready?"

# Set environment
export PS1='$ '
export TERM=xterm-256color

# Record
asciinema rec "$CAST_FILE" --cols 100 --rows 24

echo "=== Conversion ==="
echo "Converting $CAST_FILE to $GIF_FILE..."

# Check if agg is installed
if command -v agg &> /dev/null; then
    agg --speed 1.5 --font-size 14 "$CAST_FILE" "$GIF_FILE"
    echo "Done! GIF saved to $GIF_FILE"
    ls -lh "$GIF_FILE"
else
    echo "agg is not installed. You can convert manually later or install it via:"
    echo "cargo install --git https://github.com/asciinema/agg"
fi
