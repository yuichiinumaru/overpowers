#!/bin/bash
# setup-github-automation.sh

echo "🚀 Setting up GitHub workflow automation..."

# Verify GitHub CLI
if ! gh auth status >/dev/null 2>&1; then
  echo "❌ GitHub CLI not authenticated. Please run 'gh auth login' first."
  exit 1
fi

# Create workflow directory
mkdir -p .github/workflows

# Generate initial workflow
echo "🔍 Analyzing codebase and generating optimal pipeline..."
npx ruv-swarm actions generate-workflow \
  --analyze-codebase \
  --create-optimal-pipeline > .github/workflows/ci.yml

if [ $? -eq 0 ]; then
  echo "✅ GitHub workflow automation setup complete: .github/workflows/ci.yml"
else
  echo "❌ Failed to generate workflow automatically."
fi
