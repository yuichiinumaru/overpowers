import os
import re

files_to_process = [
    {
        "old_path": ".archive/staging/skills/tg-mysql-design_SKILL.md",
        "new_name": "data-sci-tg-mysql-design",
        "desc": "MySQL数据库设计助手。根据业务规则文档和存量SQL DDL脚本，设计符合阿里巴巴规范的MySQL 5.7/8.0建表语句。",
        "tags": "['mysql', 'database-design', 'ddl', 'alibaba-spec']"
    },
    {
        "old_path": ".archive/staging/skills/auto-logger_SKILL.md",
        "new_name": "infra-ops-auto-logger",
        "desc": "自动记录日常活动、对话摘要、重要事件到 memory 目录。支持定时记录、事件触发记录、每日总结。",
        "tags": "['logging', 'memory', 'automation', 'daily-summary']"
    },
    {
        "old_path": ".archive/staging/skills/cn-daily-tools_SKILL.md",
        "new_name": "general-tool-cn-daily-tools",
        "desc": "中文日常工具集：天气预报、汇率查询、新闻摘要、快递追踪。适合中文用户日常使用，无需API密钥，开箱即用。",
        "tags": "['daily-tools', 'weather', 'currency', 'news', 'tracking']"
    },
    {
        "old_path": ".archive/staging/skills/web-learner-1-0-0_SKILL.md",
        "new_name": "ai-llm-web-learner",
        "desc": "自主上网学习技能 - 让 AI 能够主动搜索、浏览和从互联网获取知识。",
        "tags": "['web-learning', 'search', 'fetch', 'browsing']"
    },
    {
        "old_path": ".archive/staging/skills/feishu-user-md_SKILL.md",
        "new_name": "infra-ops-feishu-user-md",
        "desc": "飞书端读取USER.md任务清单。实时解析并返回格式化的分类任务列表，让用户快速了解当前所有可用任务和技能。",
        "tags": "['feishu', 'task-list', 'user-md', 'parsing']",
        "extra": "author: 349840432m-dev\nlicense: MIT\nacceptLicenseTerms: true\nmetadata:\n  clawdbot:\n    emoji: \"📋\"\n    files: [\"scripts/*\"]"
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
    if "extra" in item:
        extra = "\n" + item["extra"]

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
