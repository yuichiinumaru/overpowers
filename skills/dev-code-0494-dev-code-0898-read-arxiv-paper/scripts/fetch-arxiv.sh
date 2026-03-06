#!/usr/bin/env bash

# Fetch and extract Arxiv paper source

if [ -z "$1" ]; then
    echo "Usage: $0 <arxiv_url>"
    echo "Example: $0 https://www.arxiv.org/abs/2601.07372"
    exit 1
fi

URL="$1"
# Extract the arxiv ID
ARXIV_ID=$(echo "$URL" | grep -oP '\d{4}\.\d{4,5}(v\d+)?')

if [ -z "$ARXIV_ID" ]; then
    echo "Error: Could not extract Arxiv ID from URL."
    exit 1
fi

SRC_URL="https://arxiv.org/src/$ARXIV_ID"
CACHE_DIR="$HOME/.cache/nanochat/knowledge"
TAR_FILE="$CACHE_DIR/$ARXIV_ID.tar.gz"
EXTRACT_DIR="$CACHE_DIR/$ARXIV_ID"

mkdir -p "$CACHE_DIR"

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading paper source from $SRC_URL..."
    curl -sL "$SRC_URL" -o "$TAR_FILE"
else
    echo "File $TAR_FILE already exists, skipping download."
fi

mkdir -p "$EXTRACT_DIR"
echo "Extracting to $EXTRACT_DIR..."
tar -xzf "$TAR_FILE" -C "$EXTRACT_DIR"

echo "Extraction complete."
echo "Entrypoint usually at $EXTRACT_DIR/main.tex or similar."
