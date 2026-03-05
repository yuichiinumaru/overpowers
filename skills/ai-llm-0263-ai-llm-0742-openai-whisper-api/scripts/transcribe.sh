#!/bin/bash

# Transcribe audio via OpenAI Audio Transcriptions API (Whisper).
# Usage: ./transcribe.sh <audio_file> [flags]

AUDIO_FILE="$1"
shift

if [ -z "$AUDIO_FILE" ]; then
  echo "Usage: $0 <audio_file> [flags]"
  echo ""
  echo "Flags:"
  echo "  --model <model>      Default: whisper-1"
  echo "  --out <file>         Default: <input>.txt"
  echo "  --language <lang>    ISO-639-1 code (e.g. en, es, fr)"
  echo "  --prompt <text>      Context for the transcription"
  echo "  --json               Output in JSON format (changes default extension to .json)"
  exit 1
fi

if [ ! -f "$AUDIO_FILE" ]; then
  echo "Error: File not found: $AUDIO_FILE"
  exit 1
fi

MODEL="whisper-1"
LANGUAGE=""
PROMPT=""
RESPONSE_FORMAT="text"
OUT_FILE=""

# Parse flags
args=()
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --model) MODEL="$2"; shift ;;
    --out) OUT_FILE="$2"; shift ;;
    --language) LANGUAGE="$2"; shift ;;
    --prompt) PROMPT="$2"; shift ;;
    --json) RESPONSE_FORMAT="json" ;;
    *) args+=("$1") ;;
  esac
  shift
done

# Set default output file if not provided
if [ -z "$OUT_FILE" ]; then
  if [ "$RESPONSE_FORMAT" == "json" ]; then
    OUT_FILE="${AUDIO_FILE}.json"
  else
    OUT_FILE="${AUDIO_FILE}.txt"
  fi
fi

if [ -z "$OPENAI_API_KEY" ]; then
  echo "Error: OPENAI_API_KEY environment variable is not set."
  exit 1
fi

CURL_ARGS=(
  -s
  -X POST "https://api.openai.com/v1/audio/transcriptions"
  -H "Authorization: Bearer $OPENAI_API_KEY"
  -H "Content-Type: multipart/form-data"
  -F "file=@$AUDIO_FILE"
  -F "model=$MODEL"
  -F "response_format=$RESPONSE_FORMAT"
)

if [ -n "$LANGUAGE" ]; then
  CURL_ARGS+=(-F "language=$LANGUAGE")
fi

if [ -n "$PROMPT" ]; then
  CURL_ARGS+=(-F "prompt=$PROMPT")
fi

curl "${CURL_ARGS[@]}" > "$OUT_FILE"

if [ $? -eq 0 ]; then
  echo "Transcription saved to $OUT_FILE"
else
  echo "Error: curl command failed."
  exit 1
fi
