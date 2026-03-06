#!/bin/bash
# Fetch commits since last tag or for a specific range

SINCE=${1:-$(git describe --tags --abbrev=0 2>/dev/null)}
UNTIL=${2:-"HEAD"}

if [ -z "$SINCE" ]; then
    echo "No tags found. Fetching all commits."
    git log --pretty=format:"* %s (%h)" $UNTIL
else
    echo "Fetching commits between $SINCE and $UNTIL"
    git log --pretty=format:"* %s (%h)" $SINCE..$UNTIL
fi
