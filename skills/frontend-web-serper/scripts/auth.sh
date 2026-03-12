#!/bin/bash
# Helper script for Serper authentication
# Usage: ./auth.sh <api_key>

API_KEY=$1

if [ -z "$API_KEY" ]; then
  echo "Usage: $0 <api_key>"
  exit 1
fi

serperV auth "$API_KEY"
