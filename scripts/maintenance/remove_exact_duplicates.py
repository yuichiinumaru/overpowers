import os
import sys
import hashlib
from collections import defaultdict
import re
import datetime

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

def choose_best_file(files):
    # Heuristic: prefer files without '--' in the name (which were the older format). 
    # If multiple, pick the shortest name.
    no_hyphens = [f for f in files if '--' not in f]
    if no_hyphens:
        return sorted(no_hyphens, key=len)[0]
    return sorted(files, key=len)[0]

def cleanup_duplicates(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} not found, skipping...")
        return [], 0
        
    hashes = defaultdict(list)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md") and file not in ["AGENTS.md", "README.md", "CHANGELOG.md", "SKILL.md"]:
                filepath = os.path.join(root, file)
                file_hash = get_hash(filepath)
                if file_hash:
                    hashes[file_hash].append(filepath)

    duplicates = {k: v for k, v in hashes.items() if len(v) > 1}
    
    deleted_log = []
    deleted_count = 0
    
    for h, filepaths in duplicates.items():
        # Get just the filenames for sorting/choosing
        filenames = [os.path.basename(p) for p in filepaths]
        best_name = choose_best_file(filenames)
        
        # Find the full path for the best file
        best_path = next(p for p in filepaths if os.path.basename(p) == best_name)
        
        deleted_log.append(f"### Kept: `{best_name}` (in {os.path.dirname(best_path)})")
        for path in filepaths:
            if path != best_path:
                os.remove(path)
                deleted_log.append(f"- Deleted: `{os.path.basename(path)}` (from {os.path.dirname(path)})")
                deleted_count += 1
        deleted_log.append("")

    return deleted_log, deleted_count

if __name__ == "__main__":
    directories = sys.argv[1:]
    if not directories:
        print("Usage: python3 remove_exact_duplicates.py <dir1> <dir2> ...")
        sys.exit(1)

    print(f"Starting cleanup for directories: {', '.join(directories)}...")
    
    total_deleted = 0
    full_report = []
    
    for d in directories:
        log, count = cleanup_duplicates(d)
        if count > 0:
            full_report.append(f"## Directory: {d}")
            full_report.extend(log)
            total_deleted += count
            
    if total_deleted > 0:
        report_content = f"# Deduplication Report\n\nTotal files deleted across all specified directories: {total_deleted}\n\n"
        report_content += "\n".join(full_report)

        os.makedirs(".agents/thoughts", exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = f".agents/thoughts/deleted_duplicates_{timestamp}.md"
        with open(report_path, "w") as f:
            f.write(report_content)
        print(f"Cleanup complete. Deleted {total_deleted} files total. Report saved to {report_path}")
    else:
        print("No duplicates found in the specified directories.")
