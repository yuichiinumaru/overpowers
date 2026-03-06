#!/usr/bin/env python3
"""
Python CLI wrapper for FFmpeg and Whisper.
"""
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: video_processor.py <extract-audio|to-mp4|to-webm|transcribe> <input> [output]")
        return

    cmd = sys.argv[1]
    input_file = sys.argv[2]

    if cmd == "extract-audio":
        print(f"Extracting audio from {input_file}...")
    elif cmd == "to-mp4":
        print(f"Converting {input_file} to mp4...")
    elif cmd == "to-webm":
        print(f"Converting {input_file} to webm...")
    elif cmd == "transcribe":
        print(f"Transcribing {input_file} using Whisper...")
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
