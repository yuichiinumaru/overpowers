#!/bin/bash

# Quick UI inspection with Peekaboo.
# Usage: ./quick_see.sh [app_name]

APP="$1"
OUT_PATH="/tmp/peekaboo_see.png"

if [ -n "$APP" ]; then
  echo "Inspecting $APP..."
  peekaboo see --app "$APP" --annotate --path "$OUT_PATH"
else
  echo "Inspecting full screen..."
  peekaboo see --annotate --path "$OUT_PATH"
fi

if [ $? -eq 0 ]; then
  echo "UI Map saved to: $OUT_PATH"
  if [[ "$OSTYPE" == "darwin"* ]]; then
    open "$OUT_PATH"
  fi
else
  echo "Error: Peekaboo failed. Ensure permissions are granted."
  exit 1
fi
