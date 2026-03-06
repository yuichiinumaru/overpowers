#!/bin/bash

# Check if input file is provided
if [ -z "$1" ]; then
    echo "Usage: $0 input.drawio"
    exit 1
fi

INPUT_FILE="$1"
OUTPUT_FILE="${INPUT_FILE%.drawio}.drawio.png"

# Check if drawio is installed
if ! command -v drawio &> /dev/null; then
    echo "Error: drawio command not found. Please install drawio-desktop."
    exit 1
fi

echo "Converting $INPUT_FILE to $OUTPUT_FILE..."
drawio -x -f png -s 2 -t -o "$OUTPUT_FILE" "$INPUT_FILE"

if [ $? -eq 0 ]; then
    echo "Successfully converted: $OUTPUT_FILE"
else
    echo "Error: Failed to convert $INPUT_FILE"
    exit 1
fi
