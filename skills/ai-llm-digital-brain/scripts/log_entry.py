#!/usr/bin/env python3
"""
Add an append-only entry to a Digital Brain JSONL file.
"""
import sys
import os
import json
from datetime import datetime

def main():
    if len(sys.argv) < 3:
        print("Usage: log_entry.py <file_path> <json_content>")
        print('Example: log_entry.py content/ideas.jsonl \'{"idea": "New blog post about AI", "tags": ["ai", "blog"]}\'')
        sys.exit(1)

    file_path = sys.argv[1]
    content_str = sys.argv[2]

    try:
        content = json.loads(content_str)
    except json.JSONDecodeError:
        print("Error: Invalid JSON content.")
        sys.exit(1)

    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Add standard metadata
    content["timestamp"] = datetime.now().isoformat()
    content["status"] = content.get("status", "active")

    with open(file_path, 'a') as f:
        f.write(json.dumps(content) + '\n')

    print(f"Logged entry to {file_path}")

if __name__ == "__main__":
    main()
