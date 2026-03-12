#!/usr/bin/env bash

# Helper script for Audio Transcriber

echo "Installing requirements for Audio Transcriber..."

if ! command -v ffmpeg &> /dev/null; then
    echo "ffmpeg could not be found, attempting to install..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get update && sudo apt-get install -y ffmpeg
    elif command -v brew &> /dev/null; then
        brew install ffmpeg
    else
        echo "Please install ffmpeg manually."
    fi
fi

if ! python3 -c "import faster_whisper" 2>/dev/null; then
    echo "Installing faster-whisper..."
    pip3 install faster-whisper
fi

if ! python3 -c "import whisper" 2>/dev/null; then
    echo "Installing whisper..."
    pip3 install git+https://github.com/openai/whisper.git
fi

echo "Requirements installed."
