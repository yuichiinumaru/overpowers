#!/bin/bash
# Pre-deployment checklist

echo "Checking Frontend Build..."
cd frontend && npm run build && cd ..

echo "Checking Backend Environment..."
if [ ! -f backend/.env ]; then
    echo "Warning: backend/.env not found!"
fi

echo "Checking Frontend Environment..."
if [ ! -f frontend/.env.local ]; then
    echo "Warning: frontend/.env.local not found!"
fi

echo "Running full test suite..."
./scripts/run_tests.sh

echo "Pre-deployment check complete."
