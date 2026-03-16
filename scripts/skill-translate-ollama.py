#!/usr/bin/env python3
"""
Batch Skill Translator using local Ollama instance.
Translates non-English SKILL.md files to English, preserving markdown structure.

Usage:
  uv run scripts/skill-translate-ollama.py --dry-run          # Count & preview
  uv run scripts/skill-translate-ollama.py --execute          # Full batch run
  uv run scripts/skill-translate-ollama.py --execute --limit 5 # Test with 5 skills
  uv run scripts/skill-translate-ollama.py --execute --resume # Resume from last checkpoint

Environment:
  OLLAMA_HOST: Default is http://localhost:11434
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = BASE_DIR / "skills"
CHECKPOINT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "translation-checkpoint-ollama.json"
REPORT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "translation-report.md"
BACKUP_DIR = BASE_DIR / ".archive" / "pre-translation-backup"

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
OLLAMA_MODEL = "lfm2.5-thinking"

# CJK Unicode ranges
CJK_PATTERN = re.compile(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]')
CJK_THRESHOLD = 20  # Minimum CJK chars to consider non-English

SYSTEM_PROMPT = (
    "You are a professional translator. You must output ONLY the translated text.\n"
    "Translate the following content from its original language to English. "
    "Preserve ALL markdown formatting, code blocks, file paths, command examples, YAML structure, and technical terms. "
    "Do NOT translate: variable names, function names, file paths, CLI commands, code inside ```blocks```, URLs, or proper nouns that are technical identifiers. "
    "Translate ONLY the natural language text (descriptions, instructions, comments outside code). "
    "CRITICAL: Output absolutely nothing else. No introductions, no 'Here is the translation:', no explanations, no commentary."
)


def call_ollama(model_id, text, timeout=240):
    """Call Ollama API and return (response_text, latency_seconds, 0)."""
    payload = json.dumps({
        "model": model_id,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Translate this exactly, with NO conversational text before or after:\n\n{text}"},
        ],
        "stream": False,
        "options": {
            "num_predict": 4096,
            "temperature": 0.1,
            "top_p": 0.9
        }
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
        },
    )

    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return f"HTTP {e.code}: {body[:200]}", time.time() - start, 0
    except Exception as e:
        return f"Error: {e}", time.time() - start, 0

    latency = time.time() - start
    message = data.get("message", {})
    content = message.get("content") or ""
        
    # Tokens proxy (not fully supported by default ollama response in the same way, but eval_count exists)
    tokens = data.get("eval_count", 0)

    # Clean thinking artifacts
    content = clean_output(content)
    return content, latency, tokens


def clean_output(text):
    """Remove thinking tokens and prompt artifacts."""
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    text = re.sub(r'</?think>', '', text).strip()
    lines = text.split('\n')
    cleaned = []
    
    # Strip common prefixes
    for i, line in enumerate(lines):
        stripped = line.strip()
        lower = stripped.lower()
        if lower.startswith("here is the trans"):
            continue
        if lower.startswith("the translated text is"):
            continue
        if lower.startswith("translated text:"):
            continue
        if "all markdown preserved" in lower and "adhering strictly" in lower:
            continue
        if lower.startswith("the following translation adheres strictly"):
            continue
        if "the translated content is provided below" in lower:
            continue
        if lower.startswith("translation:"):
            continue
        if lower.startswith("```markdown") and i == 0:
            continue
        
        if any(m in stripped for m in [
            'Thinking Process:', 'Analyze the Request:', 'Drafting the Translation',
            '**Role:**', '**Task:**', '**Constraints:**',
            'Output ONLY the translated', 'Professional Translator',
            'I need to translate',
        ]):
            continue
            
        cleaned.append(line)
        
    # Remove trailing markdown closure if we removed the top one
    if cleaned and cleaned[-1].strip() == "```" and text.strip().startswith("```markdown"):
        cleaned.pop()
        
    return '\n'.join(cleaned).strip()


def find_non_english_skills():
    """Scan for skills with CJK content."""
    skills = []
    for root, dirs, files in os.walk(SKILLS_DIR):
        if "SKILL.md" in files:
            path = Path(root) / "SKILL.md"
            try:
                text = path.read_text(encoding="utf-8")
                cjk_count = len(CJK_PATTERN.findall(text))
                if cjk_count >= CJK_THRESHOLD:
                    skills.append({
                        "path": str(path),
                        "rel_path": str(path.relative_to(BASE_DIR)),
                        "cjk_chars": cjk_count,
                        "size": len(text),
                    })
            except Exception:
                pass
    return sorted(skills, key=lambda x: x["rel_path"])


def split_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return None, text.strip()


def reassemble(frontmatter_yaml, body):
    if frontmatter_yaml:
        return f"---\n{frontmatter_yaml}\n---\n\n{body}\n"
    return f"{body}\n"


def chunk_text(text, max_chars=1500):
    if len(text) <= max_chars:
        return [text]

    chunks = []
    paragraphs = text.split("\n\n")
    current = []
    current_len = 0

    for para in paragraphs:
        if current_len + len(para) > max_chars and current:
            chunks.append("\n\n".join(current))
            current = [para]
            current_len = len(para)
        else:
            current.append(para)
            current_len += len(para) + 2

    if current:
        chunks.append("\n\n".join(current))

    return chunks


def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE) as f:
            return json.load(f)
    return {"completed": [], "failed": [], "skipped": []}


def save_checkpoint(data):
    CHECKPOINT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(data, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--model", type=str, default=OLLAMA_MODEL, help="Local Ollama model name")
    args = parser.parse_args()

    if not args.dry_run and not args.execute:
        print("Error: specify --dry-run or --execute")
        sys.exit(1)

    safe_model_name = re.sub(r'[^a-zA-Z0-9]', '-', args.model).strip('-')

    print("🔍 Scanning for non-English skills...")
    skills = find_non_english_skills()
    print(f"📋 Found {len(skills)} skills with CJK content")

    if args.dry_run:
        print(f"\n{'='*60}")
        print("DRY RUN — would translate:")
        for s in skills[:20]:
            print(f"  {s['rel_path']} ({s['cjk_chars']} CJK chars)")
        if len(skills) > 20:
            print(f"  ... and {len(skills)-20} more")
        return

    checkpoint = load_checkpoint() if args.resume else {"completed": [], "failed": [], "skipped": []}
    completed_paths = set(checkpoint["completed"])

    if args.resume:
        skills = [s for s in skills if s["rel_path"] not in completed_paths]
        print(f"⏩ Resuming: {len(completed_paths)} already done, {len(skills)} remaining")

    if args.limit > 0:
        skills = skills[:args.limit]
        print(f"🔒 Limited to {args.limit} skills")

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    start_time = time.time()
    success = 0
    fail = 0

    total_tokens = 0
    total_calls = 0

    for i, skill in enumerate(skills):
        path = Path(skill["path"])
        rel = skill["rel_path"]
        elapsed = time.time() - start_time
        rate = (i / elapsed * 3600) if elapsed > 0 and i > 0 else 0

        print(f"\n[{i+1}/{len(skills)}] {rel}")
        print(f"  CJK: {skill['cjk_chars']} | Rate: {rate:.0f}/hr | Mode: Ollama ({args.model})")

        try:
            text = path.read_text(encoding="utf-8")
            frontmatter, body = split_frontmatter(text)

            translated_fm = frontmatter
            if frontmatter and len(CJK_PATTERN.findall(frontmatter)) > 5:
                translated_fm, lat, tok = call_ollama(args.model, frontmatter)
                # Ensure no HTTP Error
                if translated_fm.startswith("HTTP ") or translated_fm.startswith("Error:"):
                    raise Exception(translated_fm)
                total_tokens += tok
                total_calls += 1

            chunks = chunk_text(body)
            translated_chunks = []
            
            error_occurred = False
            for chunk in chunks:
                if len(CJK_PATTERN.findall(chunk)) < 5:
                    translated_chunks.append(chunk)
                    continue

                translated, lat, tok = call_ollama(args.model, chunk)
                if translated.startswith("HTTP ") or translated.startswith("Error:"):
                    print(f"  ❌ API Error: {translated}")
                    error_occurred = True
                    break
                    
                total_tokens += tok
                total_calls += 1
                translated_chunks.append(translated)
                
            if error_occurred:
                checkpoint["failed"].append(rel)
                fail += 1
                continue

            translated_body = "\n\n".join(translated_chunks)
            final_text = reassemble(translated_fm, translated_body)
            new_cjk = len(CJK_PATTERN.findall(final_text))

            orig_cjk = skill["cjk_chars"]
            out_file_name = f"SKILL-{safe_model_name}.md"
            out_path = path.parent / out_file_name

            if new_cjk < orig_cjk * 0.5:
                out_path.write_text(final_text, encoding="utf-8")
                print(f"  ✅ Saved {out_file_name} | CJK: {orig_cjk} → {new_cjk}")
                success += 1
                checkpoint["completed"].append(rel)
            else:
                # If chunking failed or text too short, write it anyway if it lowered a bit or warn
                out_path.write_text(final_text, encoding="utf-8")
                print(f"  ⚠️  Saved {out_file_name} but CJK count still high: {orig_cjk} → {new_cjk}")
                checkpoint["completed"].append(rel)
                success += 1

        except Exception as e:
            print(f"  ❌ Error: {e}")
            checkpoint["failed"].append(rel)
            fail += 1

        if (i + 1) % 5 == 0:
            save_checkpoint(checkpoint)
            print(f"  💾 Checkpoint saved ({len(checkpoint['completed'])} done)")

    save_checkpoint(checkpoint)

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"✅ Completed: {success}")
    print(f"❌ Failed: {fail}")
    print(f"⏱️  Time: {elapsed/60:.1f} min ({elapsed/max(success,1):.1f} sec/skill)")

    report = [
        f"# Translation Report (Ollama)",
        f"",
        f"- **Date**: {datetime.now().isoformat()}",
        f"- **Model**: {args.model}",
        f"- **Translated**: {success}",
        f"- **Failed**: {fail}",
        f"- **Time**: {elapsed/60:.1f} min",
        f"- **Rate**: {success/max(elapsed/3600,0.01):.0f} skills/hr",
    ]
    REPORT_FILE.write_text("\n".join(report), encoding="utf-8")
    print(f"\n💾 Report: {REPORT_FILE}")

if __name__ == "__main__":
    main()
