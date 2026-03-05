#!/bin/bash
# YouTube Transcript Extraction Helper

VIDEO_URL=$1
BROWSER=${2:-chrome}

if [ -z "$VIDEO_URL" ]; then
    echo "Usage: $0 <youtube_url> [browser]"
    exit 1
fi

echo "--- Getting Video Title ---"
TITLE=$(yt-dlp --cookies-from-browser="$BROWSER" --get-title "$VIDEO_URL")
echo "Title: $TITLE"

echo "--- Downloading Subtitles ---"
yt-dlp --cookies-from-browser="$BROWSER" \
       --write-auto-sub \
       --write-sub \
       --sub-lang zh-Hans,zh-Hant,en \
       --skip-download \
       --output "$TITLE.%(ext)s" \
       "$VIDEO_URL"

echo "Done! Subtitles saved as '$TITLE.*'"
