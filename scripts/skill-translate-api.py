#!/usr/bin/env python3
"""
Benchmark 5 free OpenRouter models for skill translation quality & speed.
Then use the winner for batch translation of 1900+ non-English skills.

Usage:
  # Benchmark (tests 3 skills × 5 models):
  python3 scripts/skill-translate-api.py --benchmark

  # Full batch with winning model:
  python3 scripts/skill-translate-api.py --execute --model openrouter-free
  python3 scripts/skill-translate-api.py --execute --model openrouter-free --resume

Environment:
  OPENROUTER_API_KEY: Your free OpenRouter API key (get one at https://openrouter.ai)
"""

import argparse
import json
import os
import re
import sys
import time
import shutil
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = BASE_DIR / "skills"
CHECKPOINT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "translation-api-checkpoint.json"
REPORT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "translation-api-report.md"
BENCHMARK_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "translation-benchmark.md"
BACKUP_DIR = BASE_DIR / ".archive" / "pre-translation-backup"

API_URL = "https://openrouter.ai/api/v1/chat/completions"
CJK_PATTERN = re.compile(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]')
CJK_THRESHOLD = 20

# Free models to benchmark
MODELS = {
    "openrouter-free": "openrouter/auto",
    "glm-4.5-air":     "z-ai/glm-4.5-air:free",
    "nemotron-30b":    "nvidia/nemotron-3-nano-30b-a3b:free",
    "minimax-m2.5":    "minimax/minimax-m2.5:free",
    "nemotron-9b":     "nvidia/nemotron-nano-9b-v2:free",
    "lfm-1.2b":        "liquid/lfm-2.5-1.2b-thinking:free",
}

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


def get_api_key():
    """Get OpenRouter API key from env."""
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        # Try .env file
        env_file = BASE_DIR / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("OPENROUTER_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if not key:
        print("❌ OPENROUTER_API_KEY not found!")
        print("   Get a free key at: https://openrouter.ai")
        print("   Then: export OPENROUTER_API_KEY='sk-or-...'")
        print("   Or add to .env: OPENROUTER_API_KEY=sk-or-...")
        sys.exit(1)
    return key


def call_openrouter(model_id, text, api_key, max_tokens=2048, timeout=30):
    """Call OpenRouter API and return (response_text, latency_seconds, tokens_used)."""
    payload = json.dumps({
        "model": model_id,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        "max_tokens": max_tokens,
        "temperature": 0.3,
        "top_p": 0.9,
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "https://github.com/overpowers",
            "X-Title": "Overpowers Skill Translator",
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
    
    choices = data.get("choices", [])
    if choices and isinstance(choices[0], dict):
        message = choices[0].get("message", {})
        content = message.get("content") or ""
    else:
        content = ""
        
    tokens = data.get("usage", {}).get("total_tokens", 0)

    # Clean thinking artifacts
    content = clean_output(content)
    return content, latency, tokens


def clean_output(text):
    """Remove thinking tokens and prompt artifacts."""
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    text = re.sub(r'</?think>', '', text).strip()
    lines = text.split('\n')
    cleaned = []
    skip = False
    for line in lines:
        stripped = line.strip()
        if any(m in stripped for m in [
            'Thinking Process:', 'Analyze the Request:', 'Drafting the Translation',
            '**Role:**', '**Task:**', '**Constraints:**',
            'Output ONLY the translated', 'Professional Translator',
            'I need to translate',
        ]):
            skip = True
            continue
        if re.match(r'^\d+\.\s+\*\*', stripped):
            skip = True
            continue
        if skip and (stripped.startswith('*') or stripped.startswith('-') or not stripped):
            continue
        skip = False
        cleaned.append(line)
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


def run_benchmark(api_key):
    """Benchmark all models on 3 sample skills."""
    print("🔍 Finding test skills...")
    skills = find_non_english_skills()

    # Pick 3 diverse samples: small, medium, large CJK content
    skills_sorted = sorted(skills, key=lambda x: x["cjk_chars"])
    n = len(skills_sorted)
    test_skills = [
        skills_sorted[n // 4],      # ~25th percentile (small)
        skills_sorted[n // 2],      # ~50th percentile (medium)
        skills_sorted[3 * n // 4],  # ~75th percentile (large)
    ]

    print(f"📋 Selected 3 test skills:")
    for s in test_skills:
        print(f"  {s['rel_path']} ({s['cjk_chars']} CJK chars, {s['size']} bytes)")

    results = []

    for model_name, model_id in MODELS.items():
        print(f"\n{'='*60}")
        print(f"🤖 Testing: {model_name} ({model_id})")

        model_results = {
            "model": model_name,
            "model_id": model_id,
            "skills": [],
            "total_time": 0,
            "total_tokens": 0,
            "avg_cjk_reduction": 0,
        }

        for skill in test_skills:
            text = Path(skill["path"]).read_text(encoding="utf-8")
            orig_cjk = skill["cjk_chars"]

            print(f"  📄 {skill['rel_path']} ({orig_cjk} CJK)...", end=" ", flush=True)

            response, latency, tokens = call_openrouter(model_id, text, api_key)

            if response.startswith("HTTP ") or response.startswith("Error:"):
                print(f"❌ {response[:80]}")
                model_results["skills"].append({
                    "path": skill["rel_path"],
                    "status": "error",
                    "error": response[:200],
                    "latency": latency,
                })
                time.sleep(5)  # Back off on error
                continue

            new_cjk = len(CJK_PATTERN.findall(response))
            reduction = (1 - new_cjk / max(orig_cjk, 1)) * 100

            print(f"✅ {latency:.1f}s, CJK {orig_cjk}→{new_cjk} ({reduction:.0f}% reduced), {tokens} tokens")

            model_results["skills"].append({
                "path": skill["rel_path"],
                "status": "ok",
                "latency": latency,
                "tokens": tokens,
                "orig_cjk": orig_cjk,
                "new_cjk": new_cjk,
                "reduction_pct": round(reduction, 1),
            })
            model_results["total_time"] += latency
            model_results["total_tokens"] += tokens

            # Rate limit courtesy
            time.sleep(3)

        # Calculate averages
        ok_skills = [s for s in model_results["skills"] if s["status"] == "ok"]
        if ok_skills:
            model_results["avg_cjk_reduction"] = sum(
                s["reduction_pct"] for s in ok_skills
            ) / len(ok_skills)
            model_results["avg_latency"] = model_results["total_time"] / len(ok_skills)
        else:
            model_results["avg_latency"] = 0

        results.append(model_results)

    # Generate benchmark report
    print(f"\n{'='*60}")
    print("📊 BENCHMARK RESULTS")
    print(f"{'='*60}")

    report_lines = [
        "# Translation Model Benchmark",
        f"",
        f"**Date**: {datetime.now().isoformat()}",
        f"**Test**: 3 skills × 5 models",
        f"",
        "| Model | Avg Latency | Avg CJK Reduction | Total Tokens | Status |",
        "|---|---|---|---|---|",
    ]

    for r in sorted(results, key=lambda x: -x["avg_cjk_reduction"]):
        ok = len([s for s in r["skills"] if s["status"] == "ok"])
        fail = len([s for s in r["skills"] if s["status"] == "error"])
        status = f"{ok}/3 ok" + (f", {fail} errors" if fail else "")
        row = (
            f"| {r['model']} | {r.get('avg_latency', 0):.1f}s | "
            f"{r['avg_cjk_reduction']:.0f}% | {r['total_tokens']} | {status} |"
        )
        report_lines.append(row)
        print(row)

    # Estimate full batch time for best model
    best = max(results, key=lambda x: x["avg_cjk_reduction"])
    if best.get("avg_latency", 0) > 0:
        est_hours = (1904 * best["avg_latency"]) / 3600
        report_lines.append(f"")
        report_lines.append(f"**Winner**: {best['model']} ({best['avg_cjk_reduction']:.0f}% CJK reduction)")
        report_lines.append(f"**Estimated full batch**: ~{est_hours:.1f}h for 1904 skills")
        print(f"\n🏆 Winner: {best['model']} → est. {est_hours:.1f}h for full batch")

    BENCHMARK_FILE.parent.mkdir(parents=True, exist_ok=True)
    BENCHMARK_FILE.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"\n💾 Report: {BENCHMARK_FILE}")


def run_batch(api_key, model_name, limit=0, resume=False):
    """Run batch translation with selected model."""
    model_id = MODELS.get(model_name)
    if not model_id:
        # Try full model ID
        for k, v in MODELS.items():
            if model_name in v:
                model_id = v
                model_name = k
                break
    if not model_id:
        print(f"❌ Unknown model: {model_name}")
        print(f"   Available: {', '.join(MODELS.keys())}")
        sys.exit(1)

    print(f"🤖 Using model: {model_name} ({model_id})")
    print("🔍 Scanning for non-English skills...")
    skills = find_non_english_skills()
    print(f"📋 Found {len(skills)} non-English skills")

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
                fm_result, _, _ = call_openrouter(model_id, frontmatter, api_key, max_tokens=512)
                if not fm_result.startswith(("HTTP ", "Error:")):
                    translated_fm = fm_result

            # Translate body
            body_result, latency, tokens = call_openrouter(model_id, body, api_key)

            if body_result.startswith(("HTTP ", "Error:")):
                print(f"  ❌ API error: {body_result[:80]}")
                checkpoint["failed"].append(rel)
                fail += 1

                # Rate limit hit? Back off
                if "429" in body_result or "rate" in body_result.lower():
                    print("  ⏸️  Rate limited, waiting 30s...")
                    time.sleep(30)
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

        # Checkpoint every 10
        if (i + 1) % 10 == 0:
            CHECKPOINT_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(checkpoint, f, indent=2)
            print(f"  💾 Checkpoint ({len(checkpoint['completed'])} done)")

        # Courtesy delay for free tier to prevent 429 over long runs
        time.sleep(5)

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
        f"# API Translation Report",
        f"- **Date**: {datetime.now().isoformat()}",
        f"- **Model**: {model_name} ({model_id})",
        f"- **Translated**: {success}",
        f"- **Skipped**: {len(checkpoint['skipped'])}",
        f"- **Failed**: {fail}",
        f"- **Time**: {elapsed/60:.1f} min",
    ]
    REPORT_FILE.write_text("\n".join(report), encoding="utf-8")
    print(f"💾 Report: {REPORT_FILE}")


def main():
    parser = argparse.ArgumentParser(description="Translate skills via free OpenRouter API")
    parser.add_argument("--benchmark", action="store_true", help="Benchmark 5 models × 3 skills")
    parser.add_argument("--execute", action="store_true", help="Run batch translation")
    parser.add_argument("--model", type=str, default="openrouter-free", help="Model for batch")
    parser.add_argument("--limit", type=int, default=0, help="Limit skills count")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    args = parser.parse_args()

    if not args.benchmark and not args.execute:
        print("Usage:")
        print("  --benchmark          Test all 5 models on 3 skills")
        print("  --execute --model X  Run batch with model X")
        sys.exit(1)

    api_key = get_api_key()

    if args.benchmark:
        run_benchmark(api_key)
    elif args.execute:
        run_batch(api_key, args.model, args.limit, args.resume)


if __name__ == "__main__":
    main()
