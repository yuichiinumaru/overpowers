#!/bin/bash
# Helper script wrapping yt-dlp to download videos

URL=$1
FORMAT=$2

if [ -z "$URL" ]; then
    echo "Usage: ./download_video.sh <url> [format]"
    echo "Formats: 1080p, 720p, audio, best"
    exit 1
fi

if [ -z "$FORMAT" ]; then
    FORMAT="best"
fi

if ! command -v yt-dlp &> /dev/null; then
    echo "yt-dlp could not be found, please install it."
    exit 1
fi

case $FORMAT in
    "1080p")
        yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" "$URL"
        ;;
    "720p")
        yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" "$URL"
        ;;
    "audio")
        yt-dlp -f "bestaudio" --extract-audio --audio-format mp3 "$URL"
        ;;
    *)
        yt-dlp "$URL"
        ;;
esac
