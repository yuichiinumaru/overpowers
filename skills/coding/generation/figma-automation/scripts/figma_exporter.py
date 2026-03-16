#!/usr/bin/env python3
"""
Figma Tokens Exporter Helper
Generates a payload to extract design tokens from a Figma file.

Usage:
  python3 figma_exporter.py --file-key "abc123XYZ"
"""

import argparse
import json

def generate_payload(file_key):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "rube/call_tool",
        "params": {
            "name": "FIGMA_EXTRACT_DESIGN_TOKENS",
            "arguments": {
                "file_key": file_key,
                "include_local_styles": True,
                "include_variables": True
            }
        }
    }
    print("Execute the following payload via Rube MCP:")
    print(json.dumps(payload, indent=2))
    print("\nNote: The output from this tool should be passed entirely to FIGMA_DESIGN_TOKENS_TO_TAILWIND if Tailwind CSS configuration is desired.")

def main():
    parser = argparse.ArgumentParser(description="Figma Token Exporter Payload Generator")
    parser.add_argument("--file-key", required=True, help="Figma File Key (from URL)")

    args = parser.parse_args()
    generate_payload(args.file_key)

if __name__ == "__main__":
    main()
