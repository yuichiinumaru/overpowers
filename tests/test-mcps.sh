#!/usr/bin/env bash

echo -e "\033[1;36mTesting MCP Configurations...\033[0m"

echo ""
echo -e "\033[1;33m=== Kilo Code (kilo mcp list) ===\033[0m"
if command -v kilo &> /dev/null; then
    kilo mcp list
else
    echo "kilo command not found. Skipping."
fi

echo ""
echo -e "\033[1;33m=== OpenCode (opencode mcp list) ===\033[0m"
if command -v opencode &> /dev/null; then
    opencode mcp list
else
    echo "opencode command not found. Skipping."
fi

echo ""
echo -e "\033[1;33m=== Gemini CLI (gemini mcp list) ===\033[0m"
if command -v gemini &> /dev/null; then
    gemini mcp list
else
    echo "gemini command not found. Skipping."
fi

echo ""
echo -e "\033[1;32mTest complete.\033[0m"
