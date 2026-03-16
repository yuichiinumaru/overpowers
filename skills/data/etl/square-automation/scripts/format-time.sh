#!/bin/bash

# Helper script to generate RFC 3339 timestamps for Square API
# Usage: ./format-time.sh [days_offset]
# Positive offset for future, negative for past. Default is current time.

OFFSET=${1:-0}

if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS
  if [[ "$OFFSET" -eq 0 ]]; then
    date -u +"%Y-%m-%dT%H:%M:%SZ"
  else
    date -u -v "${OFFSET}d" +"%Y-%m-%dT%H:%M:%SZ"
  fi
else
  # Linux
  if [[ "$OFFSET" -eq 0 ]]; then
    date -u +"%Y-%m-%dT%H:%M:%SZ"
  else
    date -u -d "$OFFSET days" +"%Y-%m-%dT%H:%M:%SZ"
  fi
fi
