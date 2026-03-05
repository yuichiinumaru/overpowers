import sys

def split_library(path):
    print(f"Splitting Excalidraw library at: {path}")
    print("Logic to extract icons into individual JSON files goes here.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split-excalidraw-library.py <library-path>")
        sys.exit(1)
    split_library(sys.argv[1])
