#!/bin/bash
# Install Scientify npm package and update OpenClaw config

echo "📦 Installing scientify globally..."
npm install -g scientify

echo "⚙️ Updating OpenClaw config..."
# Note: This is a placeholder for actual config update logic
# It assumes a standard location for openclaw config
CONFIG_PATH="$HOME/.openclaw/config.json"
if [ -f "$CONFIG_PATH" ]; then
    if ! grep -q "scientify" "$CONFIG_PATH"; then
        sed -i 's/"plugins": \[/"plugins": ["scientify", /' "$CONFIG_PATH"
        echo "✅ Added scientify to $CONFIG_PATH"
    else
        echo "ℹ️ Scientify already in config"
    fi
else
    echo "⚠️ OpenClaw config not found at $CONFIG_PATH. Please add manually:"
    echo '{"plugins": ["scientify"]}'
fi
