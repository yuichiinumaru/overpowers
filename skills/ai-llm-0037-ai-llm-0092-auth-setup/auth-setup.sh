#!/bin/bash
# Auth Monster Setup Wizard
# Usage: ./auth-setup.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check for node_modules
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install --silent
fi

# Run the TUI wizard
npx ts-node tui-wizard.ts
