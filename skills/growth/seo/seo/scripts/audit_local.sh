#!/bin/bash
# Basic local SEO audit for HTML files
TARGET=${1:-.}

echo "--- Local SEO Audit ---"

echo -e "\n1. Checking for missing <title> tags..."
find "$TARGET" -name "*.html" -type f | while read file; do
    if ! grep -qi "<title>" "$file"; then
        echo "  [WARNING] Missing <title> in $file"
    fi
done

echo -e "\n2. Checking for missing <h1> tags..."
find "$TARGET" -name "*.html" -type f | while read file; do
    if ! grep -qi "<h1" "$file"; then
        echo "  [WARNING] Missing <h1> in $file"
    fi
done

echo -e "\n3. Checking for missing meta descriptions..."
find "$TARGET" -name "*.html" -type f | while read file; do
    if ! grep -qi 'name="description"' "$file"; then
        echo "  [WARNING] Missing meta description in $file"
    fi
done

echo -e "\n4. Checking for missing image alt attributes..."
find "$TARGET" -name "*.html" -type f | while read file; do
    if grep -i "<img" "$file" | grep -vqi "alt="; then
        echo "  [WARNING] Missing alt attribute on image(s) in $file"
    fi
done

echo -e "\nAudit Complete."
