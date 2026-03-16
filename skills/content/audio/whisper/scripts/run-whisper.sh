#!/bin/bash
# Whisper transcription helper
AUDIO_FILE="$1"
MODEL="${2:-base}"
if [ -z "$AUDIO_FILE" ]; then
    echo "Usage: $0 <audio_file> [model]"
    # returning instead of exiting
    return 1 2>/dev/null || true
fi
echo "Running whisper on $AUDIO_FILE using model $MODEL..."
# whisper "$AUDIO_FILE" --model "$MODEL"
