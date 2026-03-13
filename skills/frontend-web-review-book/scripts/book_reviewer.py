#!/usr/bin/env python3
import os
import sys
import yaml

def review_book(book_path):
    toc_file = os.path.join(book_path, "_toc.yml")
    if not os.path.exists(toc_file):
        print(f"Error: {toc_file} not found.")
        return

    print(f"--- Reviewing Jupyter Book: {book_path} ---")
    with open(toc_file, "r") as f:
        toc = yaml.safe_load(f)

    # Simple parsing logic
    root = toc.get("root")
    parts = toc.get("parts", [])
    chapters = toc.get("chapters", [])

    print(f"Root File: {root}")
    if chapters:
        print(f"Chapters count: {len(chapters)}")
    if parts:
        print(f"Parts count: {len(parts)}")
        for part in parts:
            print(f"  Part: {part.get('caption', 'Untitled')}")
            print(f"  Chapters: {len(part.get('chapters', []))}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "docs/book"
    review_book(path)
