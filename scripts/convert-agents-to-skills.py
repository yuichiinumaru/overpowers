#!/usr/bin/env python3
"""
OpenCode Agent → Antigravity Skill Converter
Converts OpenCode agent .md files into Antigravity-compatible SKILL.md format.
"""

import os
import re
import sys
from pathlib import Path


def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown."""
    frontmatter = {}
    body = content
    
    # Check for existing frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            for line in fm_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip().strip('"\'')
            body = parts[2].strip()
    
    return frontmatter, body


def extract_name_description(content: str, filename: str) -> tuple[str, str]:
    """Extract name and description from agent content."""
    name = filename.replace('.md', '').replace('_', '-')
    description = ""
    
    # Try to find first heading
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        name = h1_match.group(1).strip()
    
    # Try to find first paragraph after heading (description)
    desc_match = re.search(r'^#.+\n+(.+?)(?:\n\n|\n#)', content, re.MULTILINE | re.DOTALL)
    if desc_match:
        description = desc_match.group(1).strip()
        # Truncate if too long
        if len(description) > 200:
            description = description[:197] + '...'
    
    if not description:
        description = f"Agent skill converted from {filename}"
    
    return name, description


def convert_agent_to_skill(agent_path: Path, output_dir: Path) -> bool:
    """Convert a single agent to skill format."""
    try:
        content = agent_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  ⚠ Could not read {agent_path.name}: {e}")
        return False
    
    frontmatter, body = extract_frontmatter(content)
    name, description = extract_name_description(content, agent_path.name)
    
    # Use existing frontmatter if available
    if 'name' in frontmatter:
        name = frontmatter['name']
    if 'description' in frontmatter:
        description = frontmatter['description']
    
    # Create skill directory
    skill_name = agent_path.stem  # filename without extension
    skill_dir = output_dir / skill_name
    skill_dir.mkdir(parents=True, exist_ok=True)
    
    # Build SKILL.md
    skill_content = f"""---
name: {skill_name}
description: {description}
---

{body}
"""
    
    # Write SKILL.md
    skill_file = skill_dir / 'SKILL.md'
    skill_file.write_text(skill_content, encoding='utf-8')
    
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert-agents-to-skills.py <agents_dir> [output_dir]")
        print()
        print("Examples:")
        print("  python convert-agents-to-skills.py ./agents ./converted-skills")
        print("  python convert-agents-to-skills.py ~/.config/opencode/Overpowers/agents ~/skills")
        sys.exit(1)
    
    agents_dir = Path(sys.argv[1]).expanduser().resolve()
    output_dir = Path(sys.argv[2]).expanduser().resolve() if len(sys.argv) > 2 else agents_dir.parent / 'converted-skills'
    
    if not agents_dir.exists():
        print(f"❌ Agents directory not found: {agents_dir}")
        sys.exit(1)
    
    # Find all .md files
    agent_files = list(agents_dir.glob('*.md'))
    
    if not agent_files:
        print(f"❌ No .md files found in {agents_dir}")
        sys.exit(1)
    
    print(f"🔄 Converting {len(agent_files)} agents to skills...")
    print(f"📁 Source: {agents_dir}")
    print(f"📁 Output: {output_dir}")
    print()
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    success = 0
    failed = 0
    
    for agent_file in sorted(agent_files):
        if convert_agent_to_skill(agent_file, output_dir):
            print(f"  ✓ {agent_file.name}")
            success += 1
        else:
            failed += 1
    
    print()
    print(f"{'='*50}")
    print(f"✅ Converted: {success}")
    if failed > 0:
        print(f"⚠  Failed: {failed}")
    print(f"📁 Skills in: {output_dir}")


if __name__ == '__main__':
    main()
