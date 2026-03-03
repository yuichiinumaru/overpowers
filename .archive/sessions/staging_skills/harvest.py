import os
import re
import shutil
import difflib
from pathlib import Path

ACTIVE_SKILLS_DIR = "/home/sephiroth/Work/overpowers/skills/"
SOURCE_DIRS = [
    "/home/sephiroth/Work/overpowers/.archive/jules_session_8638764147874203649/downloaded_skills/",
    "/home/sephiroth/Work/overpowers/.archive/jules_session_8131919827456435576/skills/",
    "/home/sephiroth/Work/overpowers/.archive/jules_session_8638764147874203649/skills/"
]
STAGING_DIR = "/home/sephiroth/Work/overpowers/.archive/staging_skills/"

def get_frontmatter(content):
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}, content
    
    fm_str = match.group(1)
    body = content[match.end():].strip()
    
    fm_dict = {}
    for line in fm_str.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            fm_dict[key.strip()] = val.strip().strip('"').strip("'")
            
    return fm_dict, body

def load_active_skills():
    active_skills = {}
    print("Loading active skills...")
    for item in os.listdir(ACTIVE_SKILLS_DIR):
        skill_path = os.path.join(ACTIVE_SKILLS_DIR, item, "SKILL.md")
        if os.path.isfile(skill_path):
            try:
                with open(skill_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    fm, body = get_frontmatter(content)
                    name = fm.get('name', item).lower()
                    active_skills[name] = body[:1000] # store first 1000 chars for comparison
            except Exception as e:
                pass
    print(f"Loaded {len(active_skills)} active skills.")
    return active_skills

def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

def process_skills():
    active_skills = load_active_skills()
    processed_count = 0
    duplicate_count = 0
    
    # Track what we put in staging to avoid duplicates within the source files themselves
    staged_skills = {} 

    for src_dir in SOURCE_DIRS:
        if not os.path.exists(src_dir):
            continue
            
        print(f"Scanning {src_dir}...")
        for root, _, files in os.walk(src_dir):
            for file in files:
                if not file.endswith('.md'):
                    continue
                    
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except:
                    continue
                    
                fm, body = get_frontmatter(content)
                
                # Determine name
                name = fm.get('name', '')
                if not name:
                    # try to get from filename
                    name = file.replace('_SKILL.md', '').replace('.md', '')
                    if name == 'SKILL':
                        name = os.path.basename(root)
                        
                name = name.lower().replace(' ', '-').replace('_', '-')
                if not name or name == 'readme':
                    continue
                
                # Check exact name match
                if name in active_skills or name in staged_skills:
                    duplicate_count += 1
                    continue
                    
                # Check similarity if body is substantial
                is_dup = False
                body_sample = body[:1000]
                if len(body_sample) > 200:
                    for active_name, active_body in active_skills.items():
                        if similar(body_sample, active_body) > 0.8:
                            print(f"  [DUP] {name} is too similar to {active_name}")
                            is_dup = True
                            break
                            
                if is_dup:
                    duplicate_count += 1
                    continue
                
                # Format for staging
                desc = fm.get('description', f"Automation and tasks for {name}")
                
                formatted_content = f"---\nname: {name}\ndescription: \"{desc}\"\n---\n\n"
                
                # ensure # Header exists
                if not body.startswith('# '):
                    formatted_content += f"# {name.replace('-', ' ').title()}\n\n"
                
                formatted_content += body
                
                # Create structure
                skill_dir = os.path.join(STAGING_DIR, name)
                os.makedirs(os.path.join(skill_dir, "scripts"), exist_ok=True)
                
                with open(os.path.join(skill_dir, "SKILL.md"), 'w', encoding='utf-8') as f:
                    f.write(formatted_content)
                
                staged_skills[name] = body_sample
                processed_count += 1

    print(f"\nDone! Processed {processed_count} new unique skills.")
    print(f"Skipped {duplicate_count} duplicates.")

if __name__ == "__main__":
    process_skills()
