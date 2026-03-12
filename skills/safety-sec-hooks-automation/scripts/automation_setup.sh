#!/bin/bash
set -euo pipefail

# Setup generic automation for git hooks
echo "[*] Setting up git hooks automation..."
if [ -d ".githooks" ]; then
    git config core.hooksPath .githooks
    echo "[+] Git hooks path set to .githooks"
else
    echo "[-] Directory .githooks not found. Create it first or run hook generator."
fi

# Ensure pre-commit/pre-push hooks are executable if they exist
for hook in .githooks/*; do
    if [ -f "\$hook" ]; then
        chmod +x "\$hook"
        echo "[+] Made \$hook executable"
    fi
done

echo "[*] Automation setup complete."
