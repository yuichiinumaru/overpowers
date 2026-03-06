#!/bin/bash
# Script to check iOS development environment

echo "Checking iOS development environment..."

# Check for Xcode
if xcode-select -p &>/dev/null; then
    echo "✅ Xcode is installed at: $(xcode-select -p)"
    xcodebuild -version
else
    echo "❌ Xcode is not installed or xcode-select is not configured."
fi

# Check for Swift
if command -v swift &>/dev/null; then
    echo "✅ Swift is installed: $(swift --version | head -n 1)"
else
    echo "❌ Swift is not installed."
fi

# Check for CocoaPods
if command -v pod &>/dev/null; then
    echo "✅ CocoaPods is installed: $(pod --version)"
else
    echo "ℹ️ CocoaPods is not installed (optional if using SPM)."
fi

# Check for SwiftLint
if command -v swiftlint &>/dev/null; then
    echo "✅ SwiftLint is installed: $(swiftlint version)"
else
    echo "ℹ️ SwiftLint is not installed."
fi

# Check for Homebrew
if command -v brew &>/dev/null; then
    echo "✅ Homebrew is installed: $(brew --version | head -n 1)"
else
    echo "ℹ️ Homebrew is not installed."
fi

echo "Environment check complete."
