#!/bin/bash
# Fetch llms.txt for a given library, prioritizing context7.com

LIB=$1
if [ -z "$LIB" ]; then
    echo "Usage: $0 <org/repo>"
    exit 1
fi

# Try context7.com
URL="https://context7.com/$LIB/llms.txt"
echo "Trying context7.com: $URL"
if curl -s -f "$URL" -o /tmp/llms.txt; then
    echo "Found at context7.com!"
    cat /tmp/llms.txt
    exit 0
fi

# Fallback: Guess common official locations if it's a domain or if we can extract one
# This is a simple placeholder for more complex guessing logic
echo "llms.txt not found at context7.com. Try traditional search."
exit 1
