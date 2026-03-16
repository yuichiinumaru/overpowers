#!/usr/bin/env python3
"""
Local Ollama model comparison for skill translation quality.
Runs the SAME translation tasks through ALL models, saves each result as
SKILL-{modelname}.md for manual comparison, and logs pure inference time
(excluding model load) so larger models aren't unfairly penalized.

Usage:
  uv run scripts/skill-benchmark-ollama.py --top 5
  uv run scripts/skill-benchmark-ollama.py --models qwen3.5:2b qwen3.5:4b --top 3
  uv run scripts/skill-benchmark-ollama.py --models-file scripts/ollama-models.json --top 10

Environment:
  OLLAMA_URL: Default is http://localhost:11434
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
REPORT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "benchmark-ollama-report.md"

OLLAMA_BASE = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_CHAT_URL = f"{OLLAMA_BASE}/api/chat"

# Default models JSON sidecar
DEFAULT_MODELS_FILE = SCRIPT_DIR / "ollama-models.json"

CJK_PATTERN = re.compile(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]')
CJK_THRESHOLD = 50

SYSTEM_PROMPT = (
    "You are a professional translator. You must output ONLY the translated text.\n"
    "Translate the following content from its original language to English. "
    "Preserve ALL markdown formatting, code blocks, file paths, command examples, YAML structure, and technical terms. "
    "Do NOT translate: variable names, function names, file paths, CLI commands, code inside ```blocks```, URLs, or proper nouns that are technical identifiers. "
    "Translate ONLY the natural language text (descriptions, instructions, comments outside code). "
    "CRITICAL: Output absolutely nothing else. No introductions, no 'Here is the translation:', no explanations, no commentary."
)

# ---------------------------------------------------------------------------
# Ollama helpers
# ---------------------------------------------------------------------------

def preload_model(model_id):
    """Send a tiny warmup request so the model is fully loaded in VRAM.
    This way the first real translation doesn't include load time."""
    print(f"  ⏳ Preloading {model_id} into memory...")
    payload = json.dumps({
        "model": model_id,
        "messages": [{"role": "user", "content": "Hi"}],
        "stream": False,
        "options": {"num_predict": 1},
    }).encode("utf-8")
    req = urllib.request.Request(OLLAMA_CHAT_URL, data=payload,
                                headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            resp.read()
        print(f"  ✅ {model_id} loaded and ready")
    except Exception as e:
        print(f"  ⚠️ Preload warning: {e}")


def call_ollama(model_id, text, timeout=600):
    """Call Ollama and return (content, eval_seconds, eval_tokens, prompt_tokens).
    eval_seconds comes from Ollama's own eval_duration – pure inference, no load."""
    payload = json.dumps({
        "model": model_id,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        "stream": False,
        "options": {
            "num_predict": 8192,
            "temperature": 0.1,
            "top_p": 0.9,
        },
    }).encode("utf-8")

    req = urllib.request.Request(OLLAMA_CHAT_URL, data=payload,
                                headers={"Content-Type": "application/json"})

    wall_start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return f"HTTP {e.code}: {body[:200]}", 0, 0, 0
    except Exception as e:
        return f"Error: {e}", 0, 0, 0

    wall_time = time.time() - wall_start
    message = data.get("message", {})
    content = message.get("content") or ""

    # Ollama timing fields (nanoseconds)
    eval_duration = data.get("eval_duration", 0) / 1e9    # pure generation time
    load_duration = data.get("load_duration", 0) / 1e9    # model load time
    eval_count = data.get("eval_count", 0)                # output tokens
    prompt_eval_count = data.get("prompt_eval_count", 0)  # input tokens

    content = clean_output(content)
    return content, eval_duration, eval_count, prompt_eval_count


def clean_output(text):
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    text = re.sub(r'</?think>', '', text).strip()
    lines = text.split('\n')
    cleaned = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        lower = stripped.lower()
        if lower.startswith("here is the trans"): continue
        if lower.startswith("the translated text is"): continue
        if lower.startswith("translated text:"): continue
        if "all markdown preserved" in lower and "adhering strictly" in lower: continue
        if lower.startswith("the following translation adheres strictly"): continue
        if "the translated content is provided below" in lower: continue
        if lower.startswith("translation:"): continue
        if lower.startswith("```markdown") and i == 0: continue
        if any(m in stripped for m in [
            'Thinking Process:', 'Analyze the Request:', 'Drafting the Translation',
            '**Role:**', '**Task:**', '**Constraints:**',
            'Output ONLY the translated', 'Professional Translator',
            'I need to translate',
        ]):
            continue
        cleaned.append(line)

    if cleaned and cleaned[-1].strip() == "```" and text.strip().startswith("```markdown"):
        cleaned.pop()

    return '\n'.join(cleaned).strip()

# ---------------------------------------------------------------------------
# Skill discovery
# ---------------------------------------------------------------------------

def find_top_non_english_skills(limit=10):
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

    skills.sort(key=lambda x: x["cjk_chars"], reverse=True)
    return skills[:limit]


def sanitize_model_name(name):
    return re.sub(r'[^a-zA-Z0-9.\-]', '_', name)


def load_models(args):
    """Resolve model list from args or JSON file."""
    if args.models:
        return args.models

    mfile = Path(args.models_file) if args.models_file else DEFAULT_MODELS_FILE
    if mfile.exists():
        try:
            with open(mfile) as f:
                models = json.load(f).get("models", [])
            if models:
                return models
        except Exception:
            pass

    return ["qwen3.5:2b", "qwen3.5:4b"]

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Compare Ollama models on translation tasks")
    parser.add_argument("--models", nargs="*", default=None,
                        help="Explicit list of Ollama model names")
    parser.add_argument("--models-file", type=str, default=None,
                        help="Path to JSON with {\"models\": [...]} array")
    parser.add_argument("--top", type=int, default=10,
                        help="Number of largest non-English skills to test")
    args = parser.parse_args()

    models = load_models(args)

    print(f"🔍 Scanning for the top {args.top} largest non-English skills...")
    top_skills = find_top_non_english_skills(args.top)

    if not top_skills:
        print("No non-English skills found.")
        return

    print(f"\n📋 Translation targets ({len(top_skills)} skills):")
    for s in top_skills:
        print(f"  - {s['rel_path']} ({s['cjk_chars']} CJK, {s['size']} bytes)")

    print(f"\n🤖 Models ({len(models)}): {', '.join(models)}")

    # Per-model stats: only pure eval time (no model loading)
    results = {}
    for model in models:
        results[model] = {
            "success": 0, "fail": 0,
            "eval_seconds": 0.0,   # pure inference time from Ollama
            "eval_tokens": 0,      # output tokens
            "prompt_tokens": 0,    # input tokens
        }

    for model in models:
        print(f"\n{'='*60}")
        print(f"🚀 MODEL: {model}")
        print(f"{'='*60}")

        # Warmup: load model into VRAM once, don't count it
        preload_model(model)

        sanitized = sanitize_model_name(model)

        for i, skill in enumerate(top_skills):
            path = Path(skill["path"])
            rel = skill["rel_path"]

            print(f"\n  [{i+1}/{len(top_skills)}] {rel} ({skill['cjk_chars']} CJK)")

            try:
                text = path.read_text(encoding="utf-8")

                # Send the WHOLE file in one shot (no chunking = no extra model swaps)
                result, eval_secs, eval_toks, prompt_toks = call_ollama(model, text)

                if result.startswith("HTTP ") or result.startswith("Error:"):
                    print(f"  ❌ {result[:120]}")
                    results[model]["fail"] += 1
                    continue

                # Quality check
                new_cjk = len(CJK_PATTERN.findall(result))
                orig_cjk = skill["cjk_chars"]
                tps = eval_toks / eval_secs if eval_secs > 0 else 0

                # Save file
                out_path = path.parent / f"SKILL-{sanitized}.md"
                out_path.write_text(result + "\n", encoding="utf-8")

                print(f"  ✅ {out_path.name} | CJK: {orig_cjk}→{new_cjk}")
                print(f"     ⏱️ eval: {eval_secs:.1f}s | {eval_toks} tok out | {tps:.0f} tok/s")

                results[model]["success"] += 1
                results[model]["eval_seconds"] += eval_secs
                results[model]["eval_tokens"] += eval_toks
                results[model]["prompt_tokens"] += prompt_toks

            except Exception as e:
                print(f"  ❌ Exception: {e}")
                results[model]["fail"] += 1

    # -----------------------------------------------------------------------
    # Summary report
    # -----------------------------------------------------------------------
    print(f"\n{'='*70}")
    print("📈 COMPARISON SUMMARY (pure inference time, no model load)")
    print(f"{'='*70}")

    report = [
        "# Ollama Model Comparison – Translation Tasks",
        "",
        f"- **Date**: {datetime.now().isoformat()}",
        f"- **Skills tested**: {len(top_skills)}",
        "",
        "## Results",
        "",
        "| Model | OK | Fail | Eval Time | Output Tok | Avg TPS |",
        "|-------|----|------|-----------|------------|---------|",
    ]

    for model, r in results.items():
        suc = r["success"]
        fail = r["fail"]
        ev = r["eval_seconds"]
        tok = r["eval_tokens"]
        tps = tok / ev if ev > 0 else 0

        line = f"| `{model}` | {suc} | {fail} | {ev:.0f}s | {tok} | {tps:.0f} tok/s |"
        report.append(line)

        print(f"  {model}: {suc} ok, {fail} fail, {ev:.0f}s eval, {tps:.0f} tok/s")

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"\n💾 Report: {REPORT_FILE}")


if __name__ == "__main__":
    main()
