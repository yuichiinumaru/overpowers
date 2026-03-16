#!/bin/bash
# Batch resize images using ImageMagick
# Usage: ./batch-resize.sh <input_dir> <output_dir> <resolution (e.g., 427x240)>

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <input_dir> <output_dir> <resolution (e.g., 427x240)>"
    exit 1
fi

INPUT_DIR="$1"
OUTPUT_DIR="$2"
RESOLUTION="$3"

if ! command -v magick &> /dev/null; then
    echo "ImageMagick (magick) not found. Please install it."
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

for img in "$INPUT_DIR"/*; do
    if [ -f "$img" ]; then
        filename=$(basename "$img")
        echo "Processing $filename..."
        magick "$img" -resize "$RESOLUTION" "$OUTPUT_DIR/thumb_$filename"
    fi
done

echo "Batch resizing complete."
