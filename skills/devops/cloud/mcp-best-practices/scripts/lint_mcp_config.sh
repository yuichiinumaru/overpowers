#!/bin/bash
# Simple linter for MCP configuration patterns
config_file=$1

if [ -z "$config_file" ]; then
    echo "Usage: $0 <mcp_config.json>"
    return 1 2>/dev/null || true
fi

if ! jq -e '.' "$config_file" >/dev/null 2>&1; then
    echo "Invalid JSON format in $config_file"
    return 1 2>/dev/null || true
fi
echo "MCP configuration $config_file is valid JSON."
