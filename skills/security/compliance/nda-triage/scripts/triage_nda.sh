#!/bin/bash
# Simple keyword-based triage for NDA risk assessment
nda_file=$1

if [ -z "$nda_file" ]; then
    echo "Usage: $0 <nda.txt>"
    return 1 2>/dev/null || true
fi

red_flags=$(grep -iE '(uncapped liability|perpetual|assign|exclusive)' "$nda_file" | wc -l)
yellow_flags=$(grep -iE '(indemnification|governing law|jurisdiction)' "$nda_file" | wc -l)

echo "NDA Risk Assessment for $nda_file:"
if [ "$red_flags" -gt 0 ]; then
    echo "Classification: RED (Significant Issues Found)"
elif [ "$yellow_flags" -gt 0 ]; then
    echo "Classification: YELLOW (Needs Review)"
else
    echo "Classification: GREEN (Standard)"
fi
