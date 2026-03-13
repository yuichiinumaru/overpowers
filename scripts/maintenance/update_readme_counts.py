import os
import re

def count_files(directory, file_extension=None, specific_file=None):
    count = 0
    if not os.path.exists(directory):
        return 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file_extension and file.endswith(file_extension):
                count += 1
            elif specific_file and file == specific_file:
                count += 1
            elif not file_extension and not specific_file:
                count += 1
    return count

def main():
    agents_count = count_files('agents', file_extension='.md')
    skills_count = count_files('skills', specific_file='SKILL.md')
    workflows_count = count_files('workflows', file_extension='.md')
    scripts_count = count_files('scripts')
    hooks_count = count_files('hooks')

    total_count = agents_count + skills_count + workflows_count + scripts_count + hooks_count

    readme_path = 'README.md'
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found.")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Inventory Table
    content = re.sub(r'\|\s*\*\*Agents\*\*\s*\|\s*\d+\+?\s*\|', f'| **Agents** | {agents_count}+ |', content)
    content = re.sub(r'\|\s*\*\*Skills\*\*\s*\|\s*\d+\+?\s*\|', f'| **Skills** | {skills_count}+ |', content)
    content = re.sub(r'\|\s*\*\*Commands/Workflows\*\*\s*\|\s*\d+\+?\s*\|', f'| **Commands/Workflows** | {workflows_count}+ |', content)
    content = re.sub(r'\|\s*\*\*Scripts\*\*\s*\|\s*\d+\+?\s*\|', f'| **Scripts** | {scripts_count}+ |', content)
    content = re.sub(r'\|\s*\*\*Hooks\*\*\s*\|\s*\d+\+?\s*\|', f'| **Hooks** | {hooks_count} |', content)

    # Update Total Count
    content = re.sub(r'\*\*Total: \d+\+? components!\*\*', f'**Total: {total_count}+ components!**', content)

    # Update Structure Tree Counts
    content = re.sub(r'├── agents/\s+# \d+\+? specialized AI agents \(\.md\)', f'├── agents/                   # {agents_count}+ specialized AI agents (.md)', content)
    content = re.sub(r'├── skills/\s+# \d+\+? skills \(skill-name/SKILL\.md\)', f'├── skills/                   # {skills_count}+ skills (skill-name/SKILL.md)', content)
    content = re.sub(r'├── workflows/\s+# \d+\+? process guides / commands \(\.md\)', f'├── workflows/                # {workflows_count}+ process guides / commands (.md)', content)
    content = re.sub(r'├── hooks/\s+# \d+\+? notification integrations', f'├── hooks/                    # {hooks_count} notification integrations', content)
    content = re.sub(r'├── scripts/\s+# \d+\+? DevOps/automation helpers', f'├── scripts/                  # {scripts_count}+ DevOps/automation helpers', content)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated README.md with new counts:")
    print(f"Agents: {agents_count}")
    print(f"Skills: {skills_count}")
    print(f"Workflows: {workflows_count}")
    print(f"Scripts: {scripts_count}")
    print(f"Hooks: {hooks_count}")
    print(f"Total: {total_count}")

if __name__ == '__main__':
    main()
