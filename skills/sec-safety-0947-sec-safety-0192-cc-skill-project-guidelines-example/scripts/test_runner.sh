#!/bin/bash
# test_runner.sh - Script to run tests as per project guidelines

if [ "$1" == "backend" ]; then
    echo "Running backend tests..."
    poetry run pytest tests/
elif [ "$1" == "backend-cov" ]; then
    echo "Running backend tests with coverage..."
    poetry run pytest tests/ --cov=. --cov-report=html
elif [ "$1" == "frontend" ]; then
    echo "Running frontend tests..."
    npm run test
elif [ "$1" == "frontend-cov" ]; then
    echo "Running frontend tests with coverage..."
    npm run test -- --coverage
elif [ "$1" == "frontend-e2e" ]; then
    echo "Running frontend E2E tests..."
    npm run test:e2e
else
    echo "Usage: $0 {backend|backend-cov|frontend|frontend-cov|frontend-e2e}"
    # removed exit 1 for safety
fi
