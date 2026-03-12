#!/usr/bin/env python3
import os
import json
import yaml
import re
from pathlib import Path

SKILLS_DIR = "skills"
MAP_FILE_1 = "docs/architecture/codemaps/003-arch-skills-map.json"
MAP_FILE_2 = ".agents/knowledge/kb_skills_mapping.json"

def parse_skill(skill_dir):
    skill_path = Path(skill_dir)
    skill_md = skill_path / "SKILL.md"
    
    if not skill_md.exists():
        return None
    
    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    metadata = {}
    
    # Extract YAML frontmatter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if match:
        try:
            frontmatter = yaml.safe_load(match.group(1))
            if isinstance(frontmatter, dict):
                metadata.update(frontmatter)
        except Exception as e:
            print(f"Warning: Failed to parse frontmatter in {skill_md}: {e}")
            pass
            
        content_after_frontmatter = content[match.end():].strip()
    else:
        content_after_frontmatter = content.strip()

    name = metadata.get("name")
    if not name:
        # Try to find a heading 1
        h1_match = re.search(r"^#\s+(.+)$", content_after_frontmatter, re.MULTILINE)
        if h1_match:
            name = h1_match.group(1).strip()
        else:
            name = skill_path.name
            
    description = metadata.get("description", "").strip()
    if not description:
        # Try to find the first paragraph after a heading
        paragraphs = re.split(r'\n\s*\n', content_after_frontmatter)
        for p in paragraphs:
            p = p.strip()
            if p and not p.startswith('#') and not p.startswith('---') and not p.startswith('```') and not p.startswith('|'):
                description = p
                # Remove newlines within the paragraph
                description = ' '.join(description.split())
                break

    return {
        "id": skill_path.name,
        "name": name,
        "description": description,
        "directory": str(skill_path)
    }

def main():
    skills = []
    
    for item in os.listdir(SKILLS_DIR):
        skill_dir = os.path.join(SKILLS_DIR, item)
        if os.path.isdir(skill_dir):
            skill_data = parse_skill(skill_dir)
            if skill_data:
                skills.append(skill_data)
                
    # Sort alphabetically by ID
    skills.sort(key=lambda x: x["id"])
    
    os.makedirs(os.path.dirname(MAP_FILE_1), exist_ok=True)
    os.makedirs(os.path.dirname(MAP_FILE_2), exist_ok=True)

    with open(MAP_FILE_1, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2)
        
    with open(MAP_FILE_2, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2)
        
    print(f"Successfully mapped {len(skills)} skills.")
    print(f"Saved to {MAP_FILE_1} and {MAP_FILE_2}")

if __name__ == "__main__":
    main()
