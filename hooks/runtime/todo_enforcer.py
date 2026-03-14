#!/usr/bin/env python3
import os
import sys

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
    # Prefer continuity files in .agents/, with root fallback for legacy repos.
    tasks = []
    candidates = []
    agents_dir = os.path.join(project_root, '.agents')
    if os.path.isdir(agents_dir):
        candidates.append(agents_dir)
    candidates.append(project_root)

    seen = set()
    for base_dir in candidates:
        try:
            filenames = os.listdir(base_dir)
        except OSError:
            continue
        for filename in filenames:
            if not (filename.startswith('continuity-') and filename.endswith('.md')):
                continue
            path = os.path.join(base_dir, filename)
            if path in seen:
                continue
            seen.add(path)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except OSError:
                continue

            # Look for checklists [ ] anywhere in the continuity file.
            for line in content.splitlines():
                if line.strip().startswith('- [ ]'):
                    tasks.append(f"[{os.path.relpath(path, project_root)}] {line.strip()[5:].strip()}")
    return tasks

def main():
    project_root = os.getenv('OVERPOWERS_PATH', os.getcwd())

    tasklist_tasks = get_tasklist_tasks(project_root)
    continuity_tasks = get_continuity_tasks(project_root)

    all_pending = tasklist_tasks + continuity_tasks

    if all_pending:
        print("\n" + "!"*40)
        print("🚀 PENDING TASKS DETECTED")
        print("!"*40)
        print("The following items require your attention to ensure task continuity:")
        for t in all_pending[:10]: 
            print(f"  • {t}")
        if len(all_pending) > 10:
            print(f"  ...and {len(all_pending) - 10} more.")
        print("\nDO NOT STOP UNTIL ALL ITEMS ARE MARKED AS COMPLETED [x].")
        print("CONTINUE.")
        print("!"*40 + "\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
