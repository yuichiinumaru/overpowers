#!/bin/bash
# Helper for User File Ops - Summarize a text file

INPUT_FILE=$1
OUTPUT_FILE=$2

if [ -z "$INPUT_FILE" ]; then
  echo "Usage: $0 <input_file> [output_file]"
  exit 1
fi

if [ ! -f "$INPUT_FILE" ]; then
  echo "Error: Input file $INPUT_FILE not found."
  exit 1
fi

{
  echo "--- File Summary: $(basename "$INPUT_FILE") ---"
  echo "Path: $INPUT_FILE"
  echo "Stats:"
  wc "$INPUT_FILE" | awk '{printf "  Lines: %s\n  Words: %s\n  Bytes: %s\n", $1, $2, $3}'
  echo ""
  echo "Preview (first 10 lines):"
  head -n 10 "$INPUT_FILE" | sed 's/^/  /'
  echo "----------------------------------------"
} > "${OUTPUT_FILE:-/dev/stdout}"

if [ ! -z "$OUTPUT_FILE" ]; then
  echo "Summary written to $OUTPUT_FILE"
fi
