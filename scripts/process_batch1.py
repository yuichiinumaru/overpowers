import os
import re

files_to_process = [
    {
        "old_path": ".archive/staging/skills/pdf-analyzer_SKILL.md",
        "new_name": "data-sci-pdf-analyzer",
        "desc": "Extract text from PDF files, summarize, and analyze the content. Useful when users upload PDFs or ask questions about PDF content.",
        "tags": "['pdf', 'data-extraction', 'analysis']"
    },
    {
        "old_path": ".archive/staging/skills/triple-layer-memory_SKILL.md",
        "new_name": "ai-llm-triple-layer-memory",
        "desc": "Triple-layer memory management system for AI agents (Mem0, File Layer, Session Management) to solve long-context memory loss and context management issues.",
        "tags": "['memory', 'context-management', 'agent']"
    },
    {
        "old_path": ".archive/staging/skills/douyin-cover-builder_SKILL.md",
        "new_name": "content-media-douyin-cover-builder",
        "desc": "这是一个面向中文创作者的 OpenClaw Skill，输入主题与人物气质后，会输出可直接用于生图模型的高质量提示词与创意说明。",
        "tags": "['design', 'thumbnail', 'cover', 'branding', 'prompt', 'douyin']",
        "extra": "user-invocable: true\ndisable-model-invocation: false"
    },
    {
        "old_path": ".archive/staging/skills/stock-watchlist_SKILL.md",
        "new_name": "growth-biz-stock-watchlist",
        "desc": "Query real-time stock prices, basic quote fields, and manage a Markdown watchlist for A-share, Hong Kong, and US stocks. Use when users ask in Chinese or by ticker/code to search stocks, inspect current price and quote basics, or maintain a watchlist stored in a Markdown file.",
        "tags": "['finance', 'stock', 'investment']"
    },
    {
        "old_path": ".archive/staging/skills/molt-solver_SKILL.md",
        "new_name": "general-tool-molt-solver",
        "desc": "自动解决 Moltbook 验证码难题的专家。提取数学题，计算结果并格式化输出。",
        "tags": "['captcha', 'automation', 'moltbook']"
    }
]

task_file = ".docs/tasks/0500-extraction-skills-batch-003.md"
with open(task_file, "r") as f:
    task_content = f.read()

for item in files_to_process:
    if not os.path.exists(item["old_path"]):
        continue
    with open(item["old_path"], "r") as f:
        content = f.read()
    
    # Remove old frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL).strip()
    
    extra = item.get("extra", "")
    if extra:
        extra = "\n" + extra
        
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

with open(task_file, "w") as f:
    f.write(task_content)
