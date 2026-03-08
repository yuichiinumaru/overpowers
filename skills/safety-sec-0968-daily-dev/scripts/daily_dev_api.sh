#!/bin/bash
# daily_dev_api.sh - Helper script for Daily.dev API requests

ENDPOINT=${1:-"/feeds/foryou"}
TOKEN=$(security find-generic-password -a "$USER" -s "daily-dev-api" -w 2>/dev/null)

if [ -z "$TOKEN" ]; then
    echo "Warning: Daily.dev token not found in keychain."
    echo "Set it using: security add-generic-password -a \$USER -s daily-dev-api -w 'your_token'"
    echo "Proceeding without authentication (public endpoints only)..."
fi

if [ -n "$TOKEN" ]; then
    curl -s "https://api.daily.dev/public/v1$ENDPOINT" \
         -H "Authorization: Bearer $TOKEN" \
         -H "Content-Type: application/json"
else
    curl -s "https://api.daily.dev/public/v1$ENDPOINT" \
         -H "Content-Type: application/json"
fi

echo ""
