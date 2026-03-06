#!/bin/bash
# Helper script to compile LaTeX hypothesis reports

TEX_FILE=$1

if [ -z "$TEX_FILE" ]; then
    echo "Usage: $0 <filename.tex>"
    echo "Example: $0 hypothesis_report.tex"
    return 1 2>/dev/null || exit 1
fi

BASENAME="${TEX_FILE%.*}"

echo "Compiling $TEX_FILE using xelatex..."

# Run xelatex
xelatex -interaction=nonstopmode "$TEX_FILE"

# Check if bib file exists or needs compilation
if [ -f "${BASENAME}.aux" ] && grep -q "bibdata" "${BASENAME}.aux"; then
    echo "Running bibtex..."
    bibtex "$BASENAME"

    # Run xelatex twice more for references
    echo "Re-compiling to resolve references..."
    xelatex -interaction=nonstopmode "$TEX_FILE"
    xelatex -interaction=nonstopmode "$TEX_FILE"
fi

if [ -f "${BASENAME}.pdf" ]; then
    echo "Successfully generated ${BASENAME}.pdf"
else
    echo "Error generating PDF. Check ${BASENAME}.log for details."
fi
