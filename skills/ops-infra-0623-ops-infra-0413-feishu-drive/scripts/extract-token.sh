#!/bin/bash
# Feishu Drive Extract Token
URL="$1"

if [[ -z "$URL" ]]; then
  echo "Usage: $0 <url>"
  exit 1
fi

TOKEN=$(echo "$URL" | awk -F'/' '{print $NF}')
echo "Extracted folder_token: $TOKEN"
