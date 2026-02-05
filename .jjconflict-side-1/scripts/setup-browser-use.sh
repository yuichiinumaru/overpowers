#!/bin/bash
# Install browser-use and its dependencies

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv not found. Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

# Install browser-use
echo "Installing browser-use..."
uv pip install browser-use

# Install playwright browsers
echo "Installing Playwright browsers..."
uv run playwright install chromium

echo "Installation complete. You can now use the 'browser-use' command."
