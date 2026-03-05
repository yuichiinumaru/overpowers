#!/usr/bin/env python3
import os
import sys

def find_root_agents_md(start_path, limit=5):
    """Search upwards for AGENTS.md up to limit directories."""
    current = start_path
    for _ in range(limit):
        path = os.path.join(current, 'AGENTS.md')
        if os.path.exists(path):
            return path
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent
    return None

def main():
    cwd = os.getcwd()
    project_root = os.getenv('OVERPOWERS_PATH', os.getcwd())
    
    # Files to look for in CURRENT directory
    local_files = ['README.md', '.opencode/CONTEXT.md', 'DESIGN.md']
    
    # Always try to find the root AGENTS.md
    root_agents = find_root_agents_md(cwd)
    
    injected = False

    if root_agents:
        # Avoid double injecting if we are in root
        if os.path.dirname(root_agents) != cwd:
            with open(root_agents, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"--- GLOBAL CONTEXT: AGENTS.md (Root) ---")
                # Summary or first part
                print(content[:1500])
                print(f"--- END GLOBAL CONTEXT ---")
                injected = True

    for f_name in local_files:
        f_path = os.path.join(cwd, f_name)
        if os.path.exists(f_path):
            with open(f_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"--- LOCAL CONTEXT: {f_name} (in {cwd}) ---")
                print(content[:2000]) 
                print(f"--- END LOCAL CONTEXT: {f_name} ---")
                injected = True

    if injected:
        sys.exit(0)

if __name__ == "__main__":
    main()
