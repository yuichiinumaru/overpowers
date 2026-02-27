#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

SKILL_DIR = Path("/home/sephiroth/Work/overpowers/skills")

def has_skill_md(dir_path: Path) -> bool:
    return (dir_path / "SKILL.md").is_file() or (dir_path / "SKILL.md".lower()).is_file() or (dir_path / "SKILL.MD").is_file()

def flatten_skills():
    print(f" Flattening skills in {SKILL_DIR}")
    moved_count = 0
    
    # Check top-level directories
    for category_dir in list(SKILL_DIR.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
            
        if has_skill_md(category_dir):
            continue
            
        print(f"\n📂 Investigating category: {category_dir.name}")
        
        for root, dirs, files in os.walk(category_dir, topdown=False):
            root_path = Path(root)
            
            if root_path == category_dir:
                continue
                
            if has_skill_md(root_path):
                # Valid skill found deep in hierarchy
                skill_name = root_path.name
                target_path = SKILL_DIR / skill_name
                
                # Prevent overwrite
                counter = 1
                while target_path.exists():
                    target_path = SKILL_DIR / f"{skill_name}_{counter}"
                    counter += 1
                
                print(f"  📦 Moving skill '{root_path.relative_to(SKILL_DIR)}' -> '{target_path.relative_to(SKILL_DIR)}'")
                shutil.move(str(root_path), str(target_path))
                moved_count += 1
        
        # After moving valid skills, attempt to clean up empty directories
        for root, dirs, files in os.walk(category_dir, topdown=False):
            root_path = Path(root)
            try:
                if not any(root_path.iterdir()):
                    root_path.rmdir()
                    print(f"  🗑️ Removed empty dir: {root_path.relative_to(SKILL_DIR)}")
            except OSError as e:
                pass # Not empty
                
    print(f"\n✅ Finished! Moved {moved_count} skills to the root.")

if __name__ == "__main__":
    flatten_skills()
