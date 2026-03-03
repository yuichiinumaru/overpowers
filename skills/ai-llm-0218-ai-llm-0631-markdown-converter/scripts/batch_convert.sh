#!/bin/bash
# Batch convert documents to Markdown using markitdown

SRC_DIR="$1"
DEST_DIR="${2:-markdown_outputs}"

if [ -z "$SRC_DIR" ]; then
    echo "Usage: $0 <source_directory> [destination_directory]"
    exit 1
fi

mkdir -p "$DEST_DIR"

echo "📂 Scanning $SRC_DIR for documents..."

# Supported extensions
EXTS=("pdf" "docx" "pptx" "xlsx" "xls" "html" "csv" "json" "xml")

for ext in "${EXTS[@]}"; do
    find "$SRC_DIR" -maxdepth 1 -name "*.$ext" -type f | while read file; do
        FILENAME=$(basename "$file")
        NAME="${FILENAME%.*}"
        OUTPUT="$DEST_DIR/$NAME.md"
        
        echo "📝 Converting $FILENAME -> $OUTPUT"
        uvx markitdown "$file" -o "$OUTPUT"
    done
done

echo ""
echo "✅ Batch conversion complete. Files saved in $DEST_DIR"
