#!/usr/bin/env python3
"""
Audit and fix arXiv markdown downloads for quality issues.

Usage:
    python3 audit-fix.py --dir <arxiv-markdown-dir> [--fix] [--report <path>]

Detects:
  - FATAL_CONVERSION_ERROR: ar5iv failed to convert LaTeX to HTML
  - NO_TITLE: title not extracted from markdown
  - TINY_FILE: <1KB (only boilerplate, no real content)
  - VERY_SMALL_FILE: 1-2KB
  - SMALL_FILE: 2-5KB
  - LUATEX_GARBAGE: raw LuaTeX code instead of paper content
  - HIGH_LATEX_NOISE: excessive LaTeX inline commands
  - TRUNCATED_WARNING: ar5iv truncation warning present
  - NO_REAL_CONTENT: fewer than 5 real content lines

With --fix, automatically:
  - Re-extracts titles for NO_TITLE files
  - Cleans boilerplate navigation from markdown
"""

import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path


SKIP_TITLE_PATTERNS = [
    'quick links', 'skip', 'navigate', 'computer science',
    'mathematics', 'physics', 'statistics', 'electrical',
    'quantitative', 'economics', 'submission history',
    'acknowledgements', 'references', 'abstract',
]


def extract_title_deep(content: str) -> str:
    """Extract paper title using multiple strategies."""
    lines = content.split('\n')

    # Strategy 1: YAML frontmatter title (if already set and valid)
    fm_match = re.search(r"title:\s*'(.+?)'", content[:500])
    if fm_match and fm_match.group(1) != "Unknown":
        return fm_match.group(1)

    # Strategy 2: '# Title:...' pattern (arxiv abstract page format)
    for line in lines[:100]:
        m = re.match(r'^#\s+Title:\s*(.+)', line.strip())
        if m:
            return m.group(1).strip()

    # Strategy 3: First '# ' heading that is NOT navigation/category
    for line in lines[:100]:
        l = line.strip()
        if l.startswith('# ') and len(l) > 8:
            title_text = l[2:].strip()
            if not any(p in title_text.lower() for p in SKIP_TITLE_PATTERNS):
                if not re.match(r'^Computer Science', title_text):
                    return title_text

    # Strategy 4: First '## ' heading that looks like a real title
    for line in lines[5:80]:
        l = line.strip()
        if l.startswith('## ') and len(l) > 12:
            title_text = l[3:].strip()
            if not any(p in title_text.lower() for p in SKIP_TITLE_PATTERNS):
                return title_text

    # Strategy 5: First bold text that looks like a title
    for line in lines[5:60]:
        m = re.match(r'^\*\*(.{10,120})\*\*$', line.strip())
        if m:
            return m.group(1).strip()

    return "Unknown"


def audit_file(filepath: str) -> dict:
    """Audit a single markdown file for quality issues."""
    issues = []
    with open(filepath, 'r', errors='replace') as f:
        content = f.read()

    size = len(content)
    basename = os.path.basename(filepath)
    arxiv_id = basename.replace('.md', '')

    # Extract current title
    fm_match = re.search(r"title:\s*['\"](.+?)['\"]", content[:500])
    current_title = fm_match.group(1) if fm_match else "Unknown"

    # Try to find a better title
    best_title = extract_title_deep(content)

    # Check for fatal conversion error
    has_fatal = "Fatal error" in content or "Conversion to HTML had a Fatal error" in content
    if has_fatal:
        issues.append("FATAL_CONVERSION_ERROR")

    # Title issues
    if current_title == "Unknown":
        issues.append("NO_TITLE")

    # Size checks
    if size < 1000:
        issues.append("TINY_FILE")
    elif size < 2000:
        issues.append("VERY_SMALL_FILE")
    elif size < 5000:
        issues.append("SMALL_FILE")

    # LuaTeX garbage
    if "luatexbase" in content:
        issues.append("LUATEX_GARBAGE")

    # Truncated
    if "This document may be truncated or damaged" in content:
        issues.append("TRUNCATED_WARNING")

    # Real content check
    body = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
    content_lines = [l for l in body.split('\n') if l.strip() and not l.strip().startswith('[') and len(l.strip()) > 20]
    if len(content_lines) < 5:
        issues.append("NO_REAL_CONTENT")

    # LaTeX noise
    word_count = len(content.split())
    latex_patterns = len(re.findall(r'\\(?:textsc|textbf|mathrm|mathbb|frac|begin|end)\{', content))
    if latex_patterns / max(word_count, 1) > 0.05 and size > 5000:
        issues.append("HIGH_LATEX_NOISE")

    has_abstract = bool(re.search(r'(?i)(abstract|##\s*abstract)', content))
    section_count = len(re.findall(r'^#{1,3}\s+\d', content, re.MULTILINE))

    severity = "CRITICAL" if any(i in issues for i in [
        "FATAL_CONVERSION_ERROR", "TINY_FILE", "NO_REAL_CONTENT", "LUATEX_GARBAGE"
    ]) else "WARNING" if issues else "OK"

    return {
        "arxiv_id": arxiv_id,
        "filepath": filepath,
        "current_title": current_title,
        "best_title": best_title,
        "size_bytes": size,
        "issues": issues,
        "has_abstract": has_abstract,
        "section_count": section_count,
        "content_lines": len(content_lines),
        "word_count": word_count,
        "severity": severity,
        "title_fixable": current_title == "Unknown" and best_title != "Unknown",
    }


def fix_title(filepath: str, new_title: str) -> bool:
    """Fix the title in a file's YAML frontmatter."""
    with open(filepath, 'r') as f:
        content = f.read()

    safe_title = new_title.replace("'", "")

    # Replace title in frontmatter
    new_content = re.sub(
        r"(title:\s*')[^']*(')",
        rf"\g<1>{safe_title}\2",
        content,
        count=1
    )

    # Fallback: also handle double-quoted titles
    if new_content == content:
        new_content = re.sub(
            r'(title:\s*")[^"]*(")',
            rf'\g<1>{safe_title}\2',
            content,
            count=1
        )

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Audit and fix arXiv markdown downloads")
    parser.add_argument("--dir", "-d", required=True, help="Directory with arXiv markdown files")
    parser.add_argument("--fix", "-f", action="store_true", help="Automatically fix issues (titles)")
    parser.add_argument("--report", "-r", default=None, help="Path for JSON report output")
    parser.add_argument("--quiet", "-q", action="store_true", help="Only print summary")
    args = parser.parse_args()

    files = sorted(Path(args.dir).glob("*.md"))
    print(f"Auditing {len(files)} files in {args.dir}...")

    results = []
    for f in files:
        results.append(audit_file(str(f)))

    # Categorize
    critical = [r for r in results if r["severity"] == "CRITICAL"]
    warning = [r for r in results if r["severity"] == "WARNING"]
    ok = [r for r in results if r["severity"] == "OK"]

    all_issues = []
    for r in results:
        all_issues.extend(r["issues"])
    issue_counts = Counter(all_issues)

    ok_sizes = [r["size_bytes"] for r in ok]

    print(f"\n{'='*60}")
    print(f"ARXIV DOWNLOAD AUDIT REPORT")
    print(f"{'='*60}")
    print(f"Total files: {len(results)}")
    print(f"  OK:       {len(ok)} ({100*len(ok)//max(len(results),1)}%)")
    print(f"  Warning:  {len(warning)}")
    print(f"  Critical: {len(critical)}")
    print()
    print(f"Issue breakdown:")
    for issue, count in issue_counts.most_common():
        print(f"  {issue}: {count}")

    if ok_sizes:
        print(f"\nOK files: min={min(ok_sizes)//1024}KB, max={max(ok_sizes)//1024}KB, avg={sum(ok_sizes)//len(ok_sizes)//1024}KB, total={sum(ok_sizes)//1024//1024}MB")

    # Fix phase
    if args.fix:
        fixable = [r for r in results if r["title_fixable"]]
        print(f"\n{'='*60}")
        print(f"FIX PHASE: {len(fixable)} titles to fix")
        print(f"{'='*60}")
        fixed = 0
        for r in fixable:
            if fix_title(r["filepath"], r["best_title"]):
                fixed += 1
                if not args.quiet:
                    print(f"  FIXED {r['arxiv_id']}: '{r['best_title'][:70]}'")
        print(f"\nFixed {fixed}/{len(fixable)} titles")

    # Print detailed lists (unless quiet)
    if not args.quiet:
        if critical:
            print(f"\n{'='*60}")
            print(f"CRITICAL ({len(critical)}):")
            print(f"{'='*60}")
            for r in sorted(critical, key=lambda x: x["size_bytes"]):
                print(f"  {r['arxiv_id']:20s} {r['size_bytes']:>8d}B  {','.join(r['issues'])}")

        if warning:
            print(f"\n{'='*60}")
            print(f"WARNING ({len(warning)}):")
            print(f"{'='*60}")
            for r in sorted(warning, key=lambda x: x["size_bytes"]):
                print(f"  {r['arxiv_id']:20s} {r['size_bytes']:>8d}B  {','.join(r['issues'])}")

    # Save report
    report_path = args.report or os.path.join(args.dir, "audit-report.json")
    report = {
        "total_files": len(results),
        "ok_count": len(ok),
        "warning_count": len(warning),
        "critical_count": len(critical),
        "issue_counts": dict(issue_counts),
        "critical_ids": [r["arxiv_id"] for r in critical],
        "warning_ids": [r["arxiv_id"] for r in warning],
    }
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\nReport: {report_path}")

    # Save critical IDs list
    crit_path = os.path.join(args.dir, "critical-ids.txt")
    with open(crit_path, 'w') as f:
        for r in critical:
            f.write(r["arxiv_id"] + "\n")
    print(f"Critical IDs: {crit_path}")


if __name__ == "__main__":
    main()
