#!/usr/bin/env python3
"""Fix YAML frontmatter for extracted skills."""

import re
from pathlib import Path

SKILLS_DIR = Path("/home/sephiroth/Work/overpowers/skills")

skills_data = {
    "occupational-health-analyzer": {
        "description": "分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。",
        "tags": ["health", "occupational", "workplace", "analyzer"],
    },
    "oral-health-analyzer": {
        "description": "分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。",
        "tags": ["health", "oral-care", "dental", "analyzer"],
    },
    "rehabilitation-analyzer": {
        "description": "分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议",
        "tags": ["health", "rehabilitation", "recovery", "analyzer"],
    },
    "sexual-health-analyzer": {
        "description": "分析性健康数据、识别性健康问题模式、评估性健康状况、提供个性化性健康建议。支持与用药、慢性病、心理、营养、运动等模块的深度关联分析。",
        "tags": ["health", "sexual-health", "analyzer", "wellness"],
    },
    "skin-health-analyzer": {
        "description": "分析皮肤健康数据、识别皮肤问题模式、评估皮肤健康状况。支持与营养、慢性病、用药等数据的关联分析。",
        "tags": ["health", "skin-care", "dermatology", "analyzer"],
    },
}

def fix_frontmatter(skill_name: str, data: dict):
    """Fix the frontmatter for a skill file."""
    skill_dir = SKILLS_DIR / skill_name
    skill_file = skill_dir / "SKILL.md"
    
    if not skill_file.exists():
        print(f"❌ {skill_name}: File not found")
        return False
    
    content = skill_file.read_text(encoding="utf-8")
    
    # Remove any existing frontmatter (everything between first --- and next ---)
    # Pattern matches from first --- to the closing ---
    content = re.sub(r'^---\s*\n', '', content, count=1, flags=re.MULTILINE)
    content = re.sub(r'^.*?\n---\s*\n', '', content, count=1, flags=re.DOTALL)
    
    # Also remove any duplicate name/description lines at the beginning
    content = re.sub(r'^name:.*?\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^description:.*?\n', '', content, flags=re.MULTILINE)
    
    # Create new frontmatter
    tags_str = "\n  - ".join(data["tags"])
    frontmatter = f"""---
name: {skill_name}
description: {data["description"]}
tags:
  - {tags_str}
version: "1.0.0"
category: health
---

"""
    
    # Write back
    new_content = frontmatter + content.lstrip('\n')
    skill_file.write_text(new_content, encoding="utf-8")
    
    print(f"✅ {skill_name}: Fixed")
    return True

if __name__ == "__main__":
    print("Fixing YAML frontmatter for extracted skills...\n")
    
    for skill_name, data in skills_data.items():
        fix_frontmatter(skill_name, data)
    
    print("\n✅ All skills processed!")
