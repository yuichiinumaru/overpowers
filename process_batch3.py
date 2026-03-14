import os
import re

files_to_process = [
    {
        "old_path": ".archive/staging/skills/xhs-auto-content-by-hot_SKILL.md",
        "new_name": "content-media-xhs-auto-content-by-hot",
        "desc": "全自动生成小红书内容：获取百度热门话题 → 生成文案 → Seedream-4.5生图 → 输出图片+文案",
        "tags": "['social-media', 'rednote', 'content-generation', 'image-generation']",
        "author": "Matianle"
    },
    {
        "old_path": ".archive/staging/skills/txt-to-epub_SKILL.md",
        "new_name": "data-transform-txt-to-epub",
        "desc": "将txt文本转换为epub文件，使用纯规则进行章节识别与分割。适用于小说、教程和一般长文，不内置AI接口。",
        "tags": "['text-processing', 'epub', 'converter']"
    },
    {
        "old_path": ".archive/staging/skills/api-monitor_SKILL.md",
        "new_name": "infra-ops-api-monitor",
        "desc": "API 配额监控与手动切换技能。监控 OpenClaw 模型 API 使用量，配额不足时询问用户确认后再切换。",
        "tags": "['monitoring', 'api', 'quota', 'ops']"
    },
    {
        "old_path": ".archive/staging/skills/qqbot-prompt-optimizer_SKILL.md",
        "new_name": "ai-llm-qqbot-prompt-optimizer",
        "desc": "OpenClaw QQBot 个性化提示词优化工具。可以解决 QQ Bot 回复太官方、太傻逼的问题，让 AI 回复更符合用户自己的性格。",
        "tags": "['qqbot', 'prompt', 'personalization']",
        "metadata": "metadata:\n  clawdbot:\n    emoji: 🤖\n  github:\n    repo: openclaw/qqbot-prompt-optimizer"
    },
    {
        "old_path": ".archive/staging/skills/server-maintenance_SKILL.md",
        "new_name": "infra-ops-server-maintenance",
        "desc": "自动化服务器维护工具。检查磁盘使用率、清理缓存、优化系统资源。支持多服务器批量操作。",
        "tags": "['server', 'maintenance', 'cleanup', 'ops']"
    }
]

skipped_files = []

task_file = ".docs/tasks/0500-extraction-skills-batch-003.md"
with open(task_file, "r") as f:
    task_content = f.read()

for item in files_to_process:
    if not os.path.exists(item["old_path"]):
        continue
    with open(item["old_path"], "r") as f:
        content = f.read()
    
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL).strip()
    
    extra = ""
    if "author" in item:
        extra += f"\nauthor: {item['author']}"
    if "metadata" in item:
        extra += f"\n{item['metadata']}"

    new_frontmatter = f"""---
name: {item['new_name']}
description: {item['desc']}
tags:
{chr(10).join(['  - ' + t for t in eval(item['tags'])])}
version: 1.0.0{extra}
---

"""
    new_content = new_frontmatter + content
    new_dir = f"skills/{item['new_name']}"
    os.makedirs(new_dir, exist_ok=True)
    with open(f"{new_dir}/SKILL.md", "w") as f:
        f.write(new_content)
    
    os.remove(item["old_path"])
    task_content = task_content.replace(f"- [ ] `{item['old_path']}`", f"- [x] `{item['old_path']}`")

for skipped in skipped_files:
    if os.path.exists(skipped):
        os.remove(skipped)
    task_content = task_content.replace(f"- [ ] `{skipped}`", f"-[Skipped] `{skipped}`")

with open(task_file, "w") as f:
    f.write(task_content)
