#!/bin/bash
# Run tests for both frontend and backend

echo "Running Frontend Tests..."
cd frontend && npm test && cd ..

echo "Running Backend Tests..."
cd backend && poetry run pytest && cd ..

echo "Tests complete."
