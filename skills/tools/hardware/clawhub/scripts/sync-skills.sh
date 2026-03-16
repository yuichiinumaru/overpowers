#!/bin/bash

# Check if clawhub is installed
if ! command -v clawhub &> /dev/null; then
    echo "Error: clawhub CLI not found. Install it with: npm i -g clawhub"
    exit 1
fi

echo "Syncing all skills with ClawHub..."
clawhub update --all --no-input --force

echo "Skills sync complete."
