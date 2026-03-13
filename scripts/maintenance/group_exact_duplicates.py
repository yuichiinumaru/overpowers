import os
import hashlib
from collections import defaultdict
import re

def get_hash(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove frontmatter for pure content comparison
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL).strip()
            if len(content) < 10:
                return None
            return hashlib.md5(content.encode('utf-8')).hexdigest()
    except:
        return None

def find_exact_duplicates(directory):
    hashes = defaultdict(list)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md") and file not in ["AGENTS.md", "README.md", "CHANGELOG.md", "SKILL.md"]:
                filepath = os.path.join(root, file)
                file_hash = get_hash(filepath)
                if file_hash:
                    hashes[file_hash].append(file)
            elif file == "SKILL.md":
                filepath = os.path.join(root, file)
                file_hash = get_hash(filepath)
                if file_hash:
                    hashes[file_hash].append(os.path.basename(root))

    duplicates = {k: v for k, v in hashes.items() if len(v) > 1}
    
    print(f"\nExact duplicates in {directory}/ :")
    count = 0
    for h, files in duplicates.items():
        count += len(files) - 1
        print(f"Group: {', '.join(files)}")
    print(f"Total redundant files to remove: {count}")

find_exact_duplicates("agents")
find_exact_duplicates("workflows/toml")
