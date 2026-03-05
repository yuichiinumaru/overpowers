#!/bin/bash

# Script to analyze a design style and suggest font/colors.
# Usage: ./analyze-style.sh "Minimalism"

STYLE=$1

if [ -z "$STYLE" ]; then
  echo "Usage: $0 \"Style Name\""
  exit 1
fi

echo "Analyzing Style: $STYLE"
echo "--------------------------------"

case "$STYLE" in
  "Minimalism")
    echo "Typography: Inter, Montserrat (Google Fonts)"
    echo "Colors: Whites, Grays, and a single bold accent color."
    echo "Layout: High whitespace, grid-based, clear hierarchy."
    ;;
  "Glassmorphism")
    echo "Typography: Poppins, Outfit (Google Fonts)"
    echo "Colors: Vivid gradients with translucent white/black overlays."
    echo "Effects: Backdrop-blur, subtle borders, inner shadows."
    ;;
  "Neo-brutalism")
    echo "Typography: Space Grotesk, Lexend (Google Fonts)"
    echo "Colors: High contrast, often bold yellows/pinks/greens with thick black borders."
    echo "Layout: Overlapping elements, hard shadows, raw aesthetics."
    ;;
  *)
    echo "General Recommendations for $STYLE:"
    echo "Typography: Sans-serif for modern, Serif for classic."
    echo "Colors: Start with a 60-30-10 distribution rule."
    echo "Check inspiration sites for specific patterns."
    ;;
esac
