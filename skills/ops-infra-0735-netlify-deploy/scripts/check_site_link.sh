#!/bin/bash
STATUS=$(npx netlify status)
echo "$STATUS" | grep -q "Site id:"
if [ $? -eq 0 ]; then
    echo "✅ Site is linked to Netlify."
    SITE_NAME=$(echo "$STATUS" | grep "Site name:" | awk '{print $NF}')
    SITE_URL=$(echo "$STATUS" | grep "Site url:" | awk '{print $NF}')
    echo "Site Name: $SITE_NAME"
    echo "Site URL: $SITE_URL"
else
    echo "❌ No site linked. Please run 'npx netlify link' or 'npx netlify init'."
    exit 1
fi
