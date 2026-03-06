#!/bin/bash

# Script to format lyrics for ACE-Step.
# Usage: ./lyrics-formatter.sh "Verse 1 contents..." "Chorus contents..."

VERSE=$1
CHORUS=$2

if [ -z "$VERSE" ]; then
  echo "Usage: $0 \"Verse content\" [\"Chorus content\"]"
  exit 1
fi

echo "[Verse]"
echo "$VERSE"
echo ""
if [ ! -z "$CHORUS" ]; then
  echo "[Chorus]"
  echo "$CHORUS"
fi
