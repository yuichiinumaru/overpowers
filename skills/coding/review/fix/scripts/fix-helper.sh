#!/bin/bash
# Helper script to fix lint and formatting errors

echo "Running prettier to fix formatting..."
yarn prettier

echo "Running linc to check for remaining lint issues..."
yarn linc

if [ $? -eq 0 ]; then
    echo "All checks passed successfully."
else
    echo "Warning: There are remaining manual fixes needed. Please review the output above."
fi
