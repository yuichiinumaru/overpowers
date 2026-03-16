#!/bin/bash
# helpdesk-tools.sh - HelpDesk Rube MCP tools helper

echo "Rube MCP HelpDesk Automation Tools"
echo "----------------------------------"

echo "1. Search for available tools:"
echo "curl -X POST https://rube.app/mcp/tools/search -d '{\"query\": \"helpdesk\"}'"

echo ""
echo "2. Manage connections:"
echo "curl -X POST https://rube.app/mcp/connections/manage -d '{\"toolkit\": \"helpdesk\"}'"

echo ""
echo "Note: Ensure Rube MCP is added to your client configuration."
