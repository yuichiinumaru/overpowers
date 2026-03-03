import os
import shutil
from pathlib import Path

ARCHIVE_DIR = "/home/sephiroth/Work/overpowers/.archive/jules_session_8131919827456435576/skills/"
STAGING_DIR = "/home/sephiroth/Work/overpowers/.archive/staging_skills/"
ACTIVE_SKILLS_DIR = "/home/sephiroth/Work/overpowers/skills/"

def migrate_scripts():
    print("Checking for scripts to migrate...")
    moved_count = 0
    
    for root, _, files in os.walk(ARCHIVE_DIR):
        for file in files:
            if file.endswith(('.py', '.sh', '.ts', '.js', '.json')) and file != 'SKILL.md':
                source_path = os.path.join(root, file)
                
                # Extract skill name from path
                # Path looks like: .../skills/<skill-name>/scripts/...
                rel_path = os.path.relpath(source_path, ARCHIVE_DIR)
                parts = rel_path.split(os.sep)
                
                if len(parts) >= 2:
                    skill_name = parts[0]
                    
                    # Target directories
                    staging_skill_dir = os.path.join(STAGING_DIR, skill_name)
                    active_skill_dir = os.path.join(ACTIVE_SKILLS_DIR, skill_name)
                    
                    # Determine where this skill lives now
                    target_dir = None
                    if os.path.exists(staging_skill_dir):
                        target_dir = staging_skill_dir
                    elif os.path.exists(active_skill_dir):
                        target_dir = active_skill_dir
                        
                    if target_dir:
                        # Reconstruct the path inside the skill folder
                        # e.g., if original was skills/pdf/scripts/convert.py -> we want target_dir/scripts/convert.py
                        sub_path = os.path.join(*parts[1:-1]) if len(parts) > 2 else "scripts"
                        
                        # Always enforce putting them in 'scripts' if not already
                        if not sub_path.startswith("scripts"):
                            sub_path = os.path.join("scripts", sub_path)
                            
                        dest_folder = os.path.join(target_dir, sub_path)
                        os.makedirs(dest_folder, exist_ok=True)
                        
                        dest_path = os.path.join(dest_folder, file)
                        
                        if not os.path.exists(dest_path):
                            shutil.copy2(source_path, dest_path)
                            print(f"Moved script: {file} -> {skill_name}/scripts/")
                            moved_count += 1

    print(f"Finished migrating {moved_count} missing scripts to their proper skill folders.")

if __name__ == "__main__":
    migrate_scripts()
