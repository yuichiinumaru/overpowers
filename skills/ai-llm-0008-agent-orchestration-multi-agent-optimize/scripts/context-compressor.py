#!/usr/bin/env python3
import sys

def compress_context(context, max_tokens=4000):
    # Simple semantic compression simulation: keep first and last parts
    lines = context.splitlines()
    if len(lines) <= 20:
        return context
    
    compressed = lines[:10] + ["... [SNIP] ..."] + lines[-10:]
    return "\n".join(compressed)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: context-compressor.py <file_path>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as f:
        print(compress_context(f.read()))
