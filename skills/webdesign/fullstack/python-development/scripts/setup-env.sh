#!/usr/bin/env bash
# Helper script to set up a modern Python virtual environment
echo "Setting up Python environment..."
if command -v uv &> /dev/null; then
    uv venv
    echo "Created virtual environment with uv."
    echo "Activate with: source .venv/bin/activate"
elif command -v python3 &> /dev/null; then
    python3 -m venv .venv
    echo "Created virtual environment with python3 -m venv."
    echo "Activate with: source .venv/bin/activate"
else
    echo "⚠️ Python 3 or uv is not installed."
fi
