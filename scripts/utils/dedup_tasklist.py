#!/usr/bin/env python3
import sys
import re

def process_tasklist():
    filepath = 'docs/tasklist.md'
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

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

    def get_id(text):
        m = re.search(r'\[([0-9]{4}[^\]]*)\]', text)
        if m:
            return m.group(1)
        return text.strip()

    all_tasks = {}
    
    # Pass 1: gather uniqueness and completion status
    for section in sections_order:
        for line in section_content[section]:
            if line.strip().startswith('- ['):
                task_id = get_id(line)
                is_completed = line.strip().startswith('- [x]') or line.strip().startswith('- [X]')
                
                if task_id not in all_tasks:
                    all_tasks[task_id] = {'line': line, 'completed': is_completed, 'section': section}
                elif not all_tasks[task_id]['completed'] and is_completed:
                    # Update to completed version if a completed version is found
                    all_tasks[task_id] = {'line': line, 'completed': is_completed, 'section': section}

    # Pass 2: reconstruct
    new_sections = {s: [] for s in sections_order}
    completed_lines = []
    seen_in_output = set()

    for section in sections_order:
        for line in section_content[section]:
            if line.strip().startswith('- ['):
                task_id = get_id(line)
                if task_id in seen_in_output:
                    continue
                seen_in_output.add(task_id)
                
                task_info = all_tasks[task_id]
                if task_info['completed']:
                    completed_lines.append(task_info['line'])
                else:
                    new_sections[section].append(task_info['line'])
            else:
                # Append blank lines or non-task lines
                # Avoid massive duplicate line breaks
                if not (len(new_sections[section]) > 0 and new_sections[section][-1].strip() == '' and line.strip() == ''):
                    new_sections[section].append(line)

    completed_lines.sort(key=lambda x: get_id(x))
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in header_text:
            f.write(line)
            
        for section in sections_order:
            f.write(section + '\n')
            if section == '## ✅ Tarefas Concluídas':
                for line in completed_lines:
                    f.write(line)
                f.write('\n')
            else:
                for line in new_sections[section]:
                    f.write(line)

if __name__ == '__main__':
    process_tasklist()
