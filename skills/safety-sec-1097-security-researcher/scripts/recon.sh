#!/bin/bash
# Basic binary reconnaissance script
BINARY=$1

if [ -z "$BINARY" ]; then
    echo "Usage: $0 <binary_path>"
    exit 1
fi

if [ ! -f "$BINARY" ]; then
    echo "Error: File $BINARY not found."
    exit 1
fi

echo "--- Basic Info ---"
file "$BINARY"

echo -e "\n--- Architecture/Headers ---"
if command -v readelf >/dev/null 2>&1; then
    readelf -h "$BINARY" | head -n 20
fi

echo -e "\n--- Interesting Strings ---"
strings -a "$BINARY" | grep -Ei "password|key|secret|token|http|url|admin|root|debug" | sort -u | head -n 50

echo -e "\n--- Security Protections (if checksec available) ---"
if command -v checksec >/dev/null 2>&1; then
    checksec --file="$BINARY"
fi
