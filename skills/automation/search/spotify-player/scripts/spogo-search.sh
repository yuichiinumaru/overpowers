#!/bin/bash
# Helper script for spogo search
# Usage: ./spogo-search.sh [type] <query>

TYPE=${1:-track}
QUERY=$2

if [ -z "$QUERY" ]; then
  echo "Usage: $0 [type] <query>"
  echo "Types: track, album, artist, playlist"
  exit 1
fi

spogo search "$TYPE" "$QUERY"
