#!/usr/bin/env python3
import sys
import asyncio

try:
    from kreuzberg import batch_extract_files
except ImportError:
    print("Please install kreuzberg: pip install kreuzberg")
    sys.exit(1)

async def main():
    if len(sys.argv) < 2:
        print("Usage: batch-extract.py <file1> [file2 ...]")
        sys.exit(1)

    files = sys.argv[1:]
    print(f"Extracting {len(files)} files...")

    try:
        results = await batch_extract_files(files)
        for i, result in enumerate(results):
            print(f"--- File: {files[i]} ---")
            print(f"Extracted {len(result.content)} characters")
    except Exception as e:
        print(f"Error during extraction: {e}")

if __name__ == "__main__":
    asyncio.run(main())
