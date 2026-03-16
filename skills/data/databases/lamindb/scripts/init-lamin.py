#!/usr/bin/env python3
import sys

try:
    import lamindb as ln
except ImportError:
    print("Error: lamindb is not installed.")
    print("Install it with: pip install lamindb")
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <storage_path_or_url>")
        sys.exit(1)

    storage = sys.argv[1]

    print(f"Initializing LaminDB instance at '{storage}'...")
    try:
        ln.setup.init(storage=storage)
        print("LaminDB initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize LaminDB: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
