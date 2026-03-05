#!/bin/bash
# Script to clean iOS project artifacts

echo "Cleaning iOS project artifacts..."

# Clean DerivedData
if [ -d "$HOME/Library/Developer/Xcode/DerivedData" ]; then
    echo "Cleaning DerivedData..."
    rm -rf "$HOME/Library/Developer/Xcode/DerivedData"
    echo "✅ DerivedData cleaned."
fi

# Clean build artifacts if in a project directory
if [ -d "build" ]; then
    echo "Cleaning local build directory..."
    rm -rf build
    echo "✅ local build directory cleaned."
fi

# Clean CocoaPods cache if Pods directory exists
if [ -d "Pods" ]; then
    echo "Cleaning CocoaPods artifacts..."
    rm -rf Pods
    rm -rf Podfile.lock
    echo "✅ Pods and Podfile.lock removed."
    echo "ℹ️ Run 'pod install' to reinstall dependencies."
fi

# Clean SPM cache
if [ -d ".swiftpm" ]; then
    echo "Cleaning Swift Package Manager cache..."
    rm -rf .swiftpm
    echo "✅ .swiftpm directory removed."
fi

echo "Clean complete."
