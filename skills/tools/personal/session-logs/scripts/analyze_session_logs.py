#!/usr/bin/env python3
import argparse
import re
from collections import Counter

def analyze_log(file_path):
    stats = {
        "total_lines": 0,
        "errors": 0,
        "warnings": 0,
        "unique_ips": set(),
        "paths": Counter()
    }

    try:
        with open(file_path, "r") as f:
            for line in f:
                stats["total_lines"] += 1

                # Simple error/warning check
                if "ERROR" in line or "Exception" in line or "500" in line:
                    stats["errors"] += 1
                elif "WARN" in line:
                    stats["warnings"] += 1

                # Try to extract IP (basic regex)
                ip_match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
                if ip_match:
                    stats["unique_ips"].add(ip_match.group(0))

                # Try to extract path (basic regex for common web logs)
                path_match = re.search(r'(?:GET|POST|PUT|DELETE)\s+(/[^\s]*)', line)
                if path_match:
                    stats["paths"][path_match.group(1)] += 1

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    return stats

def main():
    parser = argparse.ArgumentParser(description="Analyze session log files for basic metrics.")
    parser.add_argument("log_file", help="Path to the log file")

    args = parser.parse_args()

    stats = analyze_log(args.log_file)
    if stats:
        print(f"--- Log Analysis Report ---")
        print(f"File: {args.log_file}")
        print(f"Total Lines: {stats['total_lines']}")
        print(f"Errors Found: {stats['errors']}")
        print(f"Warnings Found: {stats['warnings']}")
        print(f"Unique IPs: {len(stats['unique_ips'])}")

        print(f"\nTop 5 Requested Paths:")
        for path, count in stats["paths"].most_common(5):
            print(f"  {path}: {count}")

if __name__ == "__main__":
    main()
