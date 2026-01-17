#!/usr/bin/env python3
"""
Segunda passada: consolidar skills adicionais de alto valor.
"""

import os
import shutil
from pathlib import Path

SKILL_DIR = Path("/home/sephiroth/.config/opencode/skill")

# Skills adicionais de alto valor (não pegas na primeira passada)
ADDITIONAL_SKILLS = [
    # Desenvolvimento
    ("10/skills/python-development", "python-development"),
    ("10/skills/javascript-typescript", "javascript-typescript"),
    ("10/skills/backend-development", "backend-development"),
    ("10/skills/image-enhancer", "image-enhancer"),
    ("10/skills/invoice-organizer", "invoice-organizer"),
    ("10/skills/ask-questions-if-underspecified", "ask-questions-if-underspecified"),
    ("10/skills/jira-issues", "jira-issues"),
    
    # Visual Documentation (repo 20)
    ("20/visual-documentation-plugin/skills/flowchart-creator", "flowchart-creator"),
    ("20/visual-documentation-plugin/skills/architecture-diagram-creator", "architecture-diagram-creator"),
    ("20/visual-documentation-plugin/skills/dashboard-creator", "dashboard-creator"),
    ("20/visual-documentation-plugin/skills/technical-doc-creator", "technical-doc-creator"),
    ("20/visual-documentation-plugin/skills/timeline-creator", "timeline-creator"),
    
    # Engineering Workflow (repo 20)
    ("20/engineering-workflow-plugin/skills/test-fixing", "test-fixing"),
    ("20/engineering-workflow-plugin/skills/ensemble-solving", "ensemble-solving"),
    
    # Code Operations (repo 20)
    ("20/code-operations-plugin/skills/code-execution", "code-execution"),
    
    # Pydantic/DSPy úteis (repo 14, 15)
    ("14/examples/skills/web-research", "web-research"),
    ("14/examples/skills/arxiv-search", "arxiv-search"),
    
    # Prompt/skill tools (repo 17, 19)
    ("17/prompt-optimizer", "prompt-optimizer"),
    ("19/.skills/experimental/skill-evaluator", "skill-evaluator"),
    
    # Outros úteis
    ("10/skills/domain-name-brainstormer", "domain-name-brainstormer"),
    ("10/skills/lead-research-assistant", "lead-research-assistant"),
    ("10/skills/developer-growth-analysis", "developer-growth-analysis"),
    ("10/skills/slack-gif-creator", "slack-gif-creator"),
    ("10/skills/video-downloader", "video-downloader"),
    
    # Sentry skills (se existirem)
    ("51/plugins/sentry-skills/skills/code-review", "sentry-code-review"),
    ("51/plugins/sentry-skills/skills/find-bugs", "find-bugs"),
    ("51/plugins/sentry-skills/skills/deslop", "deslop"),
    
    # Trail of Bits security
    ("45/plugins/building-secure-contracts", "building-secure-contracts"),
    ("45/plugins/static-analysis", "static-analysis"),
    ("45/plugins/property-based-testing", "property-based-testing"),
    
    # Overpowers skills (obra/Overpowers)
    ("48/skills/test-driven-development", "test-driven-development"),
    ("48/skills/systematic-debugging", "systematic-debugging"),
    ("48/skills/root-cause-tracing", "root-cause-tracing"),
    ("48/skills/brainstorming", "brainstorming"),
    ("48/skills/writing-plans", "writing-plans"),
    ("48/skills/executing-plans", "executing-plans"),
    ("48/skills/dispatching-parallel-agents", "dispatching-parallel-agents"),
    ("48/skills/verification-before-completion", "verification-before-completion"),
]


def consolidate_additional():
    """Consolida skills adicionais"""
    print("=" * 60)
    print("🛠  Consolidando Skills Adicionais")
    print("=" * 60)
    
    consolidated = []
    skipped = []
    
    for src_rel, name in ADDITIONAL_SKILLS:
        src = SKILL_DIR / src_rel
        dst = SKILL_DIR / name
        
        # Verificar se já existe
        if dst.exists():
            print(f"  ⏭ {name} (já existe)")
            skipped.append(name)
            continue
        
        # Verificar se source existe
        if not src.exists():
            print(f"  ⚠ {name} (fonte não encontrada: {src_rel})")
            continue
        
        try:
            shutil.copytree(src, dst, dirs_exist_ok=True)
            
            # Remover .git
            git_dir = dst / '.git'
            if git_dir.exists():
                shutil.rmtree(git_dir)
            
            print(f"  ✓ {name}")
            consolidated.append(name)
            
        except Exception as e:
            print(f"  ✗ {name}: {e}")
    
    print("\n" + "=" * 60)
    print(f"✅ Consolidadas: {len(consolidated)}")
    print(f"⏭ Já existiam: {len(skipped)}")
    print("=" * 60)
    
    # Contar total de skills
    total = len([d for d in SKILL_DIR.iterdir() if d.is_dir() and not d.name.startswith(('_', '.')) and not d.name.isdigit()])
    print(f"\n📊 Total de skills disponíveis: {total}")


if __name__ == "__main__":
    consolidate_additional()
