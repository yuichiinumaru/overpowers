#!/bin/bash
# Pre-merge verification script
echo "Running tests before finishing development branch..."

if [ -f "package.json" ]; then
    npm test || { echo "Tests failed. Aborting merge."; exit 1; }
elif [ -f "Cargo.toml" ]; then
    cargo test || { echo "Tests failed. Aborting merge."; exit 1; }
elif [ -f "pytest.ini" ] || [ -f "pyproject.toml" ]; then
    pytest || { echo "Tests failed. Aborting merge."; exit 1; }
elif [ -f "go.mod" ]; then
    go test ./... || { echo "Tests failed. Aborting merge."; exit 1; }
else
    echo "No recognized test suite found. Proceed manually."
fi

echo "Tests passed."
