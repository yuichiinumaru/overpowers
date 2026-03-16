#!/usr/bin/env python3
"""
Batch translation of non-English skills using Gemini 2.5 Flash Lite via Google GenAI SDK.
Designed to run within free tier limits (15 RPM = 4s delay).

Usage:
  # Install SDK:
  # pip install google-genai

  # Full batch:
  # python3 scripts/skill-translate-gemini.py --execute
  
  # Resume from checkpoint:
  # python3 scripts/skill-translate-gemini.py --execute --resume
  
  # Run only a specific number of skills (e.g. half of them)
  # python3 scripts/skill-translate-gemini.py --execute --limit 950 --resume

Environment:
  GEMINI_API_KEY: Your Gemini API key (from Google AI Studio)
"""

import argparse
import json
import os
import re
import sys
import time
import shutil
from pathlib import Path
from datetime import datetime

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("❌ google-genai package not found!")
    print("   Run: pip install google-genai")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = BASE_DIR / "skills"
CHECKPOINT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "translation-gemini-checkpoint.json"
REPORT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "translation-gemini-report.md"
BACKUP_DIR = BASE_DIR / ".archive" / "pre-translation-gemini-backup"

CJK_PATTERN = re.compile(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]')
CJK_THRESHOLD = 20
MODEL_ID = "gemini-flash-lite-latest"
# Base delay: 15 RPM = 1 request every 4 seconds. Add buffer.
BASE_RATE_LIMIT_DELAY = 4.5 

def get_rate_limit_delay(rotator):
    """Calculate the optimal delay based on the number of keys to maximize throughput."""
    count = max(1, rotator.get_key_count())
    return max(0.2, BASE_RATE_LIMIT_DELAY / count)

SYSTEM_PROMPT = (
    "You are a professional translator. "
    "Translate the following content from its original language to English. "
    "Preserve ALL markdown formatting, code blocks, file paths, command examples, "
    "YAML structure, and technical terms. "
    "Do NOT translate: variable names, function names, file paths, CLI commands, "
    "code inside ```blocks```, URLs, or proper nouns that are technical identifiers. "
    "Translate ONLY the natural language text. "
    "Output ONLY the translated text, no explanations, no thinking, no commentary."
)

from api_key_rotator import get_rotator_from_env

def get_api_key_rotator():
    """Get Gemini API keys from env and return a rotator."""
    rotator = get_rotator_from_env("GEMINI_API_KEY")
    if not rotator or rotator.get_key_count() == 0:
        print("❌ GEMINI_API_KEY not found or empty!")
        print("   Get keys at: https://aistudio.google.com/app/apikey")
        print("   Then set it in .env: GEMINI_API_KEY='key1,key2,key3'")
        sys.exit(1)
        
    return rotator

def call_gemini(api_key, text):
    """Call Gemini API using a specific key and return (response_text, latency_seconds, tokens_used)."""
    start = time.time()
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[text],
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.3,
                top_p=0.9,
            ),
        )
        content = response.text or ""
        tokens = response.usage_metadata.total_token_count if response.usage_metadata else 0
    except Exception as e:
        # Check for rate limit errors
        err_msg = str(e)
        if "429" in err_msg or "quota" in err_msg.lower():
            return f"RateLimit: {e}", time.time() - start, 0
            
        # Check for invalid key errors (400 API_KEY_INVALID, or 403)
        if "API_KEY_INVALID" in err_msg or "API key not valid" in err_msg or "403" in err_msg:
            return f"InvalidKey: {e}", time.time() - start, 0
            
        return f"Error: {e}", time.time() - start, 0

    latency = time.time() - start
    return content.strip(), latency, tokens

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
    """Split YAML frontmatter from body."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return None, text.strip()

def reassemble(frontmatter, body):
    """Reassemble frontmatter + body."""
    if frontmatter:
        return f"---\n{frontmatter}\n---\n\n{body}\n"
    return f"{body}\n"

def run_batch(rotator, limit=0, resume=False, verbose=False):
    """Run batch translation with Gemini."""
    print(f"🤖 Using model: {MODEL_ID} via google-genai SDK")
    print(f"🔑 Loaded {rotator.get_key_count()} API keys in rotation")
    print(f"⏱️  Base rate limit delay per key is {BASE_RATE_LIMIT_DELAY}s")
    print("🔍 Scanning for non-English skills...")
    skills = find_non_english_skills()
    
    # Process skills in REVERSE order from the OpenRouter script
    # so they can meet in the middle if running currently.
    skills = list(reversed(skills))
    
    # Load checkpoint
    checkpoint = {"completed": [], "failed": [], "skipped": []}
    if resume and CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE) as f:
            checkpoint = json.load(f)
        completed_set = set(checkpoint["completed"])
        skills = [s for s in skills if s["rel_path"] not in completed_set]
        print(f"⏩ Resuming: {len(completed_set)} done, {len(skills)} remaining")

    if limit > 0:
        skills = skills[:limit]
        print(f"🔒 Limited to {limit} skills")

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    start_time = time.time()
    success = 0
    fail = 0

    for i, skill in enumerate(skills):
        path = Path(skill["path"])
        rel = skill["rel_path"]
        elapsed = time.time() - start_time
        rate = (i / elapsed * 3600) if elapsed > 0 and i > 0 else 0

        print(f"\n[{i+1}/{len(skills)}] {rel} ({skill['cjk_chars']} CJK) [{rate:.0f}/hr]")

        try:
            text = path.read_text(encoding="utf-8")
            frontmatter, body = split_frontmatter(text)

            # Translate frontmatter description if CJK
            translated_fm = frontmatter
            if frontmatter and len(CJK_PATTERN.findall(frontmatter)) > 5:
                while True:
                    key = rotator.get_next_key()
                    fm_result, latency, tokens = call_gemini(key, frontmatter)
                    
                    if fm_result.startswith("RateLimit:"):
                        if verbose: print(f"  [Verbose] Key ...{key[-4:]} limit: {fm_result}")
                        rotator.report_error(key, "RATE_LIMIT")
                        continue
                        
                    if fm_result.startswith("InvalidKey:"):
                        if verbose: print(f"  [Verbose] Key ...{key[-4:]} invalid: {fm_result}")
                        rotator.report_error(key, "INVALID")
                        continue
                        
                    if not fm_result.startswith("Error:"):
                        translated_fm = fm_result
                        time.sleep(get_rate_limit_delay(rotator)) # Avoid blowing rate limit on double calls
                    break

            # Translate body
            while True:
                key = rotator.get_next_key()
                body_result, latency, tokens = call_gemini(key, body)

                if body_result.startswith("RateLimit:"):
                    if verbose: print(f"  [Verbose] Key ...{key[-4:]} limit: {body_result}")
                    rotator.report_error(key, "RATE_LIMIT")
                    continue
                    
                if body_result.startswith("InvalidKey:"):
                    if verbose: print(f"  [Verbose] Key ...{key[-4:]} invalid: {body_result}")
                    rotator.report_error(key, "INVALID")
                    continue
                    
                if body_result.startswith("Error:"):
                    if verbose:
                        print(f"  ❌ API error: {body_result}")
                    else:
                        print(f"  ❌ API error: {body_result[:80]}")
                    checkpoint["failed"].append(rel)
                    fail += 1
                    break
                    
                # Success
                break
                
            if body_result.startswith("Error:"):
                continue

            # Quality gate
            orig_cjk = skill["cjk_chars"]
            new_cjk = len(CJK_PATTERN.findall(body_result))

            if new_cjk < orig_cjk * 0.5:
                # Backup + save
                backup_path = BACKUP_DIR / rel
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                if not backup_path.exists():
                    shutil.copy2(str(path), str(backup_path))

                translated = reassemble(translated_fm, body_result)
                path.write_text(translated, encoding="utf-8")
                print(f"  ✅ CJK: {orig_cjk}→{new_cjk} ({latency:.1f}s, {tokens}tok)")
                success += 1
                checkpoint["completed"].append(rel)
            else:
                print(f"  ⚠️ Low quality (CJK: {orig_cjk}→{new_cjk}), skipping")
                checkpoint["skipped"].append(rel)

        except Exception as e:
            print(f"  ❌ {e}")
            checkpoint["failed"].append(rel)
            fail += 1

        # Checkpoint every 5 (since it's slower)
        if (i + 1) % 5 == 0:
            CHECKPOINT_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(checkpoint, f, indent=2)
            print(f"  💾 Checkpoint ({len(checkpoint['completed'])} done)")

        # Mandatory delay dynamically adjusted across all available keys
        time.sleep(get_rate_limit_delay(rotator))

    # Final save
    CHECKPOINT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(checkpoint, f, indent=2)

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"✅ Translated: {success}")
    print(f"⚠️  Skipped: {len(checkpoint['skipped'])}")
    print(f"❌ Failed: {fail}")
    print(f"⏱️  Time: {elapsed/60:.1f} min ({elapsed/max(success,1):.1f}s/skill)")

    # Report
    report = [
        f"# Gemini API Translation Report",
        f"- **Date**: {datetime.now().isoformat()}",
        f"- **Model**: {MODEL_ID}",
        f"- **Translated**: {success}",
        f"- **Skipped**: {len(checkpoint['skipped'])}",
        f"- **Failed**: {fail}",
        f"- **Time**: {elapsed/60:.1f} min",
    ]
    REPORT_FILE.write_text("\n".join(report), encoding="utf-8")
    print(f"💾 Report: {REPORT_FILE}")


def main():
    parser = argparse.ArgumentParser(description="Translate skills via Gemini 2.5 Flash Lite SDK")
    parser.add_argument("--execute", action="store_true", help="Run batch translation")
    parser.add_argument("--limit", type=int, default=0, help="Limit skills count")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("-c", "--clean", action="store_true", help="Clear the invalid keys blacklist")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    rotator = get_api_key_rotator()

    if args.clean:
        rotator.clear_blacklist()
        if not args.execute:
            sys.exit(0)

    if not args.execute:
        print("Usage:")
        print("  --execute              Run batch translation")
        print("  --execute --resume     Resume from checkpoint")
        print("  --execute --limit 950  Run only a limited number of skills")
        print("  --clean, -c            Clear the persistent blacklist of invalid keys")
        sys.exit(1)

    run_batch(rotator, args.limit, args.resume, args.verbose)


if __name__ == "__main__":
    main()
