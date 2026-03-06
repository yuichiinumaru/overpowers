#!/bin/bash
if [ -z "$1" ]; then echo 'Usage: ./render-mermaid.sh <mmd-file>'; exit 1; fi
npx @mermaid-js/mermaid-cli -i "$1" -o "${1%.mmd}.png"
