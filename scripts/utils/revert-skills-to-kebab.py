#!/usr/bin/env python3
"""
Reverts skill names from snake_case back to kebab-case.
OpenCode Skills REQUIRE kebab-case in:
  1. Directory names
  2. The 'name:' field in SKILL.md frontmatter

Run this if you accidentally converted skills to snake_case.
"""
import os
import re

def to_kebab_case(name):
    """Convert snake_case to kebab-case"""
    return name.replace('_', '-')

def revert_skill_dirs(skills_dir):
    """Rename skill directories from snake_case to kebab-case"""
    if not os.path.isdir(skills_dir):
        print(f"Directory not found: {skills_dir}")
        return {}

    renames = {}
    dirs = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))]
    
    for dirname in dirs:
        if dirname.startswith("_"):
            continue  # Skip _staging etc.
        
        new_dirname = to_kebab_case(dirname)
        if new_dirname != dirname:
            old_path = os.path.join(skills_dir, dirname)
            new_path = os.path.join(skills_dir, new_dirname)
            print(f"Renaming dir: {dirname} -> {new_dirname}")
            os.rename(old_path, new_path)
            renames[dirname] = new_dirname
    
    return renames

def revert_skill_frontmatter(skills_dir):
    """Update the 'name:' field in SKILL.md files to kebab-case"""
    for dirname in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, dirname)
        if not os.path.isdir(skill_path):
            continue
        
        skill_md = os.path.join(skill_path, "SKILL.md")
        if not os.path.exists(skill_md):
            continue
        
        try:
            with open(skill_md, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find frontmatter
            match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                continue
            
            frontmatter = match.group(1)
            
            # Find and fix name field (convert underscores to hyphens)
            name_match = re.search(r'^name:\s*["\']?([^"\'\n]+)["\']?', frontmatter, re.MULTILINE)
            if name_match:
                old_name = name_match.group(1).strip()
                new_name = to_kebab_case(old_name)
                
                if old_name != new_name:
                    new_frontmatter = frontmatter.replace(f"name: {old_name}", f"name: {new_name}")
                    new_frontmatter = new_frontmatter.replace(f'name: "{old_name}"', f'name: "{new_name}"')
                    new_frontmatter = new_frontmatter.replace(f"name: '{old_name}'", f"name: '{new_name}'")
                    
                    new_content = content.replace(frontmatter, new_frontmatter)
                    
                    with open(skill_md, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"Fixed frontmatter: {dirname}/SKILL.md ({old_name} -> {new_name})")
        except Exception as e:
            print(f"Error processing {skill_md}: {e}")

if __name__ == "__main__":
    skills_dir = "/home/sephiroth/.config/opencode/Overpowers/skills"
    
    print("=== Reverting Skills to kebab-case ===")
    print("\n--- Reverting directories ---")
    revert_skill_dirs(skills_dir)
    
    print("\n--- Reverting SKILL.md frontmatter ---")
    revert_skill_frontmatter(skills_dir)
    
    print("\nDone!")
