#!/bin/bash
# Script to clean up integrated Jules branches and worktrees

JULES_DIR=".jules"
INTEGRATED_LIST="$JULES_DIR/integrated-branches.txt"
HARVESTED_DIR="$JULES_DIR/harvested"
ARCHIVED_DIR="$JULES_DIR/archived"

if [ ! -f "$INTEGRATED_LIST" ]; then
    echo "No integrated branches list found at $INTEGRATED_LIST"
    exit 0
fi

mkdir -p "$ARCHIVED_DIR"

echo "Cleaning up integrated branches..."

while IFS= read -r branch; do
    echo "Processing $branch..."
    
    # Remove worktree if it exists
    if [ -d "branches/$branch" ]; then
        git worktree remove "branches/$branch" 2>/dev/null
        echo "  - Removed worktree: branches/$branch"
    fi
    
    # Move harvested record to archived
    if [ -f "$HARVESTED_DIR/${branch}.md" ]; then
        mv "$HARVESTED_DIR/${branch}.md" "$ARCHIVED_DIR/"
        echo "  - Archived record: ${branch}.md"
    fi
    
done < "$INTEGRATED_LIST"

# Clear the list
> "$INTEGRATED_LIST"

echo "✅ Cleanup complete."
