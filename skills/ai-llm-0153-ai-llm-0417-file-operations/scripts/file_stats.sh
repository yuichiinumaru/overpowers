#!/bin/bash
FILE=$1
if [ -z "$FILE" ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "❌ Error: File not found: $FILE"
    exit 1
fi

echo "--- File Statistics for: $FILE ---"
echo "Size: $(du -h "$FILE" | cut -f1)"
echo "Lines: $(wc -l < "$FILE")"
echo "Words: $(wc -w < "$FILE")"
echo "Characters: $(wc -c < "$FILE")"
echo "Last Modified: $(stat -c %y "$FILE" 2>/dev/null || stat -f %Sm "$FILE")"
echo "--------------------------------"
