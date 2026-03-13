import os
import glob
import re

skills = [
    "content-media-3d",
    "content-media-accessibility",
    "content-media-accessibility-auditor",
    "content-media-accessibility-compliance",
    "content-media-animations",
    "content-media-assets",
    "content-media-audio",
    "content-media-baoyu-compress-image",
    "content-media-birdnet",
    "content-media-calculate-metadata",
    "content-media-camsnap",
    "content-media-can-decode",
    "content-media-canvas-design",
    "content-media-charts",
    "content-media-compositions",
    "content-media-content-creation",
    "content-media-content-shipped",
    "content-media-create-blog-post",
    "content-media-design-md",
    "content-media-design-system-starter"
]

for skill in skills:
    skill_path = os.path.join("skills", skill, "SKILL.md")
    if os.path.exists(skill_path):
        with open(skill_path, 'r') as f:
            content = f.read()
            # find bash, sh, .py, python, curl, node, npm inside the content
            matches = re.findall(r'```(?:bash|sh).*?\n(.*?)```', content, re.DOTALL)
            scripts_mentioned = re.findall(r'scripts/.*?\.py|scripts/.*?\.sh|[\w-]+\.sh|[\w-]+\.py', content)
            
            print(f"=== {skill} ===")
            if matches:
                print("Bash blocks found:")
                for m in matches:
                    print(m.strip())
            if scripts_mentioned:
                print("Scripts mentioned:", set(scripts_mentioned))
            print()
