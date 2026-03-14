#!/usr/bin/env python3
"""
Dynamic Batch Processor
Automatically discovers all skills in staging and processes them in batches of 25.
No hardcoded batch numbers - processes EVERYTHING in staging.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import math

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
STAGING_DIR = REPO_ROOT / ".archive/staging/skills"
SKILLS_DIR = REPO_ROOT / "skills"
PROCESSING_LOG = REPO_ROOT / ".docs" / "batch-processing-log.json"
BATCH_SIZE = 25  # Process in groups of 25


def discover_staging_skills() -> List[str]:
    """Discover all skill files in staging directory."""
    if not STAGING_DIR.exists():
        print(f"❌ Staging directory not found: {STAGING_DIR}")
        return []
    
    skill_files = list(STAGING_DIR.glob("*_SKILL.md")) + list(STAGING_DIR.glob("*.md"))
    
    # Extract skill names (remove _SKILL.md suffix)
    skill_names = set()
    for sf in skill_files:
        name = sf.stem
        if name.endswith('_SKILL'):
            name = name[:-6]
        skill_names.add(name)
    
    return sorted(list(skill_names))


def create_dynamic_batches(skill_names: List[str], batch_size: int = BATCH_SIZE) -> Dict[str, List[str]]:
    """Create dynamic batches from skill list."""
    batches = {}
    total = len(skill_names)
    num_batches = math.ceil(total / batch_size)
    
    for i in range(num_batches):
        batch_num = i + 1
        batch_id = f"dynamic-{batch_num:03d}"
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, total)
        batches[batch_id] = skill_names[start_idx:end_idx]
    
    return batches


# Category mapping for tags (comprehensive)
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
    "stock": ["finance", "stock", "trading"],
    "navigation": ["navigation", "maps", "location"],
    "amazon": ["ecommerce", "amazon", "shopping"],
    "android": ["android", "mobile", "development"],
    "api": ["api", "development", "integration"],
    "learning": ["education", "learning", "productivity"],
    "phone": ["communication", "phone", "automation"],
    "ppt": ["presentation", "productivity", "office"],
    "airdrop": ["crypto", "airdrop", "farming"],
    "seo": ["seo", "marketing", "optimization"],
    "algorithm": ["development", "algorithm", "utility"],
    "analytics": ["analytics", "data", "tracking"],
    "auto": ["automation", "productivity", "utility"],
    "backup": ["backup", "storage", "utility"],
    "batch": ["automation", "batch", "processing"],
    "billing": ["finance", "billing", "automation"],
    "bio": ["biology", "science", "research"],
    "bitcoin": ["crypto", "bitcoin", "trading"],
    "blog": ["content", "blog", "writing"],
    "blender": ["3d", "blender", "graphics"],
    "blockchain": ["blockchain", "crypto", "development"],
    "book": ["books", "reading", "education"],
    "browser": ["browser", "automation", "utility"],
    "budget": ["finance", "budget", "tracking"],
    "business": ["business", "entrepreneur", "strategy"],
    "calendar": ["productivity", "calendar", "scheduling"],
    "career": ["career", "job", "development"],
    "chat": ["communication", "chat", "messaging"],
    "chinese": ["chinese", "china", "language"],
    "chrome": ["browser", "chrome", "extension"],
    "claude": ["ai", "claude", "automation"],
    "cloud": ["cloud", "storage", "computing"],
    "cluster": ["automation", "cluster", "management"],
    "code": ["development", "coding", "programming"],
    "coin": ["crypto", "coin", "trading"],
    "command": ["cli", "command", "automation"],
    "communication": ["communication", "messaging", "collaboration"],
    "company": ["business", "company", "research"],
    "compiler": ["development", "compiler", "programming"],
    "compliance": ["compliance", "legal", "audit"],
    "config": ["configuration", "setup", "utility"],
    "content": ["content", "creation", "writing"],
    "contract": ["legal", "contract", "review"],
    "convert": ["conversion", "utility", "tool"],
    "cookie": ["web", "cookie", "privacy"],
    "copilot": ["ai", "copilot", "assistant"],
    "course": ["education", "course", "learning"],
    "crm": ["crm", "sales", "customer"],
    "css": ["development", "css", "frontend"],
    "customer": ["customer", "service", "support"],
    "daily": ["productivity", "daily", "routine"],
    "data": ["data", "analysis", "processing"],
    "database": ["database", "data", "storage"],
    "debug": ["debugging", "development", "utility"],
    "deep": ["ai", "deep-learning", "research"],
    "deploy": ["deployment", "devops", "automation"],
    "design": ["design", "creative", "graphics"],
    "desktop": ["desktop", "automation", "utility"],
    "dev": ["development", "devops", "tools"],
    "device": ["device", "hardware", "iot"],
    "discord": ["communication", "discord", "bot"],
    "document": ["document", "processing", "productivity"],
    "domain": ["domain", "web", "registration"],
    "douban": ["social", "douban", "china"],
    "draft": ["writing", "draft", "content"],
    "draw": ["graphics", "drawing", "creative"],
    "dribbble": ["design", "dribbble", "inspiration"],
    "dropbox": ["cloud", "storage", "file"],
    "ecommerce": ["ecommerce", "shopping", "business"],
    "editor": ["development", "editor", "tool"],
    "education": ["education", "learning", "teaching"],
    "elastic": ["database", "elastic", "search"],
    "email": ["email", "communication", "productivity"],
    "emoji": ["emoji", "communication", "fun"],
    "employee": ["hr", "employee", "management"],
    "energy": ["energy", "utility", "monitoring"],
    "english": ["language", "english", "learning"],
    "entity": ["development", "entity", "framework"],
    "env": ["environment", "config", "utility"],
    "epub": ["ebook", "epub", "reading"],
    "eslint": ["development", "linting", "quality"],
    "ethereum": ["crypto", "ethereum", "blockchain"],
    "etsy": ["ecommerce", "etsy", "shopping"],
    "excel": ["office", "excel", "spreadsheet"],
    "expense": ["finance", "expense", "tracking"],
    "facebook": ["social", "facebook", "marketing"],
    "feed": ["rss", "feed", "news"],
    "figma": ["design", "figma", "prototyping"],
    "file": ["file", "utility", "management"],
    "finance": ["finance", "money", "investment"],
    "firefox": ["browser", "firefox", "extension"],
    "fitness": ["health", "fitness", "exercise"],
    "flask": ["development", "flask", "python"],
    "flight": ["travel", "flight", "booking"],
    "flow": ["automation", "workflow", "productivity"],
    "flutter": ["development", "flutter", "mobile"],
    "food": ["food", "recipe", "cooking"],
    "form": ["form", "survey", "data"],
    "forum": ["forum", "community", "discussion"],
    "freelance": ["freelance", "work", "business"],
    "frontend": ["development", "frontend", "web"],
    "game": ["game", "gaming", "entertainment"],
    "garden": ["gardening", "hobby", "plants"],
    "gemini": ["ai", "gemini", "google"],
    "git": ["development", "git", "version-control"],
    "github": ["development", "github", "collaboration"],
    "gitlab": ["development", "gitlab", "devops"],
    "gmail": ["email", "gmail", "google"],
    "godot": ["game", "godot", "development"],
    "golang": ["development", "golang", "programming"],
    "google": ["google", "search", "utility"],
    "graphql": ["development", "graphql", "api"],
    "growth": ["business", "growth", "marketing"],
    "habit": ["productivity", "habit", "tracking"],
    "hack": ["security", "hacking", "testing"],
    "hardware": ["hardware", "electronics", "iot"],
    "health": ["health", "medical", "wellness"],
    "home": ["home", "automation", "smart"],
    "hospital": ["health", "hospital", "medical"],
    "hotel": ["travel", "hotel", "booking"],
    "html": ["development", "html", "web"],
    "http": ["development", "http", "networking"],
    "image": ["image", "graphics", "processing"],
    "instagram": ["social", "instagram", "marketing"],
    "insurance": ["finance", "insurance", "protection"],
    "integration": ["integration", "api", "automation"],
    "interview": ["career", "interview", "preparation"],
    "investment": ["finance", "investment", "trading"],
    "invoice": ["finance", "invoice", "billing"],
    "ios": ["development", "ios", "mobile"],
    "java": ["development", "java", "programming"],
    "javascript": ["development", "javascript", "programming"],
    "job": ["career", "job", "search"],
    "jupyter": ["development", "jupyter", "data-science"],
    "kafka": ["development", "kafka", "streaming"],
    "kotlin": ["development", "kotlin", "programming"],
    "kubernetes": ["devops", "kubernetes", "container"],
    "language": ["language", "learning", "translation"],
    "law": ["law", "legal", "attorney"],
    "lead": ["sales", "lead", "generation"],
    "legal": ["legal", "law", "compliance"],
    "linkedin": ["social", "linkedin", "professional"],
    "linux": ["development", "linux", "system"],
    "local": ["local", "location", "service"],
    "log": ["logging", "monitoring", "debugging"],
    "machine-learning": ["ai", "machine-learning", "data-science"],
    "macos": ["development", "macos", "system"],
    "mail": ["email", "mail", "communication"],
    "marketing": ["marketing", "business", "growth"],
    "mastodon": ["social", "mastodon", "fediverse"],
    "math": ["math", "science", "education"],
    "matrix": ["communication", "matrix", "chat"],
    "maven": ["development", "maven", "java"],
    "media": ["media", "content", "publishing"],
    "medical": ["health", "medical", "healthcare"],
    "meeting": ["productivity", "meeting", "collaboration"],
    "memory": ["productivity", "memory", "knowledge"],
    "message": ["communication", "message", "messaging"],
    "messenger": ["communication", "messenger", "chat"],
    "microservice": ["development", "microservice", "architecture"],
    "minecraft": ["game", "minecraft", "gaming"],
    "mobile": ["development", "mobile", "app"],
    "mongodb": ["development", "mongodb", "database"],
    "monitor": ["monitoring", "observability", "alerting"],
    "movie": ["entertainment", "movie", "film"],
    "music": ["music", "audio", "entertainment"],
    "mysql": ["development", "mysql", "database"],
    "network": ["networking", "network", "system"],
    "nextjs": ["development", "nextjs", "react"],
    "nginx": ["development", "nginx", "server"],
    "nodejs": ["development", "nodejs", "javascript"],
    "notion": ["productivity", "notion", "knowledge"],
    "npm": ["development", "npm", "package"],
    "obsidian": ["productivity", "obsidian", "knowledge"],
    "ocr": ["ocr", "text", "recognition"],
    "office": ["office", "productivity", "microsoft"],
    "okx": ["crypto", "okx", "exchange"],
    "online": ["online", "internet", "web"],
    "openai": ["ai", "openai", "gpt"],
    "openclaw": ["openclaw", "agent", "automation"],
    "openrouter": ["ai", "openrouter", "api"],
    "opera": ["browser", "opera", "web"],
    "opensea": ["nft", "opensea", "marketplace"],
    "optimization": ["optimization", "performance", "improvement"],
    "org": ["productivity", "org", "emacs"],
    "organization": ["productivity", "organization", "management"],
    "outlook": ["email", "outlook", "microsoft"],
    "payment": ["finance", "payment", "transaction"],
    "pdf": ["pdf", "document", "file"],
    "personal": ["personal", "productivity", "life"],
    "php": ["development", "php", "web"],
    "pinterest": ["social", "pinterest", "visual"],
    "planning": ["productivity", "planning", "organization"],
    "podcast": ["media", "podcast", "audio"],
    "poe": ["ai", "poe", "chatbot"],
    "pokemon": ["game", "pokemon", "gaming"],
    "polar": ["productivity", "polar", "knowledge"],
    "portfolio": ["career", "portfolio", "showcase"],
    "postgres": ["development", "postgres", "database"],
    "presentation": ["productivity", "presentation", "office"],
    "product": ["product", "management", "business"],
    "productivity": ["productivity", "efficiency", "tool"],
    "profile": ["profile", "user", "account"],
    "project": ["project", "management", "productivity"],
    "prompt": ["ai", "prompt", "engineering"],
    "python": ["development", "python", "programming"],
    "pytorch": ["ai", "pytorch", "machine-learning"],
    "qq": ["communication", "qq", "chat"],
    "quant": ["finance", "quant", "trading"],
    "question": ["qa", "question", "answer"],
    "quick": ["productivity", "quick", "utility"],
    "quote": ["finance", "quote", "stock"],
    "radar": ["monitoring", "radar", "detection"],
    "railway": ["deployment", "railway", "cloud"],
    "react": ["development", "react", "frontend"],
    "reading": ["reading", "books", "education"],
    "real-estate": ["realestate", "property", "housing"],
    "recipe": ["food", "recipe", "cooking"],
    "reddit": ["social", "reddit", "forum"],
    "redis": ["development", "redis", "database"],
    "refactor": ["development", "refactor", "improvement"],
    "reminder": ["productivity", "reminder", "alert"],
    "remote": ["work", "remote", "productivity"],
    "report": ["report", "data", "analysis"],
    "research": ["research", "academic", "study"],
    "resume": ["career", "resume", "job"],
    "retro": ["productivity", "retro", "reflection"],
    "review": ["review", "feedback", "evaluation"],
    "roadmap": ["planning", "roadmap", "strategy"],
    "rust": ["development", "rust", "programming"],
    "sales": ["sales", "business", "revenue"],
    "safari": ["browser", "safari", "apple"],
    "scheduling": ["productivity", "scheduling", "calendar"],
    "science": ["science", "research", "education"],
    "scrap": ["scraping", "data", "extraction"],
    "search": ["search", "discovery", "finding"],
    "security": ["security", "cybersecurity", "protection"],
    "seo": ["seo", "marketing", "optimization"],
    "server": ["server", "backend", "infrastructure"],
    "shopify": ["ecommerce", "shopify", "store"],
    "shopping": ["shopping", "ecommerce", "deal"],
    "signal": ["communication", "signal", "messaging"],
    "sketch": ["design", "sketch", "prototyping"],
    "slack": ["communication", "slack", "team"],
    "sleep": ["health", "sleep", "wellness"],
    "smart": ["smart", "automation", "iot"],
    "social": ["social", "media", "network"],
    "software": ["software", "development", "tool"],
    "soul": ["productivity", "soul", "agent"],
    "spotify": ["music", "spotify", "streaming"],
    "spreadsheet": ["productivity", "spreadsheet", "data"],
    "stability": ["ai", "stability", "image"],
    "stack": ["development", "stack", "technology"],
    "startup": ["startup", "business", "entrepreneur"],
    "statistic": ["statistics", "data", "analysis"],
    "steam": ["game", "steam", "gaming"],
    "storage": ["storage", "cloud", "file"],
    "story": ["writing", "story", "creative"],
    "strategy": ["strategy", "business", "planning"],
    "stripe": ["payment", "stripe", "finance"],
    "style": ["design", "style", "css"],
    "substack": ["content", "substack", "newsletter"],
    "svelte": ["development", "svelte", "frontend"],
    "swift": ["development", "swift", "ios"],
    "sync": ["sync", "automation", "data"],
    "system": ["system", "os", "utility"],
    "table": ["data", "table", "spreadsheet"],
    "task": ["productivity", "task", "management"],
    "tax": ["finance", "tax", "accounting"],
    "team": ["team", "collaboration", "productivity"],
    "tech": ["technology", "tech", "innovation"],
    "telegram": ["communication", "telegram", "messaging"],
    "tensorflow": ["ai", "tensorflow", "machine-learning"],
    "terminal": ["terminal", "cli", "command"],
    "terraform": ["devops", "terraform", "infrastructure"],
    "test": ["testing", "development", "quality"],
    "threads": ["social", "threads", "meta"],
    "ticket": ["ticket", "support", "booking"],
    "tiktok": ["social", "tiktok", "video"],
    "time": ["productivity", "time", "tracking"],
    "todo": ["productivity", "todo", "task"],
    "tool": ["tool", "utility", "helper"],
    "track": ["tracking", "monitoring", "analytics"],
    "trade": ["trading", "finance", "investment"],
    "training": ["training", "education", "learning"],
    "transformer": ["ai", "transformer", "nlp"],
    "travel": ["travel", "trip", "vacation"],
    "trello": ["productivity", "trello", "project"],
    "twitch": ["streaming", "twitch", "video"],
    "twitter": ["social", "twitter", "x"],
    "typeform": ["form", "typeform", "survey"],
    "typescript": ["development", "typescript", "programming"],
    "ubuntu": ["linux", "ubuntu", "system"],
    "unity": ["game", "unity", "development"],
    "unreal": ["game", "unreal", "development"],
    "user": ["user", "account", "profile"],
    "utility": ["utility", "tool", "helper"],
    "v0": ["ai", "v0", "vercel"],
    "video": ["video", "media", "editing"],
    "vim": ["development", "vim", "editor"],
    "virtual": ["virtual", "reality", "vr"],
    "visual": ["visual", "design", "graphics"],
    "vue": ["development", "vue", "frontend"],
    "wallet": ["finance", "wallet", "crypto"],
    "watch": ["watch", "monitoring", "alerting"],
    "web": ["web", "internet", "development"],
    "webhook": ["webhook", "integration", "automation"],
    "website": ["website", "web", "development"],
    "wechat": ["communication", "wechat", "china"],
    "whatsapp": ["communication", "whatsapp", "messaging"],
    "wiki": ["wiki", "knowledge", "documentation"],
    "windows": ["system", "windows", "microsoft"],
    "wordpress": ["cms", "wordpress", "website"],
    "work": ["work", "productivity", "job"],
    "workflow": ["workflow", "automation", "productivity"],
    "workspace": ["workspace", "productivity", "organization"],
    "writing": ["writing", "content", "creative"],
    "x": ["social", "x", "twitter"],
    "xiaohongshu": ["social", "xiaohongshu", "china"],
    "xcode": ["development", "xcode", "ios"],
    "youtube": ["video", "youtube", "streaming"],
    "zhihu": ["social", "zhihu", "china"],
    "zoom": ["communication", "zoom", "video"],
    "zsh": ["terminal", "zsh", "shell"],
}


def normalize_to_kebab_case(name: str) -> str:
    """Normalize any name to kebab-case."""
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
            tags = cat_tags[:3]  # Take first 3 tags
            break
    
    if '-cn' in name_lower or 'chinese' in name_lower:
        if 'chinese' not in tags:
            tags.append('chinese')
        if 'china' not in tags:
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
    """Process a single skill file from staging to skills directory."""
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
    
    for i, skill_name in enumerate(skills, 1):
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
        
        # Show progress every 10 skills
        if i % 10 == 0 or i == len(skills):
            print(f"   Progress: {i}/{len(skills)} skills processed...")
        
        print(f"{status_icon} {skill_name:45s} -> {result.get('destination', 'N/A')[-50:] if result.get('destination') else 'N/A'}")
        if result.get('description_fixed'):
            print(f"   ⚠️  Description was empty, auto-generated")
        if result.get('error') and result['status'] != 'skipped':
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
    
    parser = argparse.ArgumentParser(description='Process ALL skills in staging dynamically')
    parser.add_argument('--batch-size', type=int, default=BATCH_SIZE,
                       help=f'Skills per batch (default: {BATCH_SIZE})')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    print(f"\n{'='*60}")
    print(f"DYNAMIC BATCH PROCESSOR - ALL STAGING SKILLS")
    print(f"{'='*60}\n")
    
    # Discover all skills in staging
    print(f"🔍 Discovering skills in staging...")
    skill_names = discover_staging_skills()
    
    if not skill_names:
        print(f"✅ No skills found in staging directory")
        return 0
    
    print(f"   Found {len(skill_names)} skills in staging")
    
    # Create dynamic batches
    batches = create_dynamic_batches(skill_names, args.batch_size)
    print(f"   Created {len(batches)} batches (batch size: {args.batch_size})")
    
    # Process all batches
    all_results = []
    batches_processed = []
    
    for batch_id, skills in batches.items():
        results = process_batch(batch_id, skills)
        all_results.extend(results)
        batches_processed.append(batch_id)
        
        # Save progress after each batch
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
        
        # Generate sample for review
        print(f"\n📋 Next step: Generate 10% sample for quality review")
        print(f"   Command: python3 scripts/generators/sample-review-generator.py")
    
    return 0 if errors == 0 else 1


if __name__ == '__main__':
    exit(main())
