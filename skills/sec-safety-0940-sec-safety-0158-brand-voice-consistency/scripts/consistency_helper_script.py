#!/usr/bin/env python3
import sys

def analyze_voice(text_file):
    print(f"Analyzing brand voice consistency for content in: {text_file}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyze_voice(sys.argv[1])
    else:
        print("Usage: ./brand_voice_analyzer.py <text_file>")
