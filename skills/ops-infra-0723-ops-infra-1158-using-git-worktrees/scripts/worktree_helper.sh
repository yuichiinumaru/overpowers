#!/bin/bash
# Helper for Using Git Worktrees

BRANCH_NAME=$1
if [ -z "$BRANCH_NAME" ]; then
  echo "Usage: $0 <branch_name> [path]"
  exit 1
fi

# Detect project name
PROJECT_NAME=$(basename "$(git rev-parse --show-toplevel 2>/dev/null)")
if [ -z "$PROJECT_NAME" ]; then
  echo "Error: Not in a git repository"
  exit 1
fi

# Path selection logic
LOCATION=".worktrees"
if [ ! -d "$LOCATION" ]; then
  LOCATION="worktrees"
fi

# Override with second argument if provided
if [ ! -z "$2" ]; then
  LOCATION=$2
fi

# Check if ignored (basic check)
if ! git check-ignore -q "$LOCATION" 2>/dev/null; then
  echo "Warning: $LOCATION is not ignored in .gitignore."
fi

WORKTREE_PATH="$LOCATION/$BRANCH_NAME"

echo "Creating worktree at $WORKTREE_PATH for branch $BRANCH_NAME..."
git worktree add "$WORKTREE_PATH" -b "$BRANCH_NAME"

cd "$WORKTREE_PATH" || exit 1

# Setup logic
if [ -f package.json ]; then
  echo "Found package.json, running npm install..."
  npm install
elif [ -f requirements.txt ]; then
  echo "Found requirements.txt, running pip install..."
  pip install -r requirements.txt
fi

echo "Worktree ready at $(pwd)"
