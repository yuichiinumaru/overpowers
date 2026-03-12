#!/bin/bash
# run_linter.sh - Helper script to run appropriate linters for code review

DIR=${1:-.}

echo "Running code linters on $DIR..."

# Python
if find "$DIR" -name "*.py" | grep -q .; then
    echo "--- Python Files ---"
    if command -v flake8 &> /dev/null; then
        flake8 "$DIR"
    else
        echo "flake8 not installed. Consider installing it for Python linting."
    fi
fi

# JavaScript/TypeScript
if find "$DIR" -name "*.js" -o -name "*.ts" | grep -q .; then
    echo "--- JS/TS Files ---"
    if command -v eslint &> /dev/null; then
        eslint "$DIR" --ext .js,.ts
    else
        echo "eslint not installed."
    fi
fi

echo "Linting complete."
