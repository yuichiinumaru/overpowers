#!/usr/bin/env python3
import os
import re
import yaml
import sys

# Colors for terminal output
GREEN = "\033[0;32m"
RED = "\033[0;31m"
YELLOW = "\033[1;33m"
CYAN = "\033[0;36m"
NC = "\033[0m"

SKILLS_DIR = "skills"

def print_success(msg):
    print(f"{GREEN}✓ {msg}{NC}")

def print_error(msg):
    print(f"{RED}✗ {msg}{NC}")

def print_warning(msg):
    print(f"{YELLOW}⚠ {msg}{NC}")

def print_step(msg):
    print(f"{CYAN}▶ {msg}{NC}")

def get_frontmatter(content):
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except Exception as e:
            return None
    return None

def validate_skill(skill_path):
    skill_md = os.path.join(skill_path, "SKILL.md")
    skill_name = os.path.basename(skill_path)
    
    if not os.path.exists(skill_md):
        return False, "Missing SKILL.md"
    
    try:
        with open(skill_md, "r") as f:
            content = f.read()
    except Exception as e:
        return False, f"Could not read SKILL.md: {e}"
    
    fm = get_frontmatter(content)
    if fm is None:
        if "---\n" in content:
            return False, "Invalid YAML frontmatter"
        else:
            return False, "Missing YAML frontmatter"
            
    required_fields = ["name", "description"]
    missing = [field for field in required_fields if field not in fm]
    
    if missing:
        return False, f"Missing fields in frontmatter: {', '.join(missing)}"
        
    return True, "Valid"

def main():
    print_step("Overpowers Skill Integrity Check & Local Setup")
    
    if not os.path.isdir(SKILLS_DIR):
        print_error(f"Directory '{SKILLS_DIR}' not found.")
        sys.exit(1)
        
    skills = [d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))]
    skills.sort()
    
    total = len(skills)
    valid_count = 0
    invalid_count = 0
    
    print_step(f"Analyzing {total} skills...")
    
    for skill in skills:
        path = os.path.join(SKILLS_DIR, skill)
        is_valid, reason = validate_skill(path)
        
        if is_valid:
            valid_count += 1
        else:
            print_warning(f"Skill '{skill}': {reason}")
            invalid_count += 1
            
    print("\n" + "="*40)
    print_step("Results:")
    print(f"Total skills found: {total}")
    print_success(f"Valid skills: {valid_count}")
    if invalid_count > 0:
        print_error(f"Invalid skills: {invalid_count}")
        print_warning("Please fix the issues reported above to ensure all skills are available to agents.")
    else:
        print_success("All skills are in perfect condition!")
    print("="*40)

if __name__ == "__main__":
    main()
