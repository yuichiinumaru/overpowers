#!/usr/bin/env python3
import os
import glob
import re
import shutil

def main():
    project_root = os.getenv('OVERPOWERS_PATH', os.getcwd())
    tasks_dir = os.path.join(project_root, 'docs', 'tasks')
    completed_dir = os.path.join(tasks_dir, 'completed')
    tasklist_path = os.path.join(project_root, 'docs', 'tasklist.md')
    
    os.makedirs(completed_dir, exist_ok=True)
    
    # 1. Move completed tasks to the completed folder
    moved_count = 0
    for filepath in glob.glob(os.path.join(tasks_dir, '*.md')):
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if '**Status**: [x]' in content.lower():
                filename = os.path.basename(filepath)
                dest = os.path.join(completed_dir, filename)
                shutil.move(filepath, dest)
                moved_count += 1
    print(f"Moved {moved_count} completed tasks to docs/tasks/completed/")

    # 2. Fix the tasklist markdown itself
    with open(tasklist_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Repair missing line breaks from previous bad formatting (e.g. Jules joining lines)
    content = content.replace('- [x]', '\n- [x]').replace('- [ ]', '\n- [ ]')
    lines = [l + '\n' for l in content.split('\n') if l.strip()]

    header_text = []
    sections_order = []
    section_content = {}
    
    current_section = None
    
    for line in lines:
        if line.startswith('## '):
            current_section = line.strip()
            if current_section not in sections_order:
                sections_order.append(current_section)
                section_content[current_section] = []
        elif current_section is None:
            header_text.append(line)
        else:
            section_content[current_section].append(line)

    # Re-discover all tasks from the filesystem
    open_tasks = glob.glob(os.path.join(tasks_dir, '*.md'))
    closed_tasks = glob.glob(os.path.join(completed_dir, '*.md'))
    
    # Extract IDs to determine state
    def get_id_from_path(p):
        fname = os.path.basename(p).replace('.md', '')
        # Handle cases where there is no prefix properly if needed, but most should have prefix
        return fname

    all_fs_tasks = {}
    for p in open_tasks:
        tid = get_id_from_path(p)
        all_fs_tasks[tid] = {'path': f"tasks/{os.path.basename(p)}", 'completed': False}
        
    for p in closed_tasks:
        tid = get_id_from_path(p)
        all_fs_tasks[tid] = {'path': f"tasks/completed/{os.path.basename(p)}", 'completed': True}

    def extract_id(line):
        m = re.search(r'\[(.*?)\]\(', line)
        if m:
            return m.group(1)
        return None

    new_sections = {s: [] for s in sections_order}
    completed_lines = []
    seen_ids = set()

    for section in sections_order:
        if section == '## ✅ Tarefas Concluídas':
            continue # We will rebuild this entirely
            
        for line in section_content[section]:
            if line.strip().startswith('- ['):
                tid = extract_id(line)
                if not tid:
                    new_sections[section].append(line)
                    continue
                
                # Check actual state from filesystem
                if tid in all_fs_tasks:
                    is_completed = all_fs_tasks[tid]['completed']
                    task_path = all_fs_tasks[tid]['path']
                else:
                    # Fallback to textual info if file doesn't exist (edge case)
                    is_completed = line.strip().startswith('- [x]') or line.strip().startswith('- [X]')
                    task_path = ''
                
                if tid in seen_ids:
                    continue
                seen_ids.add(tid)
                
                # Format properly based on actual filesystem state
                match = re.search(r'(\[.*?\]\(.*?\)(.*))', line.strip())
                if match:
                    suffix = match.group(2)
                else:
                    suffix = ""
                    
                if is_completed:
                    formatted = f"- [x] [{tid}]({task_path}){suffix}\n"
                    completed_lines.append(formatted)
                else:
                    formatted = f"- [ ] [{tid}]({task_path}){suffix}\n"
                    new_sections[section].append(formatted)
                    
            else:
                new_sections[section].append(line)

    # For safety, inject any FS tasks that were completely missing from the markdown
    for tid, info in all_fs_tasks.items():
        if tid not in seen_ids:
            if info['completed']:
                completed_lines.append(f"- [x] [{tid}]({info['path']})\n")
            else:
                new_sections['## 💡 Planejamento / Novos Itens (USER-NOTES)'].append(f"- [ ] [{tid}]({info['path']})\n")
            seen_ids.add(tid)

    # Sort completed tasks
    completed_lines.sort()
    
    if '## ✅ Tarefas Concluídas' in sections_order:
        new_sections['## ✅ Tarefas Concluídas'] = completed_lines
    else:
        sections_order.append('## ✅ Tarefas Concluídas')
        new_sections['## ✅ Tarefas Concluídas'] = completed_lines
        
    with open(tasklist_path, 'w', encoding='utf-8') as f:
        for line in header_text:
            if line.strip():
                f.write(line.strip() + '\n')
        f.write('\n')
            
        for section in sections_order:
            f.write(section + '\n')
            for line in new_sections.get(section, []):
                if line.strip():
                    f.write(line)
            f.write('\n')
            
    print("Tasklist deduplicated and synchronized with docs/tasks/")

if __name__ == "__main__":
    main()
