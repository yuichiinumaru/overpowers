#!/usr/bin/env python3
import sys
import re

def parse_figma_url(url):
    # Pattern: https://figma.com/design/:fileKey/:fileName?node-id=1-2
    pattern = r'figma\.com/design/([^/]+)/[^?]+\?node-id=([^&]+)'
    match = re.search(pattern, url)
    
    if match:
        file_key = match.group(1)
        node_id = match.group(2)
        print(f"File Key: {file_key}")
        print(f"Node ID: {node_id}")
        print(f"\nNext command:")
        print(f"get_design_context(fileKey=\"{file_key}\", nodeId=\"{node_id}\")")
    else:
        print("Error: Could not parse Figma URL. Ensure it contains /design/:fileKey/ and ?node-id=")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: figma_id_parser.py <figma_url>")
        sys.exit(1)
    
    parse_figma_url(sys.argv[1])
