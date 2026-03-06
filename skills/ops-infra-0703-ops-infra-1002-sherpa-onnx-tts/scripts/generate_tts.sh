#!/bin/bash
# Sherpa-ONNX TTS wrapper
if [ -z "$1" ]; then
    echo "Usage: $0 \"Text to speech\""
else
    TEXT=$1
    echo "[Sherpa-ONNX] Synthesizing: $TEXT"
    echo "Mock: Generating audio file output.wav using local offline model."
fi
