#!/bin/bash
gh auth status > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ GitHub CLI is authenticated."
    gh auth status
else
    echo "❌ GitHub CLI is NOT authenticated. Please run 'gh auth login'."
    exit 1
fi
