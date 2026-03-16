#!/usr/bin/env python3
"""
Batch processor for Task 0500 - Extraction Skills Batch 026
Processes 25 skill assets from staging to skills directory
"""

import os
import re
import shutil
from pathlib import Path

BASE_DIR = Path("/home/sephiroth/Work/overpowers")
STAGING_DIR = BASE_DIR / ".archive/staging/skills"
SKILLS_DIR = BASE_DIR / "skills"

# Skill mapping: (staging_file, skill_name, directory_name)
SKILLS_TO_PROCESS = [
    ("wechat-mp-writer-skill-mxx_SKILL.md", "wechat-mp-writer", "wechat-mp-writer"),
    ("zhouyi-divination_SKILL.md", "zhouyi-divination", "zhouyi-divination"),
    ("complex-task-methodology_SKILL.md", "complex-task-methodology", "complex-task-methodology"),
    ("openclaw-guardian-suite_SKILL.md", "openclaw-guardian-suite", "openclaw-guardian-suite"),
    ("semantic-router_SKILL.md", "semantic-router", "semantic-router"),
    ("subagent-isolation-guard_SKILL.md", "subagent-isolation-guard", "subagent-isolation-guard"),
    ("yanjibus_SKILL.md", "yanjibus", "yanjibus"),
    ("meme-scanner_SKILL.md", "meme-scanner", "meme-scanner"),
    ("cursor-council_SKILL.md", "cursor-council", "cursor-council"),
    ("sulada-clawdchat_SKILL.md", "sulada-clawdchat", "sulada-clawdchat"),
    ("sulada-habit-tracker_SKILL.md", "sulada-habit-tracker", "sulada-habit-tracker"),
    ("sulada-knowledge-base_SKILL.md", "sulada-knowledge-base", "sulada-knowledge-base"),
    ("testa_SKILL.md", "testa", "testa"),
    ("zan-diary_SKILL.md", "zan-diary", "zan-diary"),
    ("target-info-search-summarization_SKILL.md", "target-info-search-summarization", "target-info-search-summarization"),
    ("openclaw-parking-query_SKILL.md", "openclaw-parking-query", "openclaw-parking-query"),
    ("surf-query_SKILL.md", "surf-query", "surf-query"),
    ("health-manager_SKILL.md", "health-manager", "health-manager"),
    ("learning-planner_SKILL.md", "learning-planner", "learning-planner"),
    ("reading-buddy_SKILL.md", "reading-buddy", "reading-buddy"),
    ("reading-manager_SKILL.md", "reading-manager", "reading-manager"),
    ("study-buddy_SKILL.md", "study-buddy", "study-buddy"),
    ("trip_SKILL.md", "trip", "trip"),
    ("feedback-loop_SKILL.md", "feedback-loop", "feedback-loop"),
    ("skill-assessment_SKILL.md", "skill-assessment", "skill-assessment"),
]

def ensure_frontmatter(content, skill_name):
    """Ensure the skill has proper frontmatter with non-empty description"""
    # Check if frontmatter exists
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        rest = content[frontmatter_match.end():]
        
        # Check if description exists and is non-empty
        desc_match = re.search(r'^description:\s*[\'"](.+?)[\'"]\s*$', frontmatter, re.MULTILINE)
        if desc_match and desc_match.group(1).strip():
            # Has valid description, return as-is
            return content
        
        # Check for description without quotes
        desc_match2 = re.search(r'^description:\s*(.+?)\s*$', frontmatter, re.MULTILINE)
        if desc_match2 and desc_match2.group(1).strip() and desc_match2.group(1) not in ["''", '""', "null", "~"]:
            return content
            
        # Need to add or fix description
        lines = frontmatter.split('\n')
        new_lines = []
        desc_added = False
        
        for line in lines:
            if line.startswith('name:'):
                new_lines.append(line)
                # Add description after name
                new_lines.append(f'description: "AI skill for {skill_name.replace("-", " ")}"')
                desc_added = True
            elif line.startswith('description:'):
                # Skip existing empty description
                continue
            else:
                new_lines.append(line)
        
        if not desc_added:
            # Insert description after name
            for i, line in enumerate(new_lines):
                if line.startswith('name:'):
                    new_lines.insert(i+1, f'description: "AI skill for {skill_name.replace("-", " ")}"')
                    break
        
        return '---\n' + '\n'.join(new_lines) + '\n---\n' + rest
    else:
        # No frontmatter, add it
        return f'''---
name: {skill_name}
description: "AI skill for {skill_name.replace("-", " ")}"
version: "1.0.0"
tags: ["skill", "ai"]
---

{content}'''

def process_skill(staging_file, skill_name, dir_name):
    """Process a single skill file"""
    staging_path = STAGING_DIR / staging_file
    skill_dir = SKILLS_DIR / dir_name
    dest_path = skill_dir / "SKILL.md"
    
    # Check if source exists
    if not staging_path.exists():
        return False, f"Source file not found: {staging_path}"
    
    # Read content
    try:
        content = staging_path.read_text(encoding='utf-8')
    except Exception as e:
        return False, f"Error reading {staging_path}: {e}"
    
    # Ensure proper frontmatter
    processed_content = ensure_frontmatter(content, skill_name)
    
    # Create destination directory
    try:
        skill_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return False, f"Error creating directory {skill_dir}: {e}"
    
    # Write to destination
    try:
        dest_path.write_text(processed_content, encoding='utf-8')
    except Exception as e:
        return False, f"Error writing {dest_path}: {e}"
    
    # Delete source file
    try:
        staging_path.unlink()
    except Exception as e:
        return False, f"Error deleting {staging_path}: {e}"
    
    return True, f"Successfully processed {skill_name}"

def main():
    print("=" * 60)
    print("Processing Task 0500 - Extraction Skills Batch 026")
    print("=" * 60)
    
    results = {
        'success': [],
        'failed': [],
        'skipped': []
    }
    
    for staging_file, skill_name, dir_name in SKILLS_TO_PROCESS:
        print(f"\nProcessing: {skill_name}...")
        success, message = process_skill(staging_file, skill_name, dir_name)
        
        if success:
            print(f"  ✅ {message}")
            results['success'].append((skill_name, dir_name))
        else:
            print(f"  ❌ {message}")
            results['failed'].append((skill_name, message))
    
    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"✅ Successfully processed: {len(results['success'])}")
    print(f"❌ Failed: {len(results['failed'])}")
    print(f"⏭️  Skipped: {len(results['skipped'])}")
    
    if results['success']:
        print("\n✅ Successful skills:")
        for skill_name, dir_name in results['success']:
            print(f"  - {skill_name} → skills/{dir_name}/SKILL.md")
    
    if results['failed']:
        print("\n❌ Failed skills:")
        for skill_name, reason in results['failed']:
            print(f"  - {skill_name}: {reason}")
    
    return results

if __name__ == "__main__":
    main()
