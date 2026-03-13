import os
import re
import difflib
from pathlib import Path

ACTIVE_SKILLS_DIR = "/home/sephiroth/Work/overpowers/skills/"
ARCHIVE_SESSIONS = [
    "/home/sephiroth/Work/overpowers/.archive/jules_session_8131919827456435576",
    "/home/sephiroth/Work/overpowers/.archive/jules_session_8638764147874203649",
    "/home/sephiroth/Work/overpowers/.archive/skills/"
]

def get_skill_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove frontmatter for pure content comparison
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            return content.strip()
    except:
        return ""

def load_active_skills():
    skills = {}
    print(f"Indexing active skills in {ACTIVE_SKILLS_DIR}...")
    for root, dirs, files in os.walk(ACTIVE_SKILLS_DIR):
        if "SKILL.md" in files:
            skill_name = os.path.basename(root)
            content = get_skill_content(os.path.join(root, "SKILL.md"))
            if content:
                # Store sample and full for exact matching
                skills[skill_name.lower()] = {
                    "content": content,
                    "sample": content[:500].lower()
                }
    print(f"Indexed {len(skills)} active skills.")
    return skills

def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).quick_ratio()

def audit_archive():
    active_skills = load_active_skills()
    orphans = []
    
    print("\nAuditing archive sessions...")
    for session in ARCHIVE_SESSIONS:
        if not os.path.exists(session):
            continue
            
        for root, dirs, files in os.walk(session):
            for file in files:
                if file.endswith("SKILL.md"):
                    archive_path = os.path.join(root, file)
                    archive_content = get_skill_content(archive_path)
                    if not archive_content:
                        continue
                        
                    # Extract a logical name
                    # Some files are named like 'OSINT_SKILL.md', others are in folder 'skills/name/SKILL.md'
                    folder_name = os.path.basename(root).lower()
                    file_name = file.replace("_SKILL.md", "").replace("SKILL.md", "").lower()
                    possible_name = folder_name if folder_name not in ["skills", "downloaded_skills"] else file_name
                    
                    if not possible_name:
                        continue

                    # 1. Check exact name match
                    if possible_name in active_skills:
                        continue
                        
                    # 2. Check semantic similarity
                    archive_sample = archive_content[:500].lower()
                    is_duplicate = False
                    
                    # Optimization: only check similarity if name doesn't match
                    for active_name, data in active_skills.items():
                        # Quick check on sample first
                        if archive_sample == data["sample"]:
                            is_duplicate = True
                            break
                        
                        # Deeper check if sample is different but name might be similar
                        if similar(archive_sample, data["sample"]) > 0.85:
                            is_duplicate = True
                            break
                            
                    if not is_duplicate:
                        orphans.append({
                            "name": possible_name,
                            "path": archive_path,
                            "size": len(archive_content)
                        })

    print(f"\nAudit complete!")
    if orphans:
        print(f"Found {len(orphans)} unique skills in archive that ARE NOT in /skills/:\n")
        # Sort by size to prioritize meaningful content
        for o in sorted(orphans, key=lambda x: x['size'], reverse=True):
            print(f"- [{o['name']}] ({o['size']} bytes) at {o['path']}")
    else:
        print("No unique skills found. All archive content is already active or too similar to active skills.")

if __name__ == "__main__":
    audit_archive()
