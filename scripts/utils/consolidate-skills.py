#!/usr/bin/env python3
"""
Script para descobrir e consolidar skills de múltiplos repos.
Varre todos os subdiretórios buscando SKILL.md, extrai metadados e consolida.
"""

import os
import re
import json
import shutil
from pathlib import Path
from collections import defaultdict

SKILL_DIR = Path("/home/sephiroth/.config/opencode/skill")
OUTPUT_DIR = SKILL_DIR / "_consolidated"
REPORT_FILE = SKILL_DIR / "skills-report.json"

# Skills prioritárias (Top 40)
PRIORITY_SKILLS = {
    # Dev
    "code_review", "code_refactoring", "code_documentation", "refactoring",
    # Testing
    "playwright", "webapp_testing", "qa_regression",
    # Docs
    "pdf", "docx", "pptx", "xlsx", "doc_coauthoring",
    # Cloud/Infra
    "aws", "terraform", "kubernetes", "mcp_builder",
    # Design
    "brand_guidelines", "frontend_design", "canvas_design", "theme_factory", "web_design_guidelines",
    # Productivity
    "skill_creator", "changelog_generator", "file_organizer",
    # Mobile
    "expo_app_design", "expo_deployment", "upgrading_expo", "ios-simulator",
    # Security
    "security", "audit",
    # Data
    "database_design", "csv", "data",
    # AI/LLM
    "llm_application_dev", "algorithmic_art",
    # React/Web
    "react_best_practices", "web_artifacts_builder", "vercel_deploy",
    # Misc
    "internal_comms", "content_research_writer", "meeting_insights_analyzer",
}


def extract_frontmatter(filepath: Path) -> dict:
    """Extrai metadados YAML do frontmatter de SKILL.md"""
    try:
        content = filepath.read_text(encoding='utf-8')
        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if match:
            frontmatter = {}
            for line in match.group(1).split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()
            return frontmatter
    except Exception as e:
        print(f"  ⚠ Erro lendo {filepath}: {e}")
    return {}


def discover_skills():
    """Descobre todas as skills nos repos clonados"""
    skills = []
    seen_names = set()
    
    print("🔍 Descobrindo skills...")
    
    for repo_dir in sorted(SKILL_DIR.iterdir()):
        if not repo_dir.is_dir() or repo_dir.name.startswith('_'):
            continue
            
        # Busca SKILL.md recursivamente
        for skill_file in repo_dir.rglob("SKILL.md"):
            skill_dir = skill_file.parent
            frontmatter = extract_frontmatter(skill_file)
            
            name = frontmatter.get('name', skill_dir.name)
            description = frontmatter.get('description', '')
            
            # Pular duplicatas
            if name in seen_names:
                continue
            seen_names.add(name)
            
            # Verificar se é prioritária
            is_priority = any(p in name.lower() for p in PRIORITY_SKILLS)
            
            skills.append({
                'name': name,
                'description': description[:200] if description else '',
                'source_dir': str(skill_dir),
                'repo': repo_dir.name,
                'has_scripts': (skill_dir / 'scripts').exists(),
                'has_references': (skill_dir / 'references').exists(),
                'has_assets': (skill_dir / 'assets').exists(),
                'priority': is_priority,
            })
            
            print(f"  {'⭐' if is_priority else '○'} {name} ({repo_dir.name})")
    
    return skills


def consolidate_skills(skills: list):
    """Consolida skills prioritárias para diretório unificado"""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    priority_skills = [s for s in skills if s['priority']]
    print(f"\n📦 Consolidando {len(priority_skills)} skills prioritárias...")
    
    consolidated = []
    
    for skill in priority_skills:
        src = Path(skill['source_dir'])
        dst = OUTPUT_DIR / skill['name']
        
        # Pular se já existe
        if dst.exists():
            print(f"  ⏭ {skill['name']} (já existe)")
            continue
        
        try:
            # Copiar diretório inteiro
            shutil.copytree(src, dst, dirs_exist_ok=True)
            
            # Remover .git se existir
            git_dir = dst / '.git'
            if git_dir.exists():
                shutil.rmtree(git_dir)
                
            print(f"  ✓ {skill['name']}")
            consolidated.append(skill['name'])
            
        except Exception as e:
            print(f"  ✗ {skill['name']}: {e}")
    
    return consolidated


def generate_report(skills: list, consolidated: list):
    """Gera relatório JSON"""
    report = {
        'total_discovered': len(skills),
        'total_priority': len([s for s in skills if s['priority']]),
        'total_consolidated': len(consolidated),
        'consolidated_skills': consolidated,
        'all_skills': skills,
    }
    
    REPORT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\n📄 Relatório salvo em: {REPORT_FILE}")
    return report


def main():
    print("=" * 60)
    print("🛠  OpenCode Skills Consolidator")
    print("=" * 60)
    
    # Descobrir
    skills = discover_skills()
    print(f"\n📊 Total descoberto: {len(skills)} skills")
    print(f"⭐ Prioritárias: {len([s for s in skills if s['priority']])}")
    
    # Consolidar
    consolidated = consolidate_skills(skills)
    
    # Relatório
    report = generate_report(skills, consolidated)
    
    print("\n" + "=" * 60)
    print(f"✅ Concluído! {len(consolidated)} skills consolidadas em:")
    print(f"   {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
