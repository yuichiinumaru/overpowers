#!/bin/bash
# compile_poster.sh - Automate LaTeX poster compilation

POSTER_TEX=${1:-poster.tex}
OUTPUT_NAME=$(basename "$POSTER_TEX" .tex)

echo "Compiling poster: $POSTER_TEX"

# First pass
pdflatex -interaction=nonstopmode "$POSTER_TEX"

# Check for bibliography
if grep -q "citation" "$OUTPUT_NAME.aux" 2>/dev/null; then
    echo "Running bibtex..."
    bibtex "$OUTPUT_NAME"
    pdflatex -interaction=nonstopmode "$POSTER_TEX"
fi

# Final pass
pdflatex -interaction=nonstopmode "$POSTER_TEX"

echo "Checking for overflow warnings..."
grep -i "overfull\|underfull\|badbox" "$OUTPUT_NAME.log"

if [ -f "$OUTPUT_NAME.pdf" ]; then
    echo "Successfully generated $OUTPUT_NAME.pdf"
else
    echo "Error: PDF generation failed."
    exit 1
fi
