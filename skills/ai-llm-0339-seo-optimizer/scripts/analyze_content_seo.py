#!/usr/bin/env python3
import argparse
import re

def analyze_text(text, target_keyword):
    results = {
        "word_count": len(text.split()),
        "keyword_occurrences": 0,
        "keyword_density": 0.0,
        "headings": [],
        "warnings": []
    }

    # Word count
    if results["word_count"] < 300:
        results["warnings"].append("Content is thin (under 300 words).")

    # Keyword density
    if target_keyword:
        kw_lower = target_keyword.lower()
        text_lower = text.lower()
        results["keyword_occurrences"] = text_lower.count(kw_lower)
        if results["word_count"] > 0:
            results["keyword_density"] = (results["keyword_occurrences"] * len(kw_lower.split())) / results["word_count"] * 100

        if results["keyword_occurrences"] == 0:
            results["warnings"].append(f"Target keyword '{target_keyword}' not found in content.")
        elif results["keyword_density"] > 3.0:
            results["warnings"].append(f"Keyword density might be too high ({results['keyword_density']:.2f}%). Watch out for keyword stuffing.")

    # Extract Markdown headings
    heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
    for match in heading_pattern.finditer(text):
        level = len(match.group(1))
        content = match.group(2)
        results["headings"].append({"level": level, "text": content})

    h1_count = sum(1 for h in results["headings"] if h["level"] == 1)
    if h1_count == 0:
        results["warnings"].append("No H1 tag found.")
    elif h1_count > 1:
        results["warnings"].append("Multiple H1 tags found. Standard practice is to have exactly one.")

    return results

def main():
    parser = argparse.ArgumentParser(description="Basic SEO content analyzer for Markdown text.")
    parser.add_argument("--file", required=True, help="Markdown file to analyze")
    parser.add_argument("--keyword", help="Target keyword to check for density")

    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        return

    results = analyze_text(content, args.keyword)

    print(f"--- SEO Analysis for {args.file} ---")
    print(f"Word Count: {results['word_count']}")

    if args.keyword:
        print(f"Target Keyword: '{args.keyword}'")
        print(f"Occurrences: {results['keyword_occurrences']}")
        print(f"Density: {results['keyword_density']:.2f}%")

    print(f"\nHeadings Structure:")
    for h in results["headings"]:
        print(f"{'  ' * (h['level']-1)}H{h['level']}: {h['text']}")

    if results["warnings"]:
        print("\nWarnings:")
        for w in results["warnings"]:
            print(f"- {w}")
    else:
        print("\nNo major SEO warnings found.")

if __name__ == "__main__":
    main()
