#!/usr/bin/env python3
"""
Skill Standardizer - Standardizes metadata and structure of Overpowers skills
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

import yaml

# Base paths
WORKSPACE_ROOT = Path(__file__).parent.parent


def infer_category(skill_path: Path) -> str:
    """Infer category based on parent directory"""
    parent_name = skill_path.parent.name
    mapping = {
        "ai-llm": "ai",
        "content-media": "content",
        "design-ux": "design",
        "dev-backend": "backend",
        "dev-code": "development",
        "dev-frontend": "frontend",
        "growth-biz": "business",
        "infra-ops": "operations",
        "ops-infra": "operations",
        "sci-bio": "science",
        "sci-chem": "science",
        "sci-quant": "science",
        "sec-safety": "security",
        "safety-sec": "security"
    }
    return mapping.get(parent_name, "general")


def standardize_name(name: str) -> str:
    """Convert name to hyphen-case"""
    # Replace colons, underscores and dots with hyphens
    name = name.replace(":", "-").replace("_", "-").replace(".", "-")
    # Remove any non-alphanumeric characters except hyphens
    name = re.sub(r"[^a-z0-9-]", "", name.lower())
    # Clean up double hyphens and leading/trailing hyphens
    name = re.sub(r"-+", "-", name).strip("-")
    return name


def standardize_skill(skill_path: Path, dry_run: bool = True) -> Dict:
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return {"valid": False, "error": "SKILL.md missing"}

    content = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {"valid": False, "error": "No frontmatter"}

    original_frontmatter_text = match.group(1)
    body = content[match.end():]

    try:
        frontmatter = yaml.safe_load(original_frontmatter_text)
        if not isinstance(frontmatter, dict):
            return {"valid": False, "error": "Invalid YAML"}
    except yaml.YAMLError as e:
        return {"valid": False, "error": f"YAML error: {e}"}

    modified = False

    # 1. Standardize name
    if "name" in frontmatter:
        old_name = frontmatter["name"]
        new_name = standardize_name(old_name)
        if old_name != new_name:
            frontmatter["name"] = new_name
            modified = True

    # 2. Add missing fields
    if "version" not in frontmatter:
        frontmatter["version"] = "1.0.0"
        modified = True

    if "category" not in frontmatter:
        frontmatter["category"] = infer_category(skill_path)
        modified = True

    if "tags" not in frontmatter:
        # Simple tag generation based on category and name parts
        tags = [frontmatter["category"]]
        name_parts = frontmatter.get("name", "").split("-")
        tags.extend([p for p in name_parts if len(p) > 2])
        frontmatter["tags"] = sorted(list(set(tags)))[:5]
        modified = True

    if modified and not dry_run:
        # Use a custom representer to ensure clean YAML output
        new_frontmatter_text = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True)
        new_content = f"---\n{new_frontmatter_text}---{body}"
        skill_md.write_text(new_content)

    return {
        "valid": True,
        "modified": modified,
        "original_name": original_frontmatter_text.split("\n")[0], # Hint
        "new_name": frontmatter.get("name")
    }


def main():
    dry_run = "--apply" not in sys.argv
    target_args = [arg for arg in sys.argv[1:] if arg != "--apply"]

    if target_args:
        target_paths = [Path(p).resolve() for p in target_args]
    else:
        skills_dir = WORKSPACE_ROOT / "skills"
        target_paths = sorted([p.resolve() for p in skills_dir.iterdir() if p.is_dir()])

    total = 0
    modified_count = 0

    for path in target_paths:
        if not (path / "SKILL.md").exists():
            continue

        total += 1
        result = standardize_skill(path, dry_run=dry_run)
        
        if result.get("modified"):
            modified_count += 1
            status = "[MODIFIED]" if not dry_run else "[WOULD MODIFY]"
            print(f"{status} {path.name}")

    print(f"\nSummary: {total} skills checked, {modified_count} { 'modified' if not dry_run else 'need modification' }.")


if __name__ == "__main__":
    main()
