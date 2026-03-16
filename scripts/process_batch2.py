import os
import re
import shutil

skills_data = [
    {
        "staging_path": ".archive/staging/skills/frontend-slides_SKILL.md",
        "name": "design-ux-frontend-slides",
        "description": "从零开始或通过转换PowerPoint文件创建令人惊艳、动画丰富的HTML演示文稿。当用户想要构建演示文稿、将PPT/PPTX转换为网页格式，或为演讲/推介创建幻灯片时使用。帮助非设计师通过视觉探索而非抽象选择发现他们的美学。",
        "tags": ["design", "ux", "slides", "presentation", "html"],
        "folder": "skills/design-ux-frontend-slides"
    },
    {
        "staging_path": ".archive/staging/skills/investor-materials_SKILL.md",
        "name": "growth-biz-investor-materials",
        "description": "创建和更新宣传文稿、一页简介、投资者备忘录、加速器申请、财务模型和融资材料。当用户需要面向投资者的文件、预测、资金用途表、里程碑计划或必须在多个融资资产中保持内部一致性的材料时使用。",
        "tags": ["growth", "biz", "investor", "pitch", "materials"],
        "folder": "skills/growth-biz-investor-materials"
    },
    {
        "staging_path": ".archive/staging/skills/investor-outreach_SKILL.md",
        "name": "growth-biz-investor-outreach",
        "description": "草拟冷邮件、热情介绍简介、跟进邮件、更新邮件和投资者沟通以筹集资金。当用户需要向天使投资人、风险投资公司、战略投资者或加速器进行推广，并需要简洁、个性化的面向投资者的消息时使用。",
        "tags": ["growth", "biz", "investor", "outreach", "email"],
        "folder": "skills/growth-biz-investor-outreach"
    },
    {
        "staging_path": ".archive/staging/skills/liquid-glass-design_SKILL.md",
        "name": "design-ux-liquid-glass-design",
        "description": "iOS 26 液态玻璃设计系统 — 适用于 SwiftUI、UIKit 和 WidgetKit 的动态玻璃材质，具有模糊、反射和交互式变形效果。",
        "tags": ["design", "ux", "ios", "swiftui", "liquid-glass"],
        "folder": "skills/design-ux-liquid-glass-design"
    },
    {
        "staging_path": ".archive/staging/skills/market-research_SKILL.md",
        "name": "growth-biz-market-research",
        "description": "进行市场研究、竞争分析、投资者尽职调查和行业情报，附带来源归属和决策导向的摘要。适用于用户需要市场规模、竞争对手比较、基金研究、技术扫描或为商业决策提供信息的研究时。",
        "tags": ["growth", "biz", "research", "market", "analysis"],
        "folder": "skills/growth-biz-market-research"
    },
    {
        "staging_path": ".archive/staging/skills/nanoclaw-repl_SKILL.md",
        "name": "infra-ops-nanoclaw-repl",
        "description": "操作并扩展NanoClaw v2，这是ECC基于claude -p构建的零依赖会话感知REPL。",
        "tags": ["infra", "ops", "nanoclaw", "repl", "claude"],
        "folder": "skills/infra-ops-nanoclaw-repl"
    },
    {
        "staging_path": ".archive/staging/skills/plankton-code-quality_SKILL.md",
        "name": "dev-code-plankton-code-quality",
        "description": "使用Plankton进行编写时代码质量强制执行——通过钩子在每次文件编辑时自动格式化、代码检查和Claude驱动的修复。",
        "tags": ["dev", "code", "quality", "plankton", "linting"],
        "folder": "skills/dev-code-plankton-code-quality"
    },
    {
        "staging_path": ".archive/staging/skills/ralphinho-rfc-pipeline_SKILL.md",
        "name": "dev-code-ralphinho-rfc-pipeline",
        "description": "基于RFC驱动的多智能体DAG执行模式，包含质量门、合并队列和工作单元编排。",
        "tags": ["dev", "code", "rfc", "pipeline", "agent"],
        "folder": "skills/dev-code-ralphinho-rfc-pipeline"
    },
    {
        "staging_path": ".archive/staging/skills/regex-vs-llm-structured-text_SKILL.md",
        "name": "dev-code-regex-vs-llm-structured-text",
        "description": "选择在解析结构化文本时使用正则表达式还是大型语言模型的决策框架——从正则表达式开始，仅在低置信度的边缘情况下添加大型语言模型。",
        "tags": ["dev", "code", "parsing", "regex", "llm"],
        "folder": "skills/dev-code-regex-vs-llm-structured-text"
    },
    {
        "staging_path": ".archive/staging/skills/skill-stocktake_SKILL.md",
        "name": "infra-ops-skill-stocktake",
        "description": "用于审计Claude技能和命令的质量。支持快速扫描（仅变更技能）和全面盘点模式，采用顺序子代理批量评估。",
        "tags": ["infra", "ops", "skill", "stocktake", "audit"],
        "folder": "skills/infra-ops-skill-stocktake"
    }
]

for skill in skills_data:
    staging_path = skill["staging_path"]
    if not os.path.exists(staging_path):
        print(f"File not found: {staging_path}")
        continue
        
    with open(staging_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip existing frontmatter
    content = re.sub(r'^---\n.*?\n---\n*', '', content, flags=re.DOTALL)
    
    # Generate new frontmatter
    frontmatter = f"""---
name: {skill['name']}
description: {skill['description']}
tags: [{', '.join(skill['tags'])}]
version: 1.0.0
---

"""
    
    final_content = frontmatter + content
    
    # Create folder and save
    os.makedirs(skill['folder'], exist_ok=True)
    with open(os.path.join(skill['folder'], 'SKILL.md'), 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    # Delete staged file
    os.remove(staging_path)

# Update task list
task_file = '.docs/tasks/0500-extraction-skills-batch-002.md'
with open(task_file, 'r', encoding='utf-8') as f:
    task_content = f.read()

for skill in skills_data:
    filename = os.path.basename(skill["staging_path"])
    # Replace [ ] with [x]
    task_content = re.sub(
        r'\[ \] `\.archive/staging/skills/' + re.escape(filename) + '`',
        r'[x] `.archive/staging/skills/' + filename + '`',
        task_content
    )

with open(task_file, 'w', encoding='utf-8') as f:
    f.write(task_content)

print("Processed 10 items successfully.")
