import sys
import os

def map_files_to_docs(files):
    mappings = {
        'packages/next/src/client/components/': 'Component API reference',
        'packages/next/src/server/': 'Function API reference',
        'packages/next/src/shared/lib/': 'Shared Library (varies)',
        'packages/next/src/build/': 'Configuration or build docs',
        'packages/next/src/lib/': 'Various features'
    }
    
    impacted = {}
    for file in files:
        for prefix, doc_type in mappings.items():
            if file.startswith(prefix):
                impacted[file] = doc_type
                break
    
    if not impacted:
        print("No direct documentation impacts identified from standard paths.")
    else:
        print(f"{'Source File':<50} | {'Likely Doc Impact'}")
        print("-" * 80)
        for src, impact in impacted.items():
            print(f"{src:<50} | {impact}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python doc_mapper.py <file1> [file2] ...")
        sys.exit(1)
    map_files_to_docs(sys.argv[1:])
