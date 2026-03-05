#!/bin/bash
# Clone a repo and pack it with Repomix

REPO_URL=$1
OUTPUT_NAME=$2

if [ -z "$REPO_URL" ]; then
    echo "Usage: $0 <repo_url> [output_name]"
    exit 1
fi

TMP_DIR="/tmp/docs-analysis-$(date +%s)"
OUTPUT_DIR="/tmp/repomix-outputs"
mkdir -p "$OUTPUT_DIR"

if [ -z "$OUTPUT_NAME" ]; then
    OUTPUT_NAME="repo-$(date +%s).xml"
fi

echo "Cloning $REPO_URL to $TMP_DIR..."
git clone --depth 1 "$REPO_URL" "$TMP_DIR"

cd "$TMP_DIR" || exit 1

echo "Running Repomix..."
if command -v repomix &> /dev/null; then
    repomix --output "$OUTPUT_DIR/$OUTPUT_NAME"
else
    npx repomix --output "$OUTPUT_DIR/$OUTPUT_NAME"
fi

echo "Pack completed: $OUTPUT_DIR/$OUTPUT_NAME"
# rm -rf "$TMP_DIR"
