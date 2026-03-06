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
    ("10/skills/python_development", "python_development"),
    ("10/skills/javascript_typescript", "javascript_typescript"),
    ("10/skills/backend_development", "backend_development"),
    ("10/skills/image_enhancer", "image_enhancer"),
    ("10/skills/invoice_organizer", "invoice_organizer"),
    ("10/skills/ask_questions_if_underspecified", "ask_questions_if_underspecified"),
    ("10/skills/jira_issues", "jira_issues"),
    
    # Visual Documentation (repo 20)
    ("20/visual-documentation-plugin/skills/flowchart_creator", "flowchart_creator"),
    ("20/visual-documentation-plugin/skills/architecture_diagram_creator", "architecture_diagram_creator"),
    ("20/visual-documentation-plugin/skills/dashboard_creator", "dashboard_creator"),
    ("20/visual-documentation-plugin/skills/technical_doc_creator", "technical_doc_creator"),
    ("20/visual-documentation-plugin/skills/timeline_creator", "timeline_creator"),
    
    # Engineering Workflow (repo 20)
    ("20/engineering-workflow-plugin/skills/test_fixing", "test_fixing"),
    ("20/engineering-workflow-plugin/skills/ensemble_solving", "ensemble_solving"),
    
    # Code Operations (repo 20)
    ("20/code-operations-plugin/skills/code_execution", "code_execution"),
    
    # Pydantic/DSPy úteis (repo 14, 15)
    ("14/examples/skills/web_research", "web_research"),
    ("14/examples/skills/arxiv_search", "arxiv_search"),
    
    # Prompt/skill tools (repo 17, 19)
    ("17/prompt_optimizer", "prompt_optimizer"),
    ("19/.skills/experimental/skill_evaluator", "skill_evaluator"),
    
    # Outros úteis
    ("10/skills/domain_name_brainstormer", "domain_name_brainstormer"),
    ("10/skills/lead_research_assistant", "lead_research_assistant"),
    ("10/skills/developer_growth_analysis", "developer_growth_analysis"),
    ("10/skills/slack_gif_creator", "slack_gif_creator"),
    ("10/skills/video_downloader", "video_downloader"),
    
    # Sentry skills (se existirem)
    ("51/plugins/sentry-skills/skills/code_review", "sentry-code-review"),
    ("51/plugins/sentry-skills/skills/find-bugs", "find-bugs"),
    ("51/plugins/sentry-skills/skills/deslop", "deslop"),
    
    # Trail of Bits security
    ("45/plugins/building-secure-contracts", "building-secure-contracts"),
    ("45/plugins/static-analysis", "static-analysis"),
    ("45/plugins/property-based-testing", "property-based-testing"),
    
    # Overpowers skills (yuichiinumaru/overpowers)
    ("48/skills/test_driven_development", "test_driven_development"),
    ("48/skills/systematic_debugging", "systematic_debugging"),
    ("48/skills/root-cause-tracing", "root-cause-tracing"),
    ("48/skills/brainstorming", "brainstorming"),
    ("48/skills/writing_plans", "writing_plans"),
    ("48/skills/executing_plans", "executing_plans"),
    ("48/skills/dispatching_parallel_agents", "dispatching_parallel_agents"),
    ("48/skills/verification_before_completion", "verification_before_completion"),
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
