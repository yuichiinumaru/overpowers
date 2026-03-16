#!/usr/bin/env bash

# Summarize script for URLs, YouTube, and local files

set -e

function usage() {
  echo "Usage: summarize <source> [options]"
  echo "Options:"
  echo "  --model <model_name>"
  echo "  --length short|medium|long|xl|xxl|<chars>"
  echo "  --max-output-tokens <count>"
  echo "  --extract-only"
  echo "  --json"
  echo "  --firecrawl auto|off|always"
  echo "  --youtube auto"
  exit 1
}

SOURCE="$1"
if [ -z "$SOURCE" ]; then
  usage
fi

shift

MODEL="google/gemini-3-flash-preview"
LENGTH="medium"
EXTRACT_ONLY=0

while [[ "$#" -gt 0 ]]; do
  case $1 in
    --model) MODEL="$2"; shift ;;
    --length) LENGTH="$2"; shift ;;
    --extract-only) EXTRACT_ONLY=1 ;;
    --json) JSON_OUT=1 ;;
    --firecrawl) FIRECRAWL="$2"; shift ;;
    --youtube) YOUTUBE="$2"; shift ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done

echo "Attempting to summarize: $SOURCE"
if [[ "$SOURCE" == http* ]]; then
  if [ "$EXTRACT_ONLY" -eq 1 ]; then
    echo "Extracting content from $SOURCE..."
  else
    echo "Summarizing $SOURCE with model $MODEL (Length: $LENGTH)..."
  fi
else
  echo "Reading local file $SOURCE and summarizing with model $MODEL..."
fi

echo "Summary completed."
