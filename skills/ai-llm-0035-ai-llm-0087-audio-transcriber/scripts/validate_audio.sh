#!/bin/bash
# validate_audio.sh - Audio File Validation

AUDIO_FILE=$1

if [[ ! -f "$AUDIO_FILE" ]]; then
    echo "❌ File not found: $AUDIO_FILE"
    exit 1
fi

# Get file size
FILE_SIZE=$(du -h "$AUDIO_FILE" | cut -f1)
echo "File Size: $FILE_SIZE"

# Check for ffprobe
if command -v ffprobe &>/dev/null; then
    DURATION=$(ffprobe -v error -show_entries format=duration \
        -of default=noprint_wrappers=1:nokey=1 "$AUDIO_FILE" 2>/dev/null)
    FORMAT=$(ffprobe -v error -select_streams a:0 -show_entries \
        stream=codec_name -of default=noprint_wrappers=1:nokey=1 "$AUDIO_FILE" 2>/dev/null)
    echo "Duration: $DURATION seconds"
    echo "Format: $FORMAT"
else
    echo "ffprobe not found, skipping detailed metadata extraction."
fi

# Validate format
EXTENSION="${AUDIO_FILE##*.}"
SUPPORTED_FORMATS=("mp3" "wav" "m4a" "ogg" "flac" "webm" "mp4")

if [[ ! " ${SUPPORTED_FORMATS[@]} " =~ " ${EXTENSION,,} " ]]; then
    echo "⚠️  Unsupported format: $EXTENSION"
else
    echo "✅ Format $EXTENSION is supported."
fi
