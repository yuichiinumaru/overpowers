#!/bin/bash
# Check for local repo, or clone it if missing

LIBRARY=$1
REPO_URL=$2
BASE_DIR="/tmp/cc-repos"

if [ -z "$LIBRARY" ]; then
    echo "Usage: $0 <library-name> [repo-url]"
    exit 1
fi

mkdir -p "$BASE_DIR"

if [ -d "$BASE_DIR/$LIBRARY" ]; then
    echo "Library $LIBRARY already exists in $BASE_DIR"
    exit 0
fi

if [ -z "$REPO_URL" ]; then
    echo "Repository URL required for cloning."
    exit 1
fi

echo "Cloning $LIBRARY from $REPO_URL..."
git clone "$REPO_URL" "$BASE_DIR/$LIBRARY"
