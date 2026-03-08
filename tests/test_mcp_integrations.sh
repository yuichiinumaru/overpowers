#!/usr/bin/env bash

echo "==========================================="
echo "Running MCP Integration Verification Test"
echo "==========================================="

ERRORS=0

echo -n "Checking opencode-example.json for grep_app... "
if jq -e '.mcp.grep_app' opencode-example.json > /dev/null; then
    echo "[PASS]"
else
    echo "[FAIL]"
    ERRORS=1
fi

echo -n "Checking opencode-example.json for web_search... "
if jq -e '.mcp.web_search' opencode-example.json > /dev/null; then
    echo "[PASS]"
else
    echo "[FAIL]"
    ERRORS=1
fi

echo -n "Checking templates/mcp-antigravity.json for grep_app... "
if jq -e '.mcpServers.grep_app' templates/mcp-antigravity.json > /dev/null; then
    echo "[PASS]"
else
    echo "[FAIL]"
    ERRORS=1
fi

echo -n "Checking templates/mcp-kilo.json for grep_app under 'mcp'... "
if jq -e '.mcp.grep_app' templates/mcp-kilo.json > /dev/null; then
    echo "[PASS]"
else
    echo "[FAIL]"
    ERRORS=1
fi

echo -n "Validating grep.app remote endpoint availability... "
if curl -sI -L https://mcp.grep.app | head -n 1 | grep -q "200\|404\|301"; then
    echo "[PASS] Endpoint is reachable"
else
    echo "[WARN] Endpoint might be offline or blocked"
fi

if [ $ERRORS -eq 0 ]; then
    echo "==========================================="
    echo "All tests passed successfully!"
else
    echo "==========================================="
    echo "Tests failed. Please review the output."
fi
