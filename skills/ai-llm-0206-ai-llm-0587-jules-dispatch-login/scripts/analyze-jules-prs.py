#!/usr/bin/env python3
import json
import re
import collections
import subprocess
import os
from datetime import datetime

def run_command(cmd_list):
    try:
        return subprocess.check_output(cmd_list).decode("utf-8")
    except subprocess.CalledProcessError:
        return ""

print("Fetching open PRs via gh...")
prs_json_str = run_command(["gh", "pr", "list", "--state", "open", "--limit", "200", "--json", "number,title,headRefName"])
if not prs_json_str:
    print("Failed to fetch PRs.")
    exit(1)

prs = json.loads(prs_json_str)

groups = collections.defaultdict(list)
for pr in prs:
    branch = pr["headRefName"]
    m = re.search(r"batch[- ]?(\d+)", branch.lower())
    if m:
        batch_num = m.group(1)
        groups[batch_num].append(pr)
    else:
        m2 = re.search(r"batch[- ]?(\d+)", pr["title"].lower())
        if m2:
            groups[m2.group(1)].append(pr)

stats = {
    "groups": 0, 
    "identical": 0, 
    "varied": 0, 
    "total_prs": 0,
    "line_diffs": [],
    "proportional_diffs": [] 
}

batch_reports = []

print("Analyzing diffs for each batch...")
for batch_num in sorted(groups.keys()):
    items = sorted(groups[batch_num], key=lambda x: x["number"])
    stats["groups"] += 1
    stats["total_prs"] += len(items)
    
    batch_report = []
    batch_report.append(f"## Batch {batch_num}\n")
    batch_report.append(f"- **Total Parallel PRs:** {len(items)}\n")
    
    diffs = {}
    lines_list = []
    
    for pr in items:
        diff = run_command(["gh", "pr", "diff", str(pr["number"])])
        if not diff:
            diffs[pr["number"]] = ("ERROR_FETCHING_DIFF", 0)
            continue
            
        clean_diff = "\n".join([line for line in diff.split('\n') if not line.startswith('index ') and not line.startswith('@@')])
        size = len(clean_diff.split('\n'))
        diffs[pr["number"]] = (clean_diff, size)
        lines_list.append(size)
            
    # Compare diffs
    unique_diffs = {}
    for number, (diff_content, size) in diffs.items():
        if diff_content not in unique_diffs:
            unique_diffs[diff_content] = [number]
        else:
            unique_diffs[diff_content].append(number)
            
    if len(unique_diffs) <= 1:
        batch_report.append(f"- **Variance:** NONE (0%). All agents reached the exact same deterministic output.\n")
        stats["identical"] += 1
        batch_report.append(f"- **Line Difference:** 0\n")
        batch_report.append(f"- **Proportional Difference:** 0.0%\n")
    else:
        stats["varied"] += 1
        batch_report.append(f"- **Variance:** DETECTED. The agents produced {len(unique_diffs)} distinct variations.\n")
        
        max_lines = max(lines_list) if lines_list else 0
        min_lines = min(lines_list) if lines_list else 0
        line_diff = max_lines - min_lines
        prop_diff = (line_diff / max_lines * 100) if max_lines > 0 else 0.0
        
        stats["line_diffs"].append(line_diff)
        stats["proportional_diffs"].append(prop_diff)
        
        batch_report.append(f"- **Line Difference:** {line_diff} lines (Max: {max_lines}, Min: {min_lines})\n")
        batch_report.append(f"- **Proportional Difference:** {prop_diff:.1f}%\n")
        
        for idx, (diff_content, numbers) in enumerate(unique_diffs.items()):
            size = len(diff_content.split('\n')) if diff_content != "ERROR_FETCHING_DIFF" else 0
            batch_report.append(f"  - **Variation {idx+1}** (PRs {', '.join(map(str, numbers))}): {size} lines.\n")
        
    batch_report.append("\n")
    batch_reports.extend(batch_report)
    print(f"  - Processed Batch {batch_num}: {len(unique_diffs)} variations")

report = []
report.append("# Jules Parallel Delegation Variance Report\n")
report.append("This report analyzes the pull requests generated in parallel by Jules, comparing their outputs to measure variance in reasoning and code generation for identical tasks.\n\n")

avg_line_diff = sum(stats["line_diffs"]) / len(stats["line_diffs"]) if stats["line_diffs"] else 0
avg_prop_diff = sum(stats["proportional_diffs"]) / len(stats["proportional_diffs"]) if stats["proportional_diffs"] else 0

total_groups = max(stats['groups'], 1)
report.append("## Summary Statistics\n")
report.append(f"- **Total Batches Processed:** {stats['groups']}\n")
report.append(f"- **Total PRs Evaluated:** {stats['total_prs']}\n")
report.append(f"- **Zero-Variance Batches:** {stats['identical']} ({(stats['identical']/total_groups)*100:.1f}%)\n")
report.append(f"- **Varied Batches:** {stats['varied']} ({(stats['varied']/total_groups)*100:.1f}%)\n")
if stats["varied"] > 0:
    report.append(f"- **Average Line Difference (among varied):** {avg_line_diff:.1f} lines\n")
    report.append(f"- **Average Proportional Difference (among varied):** {avg_prop_diff:.1f}%\n")
report.append("\n---\n\n")

report.extend(batch_reports)

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
os.makedirs(".agents/thoughts", exist_ok=True)
output_file = f".agents/thoughts/jules_parallel_variance_{timestamp}.md"

with open(output_file, 'w') as f:
    f.writelines(report)

print(f"Generated report at {output_file}")
