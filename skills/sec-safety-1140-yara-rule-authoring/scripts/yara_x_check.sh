#!/bin/bash
# YARA-X Helper Script

RULE_FILE=$1

if [ -z "$RULE_FILE" ]; then
    echo "Usage: $0 <rule_file.yar>"
    exit 1
fi

echo "--- Checking Syntax ---"
yr check "$RULE_FILE"

echo "--- Formatting Rule ---"
yr fmt -w "$RULE_FILE"

echo "--- Rule Structure Dump (First 20 lines) ---"
yr dump -m pe "$RULE_FILE" 2>/dev/null | head -n 20
