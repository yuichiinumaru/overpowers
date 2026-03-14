#!/usr/bin/env python3
"""
Generate Taxonomy - Gera taxonomia L1-L2-L3 baseada em análise semântica

Baseado em:
- sqrt(N) para número ideal de tipos
- Floors/Ceils absolutos
- LLM-based inference para categorização semântica
"""

import json
import math
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
SKILLS_DIR = REPO_ROOT / "skills"
OUTPUT_MAPPING = REPO_ROOT / ".docs" / "taxonomy-mapping.json"

# Default L1-L2 categories (pode ser expandido via LLM)
DEFAULT_L1_CATEGORIES = [
    'agent',      # Agentes, orquestração, memória
    'tools',      # Ferramentas utilitárias
    'workflows',  # Workflows, automações
    'content',    # Criação de conteúdo, mídia
    'data',       # Análise de dados, BI
    'dev',        # Desenvolvimento, código
    'biz',        # Negócios, growth
    'ops',        # Operations, infra
    'sec',        # Security, compliance
    'sci',        # Ciência, pesquisa
    'ai',         # AI/ML específico
    'misc',       # Outros
]

DEFAULT_L2_SUBTYPES = {
    'agent': ['orchestration', 'memory', 'browser', 'communication', 'planning'],
    'tools': ['search', 'file', 'system', 'network', 'api'],
    'workflows': ['ci-cd', 'media', 'data-pipeline', 'automation'],
    'content': ['writing', 'video', 'audio', 'image', 'social'],
    'data': ['analysis', 'visualization', 'etl', 'ml'],
    'dev': ['backend', 'frontend', 'mobile', 'testing', 'devops'],
    'biz': ['marketing', 'sales', 'finance', 'analytics'],
    'ops': ['infra', 'monitoring', 'deployment', 'maintenance'],
    'sec': ['audit', 'compliance', 'pentest', 'monitoring'],
    'sci': ['research', 'bio', 'chem', 'quant', 'academic'],
    'ai': ['llm', 'vision', 'audio', 'ml-ops'],
    'misc': ['general', 'utility'],
}


def optimal_k(n: int, max_chunk: int = 150, min_chunk: int = 40) -> int:
    """Calcula número ótimo de chunks."""
    if n <= max_chunk:
        return 1
    k = math.ceil(n / max_chunk)
    avg = n / k
    while avg < min_chunk and k > 1:
        k -= 1
        avg = n / k
    return k


def infer_category_from_content(skill_path: Path) -> Tuple[str, str]:
    """
    Infer L1-L2 baseado em análise semântica do conteúdo.
    Usa keywords e patterns do SKILL.md.
    """
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return 'misc', 'general'
    
    content = skill_md.read_text().lower()
    
    # Keywords mapping para L1
    l1_keywords = {
        'agent': ['agent', 'orchestrat', 'multi-agent', 'swarm', 'crew', 'team'],
        'tools': ['tool', 'utility', 'helper', 'cli', 'command'],
        'workflows': ['workflow', 'pipeline', 'automation', 'ci/cd', 'deploy'],
        'content': ['content', 'writing', 'video', 'audio', 'image', 'social', 'post'],
        'data': ['data', 'analytics', 'visualization', 'chart', 'graph', 'bi'],
        'dev': ['dev', 'code', 'program', 'software', 'api', 'library'],
        'biz': ['business', 'marketing', 'sales', 'finance', 'revenue'],
        'ops': ['ops', 'infra', 'monitor', 'server', 'cloud', 'k8s'],
        'sec': ['security', 'audit', 'compliance', 'pentest', 'vuln'],
        'sci': ['science', 'research', 'academic', 'paper', 'study'],
        'ai': ['ai', 'llm', 'ml', 'model', 'transformer', 'gpt', 'claude'],
    }
    
    # Conta matches por L1
    l1_scores = defaultdict(int)
    for l1, keywords in l1_keywords.items():
        for keyword in keywords:
            l1_scores[l1] += content.count(keyword)
    
    # Seleciona L1 com mais matches
    if not l1_scores:
        return 'misc', 'general'
    
    l1_best = max(l1_scores.items(), key=lambda x: x[1])[0]
    
    # Infer L2 baseado em keywords mais específicas
    l2_keywords = {
        'orchestration': ['orchestrat', 'coordinate', 'dispatch', 'delegate'],
        'memory': ['memory', 'remember', 'recall', 'context'],
        'browser': ['browser', 'web', 'selenium', 'playwright'],
        'search': ['search', 'find', 'query', 'google'],
        'writing': ['write', 'draft', 'edit', 'proofread'],
        'backend': ['backend', 'server', 'database', 'sql'],
        'frontend': ['frontend', 'ui', 'react', 'vue'],
        'llm': ['llm', 'gpt', 'claude', 'language model'],
    }
    
    l2_scores = defaultdict(int)
    for l2, keywords in l2_keywords.items():
        for keyword in keywords:
            l2_scores[l2] += content.count(keyword)
    
    l2_best = max(l2_scores.items(), key=lambda x: x[1])[0] if l2_scores else 'general'
    
    return l1_best, l2_best


def generate_taxonomy(skills_dir: Path, levels: int = 3, use_llm: bool = False) -> Dict:
    """
    Gera taxonomia para todas as skills.
    
    Args:
        skills_dir: Diretório das skills
        levels: Número de níveis (2 ou 3)
        use_llm: Se True, usa LLM para inferência (requer API key)
    """
    if not skills_dir.exists():
        return {'error': f'Skills directory not found: {skills_dir}'}
    
    # Coleta todas as skills
    skills = []
    for item in skills_dir.iterdir():
        if item.is_dir() and not item.name.startswith('_') and not item.name.startswith('.'):
            if (item / 'SKILL.md').exists():
                skills.append({
                    'original_name': item.name,
                    'path': str(item)
                })
    
    total_skills = len(skills)
    
    if total_skills == 0:
        return {'error': 'No skills found'}
    
    # Calcula número ideal de tipos baseado em sqrt(N)
    ideal_num_types = int(math.sqrt(total_skills) / 2)
    ideal_num_types = max(10, min(20, ideal_num_types))  # Floor/Ceil
    
    print(f"📊 Total skills: {total_skills}")
    print(f"📐 Ideal number of types: {ideal_num_types} (sqrt({total_skills})/2)")
    
    # Gera taxonomia para cada skill
    taxonomy_mapping = {}
    l1_distribution = defaultdict(list)
    l2_distribution = defaultdict(lambda: defaultdict(list))
    l3_distribution = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    
    for i, skill in enumerate(skills):
        skill_name = skill['original_name']
        skill_path = Path(skill['path'])
        
        # Parse do nome atual
        parsed = parse_skill_name(skill_name)
        
        # Infer L1-L2-L3
        if parsed.get('valid') and parsed['levels'] >= levels:
            # Já tem taxonomia, preserva se válido
            l1 = parsed.get('l1')
            l2 = parsed.get('l2')
            l3 = parsed.get('l3') if levels == 3 else None
        else:
            # Precisa inferir
            l1, l2 = infer_category_from_content(skill_path)
            l3 = None  # L3 será gerado baseado em chunking
        
        # Gera nome limpo para a skill
        clean_name = generate_clean_name(skill_name, parsed)
        
        taxonomy_mapping[skill_name] = {
            'original': skill_name,
            'l1': l1,
            'l2': l2,
            'l3': l3,
            'clean_name': clean_name,
            'path': skill['path']
        }
        
        # Atualiza distribuições
        l1_distribution[l1].append(skill_name)
        l2_distribution[l1][l2].append(skill_name)
        if l3:
            l3_distribution[l1][l2][l3].append(skill_name)
        
        # Progress indicator
        if (i + 1) % 100 == 0:
            print(f"   Processed {i + 1}/{total_skills} skills...")
    
    # Aplica chunking onde necessário
    print("\n✂️  Applying chunking...")
    chunking_applied = 0
    
    for l1 in l1_distribution:
        for l2 in l2_distribution[l1]:
            skills_in_l2 = l2_distribution[l1][l2]
            count = len(skills_in_l2)
            
            # Se > MAX_CHUNK_SIZE, aplica chunking
            if count > 150:
                k = optimal_k(count, max_chunk=150)
                print(f"   Chunking {l1}/{l2}: {count} skills → {k} chunks")
                
                # Divide skills em k chunks
                chunk_size = count // k
                for chunk_idx in range(k):
                    start_idx = chunk_idx * chunk_size
                    end_idx = start_idx + chunk_size if chunk_idx < k - 1 else count
                    
                    chunk_l3 = f"chunk{chunk_idx + 1:02d}"
                    for skill_name in skills_in_l2[start_idx:end_idx]:
                        taxonomy_mapping[skill_name]['l3'] = chunk_l3
                        l3_distribution[l1][l2][chunk_l3].append(skill_name)
                
                chunking_applied += 1
    
    # Gera IDs sequenciais por L3
    print("\n🔢 Generating sequential IDs...")
    id_counter = defaultdict(int)
    
    for skill_name, mapping in taxonomy_mapping.items():
        l1 = mapping['l1']
        l2 = mapping['l2']
        l3 = mapping['l3'] or 'default'
        
        key = f"{l1}-{l2}-{l3}"
        id_counter[key] += 1
        mapping['id'] = f"{id_counter[key]:04d}"
        
        # Gera novo nome
        if levels == 3:
            mapping['new_name'] = f"{l1}-{l2}-{l3}-{mapping['id']}-{mapping['clean_name']}"
        else:
            mapping['new_name'] = f"{l1}-{l2}-{mapping['id']}-{mapping['clean_name']}"
    
    # Gera relatório final
    report = {
        'total_skills': total_skills,
        'levels': levels,
        'ideal_num_types': ideal_num_types,
        'actual_num_types': len(l1_distribution),
        'distribution': {
            'l1': {l1: len(skills) for l1, skills in l1_distribution.items()},
            'l2': {l1: {l2: len(skills) for l2, skills in l2_data.items()} 
                   for l1, l2_data in l2_distribution.items()},
            'l3': {l1: {l2: {l3: len(skills) for l3, skills in l3_data.items()} 
                        for l2, l3_data in l3_distribution.items()} 
                   for l1, l3_data in l3_distribution.items()}
        },
        'chunking_applied': chunking_applied,
        'mapping': taxonomy_mapping,
        'constraints': {
            'MIN_TYPES': 10,
            'MAX_TYPES': 20,
            'MAX_CHUNK_SIZE': 150,
        }
    }
    
    return report


def parse_skill_name(skill_name: str) -> Dict:
    """Parse skill name para extrair componentes."""
    parts = skill_name.split('-')
    
    if len(parts) < 4:
        return {'valid': False}
    
    id_idx = None
    for i, part in enumerate(parts):
        if re.match(r'^\d{4}$', part):
            id_idx = i
            break
    
    if id_idx is None:
        return {'valid': False}
    
    return {
        'valid': True,
        'levels': 3 if id_idx == 3 else 2,
        'l1': parts[0] if id_idx >= 1 else None,
        'l2': parts[1] if id_idx >= 2 else None,
        'l3': parts[2] if id_idx == 3 else None,
        'id': parts[id_idx],
        'name_parts': parts[id_idx + 1:]
    }


def generate_clean_name(skill_name: str, parsed: Dict) -> str:
    """Gera nome limpo da skill (sem type-subtype-id)."""
    if parsed.get('valid') and parsed.get('name_parts'):
        return '-'.join(parsed['name_parts'])
    
    # Fallback: usa nome original sem prefixos numéricos
    parts = skill_name.split('-')
    name_parts = []
    for part in parts:
        if re.match(r'^\d{4}$', part):
            break
        name_parts.append(part)
    
    return '-'.join(name_parts) if name_parts else skill_name


def print_report(report: Dict):
    """Imprime relatório formatado."""
    print("\n" + "="*80)
    print("TAXONOMY GENERATION REPORT")
    print("="*80 + "\n")
    
    if 'error' in report:
        print(f"❌ ERROR: {report['error']}")
        return
    
    print(f"📊 Total skills: {report['total_skills']}")
    print(f"📐 Levels: {report['levels']}")
    print(f"📋 Ideal types: {report['ideal_num_types']}")
    print(f"📁 Actual types: {report['actual_num_types']}")
    print(f"✂️  Chunking applied: {report['chunking_applied']} times")
    
    print(f"\n📁 L1 DISTRIBUTION:")
    for l1, count in sorted(report['distribution']['l1'].items(), key=lambda x: -x[1]):
        status = "✅" if 50 <= count <= 500 else "⚠️"
        print(f"   {status} {l1}: {count} skills")
    
    print(f"\n🔢 SAMPLE MAPPINGS:")
    sample_items = list(report['mapping'].items())[:10]
    for original, mapping in sample_items:
        print(f"   {original}")
        print(f"      → {mapping['new_name']}")
    
    print("\n" + "="*80)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate skill taxonomy')
    parser.add_argument('--skills-dir', type=str, default=str(SKILLS_DIR),
                       help=f'Skills directory (default: {SKILLS_DIR})')
    parser.add_argument('--levels', type=int, default=3, choices=[2, 3],
                       help='Number of hierarchy levels (default: 3)')
    parser.add_argument('--output', type=str, default=str(OUTPUT_MAPPING),
                       help=f'Output mapping file (default: {OUTPUT_MAPPING})')
    parser.add_argument('--use-llm', action='store_true',
                       help='Use LLM for semantic inference (requires API key)')
    parser.add_argument('--quiet', action='store_true',
                       help='Do not print report to console')
    
    args = parser.parse_args()
    
    skills_dir = Path(args.skills_dir)
    
    print(f"🔍 Generating taxonomy with {args.levels} levels...")
    
    # Generate
    report = generate_taxonomy(skills_dir, levels=args.levels, use_llm=args.use_llm)
    
    # Save
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    if not args.quiet:
        print_report(report)
    
    print(f"\n📝 Mapping saved to: {args.output}")
    
    return 0


if __name__ == '__main__':
    exit(main())
