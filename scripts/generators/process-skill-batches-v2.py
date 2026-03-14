#!/usr/bin/env python3
"""
Batch Skill Standardizer and Migrator (v2)
Processes extraction batches (051, 053, 055) from staging to skills/
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
STAGING_DIR = REPO_ROOT / ".archive/staging/skills"
SKILLS_DIR = REPO_ROOT / "skills"

# Batch 51 skills
BATCH_51 = [
    "runningcoach", "setup-wizard", "hd-sales-clue", "csgo-monitor",
    "aicoin-trading", "bizcard", "homepod-tts", "napcat-qq",
    "read-wechat-article", "job-skills-advisor", "learn-anything-pro",
    "memecoin-analyst", "pdf-helper", "book-writer", "bili-mindmap",
    "character-profile-cn", "tmap-lbs-service", "marriott",
    "openclaw-framework", "openclaw-skill-session-memory",
    "openclaw-skill-whisper-stt", "media-news-summary", "metaso-search",
    "webchat-pro", "claw-a2a-client"
]

# Batch 53 skills
BATCH_53 = [
    "suno-skill", "agent-daily-paper", "news-writing", "evolving-agent",
    "high-visual-arvr-immersive-marketing-rijoy", "rimet-xhs-spider",
    "openclaw-teaching", "amap-traffic", "otaku-reco", "otaku-wiki",
    "moments-grid", "stock-valuation-monitor", "qq-music-radio",
    "docx-formatter", "daily-tang-poem", "cat-selfie", "zh-knowledge-manager",
    "smartsheet-write", "daily-dxc-briefing", "mermaid-workflow-skill",
    "threads", "catch-my-skill", "claw-news", "elegant-sync", "vibe-3k"
]

# Batch 55 skills
BATCH_55 = [
    "failure-analyzer", "fiverr-seller", "gumroad-seller", "human-negotiator",
    "human-security", "instagram-poster", "learning-engine", "linkedin-poster",
    "medium-writer", "metamask-wallet", "moltbook-negotiator", "moltbook-optimizer",
    "moltbook-security", "natural-conversation", "note-writer", "podcast-creator",
    "product-image-generator", "prompt-seller", "quality-checker", "quality-gate",
    "reddit-poster", "resources", "revenue-ideator", "rey-clawhub-publisher",
    "rey-deep-research"
]

# Category mapping for tags
CATEGORY_MAP = {
    "hot": ["monitor", "china", "trending"],
    "news": ["news", "media", "content"],
    "trading": ["finance", "crypto", "trading"],
    "analysis": ["analysis", "research", "data"],
    "mbti": ["psychology", "assessment", "personality"],
    "feishu": ["productivity", "collaboration", "feishu"],
    "ai": ["ai", "automation", "generation"],
    "openclaw": ["openclaw", "setup", "onboarding"],
    "weather": ["weather", "utility", "query"],
    "research": ["research", "search", "analysis"],
    "novel": ["creative", "writing", "generation"],
    "crypto": ["crypto", "trading", "finance"],
    "code": ["development", "analysis", "utility"],
    "error": ["debugging", "development", "utility"],
    "performance": ["performance", "analysis", "development"],
    "regex": ["development", "utility", "pattern"],
    "focus": ["productivity", "mindfulness", "focus"],
    "design": ["design", "creative", "visual"],
    "audio": ["audio", "music", "generation"],
    "entrepreneur": ["business", "ai", "guide"],
    "prediction": ["prediction", "market", "analysis"],
    "memos": ["productivity", "notes", "storage"],
    "security": ["security", "audit", "monitoring"],
    "tcm": ["health", "traditional-medicine", "diagnosis"],
    "writing": ["writing", "productivity", "assistant"],
    "currency": ["utility", "finance", "conversion"],
    "reminder": ["productivity", "reminder", "automation"],
    "email": ["productivity", "communication", "drafting"],
    "expense": ["finance", "tracking", "productivity"],
    "file": ["productivity", "organization", "utility"],
    "habit": ["productivity", "tracking", "self-improvement"],
    "meeting": ["productivity", "documentation", "collaboration"],
    # New categories for batches 51, 53, 55
    "coach": ["fitness", "health", "training"],
    "sales": ["business", "sales", "automation"],
    "monitor": ["monitoring", "alerting", "utility"],
    "trading": ["finance", "crypto", "trading"],
    "card": ["utility", "productivity", "generator"],
    "tts": ["audio", "voice", "synthesis"],
    "qq": ["social", "messaging", "automation"],
    "wechat": ["social", "messaging", "china"],
    "job": ["career", "skills", "advisor"],
    "learn": ["education", "learning", "ai"],
    "memecoin": ["crypto", "analysis", "finance"],
    "pdf": ["document", "utility", "processing"],
    "book": ["creative", "writing", "generation"],
    "bili": ["video", "china", "productivity"],
    "character": ["creative", "writing", "profile"],
    "marriott": ["travel", "hotel", "utility"],
    "framework": ["documentation", "guide", "openclaw"],
    "memory": ["productivity", "memory", "storage"],
    "whisper": ["audio", "transcription", "stt"],
    "search": ["search", "utility", "research"],
    "webchat": ["communication", "messaging", "utility"],
    "claw": ["openclaw", "utility", "automation"],
    "suno": ["audio", "music", "generation"],
    "paper": ["research", "academic", "automation"],
    "evolving": ["ai", "evolution", "automation"],
    "arvr": ["ar", "vr", "immersive"],
    "spider": ["scraping", "automation", "utility"],
    "teaching": ["education", "teaching", "openclaw"],
    "traffic": ["utility", "china", "data"],
    "otaku": ["entertainment", "anime", "database"],
    "moments": ["social", "productivity", "automation"],
    "stock": ["finance", "analysis", "monitoring"],
    "music": ["audio", "music", "radio"],
    "docx": ["document", "formatting", "utility"],
    "poem": ["creative", "writing", "china"],
    "cat": ["entertainment", "image", "utility"],
    "knowledge": ["productivity", "knowledge", "management"],
    "smartsheet": ["productivity", "data", "automation"],
    "briefing": ["productivity", "reporting", "automation"],
    "mermaid": ["diagram", "visualization", "utility"],
    "threads": ["social", "automation", "utility"],
    "catch": ["utility", "automation", "discovery"],
    "elegant": ["utility", "sync", "automation"],
    "vibe": ["productivity", "analysis", "utility"],
    "failure": ["debugging", "analysis", "utility"],
    "fiverr": ["business", "freelance", "automation"],
    "gumroad": ["business", "ecommerce", "automation"],
    "human": ["utility", "automation", "interaction"],
    "instagram": ["social", "automation", "content"],
    "engine": ["ai", "learning", "automation"],
    "linkedin": ["social", "professional", "automation"],
    "medium": ["writing", "publishing", "automation"],
    "metamask": ["crypto", "wallet", "automation"],
    "moltbook": ["moltbook", "automation", "optimization"],
    "natural": ["conversation", "ai", "utility"],
    "note": ["productivity", "writing", "automation"],
    "podcast": ["audio", "content", "generation"],
    "product": ["ecommerce", "image", "generation"],
    "prompt": ["ai", "marketplace", "automation"],
    "quality": ["quality", "testing", "automation"],
    "reddit": ["social", "automation", "content"],
    "resources": ["utility", "management", "organization"],
    "revenue": ["business", "ideation", "automation"],
    "publisher": ["publishing", "automation", "clawhub"],
    "deep": ["research", "analysis", "automation"]
}


def extract_name_from_content(content: str) -> Optional[str]:
    """Extract skill name from YAML frontmatter or infer from filename."""
    # Try to find name in frontmatter
    name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
    if name_match:
        return name_match.group(1).strip().strip('"\'')
    return None


def extract_description_from_content(content: str) -> Optional[str]:
    """Extract description from YAML frontmatter."""
    # Try to find description in frontmatter
    desc_match = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)
    if desc_match:
        desc = desc_match.group(1).strip().strip('"\'')
        if desc:
            return desc
    return None


def infer_description_from_content(content: str, skill_name: str) -> str:
    """Infer a description from the skill content if missing."""
    # Look for first heading or description paragraph
    lines = content.split('\n')
    for line in lines[:50]:  # Check first 50 lines
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('---'):
            # Take first meaningful line
            if len(line) > 10 and len(line) < 200:
                return f"{skill_name.replace('-', ' ').title()} - {line[:100]}"

    # Fallback generic description
    return f"Skill for {skill_name.replace('-', ' ')} operations and automation"


def categorize_skill(skill_name: str) -> Tuple[str, List[str]]:
    """Determine category and tags based on skill name."""
    name_lower = skill_name.lower()
    tags = []
    category = "utility"

    for keyword, cat_tags in CATEGORY_MAP.items():
        if keyword in name_lower:
            category = cat_tags[0]
            tags = cat_tags
            break

    # Add language tag if Chinese-related
    if '-cn' in name_lower or 'chinese' in name_lower:
        tags.append('chinese')
        tags.append('china')

    return category, tags


def create_frontmatter(name: str, description: str, category: str, tags: List[str]) -> str:
    """Create YAML frontmatter block."""
    # Ensure description is not empty
    if not description or description.strip() == '':
        description = f"Skill for {name.replace('-', ' ')} operations and automation"

    # Limit description length
    if len(description) > 200:
        description = description[:197] + "..."

    frontmatter = f"""---
name: {name}
description: "{description}"
metadata:
  openclaw:
    category: "{category}"
    tags: {tags}
    version: "1.0.0"
---

"""
    return frontmatter


def normalize_to_kebab_case(name: str) -> str:
    """Normalize any name to kebab-case (lowercase, hyphens, alphanumeric)."""
    # Convert to lowercase
    name = name.lower()
    # Replace underscores and spaces with hyphens
    name = name.replace('_', '-').replace(' ', '-')
    # Remove non-alphanumeric characters (except hyphens)
    name = re.sub(r'[^a-z0-9-]', '', name)
    # Remove consecutive hyphens
    name = re.sub(r'-+', '-', name)
    # Strip leading/trailing hyphens
    name = name.strip('-')
    return name


def process_skill_file(skill_name: str, dry_run: bool = False) -> Dict:
    """Process a single skill file from staging to skills directory."""
    result = {
        'name': skill_name,
        'status': 'pending',
        'source': None,
        'destination': None,
        'error': None,
        'frontmatter_added': False,
        'description_fixed': False
    }

    # Find source file (with or without _SKILL suffix)
    source_files = [
        STAGING_DIR / f"{skill_name}_SKILL.md",
        STAGING_DIR / f"{skill_name}.md",
    ]

    source_file = None
    for sf in source_files:
        if sf.exists():
            source_file = sf
            break

    if not source_file:
        result['status'] = 'skipped'
        result['error'] = 'Source file not found'
        return result

    result['source'] = str(source_file)

    # Read content
    try:
        content = source_file.read_text(encoding='utf-8')
    except Exception as e:
        result['status'] = 'error'
        result['error'] = f'Failed to read: {str(e)}'
        return result

    # Extract existing metadata
    existing_name = extract_name_from_content(content)
    existing_desc = extract_description_from_content(content)

    # Remove existing frontmatter if present
    content_no_frontmatter = re.sub(r'^---\n.*?\n---\n\n?', '', content, flags=re.DOTALL)

    # ALWAYS use the filename-based skill_name (normalized to kebab-case)
    # Never trust frontmatter name field as it may contain Chinese or spaces
    final_name = normalize_to_kebab_case(skill_name)

    # Get category and tags
    category, tags = categorize_skill(final_name)

    # Generate or fix description
    final_desc = existing_desc if existing_desc else infer_description_from_content(content_no_frontmatter, final_name)

    # Check if description was empty and we fixed it
    if not existing_desc or existing_desc.strip() == '':
        result['description_fixed'] = True

    # Create new frontmatter
    new_frontmatter = create_frontmatter(final_name, final_desc, category, tags)
    result['frontmatter_added'] = True

    # Combine frontmatter + content
    new_content = new_frontmatter + content_no_frontmatter

    # Create destination directory
    dest_dir = SKILLS_DIR / final_name
    dest_file = dest_dir / "SKILL.md"

    result['destination'] = str(dest_file)

    if not dry_run:
        try:
            # Create destination directory
            dest_dir.mkdir(parents=True, exist_ok=True)

            # Write new file
            dest_file.write_text(new_content, encoding='utf-8')

            # Delete source file
            source_file.unlink()

            result['status'] = 'completed'
        except Exception as e:
            result['status'] = 'error'
            result['error'] = f'Failed to process: {str(e)}'
            # Cleanup on error
            if dest_file.exists():
                dest_file.unlink()
            if dest_dir.exists() and not any(dest_dir.iterdir()):
                dest_dir.rmdir()
    else:
        result['status'] = 'would_process'

    return result


def process_batch(batch_name: str, skills: List[str], dry_run: bool = False) -> List[Dict]:
    """Process an entire batch of skills."""
    print(f"\n{'='*60}")
    print(f"Processing Batch: {batch_name}")
    print(f"Total items: {len(skills)}")
    print(f"{'='*60}\n")

    results = []
    completed = 0
    skipped = 0
    errors = 0

    for skill_name in skills:
        result = process_skill_file(skill_name, dry_run=dry_run)
        results.append(result)

        if result['status'] == 'completed':
            completed += 1
            status_icon = "✅"
        elif result['status'] == 'skipped':
            skipped += 1
            status_icon = "⏭️"
        elif result['status'] == 'error':
            errors += 1
            status_icon = "❌"
        else:
            status_icon = "📋"

        print(f"{status_icon} {skill_name:40s} -> {result.get('destination', 'N/A')}")
        if result.get('description_fixed'):
            print(f"   ⚠️  Description was empty, auto-generated")
        if result.get('error'):
            print(f"   ❌ Error: {result['error']}")

    print(f"\n{'='*60}")
    print(f"Batch {batch_name} Summary:")
    print(f"  Completed: {completed}")
    print(f"  Skipped:   {skipped}")
    print(f"  Errors:    {errors}")
    print(f"{'='*60}\n")

    return results


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Process skill extraction batches (v2)')
    parser.add_argument('--batch', choices=['51', '53', '55', 'all'], default='all',
                       help='Which batch to process')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without making changes')

    args = parser.parse_args()

    batches_to_process = []

    if args.batch == '51' or args.batch == 'all':
        batches_to_process.append(('051', BATCH_51))
    if args.batch == '53' or args.batch == 'all':
        batches_to_process.append(('053', BATCH_53))
    if args.batch == '55' or args.batch == 'all':
        batches_to_process.append(('055', BATCH_55))

    all_results = []

    for batch_num, skills in batches_to_process:
        results = process_batch(f"{batch_num}", skills, dry_run=args.dry_run)
        all_results.extend(results)

    # Final summary
    total = len(all_results)
    completed = sum(1 for r in all_results if r['status'] == 'completed')
    skipped = sum(1 for r in all_results if r['status'] == 'skipped')
    errors = sum(1 for r in all_results if r['status'] == 'error')
    would_process = sum(1 for r in all_results if r['status'] == 'would_process')

    print(f"\n{'='*60}")
    print(f"OVERALL SUMMARY")
    print(f"{'='*60}")
    if args.dry_run:
        print(f"Would process: {would_process}")
    else:
        print(f"Completed: {completed}/{total}")
    print(f"Skipped:   {skipped}/{total}")
    print(f"Errors:    {errors}/{total}")
    print(f"{'='*60}\n")

    return 0 if errors == 0 else 1


if __name__ == '__main__':
    exit(main())
