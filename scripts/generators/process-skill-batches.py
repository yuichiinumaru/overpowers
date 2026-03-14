#!/usr/bin/env python3
"""
Batch Skill Processor (Processing Only)
Processes extraction batches from staging to skills/ WITHOUT deleting source files.
Use clean-staging.py separately after verification.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
STAGING_DIR = REPO_ROOT / ".archive/staging/skills"
SKILLS_DIR = REPO_ROOT / "skills"
PROCESSING_LOG = REPO_ROOT / ".docs" / "batch-processing-log.json"

# Batch definitions (add new batches here as needed)
BATCHES = {
    '025': [
        "hot-alert-cn", "ithome-hot-cn", "jike-hot-cn", "market-analysis-cn",
        "mbti-agent", "product-hunt-cn", "quant-trading-cn", "skill-finder-cn",
        "sspai-hot-cn", "toutiao-hot-news-cn", "v2ex-hot-cn", "wechat-mp-cn",
        "xueqiu-hot-cn", "chat-with-l", "feishu-doc-writing", "feishu-readability",
        "publish-checklist", "ram-review", "ai-meeting-room", "openclaw-starter-kit",
        "ai-news-research", "weather-query-ll", "google-deep-research", "sharkflow",
        "ai-novel-chongshengfuchou"
    ],
    '027': ["character-creator"],
    '029': [
        "crypto-strategy-suite", "code-flow-visualizer", "error-message-decoder",
        "performance-profiler", "regex-generator", "focus-mind", "snapdesign-rednote",
        "minimax-opus-tune", "ai-entrepreneur-guide", "oceanbase-datapilot",
        "prediction-market-reporter", "huamu668-memos-cloud", "huamu668-openclaw-security",
        "tcn-diagnosis", "writing-assistant-pro", "btceth-dulwin-engine",
        "code-snippet-oc", "currency-converter-zh", "daily-reminder", "email-draft-oc",
        "expense-tracker-oc", "file-organizer-zh", "habit-tracker-oc", "link-saver",
        "meeting-notes-oc"
    ],
    '031': [
        "ai-writing-assistant-cn-payment", "ai-writing-assistant-cn-v1-1", "ai-writing-assistant-cn",
        "ozon-product-sourcing", "voice-note-transcriber-cn-payment", "pdf-smart-tool-cn-v1-1",
        "pdf-smart-tool-cn", "smart-customer-service-cn-payment", "smart-customer-service-cn",
        "smart-expense-tracker-cn-payment", "smart-expense-tracker-cn-v1-1", "smart-expense-tracker-cn",
        "smart-marketing-copy-cn-payment", "smart-resume-optimizer-cn", "voice-note-transcriber-cn-v1-1",
        "voice-note-transcriber-cn", "bangai-recruit", "weibo-fresh-posts", "communication-mqtt",
        "tencentcloud-faceid-detectaifakefaces", "okx-trading-exe", "kugou-mysterious-shop",
        "brainhole-factory", "safe-edit", "quick-note"
    ],
    '033': [
        "nanobanana-ppt-skills", "meihua-yishu", "truth-check", "validate-agent", "zixun",
        "document-pro", "email-reader", "video-learn", "openclaw-config-guide", "xiaoye-voice",
        "bilibili-hot-monitor", "zxz-test", "a-stock-monitor", "menews", "china-tax-calculator",
        "x-engagement", "jax-skill-security-scanner", "lobster-radio-skill", "folder-inspector",
        "smart-memory-system", "amcjt-lottery", "neo4j-cypher-query-analyze", "chinese-daily-assistant",
        "orchestrator", "architecture-governance"
    ],
    '035': [
        "agent-onchain-watch", "agent-trend-radar", "cell", "epc", "exchange", "huangli",
        "jisu-astro", "jisu-baidu", "jisu-baiduai", "jisu-bazi", "jisu-calendar", "jisu-car",
        "jisu-movie", "jisu-news", "jisu-stock", "mobileempty", "parts", "stockhistory", "vin",
        "resume-project-summarizer", "aliyun-asr", "aliyun-oss", "tencentcloud-tts",
        "openclaw-work-protocol", "coding-as-dressing"
    ],
    # Add more batches here as needed
}

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
    "voice": ["voice", "audio", "transcription"],
    "pdf": ["pdf", "document", "processing"],
    "customer": ["customer", "service", "support"],
    "recruit": ["recruitment", "hr", "hiring"],
    "lottery": ["lottery", "gaming", "prediction"],
    "architecture": ["architecture", "governance", "design"],
    "jisu": ["jisu", "api", "data"],
    "aliyun": ["aliyun", "cloud", "alibaba"],
    "tencent": ["tencent", "cloud", "services"],
    "agent": ["agent", "automation", "monitoring"],
}


def normalize_to_kebab_case(name: str) -> str:
    """Normalize any name to kebab-case (lowercase, hyphens, alphanumeric)."""
    name = name.lower()
    name = name.replace('_', '-').replace(' ', '-')
    name = re.sub(r'[^a-z0-9-]', '', name)
    name = re.sub(r'-+', '-', name)
    name = name.strip('-')
    return name


def extract_name_from_content(content: str) -> Optional[str]:
    """Extract skill name from YAML frontmatter."""
    name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
    if name_match:
        return name_match.group(1).strip().strip('"\'')
    return None


def extract_description_from_content(content: str) -> Optional[str]:
    """Extract description from YAML frontmatter."""
    desc_match = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)
    if desc_match:
        desc = desc_match.group(1).strip().strip('"\'')
        if desc:
            return desc
    return None


def infer_description_from_content(content: str, skill_name: str) -> str:
    """Infer a description from the skill content if missing."""
    lines = content.split('\n')
    for line in lines[:50]:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('---'):
            if len(line) > 10 and len(line) < 200:
                return f"{skill_name.replace('-', ' ').title()} - {line[:100]}"
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
    
    if '-cn' in name_lower or 'chinese' in name_lower:
        tags.append('chinese')
        tags.append('china')
    
    return category, tags


def create_frontmatter(name: str, description: str, category: str, tags: List[str]) -> str:
    """Create YAML frontmatter block."""
    if not description or description.strip() == '':
        description = f"Skill for {name.replace('-', ' ')} operations and automation"
    
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


def process_skill_file(skill_name: str, batch_id: str) -> Dict:
    """Process a single skill file from staging to skills directory (without deleting source)."""
    result = {
        'name': skill_name,
        'batch': batch_id,
        'status': 'pending',
        'source': None,
        'destination': None,
        'error': None,
        'frontmatter_added': False,
        'description_fixed': False,
        'timestamp': datetime.now().isoformat()
    }
    
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
    
    try:
        content = source_file.read_text(encoding='utf-8')
    except Exception as e:
        result['status'] = 'error'
        result['error'] = f'Failed to read: {str(e)}'
        return result
    
    existing_name = extract_name_from_content(content)
    existing_desc = extract_description_from_content(content)
    
    content_no_frontmatter = re.sub(r'^---\n.*?\n---\n\n?', '', content, flags=re.DOTALL)
    final_name = normalize_to_kebab_case(skill_name)
    
    category, tags = categorize_skill(final_name)
    final_desc = existing_desc if existing_desc else infer_description_from_content(content_no_frontmatter, final_name)
    
    if not existing_desc or existing_desc.strip() == '':
        result['description_fixed'] = True
    
    new_frontmatter = create_frontmatter(final_name, final_desc, category, tags)
    result['frontmatter_added'] = True
    
    new_content = new_frontmatter + content_no_frontmatter
    
    dest_dir = SKILLS_DIR / final_name
    dest_file = dest_dir / "SKILL.md"
    
    result['destination'] = str(dest_file)
    
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        # Check if file already exists
        if dest_file.exists():
            result['status'] = 'already_exists'
            result['error'] = 'Destination file already exists'
            return result
        
        dest_file.write_text(new_content, encoding='utf-8')
        result['status'] = 'processed'
    except Exception as e:
        result['status'] = 'error'
        result['error'] = f'Failed to process: {str(e)}'
        if dest_file.exists():
            dest_file.unlink()
        if dest_dir.exists() and not any(dest_dir.iterdir()):
            dest_dir.rmdir()
    
    return result


def process_batch(batch_id: str, skills: List[str]) -> List[Dict]:
    """Process an entire batch of skills."""
    print(f"\n{'='*60}")
    print(f"Processing Batch: {batch_id}")
    print(f"Total items: {len(skills)}")
    print(f"{'='*60}\n")
    
    results = []
    processed = 0
    skipped = 0
    errors = 0
    already_exists = 0
    
    for skill_name in skills:
        result = process_skill_file(skill_name, batch_id)
        results.append(result)
        
        if result['status'] == 'processed':
            processed += 1
            status_icon = "✅"
        elif result['status'] == 'skipped':
            skipped += 1
            status_icon = "⏭️"
        elif result['status'] == 'already_exists':
            already_exists += 1
            status_icon = "⚠️"
        elif result['status'] == 'error':
            errors += 1
            status_icon = "❌"
        else:
            status_icon = "📋"
        
        print(f"{status_icon} {skill_name:45s} -> {result.get('destination', 'N/A')}")
        if result.get('description_fixed'):
            print(f"   ⚠️  Description was empty, auto-generated")
        if result.get('error'):
            print(f"   ❌ Error: {result['error']}")
    
    print(f"\n{'='*60}")
    print(f"Batch {batch_id} Summary:")
    print(f"  Processed:     {processed}")
    print(f"  Already exists: {already_exists}")
    print(f"  Skipped:       {skipped}")
    print(f"  Errors:        {errors}")
    print(f"{'='*60}\n")
    
    return results


def save_processing_log(all_results: List[Dict], batches_processed: List[str]):
    """Save processing log for verification and cleanup."""
    log_data = {
        'timestamp': datetime.now().isoformat(),
        'batches_processed': batches_processed,
        'total_processed': len(all_results),
        'results': all_results,
        'summary': {
            'processed': sum(1 for r in all_results if r['status'] == 'processed'),
            'skipped': sum(1 for r in all_results if r['status'] == 'skipped'),
            'errors': sum(1 for r in all_results if r['status'] == 'error'),
            'already_exists': sum(1 for r in all_results if r['status'] == 'already_exists')
        }
    }
    
    # Load existing log if present
    existing_log = {}
    if PROCESSING_LOG.exists():
        try:
            with open(PROCESSING_LOG, 'r', encoding='utf-8') as f:
                existing_log = json.load(f)
        except:
            existing_log = {}
    
    # Merge logs
    if 'batches' not in existing_log:
        existing_log['batches'] = {}
    
    for batch_id in batches_processed:
        batch_results = [r for r in all_results if r.get('batch') == batch_id]
        existing_log['batches'][batch_id] = {
            'timestamp': datetime.now().isoformat(),
            'count': len(batch_results),
            'results': batch_results
        }
    
    existing_log['last_update'] = datetime.now().isoformat()
    
    with open(PROCESSING_LOG, 'w', encoding='utf-8') as f:
        json.dump(existing_log, f, indent=2, ensure_ascii=False)
    
    print(f"\n📝 Processing log saved to: {PROCESSING_LOG}")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Process skill extraction batches (without cleanup)')
    parser.add_argument('--batch', choices=list(BATCHES.keys()) + ['all'], default='all',
                       help='Which batch to process')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    batches_to_process = []
    
    if args.batch == 'all':
        batches_to_process = list(BATCHES.items())
    else:
        batches_to_process = [(args.batch, BATCHES[args.batch])]
    
    all_results = []
    batches_processed = []
    
    for batch_id, skills in batches_to_process:
        results = process_batch(batch_id, skills)
        all_results.extend(results)
        batches_processed.append(batch_id)
    
    # Save processing log
    if not args.dry_run:
        save_processing_log(all_results, batches_processed)
    
    # Final summary
    total = len(all_results)
    processed = sum(1 for r in all_results if r['status'] == 'processed')
    skipped = sum(1 for r in all_results if r['status'] == 'skipped')
    errors = sum(1 for r in all_results if r['status'] == 'error')
    already_exists = sum(1 for r in all_results if r['status'] == 'already_exists')
    
    print(f"\n{'='*60}")
    print(f"OVERALL SUMMARY")
    print(f"{'='*60}")
    if args.dry_run:
        print(f"Would process: {processed}")
    else:
        print(f"Processed:      {processed}/{total}")
    print(f"Already exists: {already_exists}/{total}")
    print(f"Skipped:        {skipped}/{total}")
    print(f"Errors:         {errors}/{total}")
    print(f"{'='*60}\n")
    
    if not args.dry_run:
        print(f"✅ Processing complete! Source files NOT deleted.")
        print(f"📝 Review the processing log at: {PROCESSING_LOG}")
        print(f"🧹 Run 'python3 scripts/generators/clean-staging.py' after verification to clean up staging files.")
    
    return 0 if errors == 0 else 1


if __name__ == '__main__':
    exit(main())
