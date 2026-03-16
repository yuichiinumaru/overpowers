#!/bin/bash

# Memory Lite search helper
# Usage: ./memory_grep.sh "keyword"

if [ -z "$1" ]; then
    echo "Usage: $0 <keyword>"
    exit 1
fi

grep -r "$1" memory/ MEMORY.md 2>/dev/null
