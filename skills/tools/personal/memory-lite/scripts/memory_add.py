import argparse
import os
from datetime import datetime

def add_memory(kind, text):
    if kind == "daily":
        today = datetime.now().strftime("%Y-%m-%d")
        file_path = f"memory/{today}.md"
        os.makedirs("memory", exist_ok=True)
    elif kind == "long":
        file_path = "MEMORY.md"
    else:
        print("Invalid kind. Use 'daily' or 'long'.")
        return

    with open(file_path, "a") as f:
        timestamp = datetime.now().strftime("%H:%M:%S")
        f.write(f"- [{timestamp}] {text}\n")
    print(f"Added to {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add to memory files.")
    parser.add_argument("--kind", choices=["daily", "long"], required=True)
    parser.add_argument("--text", required=True)
    
    args = parser.parse_args()
    add_memory(args.kind, args.text)
