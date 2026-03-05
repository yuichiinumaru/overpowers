#!/bin/bash
# Helper for Upgrading Expo SDK

COMMAND=$1
shift

case $COMMAND in
  "check_version")
    if [ -f package.json ]; then
      grep "\"expo\":" package.json
    else
      echo "package.json not found"
    fi
    ;;
  "upgrade")
    VERSION=$1
    echo "Upgrading to Expo SDK $VERSION..."
    npx expo install expo@$VERSION --fix
    ;;
  "fix_dependencies")
    echo "Running npx expo install --fix..."
    npx expo install --fix
    ;;
  "clear_cache")
    echo "Cleaning expo and watchman cache..."
    watchman watch-del-all
    rm -rf node_modules
    rm -rf .expo
    npm install
    ;;
  *)
    echo "Usage: $0 {check_version|upgrade <version>|fix_dependencies|clear_cache}"
    exit 1
    ;;
esac
