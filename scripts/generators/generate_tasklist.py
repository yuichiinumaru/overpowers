#!/usr/bin/env python3
"""
generate_tasklist.py

Scans a tasks directory (default docs/tasks) and generates a configuration JSON
compatible with jules-launcher-v2.sh.
"""

import os
import glob
import json
import argparse


def generate_tasklist(tasks_dir, output_file, prompt_path, repo_name):
    tasks_to_add = []
    
    # We want to ignore templates and directories
    for filename in sorted(os.listdir(tasks_dir)):
        filepath = os.path.join(tasks_dir, filename)
        
        # Skip subdirectories like 'completed' and 'planning'
        if not os.path.isfile(filepath):
            continue
            
        # Only process .md files and skip templates
        if not filename.endswith(".md") or filename.startswith("000-template"):
            continue
            
        tasks_to_add.append({
            "prompt": prompt_path,
            "task": filepath
        })
        
    output_data = {
        "repo": repo_name,
        "tasks": tasks_to_add
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
        
    print(f"✅ Generated {output_file} with {len(tasks_to_add)} tasks.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Jules JSON plan from a directory of markdown tasks.")
    parser.add_argument("-d", "--dir", default="docs/tasks", help="Directory containing markdown tasks (default: docs/tasks)")
    parser.add_argument("-o", "--output", default="docs/tasklist.json", help="Output JSON file path (default: docs/tasklist.json)")
    parser.add_argument("-p", "--prompt", required=True, help="Prompt file path to assign to all tasks (e.g., prompts/foreman.json)")
    parser.add_argument("-r", "--repo", default="", help="Optional repository name")
    
    args = parser.parse_args()
    
    generate_tasklist(args.dir, args.output, args.prompt, args.repo)
