#!/bin/bash
set -e

echo "Getting git SHAs for Code Review..."

HEAD_SHA=$(git rev-parse HEAD)
BASE_SHA=$(git merge-base HEAD origin/main 2>/dev/null || git rev-parse HEAD~1)

echo "HEAD_SHA: $HEAD_SHA"
echo "BASE_SHA: $BASE_SHA"
echo ""
echo "You can use these SHAs to request a code review."
