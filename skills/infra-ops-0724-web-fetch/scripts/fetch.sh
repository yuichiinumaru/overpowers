#!/bin/bash
# Helper for Web Fetch - Lightweight page access

URL=$1
OUTPUT_FILE=$2

if [ -z "$URL" ]; then
  echo "Usage: $0 <url> [output_file]"
  exit 1
fi

# Fetch using curl with 10s timeout
TEMP_HTML=$(mktemp)
curl -s -L --max-time 10 "$URL" -o "$TEMP_HTML"

if [ $? -ne 0 ]; then
  echo "Error: Failed to fetch $URL"
  rm "$TEMP_HTML"
  exit 1
fi

{
  echo "URL: $URL"
  # Extract title (basic)
  TITLE=$(grep -oP '(?<=<title>).*?(?=</title>)' "$TEMP_HTML" | head -1)
  echo "Title: ${TITLE:-No title found}"
  echo ""
  # Strip HTML tags and scripts (basic)
  sed -e 's/<script[^>]*>.*<\/script>//g' \
      -e 's/<style[^>]*>.*<\/style>//g' \
      -e 's/<[^>]*>//g' "$TEMP_HTML" | \
      awk 'NF' | sed 's/^[ \t]*//'
} > "${OUTPUT_FILE:-/dev/stdout}"

rm "$TEMP_HTML"
