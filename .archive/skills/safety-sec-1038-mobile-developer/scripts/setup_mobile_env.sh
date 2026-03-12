#!/bin/bash
# Check for common mobile development tools
echo "Checking mobile development environment..."
command -v xcodebuild >/dev/null 2>&1 && echo "[OK] xcodebuild" || echo "[MISSING] xcodebuild"
command -v adb >/dev/null 2>&1 && echo "[OK] adb (Android Debug Bridge)" || echo "[MISSING] adb"
command -v flutter >/dev/null 2>&1 && echo "[OK] flutter" || echo "[MISSING] flutter"
command -v react-native >/dev/null 2>&1 && echo "[OK] react-native" || echo "[MISSING] react-native"
