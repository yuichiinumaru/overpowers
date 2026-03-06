#!/bin/bash
echo 'Checking for whisper binary...'
if command -v whisper &> /dev/null; then echo 'Whisper found'; else echo 'Whisper not found'; fi
