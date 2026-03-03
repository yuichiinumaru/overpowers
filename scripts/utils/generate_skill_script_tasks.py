#!/usr/bin/env python3
import os
import glob
import math

def main():
    project_root = os.getenv('OVERPOWERS_PATH', os.getcwd())
    skills_dir = os.path.join(project_root, 'skills')
    
    if not os.path.exists(skills_dir):
        print(f"Error: {skills_dir} not found.")
        return

    needs_scripts = []
    
    # Iterate through all skill entries
    for entry in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, entry)
        if not os.path.isdir(skill_path):
            continue
            
        # Check for scripts directory
        scripts_dir = os.path.join(skill_path, 'scripts')
        has_scripts = False
        
        if os.path.isdir(scripts_dir):
            # Check if it has any files inside it (excluding hidden files usually, but let's just check if it's strictly empty)
            if any(os.path.isfile(os.path.join(scripts_dir, f)) for f in os.listdir(scripts_dir)):
                has_scripts = True
                
        if not has_scripts:
            needs_scripts.append(entry)
            
    # Sort for deterministic output
    needs_scripts.sort()
    
    print(f"Found {len(needs_scripts)} skills without helper scripts.")
    
    batch_size = 20
    num_batches = math.ceil(len(needs_scripts) / batch_size)
    
    tasks_dir = os.path.join(project_root, 'docs', 'tasks')
    os.makedirs(tasks_dir, exist_ok=True)
    
    task_entries = []
    
    for i in range(num_batches):
        batch_num = i + 1
        batch_skills = needs_scripts[i*batch_size : (i+1)*batch_size]
        
        task_id = f"0300-ops-skill-scripts-batch-{batch_num:03d}"
        task_filename = f"{task_id}.md"
        task_path = os.path.join(tasks_dir, task_filename)
        
        # Create macro task file
        with open(task_path, 'w', encoding='utf-8') as f:
            f.write(f"# Task 0300: Skill Scripts Batch {batch_num:03d}\n\n")
            f.write("**Status**: [ ]\n")
            f.write("**Priority**: LOW\n")
            f.write("**Type**: ops\n\n")
            f.write("## Objective\n")
            f.write("Analyze each skill in this batch and create helper scripts inside their `scripts/` subdirectory where it makes sense, based on the `SKILL.md` instructions.\n\n")
            f.write("## Sub-tasks\n")
            for skill in batch_skills:
                f.write(f"- [ ] `{skill}`: Check if any existing script inside the repository's `scripts/` subfolders would fit as a helper and copy it over (if applicable)\n")
                f.write(f"- [ ] `{skill}`: Analyze and create new helper scripts inside its `scripts/` directory (if applicable)\n")
                
        task_entries.append(f"- [ ] [{task_id}](tasks/{task_filename}) — Analyze and deploy Helper Scripts for Batch {batch_num:03d}")
        
    print(f"Generated {num_batches} task files in {tasks_dir}.")
    
    # Write to a summary to assist with tasklist appending
    summary_path = os.path.join(project_root, 'tmp_task_entries.txt')
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(task_entries))
        
    print(f"List of tasks written to {summary_path}. You can append them to docs/tasklist.md.")

if __name__ == "__main__":
    main()
