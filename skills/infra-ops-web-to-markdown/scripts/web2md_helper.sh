#!/bin/bash
# Helper for web-to-markdown (web2md)

URL=$1
shift

if [ -z "$URL" ]; then
  echo "Usage: $0 <url> [args]"
  echo "Example: $0 https://example.com --out ./page.md"
  exit 1
fi

# Ensure web2md is installed
if ! command -v web2md &> /dev/null; then
  echo "Error: web2md not found. Install via 'npm install -g web2md'."
  exit 1
fi

echo "Converting $URL to Markdown..."
web2md "$URL" "$@"
