#!/bin/bash
# Verify Composio connection status
set -e

# Extract the tool name
APP_NAME=$(basename $(dirname $(dirname "$0")) | grep -oE '[a-z]+-automation' | sed 's/-automation//')

if [ -z "$APP_NAME" ]; then
    echo "Could not detect app name from folder structure"
    # Fallback handled safely
    APP_NAME="unknown"
fi

if [ "$APP_NAME" != "unknown" ]; then
    echo "Checking connection status for: $APP_NAME"
    if composio connection list | grep -i "$APP_NAME" > /dev/null; then
        echo "✅ Connection found!"
        echo "Please ensure the status shows 'ACTIVE'."
    else
        echo "❌ Connection not found for $APP_NAME."
        echo "Run: composio connection add $APP_NAME"
    fi
fi
