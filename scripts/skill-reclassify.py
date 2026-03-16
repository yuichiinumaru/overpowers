#!/usr/bin/env python3
"""
Skill Reclassification Script
Reads skills, computes embeddings, assigns each to the best-fit type/subtype
from skill-taxonomy.json, and outputs a reclassification plan.

Usage:
  python3 scripts/skill-reclassify.py [--sample N] [--threshold 0.3]
"""

import json
import os
import sys
import re
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = BASE_DIR / "skills"
TAXONOMY_FILE = SCRIPT_DIR / "skill-taxonomy.json"
OUTPUT_PLAN = BASE_DIR / ".docs" / "tasks" / "planning" / "skill-reclassification-plan.json"
OUTPUT_REPORT = BASE_DIR / ".docs" / "tasks" / "planning" / "skill-reclassification-report.md"


def load_taxonomy():
    """Load taxonomy definitions."""
    with open(TAXONOMY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def extract_skill_text(skill_dir: Path) -> dict:
    """Extract description and content from a skill's SKILL.md."""
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return None

    try:
        content = skill_file.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    # Parse YAML frontmatter
    name = ""
    description = ""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            for line in frontmatter.splitlines():
                if line.strip().startswith("name:"):
                    name = line.split(":", 1)[1].strip().strip('"').strip("'")
                elif line.strip().startswith("description:"):
                    description = line.split(":", 1)[1].strip().strip('"').strip("'")

    # Get first 500 chars of body for context
    body = ""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2][:500]
    else:
        body = content[:500]

    # Clean up
    text = f"{name} {description} {body}".strip()
    if len(text) < 10:
        return None

    return {
        "name": name,
        "description": description,
        "text": text[:512],  # Truncate for embedding
        "dir_name": skill_dir.name,
    }


def clean_skill_name(dir_name: str) -> str:
    """Strip the Qwen-added chunk prefixes and duplicated type-subtype from names.

    Examples:
      ai-llm-chunk01-0031-ai-llm-draft-outreach -> draft-outreach
      agent-orchestration-default-0016-validate-agent -> validate-agent
      content-search-default-0020-douyin-transcribe-skill -> douyin-transcribe-skill
    """
    # Pattern: type-subtype-chunk/default-NNNN-[type-subtype-]name
    # Try to extract the meaningful name after the numeric index
    m = re.match(
        r'^[a-z]+-[a-z]+-(?:chunk\d+|default)-(\d{4})-(?:[a-z]+-[a-z]+-)?(.+)$',
        dir_name
    )
    if m:
        return m.group(2)

    # Orphan names without convention
    return dir_name


def load_model():
    """Load Qwen3-Embedding-0.6B via sentence-transformers."""
    try:
        import torch
        from sentence_transformers import SentenceTransformer

        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"🔧 Loading Qwen3-Embedding-0.6B on {device}...")
        model = SentenceTransformer(
            "Qwen/Qwen3-Embedding-0.6B",
            trust_remote_code=True,
            device=device,
        )
        print(f"✅ Model loaded on {device}")
        return model, device
    except ImportError:
        print("❌ sentence-transformers not installed.")
        print("   Install: pip install sentence-transformers torch")
        sys.exit(1)


def compute_embeddings(model, texts: list, device: str):
    """Compute embeddings in small batches to avoid OOM."""
    import torch

    batch_size = 4 if device == "cuda" else 8
    all_embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        # Truncate to avoid token limit issues
        batch = [t[:512] for t in batch]
        emb = model.encode(batch, convert_to_numpy=True, show_progress_bar=False)
        all_embeddings.extend(emb)

        if device == "cuda" and i % (batch_size * 10) == 0:
            torch.cuda.empty_cache()

    return all_embeddings


def build_type_embeddings(model, taxonomy, device):
    """Create reference embeddings for each type and subtype."""
    import numpy as np

    type_refs = {}
    subtype_refs = {}

    for type_name, type_data in taxonomy["types"].items():
        # Type embedding: description + keywords
        type_text = f"{type_data['description']} {' '.join(type_data['keywords'])}"
        type_refs[type_name] = model.encode(
            [type_text[:512]], convert_to_numpy=True
        )[0]

        # Subtype embeddings
        subtype_refs[type_name] = {}
        for sub_name, sub_desc in type_data["subtypes"].items():
            sub_text = f"{type_data['description']} {sub_desc} {' '.join(type_data['keywords'][:5])}"
            subtype_refs[type_name][sub_name] = model.encode(
                [sub_text[:512]], convert_to_numpy=True
            )[0]

    return type_refs, subtype_refs


def classify_skill(skill_emb, type_refs, subtype_refs):
    """Find best matching type and subtype for a skill embedding."""
    import numpy as np

    # Score against each type
    type_scores = {}
    for type_name, type_emb in type_refs.items():
        sim = np.dot(skill_emb, type_emb) / (
            np.linalg.norm(skill_emb) * np.linalg.norm(type_emb) + 1e-8
        )
        type_scores[type_name] = float(sim)

    # Top type
    best_type = max(type_scores, key=type_scores.get)
    best_type_score = type_scores[best_type]

    # Score against subtypes of best type
    subtype_scores = {}
    for sub_name, sub_emb in subtype_refs[best_type].items():
        sim = np.dot(skill_emb, sub_emb) / (
            np.linalg.norm(skill_emb) * np.linalg.norm(sub_emb) + 1e-8
        )
        subtype_scores[sub_name] = float(sim)

    best_subtype = max(subtype_scores, key=subtype_scores.get)
    best_subtype_score = subtype_scores[best_subtype]

    return {
        "type": best_type,
        "type_score": best_type_score,
        "subtype": best_subtype,
        "subtype_score": best_subtype_score,
        "type_scores_top3": dict(
            sorted(type_scores.items(), key=lambda x: -x[1])[:3]
        ),
    }


def validate_constraints(plan, taxonomy):
    """Check floor/ceil constraints and report violations."""
    constraints = taxonomy["_meta"]["constraints"]
    type_counts = defaultdict(int)
    subtype_counts = defaultdict(lambda: defaultdict(int))

    for entry in plan.values():
        type_counts[entry["type"]] += 1
        subtype_counts[entry["type"]][entry["subtype"]] += 1

    violations = []

    for type_name, count in type_counts.items():
        if count < constraints["min_skills_per_type"]:
            violations.append(
                f"⚠️  Type '{type_name}': {count} skills (below min {constraints['min_skills_per_type']})"
            )
        if count > constraints["max_skills_per_type"]:
            violations.append(
                f"❌ Type '{type_name}': {count} skills (above max {constraints['max_skills_per_type']})"
            )

    for type_name, subs in subtype_counts.items():
        if len(subs) > constraints["max_subtypes_per_type"]:
            violations.append(
                f"❌ Type '{type_name}': {len(subs)} subtypes (above max {constraints['max_subtypes_per_type']})"
            )
        for sub_name, count in subs.items():
            if count > constraints["max_skills_per_subtype"]:
                violations.append(
                    f"⚠️  Subtype '{type_name}/{sub_name}': {count} skills (above max {constraints['max_skills_per_subtype']})"
                )

    return violations, dict(type_counts), {
        k: dict(v) for k, v in subtype_counts.items()
    }


def generate_report(plan, violations, type_counts, subtype_counts, taxonomy):
    """Generate a markdown report."""
    lines = [
        "# Skill Reclassification Report",
        "",
        f"**Total skills classified**: {len(plan)}",
        f"**Types used**: {len(type_counts)}",
        f"**Constraint violations**: {len(violations)}",
        "",
        "## Type Distribution",
        "",
        "| Type | Count | % |",
        "|---|---|---|",
    ]

    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        pct = c / len(plan) * 100
        lines.append(f"| {t} | {c} | {pct:.1f}% |")

    lines.extend(["", "## Subtype Distribution", ""])

    for t in sorted(subtype_counts.keys()):
        lines.append(f"### {t}")
        lines.append("")
        lines.append("| Subtype | Count |")
        lines.append("|---|---|")
        for s, c in sorted(subtype_counts[t].items(), key=lambda x: -x[1]):
            lines.append(f"| {s} | {c} |")
        lines.append("")

    if violations:
        lines.extend(["## ⚠️ Constraint Violations", ""])
        for v in violations:
            lines.append(f"- {v}")
        lines.append("")

    lines.extend([
        "## Low-Confidence Classifications (< 0.4)",
        "",
        "| Skill | Assigned Type | Score |",
        "|---|---|---|",
    ])

    for name, entry in sorted(plan.items(), key=lambda x: x[1]["type_score"]):
        if entry["type_score"] < 0.4:
            lines.append(
                f"| {entry['clean_name']} | {entry['type']}/{entry['subtype']} | {entry['type_score']:.3f} |"
            )

    return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Reclassify skills using embeddings")
    parser.add_argument("--sample", type=int, default=0, help="Process only N random skills (0=all)")
    parser.add_argument("--threshold", type=float, default=0.3, help="Minimum confidence threshold")
    args = parser.parse_args()

    print("🔍 Skill Reclassification Tool v2.0")
    print("=" * 60)

    # Load taxonomy
    taxonomy = load_taxonomy()
    print(f"📋 Loaded taxonomy: {len(taxonomy['types'])} types")

    # Scan skills
    print(f"📂 Scanning {SKILLS_DIR}...")
    skill_dirs = sorted([d for d in SKILLS_DIR.iterdir() if d.is_dir()])

    if args.sample > 0:
        import random
        random.shuffle(skill_dirs)
        skill_dirs = skill_dirs[: args.sample]
        print(f"   (sampling {args.sample} skills)")

    # Extract skill texts
    skills = {}
    for d in skill_dirs:
        info = extract_skill_text(d)
        if info:
            skills[d.name] = info

    print(f"✅ Found {len(skills)} skills with content")

    # Load model
    model, device = load_model()

    # Build type reference embeddings
    print("📊 Computing type reference embeddings...")
    type_refs, subtype_refs = build_type_embeddings(model, taxonomy, device)

    # Compute skill embeddings
    print(f"🔮 Computing embeddings for {len(skills)} skills...")
    skill_names = list(skills.keys())
    skill_texts = [skills[n]["text"] for n in skill_names]
    skill_embeddings = compute_embeddings(model, skill_texts, device)

    # Classify each skill
    print("🏷️  Classifying skills...")
    plan = {}
    for i, name in enumerate(skill_names):
        result = classify_skill(skill_embeddings[i], type_refs, subtype_refs)
        clean = clean_skill_name(name)
        plan[name] = {
            "current_path": f"skills/{name}",
            "new_path": f"skills/{result['type']}/{result['subtype']}/{clean}",
            "type": result["type"],
            "subtype": result["subtype"],
            "type_score": result["type_score"],
            "subtype_score": result["subtype_score"],
            "clean_name": clean,
            "original_description": skills[name].get("description", ""),
        }

        if (i + 1) % 500 == 0:
            print(f"   ... {i + 1}/{len(skill_names)}")

    print(f"✅ Classified {len(plan)} skills")

    # Validate constraints
    print("🔍 Validating constraints...")
    violations, type_counts, subtype_counts = validate_constraints(plan, taxonomy)

    if violations:
        print(f"⚠️  {len(violations)} constraint violations found")
        for v in violations[:5]:
            print(f"   {v}")
    else:
        print("✅ All constraints satisfied")

    # Save plan
    OUTPUT_PLAN.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PLAN, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
    print(f"💾 Plan saved to: {OUTPUT_PLAN}")

    # Generate and save report
    report = generate_report(plan, violations, type_counts, subtype_counts, taxonomy)
    with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"📊 Report saved to: {OUTPUT_REPORT}")

    # Summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        bar = "█" * (c // 20)
        print(f"  {t:12s} {c:4d} {bar}")


if __name__ == "__main__":
    main()
