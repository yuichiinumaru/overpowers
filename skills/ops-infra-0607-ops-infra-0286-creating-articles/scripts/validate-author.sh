#!/bin/bash
# Validate author in _config.yml
CONFIG_FILE="../../_config.yml"
AUTHOR="$1"

if [[ -z "$AUTHOR" ]]; then
  echo "Usage: $0 <author-name>"
  exit 1
fi

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Error: $CONFIG_FILE not found."
  exit 1
fi

if grep -q "^\s*authors:.*" "$CONFIG_FILE" || grep -q "^\s*${AUTHOR}:" "$CONFIG_FILE"; then
    if grep -q "^\s*${AUTHOR}:" "$CONFIG_FILE"; then
      echo "Author $AUTHOR found in $CONFIG_FILE."
      exit 0
    else
      echo "Author $AUTHOR not found in $CONFIG_FILE."
      exit 1
    fi
else
    echo "Could not parse _config.yml authors."
    exit 1
fi
