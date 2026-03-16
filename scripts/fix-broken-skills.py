#!/usr/bin/env python3
"""
Fix broken YAML frontmatter in SKILL.md files.

Error categories found in scan of 117 broken files:
1. yaml_parse_error (103): Mostly nested unescaped quotes in description
2. empty_file (5): Completely empty files
3. missing_open_delim (5): No opening --- delimiter
4. string_frontmatter (2): Entire frontmatter is a plain string
5. yaml_comment_as_field (2): # used instead of YAML keys
6. broken_quoting (1): Unclosed quotes
7. empty_description (1): description field is empty/null

Strategy: Don't try to parse YAML. Instead, use line-level extraction
to identify name/description/metadata fields and reconstruct clean YAML.

Usage:
    python scripts/fix-broken-skills.py --scan          # Dry run: list issues
    python scripts/fix-broken-skills.py --execute       # Fix all issues
    python scripts/fix-broken-skills.py --execute --limit 5  # Fix first 5
"""

import argparse
import re
import sys
import yaml
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parent.parent / "skills"


def is_valid_frontmatter(content: str) -> bool:
    """Check if a SKILL.md file has valid YAML frontmatter."""
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return False
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            fm_text = '\n'.join(lines[1:i])
            try:
                parsed = yaml.safe_load(fm_text)
                if not isinstance(parsed, dict):
                    return False
                if 'description' not in parsed or not parsed.get('description'):
                    return False
                return True
            except yaml.YAMLError:
                return False
    return False


def extract_body(content: str) -> str:
    """Extract body after frontmatter from content."""
    lines = content.split('\n')
    if lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                return '\n'.join(lines[i + 1:]).strip()
        return ''
    for i, line in enumerate(lines):
        if line.strip() == '---' and i > 0:
            return '\n'.join(lines[i + 1:]).strip()
    yaml_like_end = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            yaml_like_end = i
            break
        if re.match(r'^[\w-]+\s*:', stripped) or re.match(r'^\s+\w', stripped):
            yaml_like_end = i + 1
        else:
            break
    if yaml_like_end > 0:
        return '\n'.join(lines[yaml_like_end:]).strip()
    return content.strip()


def extract_raw_frontmatter_lines(content: str) -> list[str]:
    """Get raw frontmatter lines (without --- delimiters)."""
    lines = content.split('\n')
    if lines[0].strip() == '---':
        fm_lines = []
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                return fm_lines
            fm_lines.append(lines[i])
        return fm_lines
    fm_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped == '---':
            break
        if re.match(r'^[\w-]+\s*:', stripped) or re.match(r'^\s+\w', stripped) or not stripped:
            fm_lines.append(line)
        else:
            break
    return fm_lines


def extract_name_from_lines(fm_lines: list[str]) -> str | None:
    for line in fm_lines:
        m = re.match(r"^(?:#\s*)?name:\s*['\"]?(.+?)['\"]?\s*$", line.strip())
        if m:
            return m.group(1).strip().strip("'\"")
    return None


def extract_description_from_lines(fm_lines: list[str]) -> str | None:
    text = '\n'.join(fm_lines)
    m = re.search(r'^description:\s*(.+?)(?:\n(?=[a-zA-Z_][\w-]*:)|\Z)', text,
                  re.MULTILINE | re.DOTALL)
    if m:
        desc = m.group(1).strip()
        if (desc.startswith('"') and desc.endswith('"')) or \
           (desc.startswith("'") and desc.endswith("'")):
            desc = desc[1:-1]
        elif desc.startswith('"') or desc.startswith("'"):
            desc = desc[1:]
        return desc.strip()
    m = re.search(r'^##\s*Description\s*\n(.+?)(?:\n##|\Z)', text,
                  re.MULTILINE | re.DOTALL)
    if m:
        return m.group(1).strip().strip('"\'')
    return None


def derive_description_from_body(body: str) -> str:
    if not body or not body.strip():
        return "No description available."
    lines = body.strip().split('\n')
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('# ') and len(stripped) > 4:
            desc = stripped.lstrip('#').strip()
            if len(desc) > 10:
                return desc[:200]
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not stripped.startswith('---') and len(stripped) > 10:
            return stripped[:200]
    return "No description available."


def derive_name_from_path(filepath: Path) -> str:
    return filepath.parent.name


def sanitize_description(desc: str) -> str:
    desc = desc.replace('\\"', "'")
    desc = desc.replace('"', "'")
    desc = re.sub(r'\\([^nrtbf\\/])', r'\1', desc)
    desc = desc.replace('`', "'")
    desc = desc.strip()
    desc = re.sub(r'\s+', ' ', desc)
    return desc


def fix_skill_file(filepath: Path) -> tuple[bool, str]:
    content = filepath.read_text(encoding='utf-8', errors='replace')
    if is_valid_frontmatter(content):
        return False, "already valid"
    if not content.strip():
        name = derive_name_from_path(filepath)
        new_content = f'---\nname: {name}\ndescription: "No description available."\n---\n'
        filepath.write_text(new_content, encoding='utf-8')
        return True, "was empty, added minimal frontmatter"

    body = extract_body(content)
    fm_lines = extract_raw_frontmatter_lines(content)
    name = extract_name_from_lines(fm_lines)
    if not name:
        name = derive_name_from_path(filepath)
    desc = extract_description_from_lines(fm_lines)
    if not desc:
        fm_text = '\n'.join(fm_lines).strip()
        if fm_text and not re.match(r'^[\w-]+\s*:', fm_text):
            desc = fm_text
        else:
            desc = derive_description_from_body(body)
    desc = sanitize_description(desc)

    metadata_lines = []
    in_metadata = False
    for line in fm_lines:
        if line.strip().startswith('metadata:'):
            in_metadata = True
            metadata_lines.append(line)
        elif in_metadata and (line.startswith('  ') or line.startswith('\t')):
            metadata_lines.append(line)
        elif in_metadata:
            in_metadata = False

    new_fm = f'---\nname: {name}\ndescription: "{desc}"\n'
    if metadata_lines:
        new_fm += '\n'.join(metadata_lines) + '\n'
    new_fm += '---\n'
    if body:
        new_content = new_fm + '\n' + body + '\n'
    else:
        new_content = new_fm
    if is_valid_frontmatter(new_content):
        filepath.write_text(new_content, encoding='utf-8')
        return True, "fixed frontmatter"
    else:
        fallback_desc = derive_description_from_body(body) if body else "No description available."
        fallback_desc = sanitize_description(fallback_desc)
        new_content = f'---\nname: {name}\ndescription: "{fallback_desc}"\n---\n'
        if body:
            new_content += '\n' + body + '\n'
        filepath.write_text(new_content, encoding='utf-8')
        return True, "rebuilt from scratch (fallback)"


def scan_all_skills() -> list[Path]:
    broken = []
    for skill_path in sorted(SKILLS_ROOT.rglob("SKILL.md")):
        if skill_path.name != "SKILL.md":
            continue
        try:
            content = skill_path.read_text(encoding='utf-8', errors='replace')
            if not is_valid_frontmatter(content):
                broken.append(skill_path)
        except Exception as e:
            print(f"  ⚠️  Error reading {skill_path}: {e}")
    return broken


def main():
    parser = argparse.ArgumentParser(description="Fix broken YAML frontmatter in SKILL.md files")
    parser.add_argument("--scan", action="store_true", help="Dry run: list all broken files")
    parser.add_argument("--execute", action="store_true", help="Apply fixes")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of files to process")
    args = parser.parse_args()
    if not args.scan and not args.execute:
        parser.print_help()
        return

    print("🔍 Scanning SKILL.md files for frontmatter issues...")
    broken = scan_all_skills()
    if args.limit > 0:
        broken = broken[:args.limit]
    print(f"\n📊 Found {len(broken)} files with broken frontmatter\n")

    if args.scan:
        for p in broken:
            rel = p.relative_to(SKILLS_ROOT)
            print(f"  ❌ {rel}")
        return

    if args.execute:
        fixed = 0
        failed = 0
        for p in broken:
            rel = p.relative_to(SKILLS_ROOT)
            try:
                was_fixed, msg = fix_skill_file(p)
                if was_fixed:
                    fixed += 1
                    print(f"  ✅ {rel}: {msg}")
                else:
                    print(f"  ⏭️  {rel}: {msg}")
            except Exception as e:
                failed += 1
                print(f"  ❌ {rel}: ERROR - {e}")

        print(f"\n🏁 Done: {fixed} fixed, {failed} failed")
        print("\n🔍 Re-scanning to verify...")
        still_broken = scan_all_skills()
        print(f"📊 Files still broken: {len(still_broken)}")
        if still_broken:
            for p in still_broken:
                print(f"  ❌ {p.relative_to(SKILLS_ROOT)}")


if __name__ == "__main__":
    main()
