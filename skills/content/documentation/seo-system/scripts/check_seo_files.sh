#!/bin/bash

# Check if SEO system files exist in the project

SEO_DIR="src/lib/seo"
FILES=("index.ts" "config.ts" "metadata.ts" "json-ld.ts")

echo "Checking SEO system files in $SEO_DIR..."

if [ ! -d "$SEO_DIR" ]; then
    echo "[ERROR] SEO directory $SEO_DIR not found."
    exit 1
fi

for f in "${FILES[@]}"; do
    if [ -f "$SEO_DIR/$f" ]; then
        echo "[OK] Found $f"
    else
        echo "[MISSING] $f"
    fi
done

if [ -d "src/app/api/og" ]; then
    echo "[OK] Found dynamic OG API route"
else
    echo "[WARN] Dynamic OG API route not found"
fi
