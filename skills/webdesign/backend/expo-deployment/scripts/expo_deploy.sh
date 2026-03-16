#!/usr/bin/env bash

# Expo EAS Deployment Trigger Helper
# Usage: ./expo_deploy.sh production ios

PROFILE=${1:-production}
PLATFORM=${2:-all}

echo "Starting EAS Build for profile: $PROFILE on platform: $PLATFORM"

# Checking for eas-cli
if ! command -v eas &> /dev/null; then
    echo "eas-cli not found. Installing..."
    npm install -g eas-cli
fi

echo "Running command: eas build --profile $PROFILE --platform $PLATFORM --non-interactive"
# Uncomment the line below to actually run it
# eas build --profile $PROFILE --platform $PLATFORM --non-interactive

echo "Deployment triggered successfully (mocked)."
