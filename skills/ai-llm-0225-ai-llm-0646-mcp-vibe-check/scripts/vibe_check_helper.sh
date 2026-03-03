#!/bin/bash

# Vibe Check MCP helper script
# Usage: ./vibe_check_helper.sh request.json

if [ -z "$1" ]; then
    echo "Usage: $0 <request.json>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: File $1 not found."
    exit 1
fi

# Determine script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SKILL_ROOT="$(dirname "$SCRIPT_DIR")"

# Pipe request to node server
node "$SKILL_ROOT/build/index.js" < "$1"
