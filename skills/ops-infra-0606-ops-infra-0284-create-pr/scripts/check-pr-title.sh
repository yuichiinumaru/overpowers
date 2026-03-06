#!/bin/bash
# A script to validate PR titles based on the skill documentation
TITLE="$1"
if [[ -z "$TITLE" ]]; then
  echo "Usage: $0 \"<type>(<scope>): <summary>\""
  exit 1
fi

REGEX="^(feat|fix|perf|test|docs|refactor|build|ci|chore|style|revert)(\([a-z0-9-]+\))?: .+$"

if [[ $TITLE =~ $REGEX ]]; then
  echo "✅ Valid PR title: $TITLE"
  exit 0
else
  echo "❌ Invalid PR title: $TITLE"
  echo "Format should be: <type>(<scope>): <summary>"
  echo "Valid types: feat, fix, perf, test, docs, refactor, build, ci, chore, style, revert"
  exit 1
fi
