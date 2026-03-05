#!/bin/bash
# Build design tokens using Style Dictionary

if command -v style-dictionary &> /dev/null; then
    echo "Running Style Dictionary..."
    style-dictionary build --config style-dictionary.config.json
else
    echo "Style Dictionary not found. Please install it with:"
    echo "npm install -g style-dictionary"
    echo ""
    echo "Or run it via npx:"
    echo "npx style-dictionary build --config style-dictionary.config.json"
fi
