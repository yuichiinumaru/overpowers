#!/bin/bash
# Basic Binary Information Helper

TARGET=$1

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <binary_file>"
    exit 1
fi

echo "--- File Type ---"
file "$TARGET"

echo "--- Shared Library Dependencies ---"
ldd "$TARGET" 2>/dev/null || echo "ldd failed (might not be a dynamic executable)"

echo "--- Interesting Strings (First 20) ---"
strings "$TARGET" | grep -E "https?://|/etc/|/bin/|/usr/|error|fail|success" | head -n 20
