#!/bin/bash
# Helper script to wrap nano-pdf CLI usage

if [ "$#" -lt 3 ]; then
    echo "Usage: $0 <pdf_file> <page_number> <instruction>"
    echo "Example: $0 deck.pdf 1 \"Change the title to 'Q3 Results'\""
    exit 1
fi

PDF_FILE="$1"
PAGE_NUMBER="$2"
INSTRUCTION="$3"

if [ ! -f "$PDF_FILE" ]; then
    echo "Error: PDF file $PDF_FILE not found."
    exit 1
fi

if ! command -v nano-pdf &> /dev/null; then
    echo "Error: nano-pdf CLI not found in PATH."
    exit 1
fi

echo "Running: nano-pdf edit \"$PDF_FILE\" \"$PAGE_NUMBER\" \"$INSTRUCTION\""
nano-pdf edit "$PDF_FILE" "$PAGE_NUMBER" "$INSTRUCTION"
