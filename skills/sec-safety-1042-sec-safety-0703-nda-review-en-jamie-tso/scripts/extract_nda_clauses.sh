#!/bin/bash
# Helper to extract potential clauses from an NDA text for review
nda_file=$1

if [ -z "$nda_file" ]; then
    echo "Usage: $0 <nda.txt>"
    return 1 2>/dev/null || true
fi

echo "Extracting potential issue clauses from $nda_file..."
grep -iE '(indemn|liability|jurisdiction|term|surviv|confidentiality)' "$nda_file"
