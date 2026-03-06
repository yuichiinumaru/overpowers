#!/bin/bash
# Python Expert QA Helper
# This script runs basic quality checks on Python files using ruff and mypy.

TARGET=${1:-"."}

echo "Starting Python quality checks for: $TARGET"

# Check if ruff is installed
if command -v ruff &> /dev/null; then
    echo "[1/2] Running ruff check..."
    ruff check "$TARGET"
else
    echo "[!] ruff not found. Install it with: pip install ruff"
fi

# Check if mypy is installed
if command -v mypy &> /dev/null; then
    echo "[2/2] Running mypy type check..."
    mypy "$TARGET"
else
    echo "[!] mypy not found. Install it with: pip install mypy"
fi

echo "Python quality checks completed."
