#!/usr/bin/env bash
# Helper script to verify Rube MCP connection for this skill
echo "Checking Rube MCP connection..."
if command -v curl &> /dev/null; then
    # Note: Rube MCP operates via the client configuration, this just checks if the endpoint is reachable
    HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://rube.app/mcp)
    if [ "$HTTP_STATUS" -eq 200 ] || [ "$HTTP_STATUS" -eq 400 ] || [ "$HTTP_STATUS" -eq 404 ]; then
        echo "✅ Rube MCP endpoint is reachable."
        echo "Please ensure 'https://rube.app/mcp' is added to your MCP client configuration."
        echo "Then use RUBE_MANAGE_CONNECTIONS tool to authenticate the required toolkit."
    else
        echo "⚠️ Rube MCP endpoint returned status: $HTTP_STATUS"
        echo "Check your internet connection or the Rube MCP service status."
    fi
else
    echo "⚠️ curl is not installed. Cannot verify Rube MCP endpoint reachability."
    echo "Please ensure 'https://rube.app/mcp' is added to your MCP client configuration."
fi
