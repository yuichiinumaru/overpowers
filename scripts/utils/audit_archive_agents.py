import os
import re
import difflib
from pathlib import Path

ACTIVE_AGENTS_DIR = "/home/sephiroth/Work/overpowers/agents/"
ARCHIVE_DIRS = [
    "/home/sephiroth/Work/overpowers/.archive/agents/",
    "/home/sephiroth/Work/overpowers/.archive/"
]

def get_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove frontmatter for pure content comparison
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            return content.strip()
    except:
        return ""

def load_active():
    items = {}
    print(f"Indexing active agents in {ACTIVE_AGENTS_DIR}...")
    if not os.path.exists(ACTIVE_AGENTS_DIR):
        print(f"Directory {ACTIVE_AGENTS_DIR} not found.")
        return items
        
    for root, dirs, files in os.walk(ACTIVE_AGENTS_DIR):
        for file in files:
            if file.endswith(".md") and file not in ["AGENTS.md", "README.md", "CHANGELOG.md"]:
                item_name = file.replace(".md", "").replace("ovp-", "")
                content = get_content(os.path.join(root, file))
                if content:
                    items[item_name.lower()] = {
                        "content": content,
                        "sample": content[:500].lower()
                    }
    print(f"Indexed {len(items)} active agents.")
    return items

def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).quick_ratio()

def audit_archive():
    active_items = load_active()
    orphans = []
    
    print("\nAuditing archive directories...")
    checked_files = set()
    
    for session in ARCHIVE_DIRS:
        if not os.path.exists(session):
            continue
            
        for root, dirs, files in os.walk(session):
            # Skip skills directories if we are in the general archive
            if "skills" in root.split(os.sep):
                continue
                
            for file in files:
                if file.endswith(".md") and file not in ["AGENTS.md", "README.md", "CHANGELOG.md"]:
                    archive_path = os.path.join(root, file)
                    if archive_path in checked_files:
                        continue
                    checked_files.add(archive_path)
                    
                    archive_content = get_content(archive_path)
                    if not archive_content or len(archive_content) < 50:
                        continue
                        
                    file_name = file.replace(".md", "").replace("ovp-", "").lower()
                    
                    # 1. Check exact name match
                    if file_name in active_items:
                        continue
                        
                    # 2. Check semantic similarity
                    archive_sample = archive_content[:500].lower()
                    is_duplicate = False
                    
                    for active_name, data in active_items.items():
                        if archive_sample == data["sample"]:
                            is_duplicate = True
                            break
                        
                        if similar(archive_sample, data["sample"]) > 0.85:
                            is_duplicate = True
                            break
                            
                    if not is_duplicate:
                        orphans.append({
                            "name": file_name,
                            "path": archive_path,
                            "size": len(archive_content)
                        })

    print(f"\nAudit complete!")
    if orphans:
        print(f"Found {len(orphans)} unique agent-like markdowns in archive that ARE NOT in /agents/:\n")
        for o in sorted(orphans, key=lambda x: x['size'], reverse=True):
            print(f"- [{o['name']}] ({o['size']} bytes) at {o['path']}")
    else:
        print("No unique items found. All archive content is already active or too similar.")

if __name__ == "__main__":
    audit_archive()
