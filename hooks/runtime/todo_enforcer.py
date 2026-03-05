#!/usr/bin/env python3
import os
import sys
import re

def get_tasklist_tasks(project_root):
    tasklist_path = os.path.join(project_root, 'docs', 'tasklist.md')
    if not os.path.exists(tasklist_path):
        return []

    with open(tasklist_path, 'r', encoding='utf-8') as f:
        content = f.read()

    open_tasks = []
    for line in content.splitlines():
        if line.strip().startswith('- [ ]'):
            open_tasks.append(line.strip())
    return open_tasks

def get_continuity_tasks(project_root):
    continuity_path = os.path.join(project_root, 'continuity.md')
    if not os.path.exists(continuity_path):
        return []

    with open(continuity_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the "Pending Tasks" section
    pending_section = re.search(r'## Pending Tasks.*?\n(.*?)(?:\n##|$)', content, re.DOTALL | re.IGNORECASE)
    if not pending_section:
        return []

    tasks = []
    for line in pending_section.group(1).strip().splitlines():
        if line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '-')):
            tasks.append(line.strip())
    return tasks

def main():
    project_root = os.getenv('OVERPOWERS_PATH', os.getcwd())
    
    tasklist_tasks = get_tasklist_tasks(project_root)
    continuity_tasks = get_continuity_tasks(project_root)

    all_pending = []
    if continuity_tasks:
        all_pending.extend(continuity_tasks)
    
    # Avoid duplicates if they appear in both
    for t in tasklist_tasks:
        # Simple heuristic to avoid repeating tasks already listed in continuity
        if not any(t[5:].strip().lower() in ct.lower() for t in [t] for ct in continuity_tasks):
            all_pending.append(t)

    if all_pending:
        print("--- PENDING TASKS DETECTED ---")
        print("Please continue working on the remaining items to ensure the task is completed:")
        for t in all_pending[:5]: 
            print(f"  {t}")
        if len(all_pending) > 5:
            print(f"  ...and {len(all_pending) - 5} more.")
        print("\nDO NOT STOP UNTIL ALL TASKS ARE MARKED AS COMPLETED.")
        print("CONTINUE.")
        sys.exit(0)

if __name__ == "__main__":
    main()
