#!/bin/bash
# Extract a frame from a video

if [ $# -eq 0 ]; then
    echo "Usage: $0 /path/to/video.mp4 [--time 00:00:10] --out /tmp/frame.jpg"
    exit 1
fi

VIDEO_PATH=""
OUT_PATH=""
TIME="00:00:00"

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --out) OUT_PATH="$2"; shift ;;
        --time) TIME="$2"; shift ;;
        *) VIDEO_PATH="$1" ;;
    esac
    shift
done

if [ -z "$VIDEO_PATH" ] || [ -z "$OUT_PATH" ]; then
    echo "Usage: $0 /path/to/video.mp4 [--time 00:00:10] --out /tmp/frame.jpg"
    exit 1
fi

ffmpeg -ss "$TIME" -i "$VIDEO_PATH" -vframes 1 -q:v 2 "$OUT_PATH"
