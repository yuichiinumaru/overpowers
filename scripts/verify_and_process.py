#!/usr/bin/env python3
"""Verify batches 01-25 and process from 51+"""
import os, re
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

STAGING = Path("/home/sephiroth/Work/overpowers/.archive/staging/skills")
SKILLS = Path("/home/sephiroth/Work/overpowers/skills")
TASKS = Path("/home/sephiroth/Work/overpowers/.docs/tasks")
CHANGELOG = Path("/home/sephiroth/Work/overpowers/CHANGELOG.md")

def check_batch(batch_num):
    """Check if batch is complete"""
    task_file = TASKS / f"0500-extraction-skills-batch-{batch_num:03d}.md"
    if not task_file.exists():
        return None, "No task file"
    
    content = task_file.read_text()
    unchecked = len(re.findall(r'^- \[ \]', content, re.MULTILINE))
    checked = len(re.findall(r'^- \[x\]', content, re.MULTILINE))
    total = unchecked + checked
    
    if total == 0:
        return None, "Empty task file"
    
    if unchecked == 0:
        return 100, f"Complete ({checked}/{total})"
    elif checked == 0:
        return 0, f"Not started (0/{total})"
    else:
        pct = int(checked/total*100)
        return pct, f"In progress ({checked}/{total}, {pct}%)"

def get_files_from_task(batch_num):
    """Get pending files from task"""
    task_file = TASKS / f"0500-extraction-skills-batch-{batch_num:03d}.md"
    if not task_file.exists():
        return []
    content = task_file.read_text()
    matches = re.findall(r'`\.archive/staging/skills/([^`]+)_SKILL\.md`', content)
    # Only return files that still exist in staging
    return [f for f in matches if (STAGING / f"{f}_SKILL.md").exists()]

def get_category(name):
    domain, subdomain = "general", "tool"
    mappings = {
        "ai-llm": ("ai-llm", "ai"), "agent": ("agent", "ai"), "memory": ("agent", "memory"),
        "content": ("content-media", "content"), "media": ("content-media", "media"),
        "video": ("content-media", "video"), "image": ("content-media", "image"),
        "finance": ("finance", "trading"), "stock": ("finance", "stocks"), "crypto": ("finance", "crypto"),
        "health": ("health", "wellness"), "game": ("entertainment", "gaming"),
        "social": ("social", "platform"), "wechat": ("social", "wechat"),
        "search": ("tool", "search"), "converter": ("tool", "conversion"),
        "analyzer": ("tool", "analytics"), "dev": ("dev", "development"),
    }
    for key, (d, s) in mappings.items():
        if key in name.lower():
            return d, s
    return domain, subdomain

def process_file(f):
    try:
        p = STAGING / f
        if not p.exists():
            return None
        name = f.replace("_SKILL.md", "")
        domain, subdomain = get_category(name)
        desc = f"Skill for {name.replace('-', ' ').title()}"
        fm = f'---\nname: {name}\ndescription: {desc}\ntags:\n  - {domain}\n  - {subdomain}\nversion: 1.0.0\n---\n'
        content = p.read_text()
        content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
        d = SKILLS / name
        d.mkdir(exist_ok=True)
        (d / "SKILL.md").write_text(fm + content)
        p.unlink()
        return (f, name, desc)
    except Exception as e:
        return (f, None, str(e))

def process_batch(batch_num):
    files = get_files_from_task(batch_num)
    if not files:
        return [], []
    
    print(f"\nBATCH {batch_num:03d}: Processing {len(files)} files")
    ok = []
    with ProcessPoolExecutor(max_workers=4) as ex:
        for r in as_completed([ex.submit(process_file, f) for f in files]):
            res = r.result()
            if res and res[1]:
                ok.append(res)
    
    # Update task
    task_file = TASKS / f"0500-extraction-skills-batch-{batch_num:03d}.md"
    if task_file.exists() and ok:
        c = task_file.read_text()
        for o in ok:
            c = c.replace(f"- [ ] `{o[0]}`", f"- [x] `{o[0]}` → `skills/{o[1]}/`")
        task_file.write_text(c)
    
    # Update changelog
    if ok:
        entry = f"## [2026-03-16] - Batch {batch_num:03d} Completion\n### Added\n- {len(ok)} skills:\n"
        for o in ok:
            entry += f"  - `{o[1]}` - {o[2][:60]}\n"
        entry += "**Author**: gemini-cli-orchestrator\n\n"
        c = CHANGELOG.read_text() if CHANGELOG.exists() else ""
        CHANGELOG.write_text(entry + c)
    
    return ok, files

print("="*80)
print("BATCH VERIFICATION: 01-25")
print("="*80)

pending = []
for bn in list(range(1, 26, 2)):  # Odd batches 1-25
    pct, msg = check_batch(bn)
    status = "✅" if pct == 100 else "⏳" if pct and pct > 0 else "🔴" if pct == 0 else "❓"
    print(f"{status} Batch {bn:03d}: {msg}")
    if pct is not None and pct < 100:
        pending.append(bn)

print(f"\n{'='*80}")
print(f"Pending batches in 01-25: {pending if pending else 'None!'}")
print(f"{'='*80}\n")

# Now process from batch 51
print("="*80)
print("PROCESSING ODD BATCHES FROM 51+")
print("="*80)

total_processed = 0
for bn in range(51, 80, 2):  # 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79
    ok, all_files = process_batch(bn)
    if ok or all_files:
        print(f"  ✅ {len(ok)}/{len(all_files)} processed")
        total_processed += len(ok)

print(f"\n{'='*80}")
print(f"🎉 TOTAL FROM BATCHES 51+: {total_processed} skills")
print(f"{'='*80}\n")
