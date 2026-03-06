#!/bin/bash
# Helper script to download and unpack arxiv paper source

if [ -z "$1" ]; then
    echo "Usage: $0 <arxiv_id>"
    exit 1
fi

ARXIV_ID="$1"
CACHE_DIR=~/.cache/nanochat/knowledge
mkdir -p "$CACHE_DIR"

TAR_FILE="$CACHE_DIR/${ARXIV_ID}.tar.gz"
EXTRACT_DIR="$CACHE_DIR/${ARXIV_ID}"

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading source for $ARXIV_ID..."
    curl -L "https://arxiv.org/src/$ARXIV_ID" -o "$TAR_FILE"
else
    echo "Source already downloaded at $TAR_FILE."
fi

if [ ! -d "$EXTRACT_DIR" ]; then
    echo "Extracting to $EXTRACT_DIR..."
    mkdir -p "$EXTRACT_DIR"
    tar -xzf "$TAR_FILE" -C "$EXTRACT_DIR"
else
    echo "Already extracted at $EXTRACT_DIR."
fi

echo "Source available at: $EXTRACT_DIR"
# Attempt to find the main tex file
MAIN_TEX=$(find "$EXTRACT_DIR" -maxdepth 1 -name "*.tex" | head -n 1)
if [ -n "$MAIN_TEX" ]; then
    echo "Possible entrypoint: $MAIN_TEX"
else
    echo "No .tex files found in root."
fi
