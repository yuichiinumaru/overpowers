#!/usr/bin/env python3
"""
Prune duplicate/translated skills identified by the similarity detector.

Reads similar-skills-data.json, applies a heuristic to decide which skill
in each high-similarity pair to archive, then moves the duplicates to
.archive/pruned-skills/.

Usage:
    python3 scripts/prune-duplicate-skills.py              # dry-run (default)
    python3 scripts/prune-duplicate-skills.py --execute     # actually move files
"""

import json
import os
import shutil
import sys
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = BASE_DIR / "skills"
ARCHIVE_DIR = BASE_DIR / ".archive" / "pruned-skills"
DATA_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "similar-skills-data.json"
TASKS_DIR = BASE_DIR / ".docs" / "tasks"
REPORT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "prune-report.md"

SIMILARITY_THRESHOLD = 0.80


def load_similarity_data():
    """Load the similarity detector output."""
    with open(DATA_FILE) as f:
        return json.load(f)


def identify_files_to_archive(data):
    """Apply heuristic to decide which file in each pair to archive."""
    pairs = data["similar_pairs"]
    high = [p for p in pairs if p.get("similarity", 0) >= SIMILARITY_THRESHOLD]

    to_archive = set()
    reasons = {}

    for p in high:
        s1, s2 = p["skill1_path"], p["skill2_path"]
        sim = p["similarity"]

        # Skip if one is already marked for archival
        if s1 in to_archive and s2 in to_archive:
            continue

        chosen = None
        reason = ""

        # 1. Rules subfolder duplicates — archive the rules/ copy
        if "/rules/" in s2 and "/rules/" not in s1:
            chosen, reason = s2, f"rules/ subfolder copy of {s1} (sim={sim:.0%})"
        elif "/rules/" in s1 and "/rules/" not in s2:
            chosen, reason = s1, f"rules/ subfolder copy of {s2} (sim={sim:.0%})"

        # 2. Language-specific suffixes (_EN, _CN, _ZH, etc.)
        elif any(suf in s2.upper() for suf in ["_EN.", "_CN.", "_ZH.", "_JA.", "_RU.", "_KO."]):
            chosen, reason = s2, f"language variant of {s1} (sim={sim:.0%})"
        elif any(suf in s1.upper() for suf in ["_EN.", "_CN.", "_ZH.", "_JA.", "_RU.", "_KO."]):
            chosen, reason = s1, f"language variant of {s2} (sim={sim:.0%})"

        # 3. CJK-named skills — archive in favor of English version
        elif any("\u4e00" <= c <= "\u9fff" for c in s2):
            chosen, reason = s2, f"CJK duplicate of {s1} (sim={sim:.0%})"
        elif any("\u4e00" <= c <= "\u9fff" for c in s1):
            chosen, reason = s1, f"CJK duplicate of {s2} (sim={sim:.0%})"

        # 4. Both English — archive the longer path (more nested = likely fragment)
        else:
            if len(s2) >= len(s1):
                chosen, reason = s2, f"longer-path duplicate of {s1} (sim={sim:.0%})"
            else:
                chosen, reason = s1, f"longer-path duplicate of {s2} (sim={sim:.0%})"

        if chosen and chosen not in to_archive:
            to_archive.add(chosen)
            reasons[chosen] = reason

    return to_archive, reasons


def get_skill_dirs_to_archive(files_to_archive):
    """Determine which entire skill directories can be archived."""
    # Group files by their skill directory (skills/<name>/)
    dir_files = defaultdict(set)
    for f in files_to_archive:
        parts = f.split("/")
        if len(parts) >= 2 and parts[0] == "skills":
            skill_dir = f"{parts[0]}/{parts[1]}"
            dir_files[skill_dir].add(f)

    # Check which skill dirs have ALL their files marked for archival
    full_dirs = set()
    partial_dirs = defaultdict(set)

    for skill_dir, marked_files in dir_files.items():
        abs_dir = BASE_DIR / skill_dir
        if abs_dir.is_dir():
            # Count all .md files in this skill dir
            all_md = set()
            for root, _, files in os.walk(abs_dir):
                for fname in files:
                    if fname.endswith(".md"):
                        rel = os.path.relpath(os.path.join(root, fname), BASE_DIR)
                        all_md.add(rel)

            if all_md and marked_files >= all_md:
                full_dirs.add(skill_dir)
            else:
                partial_dirs[skill_dir] = marked_files

    return full_dirs, partial_dirs


def move_to_archive(files_to_archive, full_dirs, partial_dirs, dry_run=True):
    """Move files/directories to .archive/."""
    moved_count = 0
    errors = []

    if not dry_run:
        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Move entire directories
    for skill_dir in sorted(full_dirs):
        src = BASE_DIR / skill_dir
        dst = ARCHIVE_DIR / skill_dir
        if dry_run:
            print(f"  [DIR]  {skill_dir}/ → .archive/pruned-skills/{skill_dir}/")
            moved_count += 1
        else:
            try:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dst))
                print(f"  ✅ [DIR] {skill_dir}/")
                moved_count += 1
            except Exception as e:
                errors.append(f"DIR {skill_dir}: {e}")
                print(f"  ❌ [DIR] {skill_dir}: {e}")

    # Move individual files from partial dirs
    for skill_dir, files in sorted(partial_dirs.items()):
        for f in sorted(files):
            src = BASE_DIR / f
            dst = ARCHIVE_DIR / f
            if dry_run:
                print(f"  [FILE] {f} → .archive/pruned-skills/{f}")
                moved_count += 1
            else:
                try:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src), str(dst))
                    print(f"  ✅ [FILE] {f}")
                    moved_count += 1
                except Exception as e:
                    errors.append(f"FILE {f}: {e}")
                    print(f"  ❌ [FILE] {f}: {e}")

    return moved_count, errors


def clean_batch_tasks(files_to_archive, full_dirs, dry_run=True):
    """Remove references to archived skills from batch task files."""
    # Build set of skill directory names that were fully archived
    archived_dir_names = {d.split("/")[1] for d in full_dirs if "/" in d}

    # Build set of individual files that were archived
    archived_files = set(files_to_archive)

    batch_files = sorted(TASKS_DIR.glob("0500-extraction-skills-batch-*.md"))
    modified_count = 0
    emptied = []

    for bf in batch_files:
        content = bf.read_text()
        lines = content.split("\n")
        new_lines = []
        removed = 0

        for line in lines:
            skip = False
            # Check if line references an archived skill directory or file
            for ad in archived_dir_names:
                if f"skills/{ad}" in line:
                    skip = True
                    break
            if not skip:
                for af in archived_files:
                    if af in line:
                        skip = True
                        break
            if skip:
                removed += 1
            else:
                new_lines.append(line)

        if removed > 0:
            modified_count += 1
            new_content = "\n".join(new_lines)
            # Check if batch is now effectively empty (no skill references)
            has_skills = any("skills/" in l for l in new_lines)

            if dry_run:
                status = "EMPTY → archive" if not has_skills else f"-{removed} lines"
                print(f"  [BATCH] {bf.name}: {status}")
                if not has_skills:
                    emptied.append(bf.name)
            else:
                if not has_skills:
                    # Move empty batch to archive
                    archive_batch = ARCHIVE_DIR / "emptied-batches" / bf.name
                    archive_batch.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(bf), str(archive_batch))
                    print(f"  ✅ [BATCH] {bf.name}: emptied → archived")
                    emptied.append(bf.name)
                else:
                    bf.write_text(new_content)
                    print(f"  ✅ [BATCH] {bf.name}: removed {removed} lines")

    return modified_count, emptied


def generate_report(files_to_archive, reasons, full_dirs, partial_dirs,
                    moved_count, batch_modified, emptied_batches, dry_run):
    """Generate a markdown report of the pruning operation."""
    lines = [
        "# Skill Pruning Report",
        "",
        f"**Date**: 2026-03-16",
        f"**Mode**: {'DRY RUN' if dry_run else 'EXECUTED'}",
        f"**Similarity threshold**: {SIMILARITY_THRESHOLD:.0%}",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Files identified for archival | {len(files_to_archive)} |",
        f"| Full directories archived | {len(full_dirs)} |",
        f"| Partial directories (files only) | {len(partial_dirs)} |",
        f"| Items moved | {moved_count} |",
        f"| Batch tasks modified | {batch_modified} |",
        f"| Batch tasks emptied | {len(emptied_batches)} |",
        "",
        "## Archived Directories (full)",
        "",
    ]

    for d in sorted(full_dirs):
        lines.append(f"- `{d}/`")

    lines.extend(["", "## Archived Files (partial)", ""])

    for d, files in sorted(partial_dirs.items()):
        lines.append(f"### `{d}/`")
        for f in sorted(files):
            reason = reasons.get(f, "")
            lines.append(f"- `{f}` — {reason}")
        lines.append("")

    if emptied_batches:
        lines.extend(["## Emptied Batch Tasks", ""])
        for b in emptied_batches:
            lines.append(f"- `{b}`")

    content = "\n".join(lines) + "\n"

    if not dry_run:
        REPORT_FILE.write_text(content)
        print(f"\n📝 Report saved to {REPORT_FILE.relative_to(BASE_DIR)}")

    return content


def main():
    dry_run = "--execute" not in sys.argv

    mode = "DRY RUN" if dry_run else "EXECUTING"
    print(f"🗑️  Skill Pruning Tool — {mode}")
    print("=" * 60)

    # Load data
    print("\n📂 Loading similarity data...")
    data = load_similarity_data()

    # Identify what to archive
    print("🔍 Identifying duplicates...")
    files_to_archive, reasons = identify_files_to_archive(data)
    print(f"   Found {len(files_to_archive)} files to archive")

    # Determine full vs partial dir archival
    full_dirs, partial_dirs = get_skill_dirs_to_archive(files_to_archive)
    print(f"   Full directories: {len(full_dirs)}")
    print(f"   Partial directories: {len(partial_dirs)}")

    # Move files
    print(f"\n📦 {'Would move' if dry_run else 'Moving'} files to .archive/pruned-skills/...")
    moved, errors = move_to_archive(files_to_archive, full_dirs, partial_dirs, dry_run)

    # Clean batch tasks
    print(f"\n🧹 {'Would clean' if dry_run else 'Cleaning'} batch task files...")
    batch_modified, emptied = clean_batch_tasks(files_to_archive, full_dirs, dry_run)

    # Generate report
    print(f"\n📊 Generating report...")
    generate_report(files_to_archive, reasons, full_dirs, partial_dirs,
                    moved, batch_modified, emptied, dry_run)

    # Summary
    print(f"\n{'=' * 60}")
    print(f"📊 SUMMARY ({mode}):")
    print(f"   Files to archive: {len(files_to_archive)}")
    print(f"   Full dirs: {len(full_dirs)}")
    print(f"   Partial dirs: {len(partial_dirs)}")
    print(f"   Items {'would be' if dry_run else ''} moved: {moved}")
    print(f"   Batch tasks {'would be' if dry_run else ''} modified: {batch_modified}")
    print(f"   Batch tasks {'would be' if dry_run else ''} emptied: {len(emptied)}")

    if errors:
        print(f"\n⚠️  Errors: {len(errors)}")
        for e in errors:
            print(f"   {e}")

    if dry_run:
        print(f"\n💡 To execute, run: python3 {sys.argv[0]} --execute")

    print("=" * 60)


if __name__ == "__main__":
    main()
