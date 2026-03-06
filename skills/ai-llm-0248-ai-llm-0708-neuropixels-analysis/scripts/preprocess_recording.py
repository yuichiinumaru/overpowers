#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: preprocess_recording.py <input_dir> --output <output_dir>")
        sys.exit(1)
    print(f"Preprocessing recording from {sys.argv[1]}")

if __name__ == "__main__":
    main()
