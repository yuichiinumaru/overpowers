#!/usr/bin/env python3
"""
Batch Skill Translator using local Qwen3.5-2B model.
Translates non-English SKILL.md files to English, preserving markdown structure.

Usage:
  python3 scripts/skill-translate-local.py --dry-run          # Count & preview
  python3 scripts/skill-translate-local.py --execute           # Full batch run
  python3 scripts/skill-translate-local.py --execute --limit 5 # Test with 5 skills
  python3 scripts/skill-translate-local.py --execute --resume  # Resume from last checkpoint

Environment:
  MODEL_PATH: Override model directory (default: llm-models/Qwen3.5-2B)
  DEVICE: Override device (default: cuda if available, else cpu)
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = BASE_DIR / "skills"
MODEL_DIR = os.environ.get("MODEL_PATH", str(BASE_DIR / "llm-models" / "Qwen3.5-2B"))
CHECKPOINT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "translation-checkpoint.json"
REPORT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "translation-report.md"
BACKUP_DIR = BASE_DIR / ".archive" / "pre-translation-backup"

# CJK Unicode ranges
CJK_PATTERN = re.compile(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]')
CJK_THRESHOLD = 20  # Minimum CJK chars to consider non-English


def find_non_english_skills():
    """Scan for skills with significant CJK content."""
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


def reassemble(frontmatter_yaml, body):
    """Reassemble frontmatter + body."""
    if frontmatter_yaml:
        return f"---\n{frontmatter_yaml}\n---\n\n{body}\n"
    return f"{body}\n"


def build_prompt(text, section="full"):
    """Build translation prompt for the model."""
    return (
        "<|im_start|>system\n"
        "You are a professional translator. /no_think\n"
        "Translate the following content from its original language to English. "
        "Preserve ALL markdown formatting, code blocks, file paths, command examples, YAML structure, and technical terms. "
        "Do NOT translate: variable names, function names, file paths, CLI commands, code inside ```blocks```, URLs, or proper nouns that are technical identifiers. "
        "Translate ONLY the natural language text (descriptions, instructions, comments outside code). "
        "Output ONLY the translated text, no explanations, no thinking, no commentary.\n"
        "<|im_end|>\n"
        "<|im_start|>user\n"
        f"{text}\n"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
    )


def clean_output(text):
    """Remove thinking tokens and prompt artifacts from model output."""
    # Strip <think>...</think> blocks (greedy, handles multiline)
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    # Strip any remaining think tags
    text = re.sub(r'</?think>', '', text).strip()
    # Remove lines that are clearly prompt echo ("Thinking Process:", "Analyze the Request:")
    lines = text.split('\n')
    cleaned = []
    skip = False
    for line in lines:
        stripped = line.strip()
        if any(marker in stripped for marker in [
            'Thinking Process:', 'Analyze the Request:', 'Analyze the Source',
            'Drafting the Translation', 'Drafting Translation',
            '**Role:**', '**Task:**', '**Constraints:**',
            'Output ONLY the translated', 'Professional Translator',
            'Translation:', 'I need to translate',
        ]):
            skip = True
            continue
        # Skip numbered analysis steps (e.g., "1.  **Analyze the Request:**")
        if re.match(r'^\d+\.\s+\*\*', stripped):
            skip = True
            continue
        if skip and (stripped.startswith('*') or stripped.startswith('-') or not stripped):
            continue  # Skip sub-bullets and blanks in skipped section
        skip = False
        cleaned.append(line)
    return '\n'.join(cleaned).strip()


def chunk_text(text, max_chars=1500):
    """Split text into chunks at paragraph boundaries."""
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


class Translator:
    def __init__(self, model_dir, device=None):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM

        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        print(f"🔧 Loading model from {model_dir} on {self.device}...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_dir, trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            model_dir,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map=self.device,
            trust_remote_code=True,
        )
        self.model.eval()
        print(f"✅ Model loaded ({self.device})")

    def translate(self, text, max_new_tokens=2048):
        """Translate a chunk of text."""
        import torch

        # Skip if no CJK content
        if len(CJK_PATTERN.findall(text)) < 5:
            return text

        prompt = build_prompt(text)
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048)
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}

        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=0.3,
                top_p=0.9,
                repetition_penalty=1.1,
                pad_token_id=self.tokenizer.eos_token_id,
            )

        # Decode only the generated part
        generated = output[0][inputs["input_ids"].shape[1]:]
        result = self.tokenizer.decode(generated, skip_special_tokens=True).strip()

        # Clean thinking artifacts
        result = clean_output(result)

        # Basic sanity: if result is empty or way too short, return original
        if len(result) < len(text) * 0.2:
            return text

        return result

    def translate_skill(self, skill_path):
        """Translate a full SKILL.md file."""
        text = Path(skill_path).read_text(encoding="utf-8")
        frontmatter, body = split_frontmatter(text)

        # Translate frontmatter description if it has CJK
        translated_fm = frontmatter
        if frontmatter and len(CJK_PATTERN.findall(frontmatter)) > 5:
            translated_fm = self.translate(frontmatter, max_new_tokens=512)

        # Translate body in chunks
        chunks = chunk_text(body)
        translated_chunks = []
        for chunk in chunks:
            translated = self.translate(chunk)
            translated_chunks.append(translated)

        translated_body = "\n\n".join(translated_chunks)
        return reassemble(translated_fm, translated_body)


def load_checkpoint():
    """Load translation progress."""
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE) as f:
            return json.load(f)
    return {"completed": [], "failed": [], "skipped": []}


def save_checkpoint(data):
    """Save translation progress."""
    CHECKPOINT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(data, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Batch translate skills with local LLM")
    parser.add_argument("--dry-run", action="store_true", help="Count and preview only")
    parser.add_argument("--execute", action="store_true", help="Actually translate")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of skills")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--device", type=str, default=None, help="Device: cuda or cpu")
    args = parser.parse_args()

    if not args.dry_run and not args.execute:
        print("Error: specify --dry-run or --execute")
        sys.exit(1)

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

        total_bytes = sum(s["size"] for s in skills)
        print(f"\nTotal: {len(skills)} files, {total_bytes/1024/1024:.1f} MB")
        est_time = len(skills) * 15  # ~15 sec per skill estimate for 2B
        print(f"Estimated time (2B model): ~{est_time//3600}h {(est_time%3600)//60}m")
        return

    # Load checkpoint for resume
    checkpoint = load_checkpoint() if args.resume else {"completed": [], "failed": [], "skipped": []}
    completed_paths = set(checkpoint["completed"])

    # Filter already-done
    if args.resume:
        skills = [s for s in skills if s["rel_path"] not in completed_paths]
        print(f"⏩ Resuming: {len(completed_paths)} already done, {len(skills)} remaining")

    if args.limit > 0:
        skills = skills[:args.limit]
        print(f"🔒 Limited to {args.limit} skills")

    # Load model
    translator = Translator(MODEL_DIR, device=args.device)

    # Ensure backup dir
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    # Translate
    start_time = time.time()
    success = 0
    fail = 0

    for i, skill in enumerate(skills):
        path = Path(skill["path"])
        rel = skill["rel_path"]
        elapsed = time.time() - start_time
        rate = (i / elapsed * 3600) if elapsed > 0 and i > 0 else 0

        print(f"\n[{i+1}/{len(skills)}] {rel} ({skill['cjk_chars']} CJK) "
              f"[{rate:.0f}/hr]")

        try:
            # Backup original
            backup_path = BACKUP_DIR / rel
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            import shutil
            shutil.copy2(str(path), str(backup_path))

            # Translate
            translated = translator.translate_skill(str(path))

            # Sanity check: translated should have fewer CJK chars
            orig_cjk = skill["cjk_chars"]
            new_cjk = len(CJK_PATTERN.findall(translated))

            if new_cjk < orig_cjk * 0.5:
                path.write_text(translated, encoding="utf-8")
                print(f"  ✅ CJK: {orig_cjk} → {new_cjk}")
                success += 1
                checkpoint["completed"].append(rel)
            else:
                print(f"  ⚠️  Translation quality low (CJK: {orig_cjk} → {new_cjk}), skipping")
                checkpoint["skipped"].append(rel)

        except Exception as e:
            print(f"  ❌ Error: {e}")
            checkpoint["failed"].append(rel)
            fail += 1

        # Checkpoint every 10 skills
        if (i + 1) % 10 == 0:
            save_checkpoint(checkpoint)
            print(f"  💾 Checkpoint saved ({len(checkpoint['completed'])} done)")

    # Final save
    save_checkpoint(checkpoint)

    # Summary
    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"✅ Completed: {success}")
    print(f"⚠️  Skipped (low quality): {len(checkpoint['skipped'])}")
    print(f"❌ Failed: {fail}")
    print(f"⏱️  Time: {elapsed/60:.1f} min ({elapsed/max(success,1):.1f} sec/skill)")

    # Generate report
    report = [
        f"# Translation Report",
        f"",
        f"- **Date**: {datetime.now().isoformat()}",
        f"- **Model**: Qwen3.5-2B",
        f"- **Translated**: {success}",
        f"- **Skipped**: {len(checkpoint['skipped'])}",
        f"- **Failed**: {fail}",
        f"- **Time**: {elapsed/60:.1f} min",
        f"- **Rate**: {success/max(elapsed/3600,0.01):.0f} skills/hr",
    ]
    REPORT_FILE.write_text("\n".join(report), encoding="utf-8")
    print(f"\n💾 Report: {REPORT_FILE}")


if __name__ == "__main__":
    main()
