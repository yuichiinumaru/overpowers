#!/bin/bash
# Transcribe audio using OpenAI Whisper API
# Usage: ./transcribe.sh /path/to/audio.m4a [--model whisper-1] [--out /tmp/transcript.txt] [--language en] [--prompt "Speaker names: Peter, Daniel"] [--json]

set -e

# Default values
MODEL="whisper-1"
AUDIO_FILE=""
OUTPUT_FILE=""
LANGUAGE=""
PROMPT=""
JSON_OUTPUT=false

# Parse positional arguments
if [[ "$1" != -* ]]; then
  AUDIO_FILE="$1"
  shift
fi

# Parse flags
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --model) MODEL="$2"; shift ;;
    --out) OUTPUT_FILE="$2"; shift ;;
    --language) LANGUAGE="$2"; shift ;;
    --prompt) PROMPT="$2"; shift ;;
    --json) JSON_OUTPUT=true ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done

if [ -z "$AUDIO_FILE" ]; then
  echo "Error: Audio file path is required."
  echo "Usage: ./transcribe.sh /path/to/audio.m4a [--model whisper-1] [--out /tmp/transcript.txt] [--language en] [--prompt \"Speaker names: Peter, Daniel\"] [--json]"
  exit 1
fi

if [ -z "$OPENAI_API_KEY" ]; then
    # Try to extract API key from ~/.openclaw/openclaw.json if jq is available
    if command -v jq >/dev/null 2>&1 && [ -f "$HOME/.openclaw/openclaw.json" ]; then
        OPENAI_API_KEY=$(jq -r '.skills["openai-whisper-api"].apiKey // empty' "$HOME/.openclaw/openclaw.json")
    fi
    if [ -z "$OPENAI_API_KEY" ]; then
        echo "Error: OPENAI_API_KEY environment variable is not set."
        exit 1
    fi
fi

# Set default output file if not provided
if [ -z "$OUTPUT_FILE" ]; then
  if [ "$JSON_OUTPUT" = true ]; then
    OUTPUT_FILE="${AUDIO_FILE%.*}.json"
  else
    OUTPUT_FILE="${AUDIO_FILE%.*}.txt"
  fi
fi

# Construct curl command arguments
CURL_ARGS=(
  -H "Authorization: Bearer $OPENAI_API_KEY"
  -F "file=@$AUDIO_FILE"
  -F "model=$MODEL"
)

if [ -n "$LANGUAGE" ]; then
  CURL_ARGS+=(-F "language=$LANGUAGE")
fi

if [ -n "$PROMPT" ]; then
  CURL_ARGS+=(-F "prompt=$PROMPT")
fi

if [ "$JSON_OUTPUT" = true ]; then
  CURL_ARGS+=(-F "response_format=json")
else
  CURL_ARGS+=(-F "response_format=text")
fi

# Execute curl request
echo "Transcribing $AUDIO_FILE using model $MODEL..."
curl -s -X POST https://api.openai.com/v1/audio/transcriptions "${CURL_ARGS[@]}" -o "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo "Transcription completed successfully."
    echo "Saved to: $OUTPUT_FILE"
else
    echo "Transcription failed."
    exit 1
fi
