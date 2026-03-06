#!/bin/bash
if [ -z "$1" ]; then echo 'Usage: ./build-slides.sh <markdown-file>'; exit 1; fi
npx @marp-team/marp-cli "$1" -o "${1%.md}.pdf"
