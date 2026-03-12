#!/bin/bash
# Helper script to run pre-verification steps (prettier and lint)
# Usage: ./verify.sh

echo "Running yarn prettier..."
yarn prettier
if [ $? -ne 0 ]; then
  echo "Prettier formatting failed. Please fix before continuing."
  exit 1
fi

echo "Running yarn linc..."
yarn linc
if [ $? -ne 0 ]; then
  echo "Linting failed. Please fix before continuing."
  exit 1
fi

echo "Pre-verification steps passed successfully."
