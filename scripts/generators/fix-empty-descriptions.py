#!/usr/bin/env python3
"""
Fix SKILL.md files that have an empty description field.

Scans all skills/*/SKILL.md files and replaces `description: ''` with a
description auto-extracted from the first heading or first paragraph of the
markdown body.

Usage:
    uv run scripts/generators/fix-empty-descriptions.py [--dry-run]
"""

import os
import re
import sys
import yaml

SKILLS_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'skills')

def _quote_yaml(s):
    """Quote a string for YAML without using yaml.dump (which adds '...')."""
    if not s:
        return "''"
    # If it contains special chars, wrap in single quotes (escaping internal single quotes)
    if any(c in s for c in ":{}[]&*?|>!%@`#,"):
        return "'" + s.replace("'", "''") + "'"
    return s

def extract_description(body):
    """Extract a description from the markdown body."""
    lines = body.strip().split('\n')
    
    # Strategy 1: First heading text
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            heading = stripped.lstrip('#').strip()
            if heading and len(heading) > 5:
                return heading[:150]
    
    # Strategy 2: First non-empty paragraph
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not stripped.startswith('```') and not stripped.startswith('|') and not stripped.startswith('-') and not stripped.startswith('>'):
            # Clean up markdown links
            clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', stripped)
            if len(clean) > 10:
                return clean[:150]
    
    return None


def fix_skill(skill_path, dry_run=False):
    """Fix a single SKILL.md file. Returns True if fixed."""
    try:
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return False
    
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter_str = parts[1]
    body = parts[2]
    
    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError:
        return False
    
    if not isinstance(frontmatter, dict):
        return False
    
    desc = frontmatter.get('description', None)
    
    # Only fix truly empty descriptions
    if desc is not None and desc != '' and desc != "''":
        return False
    
    new_desc = extract_description(body)
    if not new_desc:
        skill_name = os.path.basename(os.path.dirname(skill_path))
        new_desc = f"Skill: {skill_name.replace('-', ' ').title()}"
    
    # Replace the description in the frontmatter string
    # Handle both `description: ''` and `description: ""`
    new_frontmatter = re.sub(
        r"description:\s*['\"]?['\"]?\s*\n",
        f"description: {_quote_yaml(new_desc)}\n",
        frontmatter_str
    )
    
    # Handle multiline description values from yaml
    if new_frontmatter == frontmatter_str:
        # Fallback: try a broader regex
        new_frontmatter = re.sub(
            r"description:\s*''",
            f"description: {_quote_yaml(new_desc)}",
            frontmatter_str
        )
    
    if new_frontmatter == frontmatter_str:
        return False
    
    new_content = f"---{new_frontmatter}---{body}"
    
    if dry_run:
        print(f"  [DRY-RUN] Would fix: {skill_path}")
        print(f"            New desc: {new_desc[:80]}")
        return True
    
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


def main():
    dry_run = '--dry-run' in sys.argv
    skills_dir = os.path.abspath(SKILLS_DIR)
    
    if not os.path.isdir(skills_dir):
        print(f"❌ Skills directory not found: {skills_dir}")
        sys.exit(1)
    
    print(f"🔍 Scanning {skills_dir} for skills with empty descriptions...")
    if dry_run:
        print("   (DRY-RUN mode — no files will be modified)\n")
    
    fixed = 0
    skipped = 0
    errors = 0
    
    for folder in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, folder, 'SKILL.md')
        if not os.path.isfile(skill_path):
            continue
        
        try:
            if fix_skill(skill_path, dry_run):
                fixed += 1
                if not dry_run:
                    print(f"  ✅ Fixed: {folder}")
            else:
                skipped += 1
        except Exception as e:
            errors += 1
            print(f"  ❌ Error in {folder}: {e}")
    
    print(f"\n{'='*50}")
    print(f"Fixed: {fixed}")
    print(f"Skipped (already OK): {skipped}")
    print(f"Errors: {errors}")
    

if __name__ == '__main__':
    main()
