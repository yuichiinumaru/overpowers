#!/usr/bin/env python3
"""
Skill Restructuring Executor
Reads the reclassification plan and physically moves skill directories
into the new type/subtype/name hierarchy.

Usage:
  python3 scripts/skill-restructure-execute.py --dry-run   (preview only)
  python3 scripts/skill-restructure-execute.py --execute    (actually move)
"""

import json
import os
import shutil
import sys
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = BASE_DIR / "skills"
PLAN_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "skill-reclassification-plan.json"
REPORT_FILE = BASE_DIR / ".docs" / "tasks" / "planning" / "skill-restructure-result.md"


def load_plan():
    """Load the reclassification plan."""
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def execute_restructure(plan, dry_run=True):
    """Move skill directories into new hierarchy."""
    moved = 0
    skipped = 0
    errors = []
    type_counts: dict[str, int] = defaultdict(int)
    subtype_counts: dict[str, dict[str, int]] = {}

    for old_name, entry in sorted(plan.items()):
        old_path = BASE_DIR / entry["current_path"]
        new_dir = SKILLS_DIR / entry["type"] / entry["subtype"]
        new_path = new_dir / entry["clean_name"]

        if not old_path.exists():
            skipped += 1
            continue

        # Handle name collision
        if new_path.exists():
            # Append a suffix
            suffix = 1
            while new_path.exists():
                new_path = new_dir / f"{entry['clean_name']}-{suffix}"
                suffix += 1

        if dry_run:
            print(f"  {old_path.relative_to(BASE_DIR)} → {new_path.relative_to(BASE_DIR)}")
        else:
            new_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(old_path), str(new_path))

        moved += 1
        type_counts[entry["type"]] += 1
        if entry["type"] not in subtype_counts:
            subtype_counts[entry["type"]] = defaultdict(int)
        subtype_counts[entry["type"]][entry["subtype"]] += 1

    return moved, skipped, errors, dict(type_counts), {
        k: dict(v) for k, v in subtype_counts.items()
    }


def generate_report(moved, skipped, errors, type_counts, subtype_counts, dry_run):
    """Generate restructuring report."""
    mode = "DRY RUN" if dry_run else "EXECUTED"
    lines = [
        f"# Skill Restructuring Report ({mode})",
        "",
        f"- **Moved**: {moved}",
        f"- **Skipped (not found)**: {skipped}",
        f"- **Errors**: {len(errors)}",
        "",
        "## Type Distribution After Move",
        "",
        "| Type | Count |",
        "|---|---|",
    ]
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {t} | {c} |")

    if errors:
        lines.extend(["", "## Errors", ""])
        for e in errors:
            lines.append(f"- {e}")

    return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Execute skill restructuring")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving")
    parser.add_argument("--execute", action="store_true", help="Actually move files")
    args = parser.parse_args()

    if not args.dry_run and not args.execute:
        print("Error: specify --dry-run or --execute")
        sys.exit(1)

    dry_run = args.dry_run

    print(f"🔧 Skill Restructuring {'(DRY RUN)' if dry_run else '(EXECUTE)'}")
    print("=" * 60)

    # Load plan
    plan = load_plan()
    print(f"📋 Loaded plan with {len(plan)} entries")

    # Execute
    print(f"\n{'📋 Preview:' if dry_run else '🚀 Moving skills...'}")
    moved, skipped, errors, type_counts, subtype_counts = execute_restructure(
        plan, dry_run
    )

    # Summary
    print(f"\n{'=' * 60}")
    print(f"✅ {'Would move' if dry_run else 'Moved'}: {moved}")
    print(f"⏭️  Skipped: {skipped}")
    if errors:
        print(f"❌ Errors: {len(errors)}")

    print("\n📊 Distribution:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        bar = "█" * (c // 20)
        print(f"  {t:12s} {c:4d} {bar}")

    # Generate report
    report = generate_report(moved, skipped, errors, type_counts, subtype_counts, dry_run)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n💾 Report saved to: {REPORT_FILE}")

    if dry_run:
        print("\n💡 Run with --execute to actually move the files")


if __name__ == "__main__":
    main()
