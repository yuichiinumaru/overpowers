import os
import re

missing_skills = [
    "skills/sec-safety-1114-stripe-integration",
    "skills/sec-safety-1116-swarm-advanced",
    "skills/sec-safety-1117-systematic-debugging",
    "skills/sec-safety-1118-task-coordination-strategies",
    "skills/sec-safety-1119-team-composition-patterns",
    "skills/sec-safety-1129-uspto-database"
]

for folder in missing_skills:
    skill_file = os.path.join(folder, "SKILL.md")
    if os.path.exists(skill_file):
        with open(skill_file, 'r') as f:
            content = f.read()
            
        scripts_dir = os.path.join(folder, "scripts")
        if not os.path.exists(scripts_dir):
            continue
            
        scripts = os.listdir(scripts_dir)
        
        # Check if "## Helper Scripts" exists
        if "## Helper Scripts" not in content and len(scripts) > 0:
            helper_scripts_section = "\n## Helper Scripts\n\nThis skill includes helper scripts to facilitate operations:\n\n"
            for script in scripts:
                helper_scripts_section += f"- **scripts/{script}**: Utility script for {script.split('.')[0].replace('_', ' ')}.\n"
                
            helper_scripts_section += "\nUsage:\n```bash\n"
            for script in scripts:
                if script.endswith('.py'):
                    helper_scripts_section += f"python3 scripts/{script}\n"
                elif script.endswith('.sh'):
                    helper_scripts_section += f"./scripts/{script}\n"
                elif script.endswith('.js'):
                    helper_scripts_section += f"node scripts/{script}\n"
            helper_scripts_section += "```\n"
            
            # append before ## Best Practices or at the end
            if "## Best Practices" in content:
                content = content.replace("## Best Practices", helper_scripts_section + "\n## Best Practices")
            elif "## Related" in content:
                 content = content.replace("## Related", helper_scripts_section + "\n## Related")
            else:
                content += "\n" + helper_scripts_section
                
            with open(skill_file, 'w') as f:
                f.write(content)
                
            print(f"Updated {skill_file} with Helper Scripts section")
        else:
            print(f"Helper Scripts already in {skill_file} or no scripts found.")
            
