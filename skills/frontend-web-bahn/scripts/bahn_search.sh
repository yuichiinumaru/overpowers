#!/usr/bin/env bash
# Wrapper for bahn-cli search

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: bahn_search.sh <from> <to> [options]"
    exit 1
fi

FROM=$1
TO=$2
shift 2
OPTIONS=$@

# Assuming bahn-cli is in ~/Code/bahn-cli as per SKILL.md
cd ~/Code/bahn-cli 2>/dev/null || { echo "Error: bahn-cli not found in ~/Code/bahn-cli"; exit 1; }

node index.js search "$FROM" "$TO" $OPTIONS
