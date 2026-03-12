#!/usr/bin/env python3
"""
GEO Fundamentals - Audit Checker
Analyzes content files for Generative Engine Optimization readiness.
"""
import os
import sys
import re

def check_file(filepath):
    """Audits a single markdown or text file for GEO elements."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    score = 0
    max_score = 6
    feedback = []

    # 1. Question-based titles (H1/H2 starting with How, What, Why, etc.)
    if re.search(r'^#+\s+(How|What|Why|When|Where|Who|Is|Are|Do|Does|Can)\s', content, re.IGNORECASE | re.MULTILINE):
        score += 1
        feedback.append("✅ Question-based headings found")
    else:
        feedback.append("❌ Missing question-based headings (How/What/Why/etc)")

    # 2. Summary / TL;DR
    if re.search(r'(?i)\b(TL;DR|Summary|Key Takeaways|Briefly)\b', content[:1000]):
        score += 1
        feedback.append("✅ Summary/TL;DR found near the top")
    else:
        feedback.append("❌ Missing Summary/TL;DR near the top")

    # 3. Statistics / Data markers (%, numbers with "according to", "study", "research")
    if re.search(r'\b\d+%\b|\b(study|research|according to|data shows)\b', content, re.IGNORECASE):
        score += 1
        feedback.append("✅ Statistical/Data markers found")
    else:
        feedback.append("❌ Low density of statistics or data markers")

    # 4. Expert Quotes
    if re.search(r'"[^"]+"(?:[^"]+?)(said|stated|according to|says)(?:\s+[A-Z][a-z]+)+', content) or 'blockquote' in content.lower() or '>' in content:
        score += 1
        feedback.append("✅ Potential expert quotes/citations found")
    else:
        feedback.append("❌ Missing expert quotes or blockquotes")

    # 5. FAQ Section
    if re.search(r'(?i)\b(FAQ|Frequently Asked Questions)\b', content):
        score += 1
        feedback.append("✅ FAQ section found")
    else:
        feedback.append("❌ Missing FAQ section")

    # 6. Dates/Timestamps
    if re.search(r'(?i)\b(Last updated|Published|Date):\s*\d', content) or re.search(r'\b(202[3-9]|20[3-9]\d)\b', content):
        score += 1
        feedback.append("✅ Recent dates/timestamps found")
    else:
        feedback.append("❌ Missing recent timestamps or 'Last updated' markers")

    return score, max_score, feedback

def main(path):
    print(f"--- GEO Audit for {path} ---")
    if os.path.isfile(path):
        files = [path]
    elif os.path.isdir(path):
        files = []
        for root, _, filenames in os.walk(path):
            for filename in filenames:
                if filename.endswith('.md') or filename.endswith('.txt') or filename.endswith('.html'):
                    files.append(os.path.join(root, filename))
    else:
        print("Invalid path")
        sys.exit(1)

    total_score = 0
    total_max = 0

    for f in files:
        score, max_score, feedback = check_file(f)
        total_score += score
        total_max += max_score
        print(f"\nFile: {f}")
        print(f"Score: {score}/{max_score}")
        for item in feedback:
            print(f"  {item}")

    print("\n--- Final Report ---")
    print(f"Total GEO Score: {total_score}/{total_max} ({(total_score/total_max)*100:.1f}%)" if total_max > 0 else "No files audited")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python geo_checker.py <file_or_directory>")
        sys.exit(1)

    main(sys.argv[1])
