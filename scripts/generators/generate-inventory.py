#!/usr/bin/env python3
"""
Generate comprehensive inventory of Overpowers assets.
Creates markdown files listing all agents, skills, scripts, workflows, hooks, and services.
"""

import os
import json
from pathlib import Path
from collections import defaultdict

OVERPOWERS_ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = OVERPOWERS_ROOT / ".docs"

def scan_agents():
    """Scan all agents in agents/ directory."""
    agents_dir = OVERPOWERS_ROOT / "agents"
    agents = []
    
    if agents_dir.exists():
        for agent_file in sorted(agents_dir.glob("*.md")):
            name = agent_file.stem
            # Read first line for description
            try:
                content = agent_file.read_text()
                lines = content.split('\n')
                description = ""
                for line in lines:
                    if line.startswith('#'):
                        description = line.lstrip('#').strip()
                        break
                agents.append({
                    "name": name,
                    "file": str(agent_file.relative_to(OVERPOWERS_ROOT)),
                    "description": description
                })
            except:
                agents.append({"name": name, "file": str(agent_file.relative_to(OVERPOWERS_ROOT)), "description": ""})
    
    return agents

def scan_skills():
    """Scan all skills in skills/ directory."""
    skills_dir = OVERPOWERS_ROOT / "skills"
    skills = []
    
    if skills_dir.exists():
        for skill_dir in sorted(skills_dir.iterdir()):
            if skill_dir.is_dir():
                skill_file = skill_dir / "SKILL.md"
                name = skill_dir.name
                description = ""
                
                if skill_file.exists():
                    try:
                        content = skill_file.read_text()
                        # Extract description from frontmatter
                        if content.startswith('---'):
                            parts = content.split('---', 2)
                            if len(parts) >= 3:
                                frontmatter = parts[1]
                                for line in frontmatter.split('\n'):
                                    if line.startswith('description:'):
                                        description = line.split(':', 1)[1].strip().strip('"\'')
                                        break
                    except:
                        pass
                
                skills.append({
                    "name": name,
                    "path": str(skill_dir.relative_to(OVERPOWERS_ROOT)),
                    "description": description
                })
    
    return skills

def scan_scripts():
    """Scan all scripts in scripts/ directory."""
    scripts_dir = OVERPOWERS_ROOT / "scripts"
    scripts = defaultdict(list)
    
    if scripts_dir.exists():
        for category_dir in sorted(scripts_dir.iterdir()):
            if category_dir.is_dir():
                category = category_dir.name
                for script_file in sorted(category_dir.glob("*")):
                    if script_file.is_file():
                        scripts[category].append({
                            "name": script_file.name,
                            "path": str(script_file.relative_to(OVERPOWERS_ROOT))
                        })
    
    return dict(scripts)

def scan_workflows():
    """Scan all workflows in workflows/ directory."""
    workflows_dir = OVERPOWERS_ROOT / "workflows"
    workflows = []
    
    if workflows_dir.exists():
        for wf_file in sorted(workflows_dir.glob("*.md")):
            name = wf_file.stem
            description = ""
            
            try:
                content = wf_file.read_text()
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1]
                        for line in frontmatter.split('\n'):
                            if line.startswith('description:'):
                                description = line.split(':', 1)[1].strip().strip('"\'')
                                break
            except:
                pass
            
            workflows.append({
                "name": name,
                "file": str(wf_file.relative_to(OVERPOWERS_ROOT)),
                "description": description
            })
    
    return workflows

def scan_hooks():
    """Scan all hooks in hooks/ directory."""
    hooks_dir = OVERPOWERS_ROOT / "hooks"
    hooks = []
    
    if hooks_dir.exists():
        for hook_file in sorted(hooks_dir.glob("*.js")):
            name = hook_file.stem
            hooks.append({
                "name": name,
                "file": str(hook_file.relative_to(OVERPOWERS_ROOT))
            })
    
    return hooks

def scan_services():
    """Scan all services in services/ directory."""
    services_dir = OVERPOWERS_ROOT / "services"
    services = []
    
    if services_dir.exists():
        for service_dir in sorted(services_dir.iterdir()):
            if service_dir.is_dir():
                name = service_dir.name
                readme = service_dir / "README.md"
                description = ""
                
                if readme.exists():
                    try:
                        content = readme.read_text()
                        lines = content.split('\n')
                        for line in lines:
                            if line.startswith('#'):
                                description = line.lstrip('#').strip()
                                break
                    except:
                        pass
                
                services.append({
                    "name": name,
                    "path": str(service_dir.relative_to(OVERPOWERS_ROOT)),
                    "description": description
                })
    
    return services

def scan_commands():
    """Scan all commands in commands/ directory."""
    commands_dir = OVERPOWERS_ROOT / "commands"
    commands = []
    
    if commands_dir.exists():
        for cmd_file in sorted(commands_dir.glob("*.md")):
            name = cmd_file.stem
            description = ""
            
            try:
                content = cmd_file.read_text()
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1]
                        for line in frontmatter.split('\n'):
                            if line.startswith('description:'):
                                description = line.split(':', 1)[1].strip().strip('"\'')
                                break
            except:
                pass
            
            commands.append({
                "name": name,
                "file": str(cmd_file.relative_to(OVERPOWERS_ROOT)),
                "description": description
            })
    
    return commands

def generate_inventory_md():
    """Generate comprehensive inventory markdown."""
    agents = scan_agents()
    skills = scan_skills()
    scripts = scan_scripts()
    workflows = scan_workflows()
    hooks = scan_hooks()
    services = scan_services()
    commands = scan_commands()
    
    # Calculate totals
    total_scripts = sum(len(s) for s in scripts.values())
    
    md = f"""# Overpowers Complete Inventory

> Auto-generated inventory of all Overpowers assets.
> Last updated: {os.popen('date -Iseconds').read().strip()}

## Summary

| Category | Count |
|----------|-------|
| Agents | {len(agents)} |
| Skills | {len(skills)} |
| Scripts | {total_scripts} |
| Workflows | {len(workflows)} |
| Hooks | {len(hooks)} |
| Services | {len(services)} |
| Commands | {len(commands)} |

---

## Agents ({len(agents)})

| Name | Description |
|------|-------------|
"""
    
    for agent in agents:
        desc = agent.get('description', '')[:80]
        md += f"| `{agent['name']}` | {desc} |\n"
    
    md += f"""
---

## Skills ({len(skills)})

| Name | Description |
|------|-------------|
"""
    
    for skill in skills:
        desc = skill.get('description', '')[:80]
        md += f"| `{skill['name']}` | {desc} |\n"
    
    md += f"""
---

## Scripts ({total_scripts})

"""
    
    for category, script_list in scripts.items():
        md += f"### {category} ({len(script_list)})\n\n"
        for script in script_list:
            md += f"- `{script['name']}`\n"
        md += "\n"
    
    md += f"""---

## Workflows ({len(workflows)})

| Name | Description |
|------|-------------|
"""
    
    for wf in workflows:
        desc = wf.get('description', '')[:80]
        md += f"| `{wf['name']}` | {desc} |\n"
    
    md += f"""
---

## Hooks ({len(hooks)})

| Name |
|------|
"""
    
    for hook in hooks:
        md += f"| `{hook['name']}` |\n"
    
    md += f"""
---

## Services ({len(services)})

| Name | Description |
|------|-------------|
"""
    
    for service in services:
        desc = service.get('description', '')[:80]
        md += f"| `{service['name']}` | {desc} |\n"
    
    md += f"""
---

## Commands ({len(commands)})

| Name | Description |
|------|-------------|
"""
    
    for cmd in commands:
        desc = cmd.get('description', '')[:80]
        md += f"| `{cmd['name']}` | {desc} |\n"
    
    return md

def update_readme_counts():
    """Update counts in README.md based on actual directory contents."""
    import re
    readme_path = OVERPOWERS_ROOT / "README.md"
    if not readme_path.exists():
        return

    content = readme_path.read_text()
    original = content

    # Count actual assets
    agents_dir = OVERPOWERS_ROOT / "agents"
    skills_dir = OVERPOWERS_ROOT / "skills"
    workflows_dir = OVERPOWERS_ROOT / "workflows"
    hooks_dir = OVERPOWERS_ROOT / "hooks"
    scripts_dir = OVERPOWERS_ROOT / "scripts"

    n_agents = len(list(agents_dir.glob("*.md"))) if agents_dir.exists() else 0
    n_skills = sum(1 for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()) if skills_dir.exists() else 0
    n_workflows = len(list(workflows_dir.glob("*.md"))) if workflows_dir.exists() else 0
    n_hooks = len(list(hooks_dir.glob("*.md"))) if hooks_dir.exists() else 0
    n_scripts = sum(1 for f in scripts_dir.rglob("*") if f.is_file() and f.suffix in ('.sh', '.py')) if scripts_dir.exists() else 0

    # Replace counts in README — match patterns like "475+ specialized AI agents"
    replacements = [
        (r'\d+\+?\s+specialized AI agents', f'{n_agents}+ specialized AI agents'),
        (r'\d+\+?\s+skills \(skill-name/SKILL\.md\)', f'{n_skills}+ skills (skill-name/SKILL.md)'),
        (r'\d+\+?\s+process guides / commands', f'{n_workflows}+ process guides / commands'),
        (r'\d+\s+notification integrations', f'{n_hooks} notification integrations'),
        (r'\d+\+?\s+DevOps/automation helpers', f'{n_scripts}+ DevOps/automation helpers'),
    ]

    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    if content != original:
        readme_path.write_text(content)
        print(f"📝 Updated README.md counts: agents={n_agents}, skills={n_skills}, workflows={n_workflows}, hooks={n_hooks}, scripts={n_scripts}")
    else:
        print("📝 README.md counts already up to date.")


def main():
    # Ensure docs directory exists
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate and save inventory
    inventory_md = generate_inventory_md()
    inventory_file = DOCS_DIR / "inventory.md"
    inventory_file.write_text(inventory_md)
    print(f"✅ Generated {inventory_file}")
    print(f"   Size: {len(inventory_md)} bytes")

    # Auto-update README.md counts
    update_readme_counts()

if __name__ == "__main__":
    main()
