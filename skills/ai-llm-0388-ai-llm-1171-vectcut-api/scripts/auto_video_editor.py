#!/usr/bin/env python3
"""
Script for Excel-driven batch video processing.
"""
import sys

def process_batch(excel_file):
    print(f"Processing batch from {excel_file} via VectCutAPI...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python auto_video_editor.py <input.xlsx>")
        sys.exit(1)
    process_batch(sys.argv[1])
