#!/bin/bash
# Jules Harvest Script - optimized for local analysis

set -e

BRANCHES_DIR="branches"
JULES_DIR=".jules"
HARVESTED_DIR="$JULES_DIR/harvested"

# Ensure directories exist
mkdir -p "$BRANCHES_DIR" "$HARVESTED_DIR"

# Fetch all
echo "📥 Fetching all branches from origin..."
git fetch --all --prune

# Get Jules branches
JULES_BRANCHES=$(git branch -r | grep 'origin/jules/' | sed 's|origin/||' | tr -d ' ')

if [ -z "$JULES_BRANCHES" ]; then
    echo "No Jules branches found on remote."
    exit 0
fi

echo "Found Jules branches to harvest:"
echo "$JULES_BRANCHES"

# Process each branch
for BRANCH in $JULES_BRANCHES; do
    # Replace slashes with hyphens for folder names
    SAFE_NAME=$(echo "$BRANCH" | tr '/' '-')
    WORKTREE_PATH="$BRANCHES_DIR/$SAFE_NAME"
    
    if [ -d "$WORKTREE_PATH" ]; then
        echo "⏭️  Skipping $BRANCH (already exists in $WORKTREE_PATH)"
        continue
    fi
    
    echo "🌾 Harvesting $BRANCH into $WORKTREE_PATH..."
    
    # Create worktree
    if git worktree add "$WORKTREE_PATH" "origin/$BRANCH" 2>/dev/null; then
        # Generate catalog entry
        COMMITS=$(git -C "$WORKTREE_PATH" log main..HEAD --oneline 2>/dev/null | wc -l || echo "?")
        STATS=$(git -C "$WORKTREE_PATH" diff main --stat 2>/dev/null | tail -1 || echo "unknown")
        
        cat > "$HARVESTED_DIR/$SAFE_NAME.md" << EOF
# Branch: $BRANCH

## Metadata
- **Harvested:** $(date -Iseconds)
- **Commits:** $COMMITS
- **Stats:** $STATS

## Worktree Path
\`$WORKTREE_PATH/\`

## Status
🟡 **Pending Triage** - Ready for local analysis
EOF
        echo "  ✅ Created worktree and catalog entry"
    else
        echo "  ❌ Failed to create worktree for $BRANCH"
    fi
done

echo ""
echo "✅ Harvest complete! Catalog updated in $HARVESTED_DIR"
