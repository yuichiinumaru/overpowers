#!/usr/bin/env python3
import os
import glob

def build_pattern_readme():
    print("Building patterns README...")

    if not os.path.exists("patterns"):
        os.makedirs("patterns")
        print("Created patterns directory")

    patterns = glob.glob("patterns/*.md")

    with open("PATTERNS_INDEX.md", "w") as out:
        out.write("# Pattern Index\n\n")
        out.write("List of available patterns in this directory:\n\n")

        if not patterns:
            out.write("*No patterns found yet. Add markdown files to the patterns/ directory.*\n")
        else:
            for pattern in sorted(patterns):
                filename = os.path.basename(pattern)
                out.write(f"- [{filename}]({pattern})\n")

    print("Created PATTERNS_INDEX.md")

if __name__ == "__main__":
    build_pattern_readme()
