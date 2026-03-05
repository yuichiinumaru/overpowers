#!/usr/bin/env python3
import os
import glob
import shutil

def is_fully_completed(content):
    lines = content.split('\n')
    has_checked_subtask = False
    for line in lines:
        stripped = line.strip()
        # Look for subtasks, typically starting with "- [ ]" or "- [x]"
        if stripped.startswith('- [ ]') or stripped.startswith('- [  ]'):
            return False # Found an incomplete task
        if stripped.startswith('- [x]') or stripped.startswith('- [X]'):
            has_checked_subtask = True
            
    # Return true only if we found checked tasks and no unchecked tasks
    return has_checked_subtask

def main():
    base_dir = "docs/tasks"
    completed_dir = os.path.join(base_dir, "completed")
    os.makedirs(completed_dir, exist_ok=True)
    
    files = glob.glob(os.path.join(base_dir, "0300-ops-skill-scripts-batch*.md"))
    
    print(f"Buscando em {len(files)} arquivos de batch em {base_dir}...")
    
    moved = 0
    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if is_fully_completed(content):
            dest = os.path.join(completed_dir, os.path.basename(filepath))
            print(f"[COMPLETO] Movendo {os.path.basename(filepath)} para {completed_dir}/")
            shutil.move(filepath, dest)
            moved += 1
        else:
            # print(f"[INCOMPLETO] {os.path.basename(filepath)} ainda tem tarefas pendentes.")
            pass
            
    print(f"\nFinalizado! {moved} arquivos movidos.")

if __name__ == "__main__":
    main()
