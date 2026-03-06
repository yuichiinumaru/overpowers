#!/bin/bash
# Script to list Jules account usage and rotation status

ACCOUNTS_FILE=".jules/accounts.json"

if [ ! -f "$ACCOUNTS_FILE" ]; then
    echo "Error: $ACCOUNTS_FILE not found."
    exit 1
fi

echo "Jules Account Status:"
echo "-------------------"
cat "$ACCOUNTS_FILE" | jq -r '.accounts[] | "\(.email): \(.daily_used)/100 daily, \(.concurrent)/15 concurrent"'
echo "-------------------"
echo "Last reset: $(cat "$ACCOUNTS_FILE" | jq -r '.last_reset')"
