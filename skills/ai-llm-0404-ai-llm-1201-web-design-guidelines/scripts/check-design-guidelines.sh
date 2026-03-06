#!/bin/bash
# Web Design Guidelines Checker
TARGET_DIR="${1:-.}"
echo "Checking web design guidelines in $TARGET_DIR..."
grep -rn "class=" "$TARGET_DIR" | wc -l | awk '{print $1 " class definitions found. Ensure they follow the design system."}'
