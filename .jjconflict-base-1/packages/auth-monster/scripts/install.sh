#!/bin/bash

# OpenCode Auth Monster - One-line Installer
# Usage: curl -sSL https://raw.githubusercontent.com/username/opencode-auth-monster/main/scripts/install.sh | bash

set -e

echo "👹 OpenCode Auth Monster Installer"
echo "----------------------------------"

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Error: Node.js is not installed."
    exit 1
fi

# Check for npm
if ! command -v npm &> /dev/null; then
    echo "❌ Error: npm is not installed."
    exit 1
fi

# Create temporary directory
TEMP_DIR=$(mktemp -d)
echo "📂 Created temporary directory: $TEMP_DIR"

# Clone repository (assuming public for now, or user has access)
echo "📥 Cloning repository..."
git clone https://github.com/opencode-monster/auth-monster.git "$TEMP_DIR" --depth 1 || {
    echo "❌ Failed to clone repository. Make sure you have git installed and access to the repo."
    exit 1
}

cd "$TEMP_DIR"

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Build project
echo "🔨 Building project..."
npm run build

# Install globally
echo "🚀 Installing globally..."
sudo npm install -g . || npm install -g .

echo "----------------------------------"
echo "✅ Installation complete!"
echo "Try running: opencode-monster --help"

# Optional Onboarding
read -p "👹 Would you like to run the onboarding wizard now? (y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    opencode-monster onboard
fi

# Cleanup
rm -rf "$TEMP_DIR"
