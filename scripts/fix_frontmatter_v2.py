#!/usr/bin/env python3
"""Fix YAML frontmatter for extracted skills - manual line-by-line approach."""

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
    
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    
    # Find where the actual content starts (after all frontmatter)
    content_start = 0
    in_frontmatter = False
    dash_count = 0
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '---':
            dash_count += 1
            if dash_count >= 2:
                content_start = i + 1
                break
        elif dash_count > 0 and not in_frontmatter:
            in_frontmatter = True
    
    # Also skip any lines with name:, description:, etc. at the start
    while content_start < len(lines):
        line = lines[content_start].strip()
        if line.startswith('name:') or line.startswith('description:') or line.startswith('---'):
            content_start += 1
        else:
            break
    
    # Create new frontmatter
    tags_str = "\n  - ".join(data["tags"])
    frontmatter = [
        "---",
        f"name: {skill_name}",
        f"description: {data['description']}",
        "tags:",
        f"  - {tags_str}",
        'version: "1.0.0"',
        "category: health",
        "---",
        ""
    ]
    
    # Combine
    new_lines = frontmatter + lines[content_start:]
    new_content = '\n'.join(new_lines)
    
    skill_file.write_text(new_content, encoding="utf-8")
    
    print(f"✅ {skill_name}: Fixed")
    return True

if __name__ == "__main__":
    print("Fixing YAML frontmatter for extracted skills...\n")
    
    for skill_name, data in skills_data.items():
        fix_frontmatter(skill_name, data)
    
    print("\n✅ All skills processed!")
