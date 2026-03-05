#!/bin/bash
# publish-workflow.sh - Hugging Face paper publishing workflow helper

ARXIV_ID=$1
REPO_ID=$2
REPO_TYPE=${3:-"model"}

if [ -z "$ARXIV_ID" ] || [ -z "$REPO_ID" ]; then
    echo "Usage: $0 <arxiv_id> <repo_id> [repo_type]"
    echo "Example: $0 2301.12345 username/model-name"
    exit 1
fi

echo "Step 1: Indexing paper..."
python3 scripts/paper_manager.py index --arxiv-id "$ARXIV_ID"

echo "Step 2: Linking to $REPO_TYPE..."
python3 scripts/paper_manager.py link --repo-id "$REPO_ID" --repo-type "$REPO_TYPE" --arxiv-id "$ARXIV_ID"

echo "Workflow complete."
