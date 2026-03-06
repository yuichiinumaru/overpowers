#!/usr/bin/env python3
import sys

try:
    import lamindb as ln
except ImportError:
    print("Please install lamindb: pip install lamindb")
    sys.exit(1)

def main():
    print("Initializing LaminDB tracking...")
    ln.track()
    print("Tracking started. Run your analysis, then call ln.finish().")

if __name__ == "__main__":
    main()
