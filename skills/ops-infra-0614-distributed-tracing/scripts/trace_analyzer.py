#!/usr/bin/env python3
"""
Trace Analyzer Script
Analyzes dummy trace files (JSON format) to identify slow spans.

Usage:
  python3 trace_analyzer.py --file trace.json --threshold 500
"""

import json
import argparse
import sys

def analyze_trace(filepath, threshold):
    try:
        with open(filepath, 'r') as f:
            trace_data = json.load(f)

        print(f"Analyzing trace data from {filepath}...")

        slow_spans = []
        # Assume trace_data is a list of spans
        for span in trace_data.get('spans', []):
            duration = span.get('duration_ms', 0)
            if duration > threshold:
                slow_spans.append((span.get('name', 'unknown'), duration))

        if slow_spans:
            print(f"Found {len(slow_spans)} slow spans (> {threshold}ms):")
            for name, duration in slow_spans:
                print(f"  - {name}: {duration}ms")
        else:
            print(f"No spans found exceeding {threshold}ms.")

    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
    except json.JSONDecodeError:
        print(f"Error: {filepath} is not valid JSON.")

def main():
    parser = argparse.ArgumentParser(description="Distributed Trace Analyzer")
    parser.add_argument("--file", required=True, help="Path to JSON trace file")
    parser.add_argument("--threshold", type=int, default=1000, help="Duration threshold in ms")

    args = parser.parse_args()
    analyze_trace(args.file, args.threshold)

if __name__ == "__main__":
    main()
