#!/usr/bin/env bash

# Fix Lint and Formatting

set -e

echo "Running prettier..."
yarn prettier

echo "Running linc..."
yarn linc

echo "Fixes applied and linting checked."
