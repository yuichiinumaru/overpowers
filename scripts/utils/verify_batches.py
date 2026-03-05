#!/usr/bin/env python3
import os
import glob
import re

def main():
    project_root = os.getenv('OVERPOWERS_PATH', os.getcwd())
    tasks_dir = os.path.join(project_root, 'docs', 'tasks')
    completed_dir = os.path.join(tasks_dir, 'completed')
    
    all_batches = glob.glob(os.path.join(tasks_dir, '0300-*.md')) + glob.glob(os.path.join(completed_dir, '0300-*.md'))
    
    true_states = {}
    
    for filepath in all_batches:
        filename = os.path.basename(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count total subtasks vs completed subtasks
        total_subtasks = len(re.findall(r'^- \[(?: |x|X)\]', content, re.MULTILINE))
        completed_subtasks = len(re.findall(r'^- \[(?:x|X)\]', content, re.MULTILINE))
        
        # Account for the single Status line at the top
        # A file with N skills will have 2*N subtasks + 1 top-level status
        # Let's count only lines starting with `- [ ]` or `- [x]` to be safe, excluding `**Status**: [x]`
        subtasks_matches = re.findall(r'^- \[( |x|X)\]', content, re.MULTILINE)
        
        total_subtasks = len(subtasks_matches)
        completed_subtasks = sum(1 for m in subtasks_matches if m.lower() == 'x')
            
        is_truly_completed = (total_subtasks > 0 and total_subtasks == completed_subtasks)
        
        # Correct the header status if needed
        is_header_completed = '**Status**: [x]' in content.lower() or '**Status**: [X]' in content
        
        if is_truly_completed != is_header_completed:
            print(f"Mismatch in {filename}: Subtasks {completed_subtasks}/{total_subtasks}, Header: {is_header_completed}. Fixing header.")
            if is_truly_completed:
                content = re.sub(r'\*\*Status\*\*: \[\s*\]', r'**Status**: [x]', content, flags=re.IGNORECASE)
            else:
                content = re.sub(r'\*\*Status\*\*: \[[xX]\]', r'**Status**: [ ]', content, flags=re.IGNORECASE)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        
        true_states[filename] = {
            'completed': is_truly_completed,
            'current_path': filepath
        }
        
    print(f"Verified {len(true_states)} batch files.")

if __name__ == "__main__":
    main()
