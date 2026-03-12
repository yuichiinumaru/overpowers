#!/bin/bash

# Extract Error Codes Helper
# Requirement: yarn

echo "Running yarn extract-errors..."
yarn extract-errors

echo ""
echo "Checking for unassigned error codes..."
# This is a placeholder for a more specific check if known
grep -r "TODO: assign error code" . | grep -v "node_modules"

echo ""
echo "Verification complete."
