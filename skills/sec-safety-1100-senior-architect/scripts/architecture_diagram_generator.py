import os
import sys

def generate_diagram(path):
    print(f"--- Architecture Diagram Generator for {path} ---")
    print("Scanning directory structure...")
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files[:5]: # Limit to first 5 files
            print(f"{subindent}{f}")
        if len(files) > 5:
            print(f"{subindent}...")
        if level > 2: # Limit depth
            break

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    generate_diagram(target)
