#!/usr/bin/env python3
import argparse
import os

def score_agents_md(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        content = f.read()

    sections = {
        "Build": ["build", "compile"],
        "Lint": ["lint", "format", "prettier", "eslint"],
        "Test": ["test", "pytest", "jest", "vitest"],
        "Conventions": ["convention", "style", "pattern", "rule"]
    }

    score = 0
    total = len(sections)
    found_sections = []

    for section, keywords in sections.items():
        found = False
        for kw in keywords:
            if kw.lower() in content.lower():
                found = True
                break
        if found:
            score += 1
            found_sections.append(section)

    print(f"Quality Score for {file_path}: {score}/{total}")
    print(f"Found Sections: {', '.join(found_sections)}")
    
    missing = set(sections.keys()) - set(found_sections)
    if missing:
        print(f"Missing Sections: {', '.join(missing)}")
    
    if score == total:
        print("✅ Excellent: All required sections are present.")
    elif score >= total / 2:
        print("⚠️ Fair: Some key sections are missing.")
    else:
        print("❌ Poor: Most core sections are missing.")

def main():
    parser = argparse.ArgumentParser(description='Score quality of AGENTS.md')
    parser.add_argument('file', default='AGENTS.md', nargs='?', help='Path to AGENTS.md')

    args = parser.parse_args()
    score_agents_md(args.file)

if __name__ == "__main__":
    main()
