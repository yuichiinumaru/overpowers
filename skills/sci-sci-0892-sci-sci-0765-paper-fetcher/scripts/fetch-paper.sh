#!/bin/bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <DOI1> [DOI2...]"
    # omitted exit
fi

DEST_DIR="research/papers"
mkdir -p "$DEST_DIR"

for doi in "$@"; do
    echo "Fetching paper for DOI: $doi"

    # Try different sci-hub domains
    DOMAINS=("se" "st" "ru" "su")
    SUCCESS=0

    for domain in "${DOMAINS[@]}"; do
        URL="https://sci-hub.$domain/$doi"

        # We fetch the page, and try to find the PDF iframe or button link
        PAGE=$(curl -sL -A "Mozilla/5.0" "$URL" || echo "")

        # Very basic regex to find a PDF link starting with // or https://
        PDF_URL=$(echo "$PAGE" | grep -oE "src=['\"](//[^'\"]+\.pdf.*?)['\"]|href=['\"](//[^'\"]+\.pdf.*?)['\"]" | head -n 1 | sed -E "s/.*=['\"](//.*)['\"]/\1/")

        if [ -n "$PDF_URL" ]; then
            # Sometimes URL starts with //
            if [[ "$PDF_URL" == //* ]]; then
                PDF_URL="https:$PDF_URL"
            fi

            FILENAME=$(echo "$doi" | tr '/' '_').pdf
            FILEPATH="$DEST_DIR/$FILENAME"

            echo "Downloading PDF from $PDF_URL to $FILEPATH..."
            curl -sL -A "Mozilla/5.0" -o "$FILEPATH" "$PDF_URL"

            if [ -s "$FILEPATH" ]; then
                echo "Successfully downloaded $doi to $FILEPATH"
                SUCCESS=1
                break
            else
                rm "$FILEPATH"
                echo "Download failed (empty file)."
            fi
        fi
    done

    if [ "$SUCCESS" -eq 0 ]; then
        echo "Failed to fetch PDF for $doi from any known Sci-Hub domains."
    fi
done
