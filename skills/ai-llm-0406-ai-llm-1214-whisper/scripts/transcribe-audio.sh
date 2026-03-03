#!/bin/bash
# Wrapper around the Whisper CLI
if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_audio_file>"
    exit 1
fi
echo "Transcribing $1 using local Whisper CLI..."
# In reality, this would be: whisper "$1" --model base
echo "(Simulated) Transcription saved to ${1%.*}.txt"
