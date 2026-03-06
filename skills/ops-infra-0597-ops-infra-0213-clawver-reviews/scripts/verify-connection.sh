#!/bin/bash
# Verify Clawver API connection

if [ -z "$CLAW_API_KEY" ]; then
    echo "❌ Missing required environment variable: CLAW_API_KEY"
    echo "Please set it before running the script."
else
    echo "Checking Clawver connection..."
    response=$(curl -s -o /dev/null -w "%{http_code}" "https://api.clawver.store/v1/stores/me/reviews" -H "Authorization: Bearer $CLAW_API_KEY")

    if [ "$response" == "200" ]; then
        echo "✅ Successfully connected to Clawver API."
    elif [ "$response" == "401" ] || [ "$response" == "403" ]; then
        echo "❌ Authentication failed. Please check your CLAW_API_KEY."
    else
        echo "❌ Failed to connect to Clawver API (HTTP $response)."
    fi
fi
