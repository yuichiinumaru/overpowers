#!/bin/bash
# Install bmad-method globally

echo "Installing bmad-method..."
if npm install -g bmad-method || npx bmad-method@latest install; then
    echo "✅ bmad-method installed successfully."
else
    echo "❌ Failed to install bmad-method."
fi
