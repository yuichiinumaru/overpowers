#!/bin/bash
# Helper script to convert markdown to HTML using pandoc or marked
input_file=$1
output_file=$2

if [ -z "$input_file" ]; then
    echo "Usage: $0 <input.md> [output.html]"
    return 1 2>/dev/null || true
fi

if [ -z "$output_file" ]; then
    output_file="${input_file%.*}.html"
fi

echo "Converting $input_file to $output_file..."
if command -v pandoc &> /dev/null; then
    pandoc "$input_file" -o "$output_file"
elif command -v marked &> /dev/null; then
    marked "$input_file" -o "$output_file"
else
    echo "Error: Neither pandoc nor marked is installed."
    return 1 2>/dev/null || true
fi
echo "Done."
