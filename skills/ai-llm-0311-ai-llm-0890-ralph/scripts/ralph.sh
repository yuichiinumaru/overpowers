#!/bin/bash
# Ralph utility script to archive runs and reset progress

set -e

PROJECT_DIR=${1:-"."}
PRD_FILE="$PROJECT_DIR/prd.json"
PROGRESS_FILE="$PROJECT_DIR/progress.txt"

if [ ! -f "$PRD_FILE" ]; then
    echo "No prd.json found in $PROJECT_DIR"
else
    # Extract branchName using python/json module or grep
    BRANCH_NAME=$(grep -o '"branchName": *"[^"]*"' "$PRD_FILE" | cut -d'"' -f4 | sed 's/ralph\///g' || echo "unknown")
    DATE_STR=$(date +%Y-%m-%d)
    ARCHIVE_DIR="$PROJECT_DIR/archive/$DATE_STR-$BRANCH_NAME"

    mkdir -p "$ARCHIVE_DIR"
    cp "$PRD_FILE" "$ARCHIVE_DIR/"
    if [ -f "$PROGRESS_FILE" ]; then
        cp "$PROGRESS_FILE" "$ARCHIVE_DIR/"
        # Reset progress.txt
        echo "# Ralph Progress" > "$PROGRESS_FILE"
    fi

    echo "Archived previous run to $ARCHIVE_DIR"
fi
