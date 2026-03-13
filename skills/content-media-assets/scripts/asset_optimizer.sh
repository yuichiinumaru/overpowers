#!/usr/bin/env bash
# Helper for asset management in Remotion

echo "--- Remotion Asset Management ---"
echo "Rule 1: Place assets in 'public/' folder."
echo "Rule 2: Use staticFile('filename.ext') to reference them."
echo ""

if [ ! -d "public" ]; then
    echo "Warning: 'public/' directory not found in current path."
else
    echo "Files in public/:"
    ls -F public/
fi

echo ""
echo "Example usage in code:"
echo "import { Img, staticFile } from 'remotion';"
echo "<Img src={staticFile('logo.png')} />"
