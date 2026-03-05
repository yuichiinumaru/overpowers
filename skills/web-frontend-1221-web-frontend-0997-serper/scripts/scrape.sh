#!/bin/bash
# Helper script for Serper scrape
# Usage: ./scrape.sh <url1,url2,...>

URLS=$1

if [ -z "$URLS" ]; then
  echo "Usage: $0 <url1,url2,...>"
  exit 1
fi

serperV scrape -u "$URLS"
