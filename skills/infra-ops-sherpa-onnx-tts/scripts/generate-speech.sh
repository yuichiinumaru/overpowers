#!/bin/bash

# Helper script to simplify local TTS generation with sherpa-onnx
# Usage: ./generate-speech.sh <text> <output_file>

TEXT=$1
OUTPUT=${2:-"output.wav"}

if [[ -z "$TEXT" ]]; then
  echo "Usage: $0 <text> [output_file]"
  exit 1
fi

# Determine base dir of the skill
BASE_DIR=$(cd "$(dirname "$0")/.." && pwd)

# Check if wrapper exists
if [[ ! -f "$BASE_DIR/bin/sherpa-onnx-tts" ]]; then
  echo "Error: sherpa-onnx-tts wrapper not found in $BASE_DIR/bin"
  exit 1
fi

# Run the TTS
"$BASE_DIR/bin/sherpa-onnx-tts" -o "$OUTPUT" "$TEXT"

if [[ $? -eq 0 ]]; then
  echo "Speech generated successfully: $OUTPUT"
else
  echo "Error generating speech."
  exit 1
fi
