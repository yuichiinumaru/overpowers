#!/usr/bin/env bash

# Helper script for tracking active Foodora orders via ordercli
# Usage: ./track-foodora-orders.sh

if ! command -v ordercli &> /dev/null; then
    echo "ordercli command not found. Please install it first."
    exit 1
fi

echo "Tracking active Foodora orders..."
ordercli foodora orders --watch
