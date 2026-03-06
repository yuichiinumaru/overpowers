#!/usr/bin/env bash
# Helper script to install the OpenAI Developer Docs MCP server

echo "Installing OpenAI Developer Docs MCP server..."
if command -v codex &> /dev/null; then
    codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
    echo "Done. Please restart your agent/codex environment to use the MCP."
else
    echo "Error: 'codex' command not found. Ensure your environment has the MCP client available."
fi
