#!/bin/bash
# List all cloned repositories in the standard location

BASE_DIR="/tmp/cc-repos"

if [ -d "$BASE_DIR" ]; then
    echo "Cloned repositories in $BASE_DIR:"
    ls -F "$BASE_DIR"
else
    echo "No repositories cloned yet. Directory $BASE_DIR does not exist."
fi
