#!/bin/bash
# Verify GitHub CLI installation and authentication

if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) could not be found."
    echo "Please install it from https://cli.github.com/"
else
    echo "Checking GitHub authentication..."
    if gh auth status &> /dev/null; then
        echo "✅ GitHub CLI is authenticated."
    else
        echo "❌ GitHub CLI is not authenticated."
        echo "Run: gh auth login"
    fi
fi
