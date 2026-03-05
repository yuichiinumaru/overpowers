#!/bin/bash
if [ -n "$RENDER_API_KEY" ]; then
    echo "✅ RENDER_API_KEY is set."
else
    echo "⚠️ RENDER_API_KEY is not set in environment."
fi

render whoami -o json > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Render CLI is authenticated."
    render whoami
else
    echo "❌ Render CLI is NOT authenticated. Please run 'render login' or set RENDER_API_KEY."
    exit 1
fi
