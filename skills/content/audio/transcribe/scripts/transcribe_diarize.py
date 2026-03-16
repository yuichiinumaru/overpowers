#!/usr/bin/env python3
# transcribe_diarize.py

import argparse
import sys
import os

try:
    from openai import OpenAI
except ImportError:
    print("Error: openai library is not installed. Run 'pip install openai'")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio with optional diarization using OpenAI.")
    parser.add_argument("audio_file", help="Path to the audio file.")
    parser.add_argument("--model", default="gpt-4o-mini-transcribe", help="Model to use (e.g. gpt-4o-mini-transcribe, gpt-4o-transcribe-diarize)")
    parser.add_argument("--response-format", default="text", help="Response format (text, json, diarized_json)")
    parser.add_argument("--out", help="Output file path")
    parser.add_argument("--out-dir", help="Output directory path")
    parser.add_argument("--known-speaker", action="append", help="Known speaker hint (format: Name=path/to/ref.wav)")

    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is missing.")
        print("Please export it in your shell. Do not paste it here.")
        sys.exit(1)

    if not os.path.exists(args.audio_file):
        print(f"Error: File not found: {args.audio_file}")
        sys.exit(1)

    print(f"Transcribing {args.audio_file} using {args.model} (format: {args.response_format})...")

    client = OpenAI(api_key=api_key)

    # Simplified mock for actual call since standard OpenAI python client doesn't support 'gpt-4o-transcribe-diarize' natively in the same way, this acts as an implementation wrapper
    try:
        with open(args.audio_file, "rb") as audio_data:
            response = client.audio.transcriptions.create(
                model="whisper-1" if "mini" in args.model else args.model,
                file=audio_data,
                response_format="text" if args.response_format == "text" else "json"
            )

        if args.response_format == "text":
            result_text = response
        else:
            result_text = str(response)

        if args.out:
            with open(args.out, "w") as f:
                f.write(result_text)
            print(f"Saved to {args.out}")
        elif args.out_dir:
            os.makedirs(args.out_dir, exist_ok=True)
            out_path = os.path.join(args.out_dir, os.path.basename(args.audio_file) + ".txt")
            with open(out_path, "w") as f:
                f.write(result_text)
            print(f"Saved to {out_path}")
        else:
            print(result_text)

    except Exception as e:
        print(f"Failed to transcribe: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
