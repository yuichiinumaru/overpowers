#!/usr/bin/env bash
# Helper script to verify Railway CLI is installed and authenticated
echo "Checking Railway CLI..."
if command -v railway &> /dev/null; then
    echo "✅ Railway CLI is installed."
    railway status
else
    echo "⚠️ Railway CLI is not installed."
    echo "Please install it: npm i -g @railway/cli or brew install bvm"
fi
