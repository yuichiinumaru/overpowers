#!/bin/bash
npx netlify status | grep -q "Logged in as"
if [ $? -eq 0 ]; then
    echo "✅ Netlify CLI is authenticated."
    npx netlify status
else
    echo "❌ Netlify CLI is NOT authenticated. Please run 'npx netlify login'."
    exit 1
fi
