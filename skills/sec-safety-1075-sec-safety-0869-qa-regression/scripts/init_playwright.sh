#!/bin/bash
# Initialize Playwright for QA Regression testing

echo "--- Initializing Playwright ---"

if [ ! -f package.json ]; then
    echo "Creating package.json..."
    npm init -y
fi

echo "Installing dependencies..."
npm install playwright @playwright/test

echo "Installing Playwright browsers..."
npx playwright install

echo "Creating tests directory..."
mkdir -p tests/auth tests/dashboard tests/users tests/helpers

echo "Playwright initialization complete."
echo "You can now create your .spec.ts files in the tests/ directory."
