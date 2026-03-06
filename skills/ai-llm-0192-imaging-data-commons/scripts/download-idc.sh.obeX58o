#!/bin/bash
# download-idc.sh - IDC data download helper

IDENTIFIER=$1
OUTPUT_DIR=${2:-"./data"}

if [ -z "$IDENTIFIER" ]; then
    echo "Usage: $0 <collection_id|SeriesInstanceUID|manifest_file> [output_dir]"
    echo "Example: $0 rider_pilot ./downloads"
    exit 1
fi

echo "Downloading $IDENTIFIER to $OUTPUT_DIR..."
# idc download auto-detects identifier type
idc download "$IDENTIFIER" --download-dir "$OUTPUT_DIR"
