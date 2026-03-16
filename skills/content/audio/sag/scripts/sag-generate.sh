#!/bin/bash
# Wrapper script to generate audio file using sag

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <voice> <text> [output_file]"
    echo "Example: $0 Clawd \"Your message here\" /tmp/voice-reply.mp3"
else
    VOICE="$1"
    TEXT="$2"
    OUTPUT="${3:-/tmp/voice-reply.mp3}"

    echo "Generating audio with voice '$VOICE'..."
    sag -v "$VOICE" -o "$OUTPUT" "$TEXT"
    echo "Done! Output saved to $OUTPUT"
    echo "Include in reply: MEDIA:$OUTPUT"
fi
