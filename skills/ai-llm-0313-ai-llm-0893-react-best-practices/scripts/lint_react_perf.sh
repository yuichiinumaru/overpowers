#!/bin/bash
# A simple bash script to scan React code for common performance anti-patterns mentioned in Vercel React Best Practices

if [ -z "$1" ]; then
    echo "Usage: $0 <path-to-react-files>"
else
    target_path="$1"

    echo "Running simple performance lints on $target_path..."
    echo "--------------------------------------------------"

    echo "Checking for && conditionals which might render 0..."
    grep -rn " && " "$target_path" --include=\*.{jsx,tsx} | grep -v "className" || echo "No issues found."

    echo ""
    echo "Checking for direct barrel imports..."
    grep -rn "from '.*index'" "$target_path" --include=\*.{js,ts,jsx,tsx} || echo "No issues found."

    echo ""
    echo "Checking for missing next/dynamic imports..."
    grep -rn "import " "$target_path" --include=\*.{jsx,tsx} | grep -i "chart" || echo "No issues found."

    echo "--------------------------------------------------"
    echo "Done."
fi
