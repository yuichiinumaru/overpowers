#!/usr/bin/env bash

# Helper script for nano-pdf CLI

if [ $# -eq 0 ]; then
  echo "Usage: $0 <command> [args...]"
  echo "Example: $0 edit deck.pdf 1 \"Change the title to 'Q3 Results'\""
  exit 1
fi

nano-pdf "$@"
