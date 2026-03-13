#!/usr/bin/env bash
# Shortcuts for Semi Design MCP tools

echo "--- Semi Design MCP Helper ---"
echo "1. Get component document"
echo "2. Get component file list"
echo "3. Get file code"
echo "4. Get function code"

read -p "Select [1-4]: " choice

case $choice in
  1) read -p "Component: " c; echo "Call: semi-mcp:get_semi_document(component=\"$c\")" ;;
  2) read -p "Component: " c; echo "Call: semi-mcp:get_component_file_list(component=\"$c\")" ;;
  3) read -p "File path: " f; echo "Call: semi-mcp:get_file_code(filePath=\"$f\")" ;;
  4) read -p "Function: " fn; read -p "File: " f; echo "Call: semi-mcp:get_function_code(functionName=\"$fn\", filePath=\"$f\")" ;;
  *) echo "Invalid choice"; exit 1 ;;
esac
