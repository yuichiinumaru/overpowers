#!/bin/bash
# Check permissions of sensitive directories to ensure Principle of Least Privilege
SENSITIVE_PATHS=(".git" ".env" "config" "scripts" "hooks")

echo "Checking sensitive path permissions..."
for path in "${SENSITIVE_PATHS[@]}"; do
    if [ -e "$path" ]; then
        perms=$(stat -c "%a" "$path")
        echo "Path: $path | Permissions: $perms"
        # Warn if world-writable or group-writable
        if [[ "$perms" =~ .*[2367]. ]]; then
            echo "  [WARNING] $path has broad group write permissions."
        fi
        if [[ "$perms" =~ .*.[2367] ]]; then
            echo "  [WARNING] $path is world-writable!"
        fi
    fi
done
