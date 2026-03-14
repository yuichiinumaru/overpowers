#!/usr/bin/env python3
"""
Analyze Taxonomy - Analisa a distribuição atual de skills e identifica problemas

Baseado em: Information-theoretic approaches to taxonomy design
- Floors/Ceils absolutos previnem colapso semântico
- Filtro percentual (20%) é secundário
- Chunk size max 150 skills por L3
"""

import json
import math
import re
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
SKILLS_DIR = REPO_ROOT / "skills"
OUTPUT_REPORT = REPO_ROOT / ".docs" / "taxonomy-analysis-report.json"

# Floors/Ceils ABSOLUTOS (mais importantes que %)
# Baseado em: sqrt(N) para N skills
TAXONOMY_CONSTRAINTS = {
    'MIN_TYPES': 10,
    'MAX_TYPES': 20,
    'MIN_SKILLS_PER_TYPE': 50,
    'MAX_SKILLS_PER_TYPE': 500,
    'MIN_SUBTYPES_PER_TYPE': 4,
    'MAX_SUBTYPES_PER_TYPE': 20,
    'MIN_SKILLS_PER_SUBTYPE': 5,
    'MAX_SKILLS_PER_SUBTYPE': 80,  # 2.5× a média
    'MAX_CHUNK_SIZE': 150,  # Chunk size ideal para LLM attention
    'MIN_CHUNK_SIZE': 40,   # Mínimo para valer overhead
}


def parse_skill_name(skill_name: str) -> Dict:
    """
    Parse skill name no formato: L1-L2-L3-nnnn-skill-name
    ou: type-subtype-nnnn-name (2 níveis)
    """
    parts = skill_name.split('-')
    
    if len(parts) < 4:
        return {
            'valid': False,
            'error': 'Nome muito curto (precisa de pelo menos type-subtype-nnnn-name)',
            'original': skill_name
        }
    
    # Tenta detectar se tem ID de 4 dígitos
    id_idx = None
    for i, part in enumerate(parts):
        if re.match(r'^\d{4}$', part):
            id_idx = i
            break
    
    if id_idx is None:
        return {
            'valid': False,
            'error': 'Sem ID numérico de 4 dígitos',
            'original': skill_name
        }
    
    # Extrai componentes
    l1 = parts[0] if id_idx >= 1 else None
    l2 = parts[1] if id_idx >= 2 else None
    l3 = parts[2] if id_idx >= 3 else None
    skill_id = parts[id_idx]
    name_parts = parts[id_idx + 1:]
    
    # Determina número de níveis
    levels = 3 if l3 and id_idx == 3 else (2 if l2 and id_idx == 2 else 1)
    
    return {
        'valid': True,
        'levels': levels,
        'l1': l1,
        'l2': l2 if levels >= 2 else None,
        'l3': l3 if levels >= 3 else None,
        'id': skill_id,
        'name': '-'.join(name_parts),
        'original': skill_name
    }


def analyze_taxonomy(skills_dir: Path) -> Dict:
    """
    Analisa a taxonomia atual das skills.
    """
    if not skills_dir.exists():
        return {'error': f'Skills directory not found: {skills_dir}'}
    
    # Coleta todas as skills
    skills = []
    for item in skills_dir.iterdir():
        if item.is_dir() and not item.name.startswith('_') and not item.name.startswith('.'):
            # Verifica se tem SKILL.md (é uma skill válida)
            if (item / 'SKILL.md').exists():
                skills.append(item.name)
    
    total_skills = len(skills)
    
    if total_skills == 0:
        return {'error': 'No skills found'}
    
    # Analisa cada skill
    parsed_skills = []
    for skill_name in skills:
        parsed = parse_skill_name(skill_name)
        parsed['path'] = str(skills_dir / skill_name)
        parsed_skills.append(parsed)
    
    # Estatísticas de validade
    valid_skills = [s for s in parsed_skills if s.get('valid')]
    invalid_skills = [s for s in parsed_skills if not s.get('valid')]
    
    # Distribuição por níveis
    levels_distribution = defaultdict(int)
    for skill in valid_skills:
        levels_distribution[skill['levels']] += 1
    
    # Distribuição por L1 (type)
    l1_distribution = defaultdict(list)
    for skill in valid_skills:
        if skill.get('l1'):
            l1_distribution[skill['l1']].append(skill)
    
    # Distribuição por L2 (subtype)
    l2_distribution = defaultdict(lambda: defaultdict(list))
    for skill in valid_skills:
        if skill.get('l1') and skill.get('l2'):
            l2_distribution[skill['l1']][skill['l2']].append(skill)
    
    # Distribuição por L3
    l3_distribution = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for skill in valid_skills:
        if skill.get('l1') and skill.get('l2') and skill.get('l3'):
            l3_distribution[skill['l1']][skill['l2']][skill['l3']].append(skill)
    
    # Validação contra constraints
    validation_issues = []
    
    # Valida tipos (L1)
    num_types = len(l1_distribution)
    if num_types < TAXONOMY_CONSTRAINTS['MIN_TYPES']:
        validation_issues.append({
            'level': 'L1',
            'issue': 'Muito poucos tipos',
            'current': num_types,
            'min': TAXONOMY_CONSTRAINTS['MIN_TYPES'],
            'severity': 'CRITICAL'
        })
    if num_types > TAXONOMY_CONSTRAINTS['MAX_TYPES']:
        validation_issues.append({
            'level': 'L1',
            'issue': 'Muitos tipos',
            'current': num_types,
            'max': TAXONOMY_CONSTRAINTS['MAX_TYPES'],
            'severity': 'WARNING'
        })
    
    # Valida skills por tipo
    for l1, l1_skills in l1_distribution.items():
        count = len(l1_skills)
        if count < TAXONOMY_CONSTRAINTS['MIN_SKILLS_PER_TYPE']:
            validation_issues.append({
                'level': 'L1',
                'category': l1,
                'issue': 'Muito poucas skills neste tipo',
                'current': count,
                'min': TAXONOMY_CONSTRAINTS['MIN_SKILLS_PER_TYPE'],
                'severity': 'CRITICAL'
            })
        if count > TAXONOMY_CONSTRAINTS['MAX_SKILLS_PER_TYPE']:
            validation_issues.append({
                'level': 'L1',
                'category': l1,
                'issue': 'Muitas skills neste tipo (precisa split)',
                'current': count,
                'max': TAXONOMY_CONSTRAINTS['MAX_SKILLS_PER_TYPE'],
                'severity': 'CRITICAL'
            })
        
        # Valida subtipos (L2)
        num_subtypes = len(l2_distribution.get(l1, {}))
        if num_subtypes < TAXONOMY_CONSTRAINTS['MIN_SUBTYPES_PER_TYPE']:
            validation_issues.append({
                'level': 'L2',
                'category': l1,
                'issue': 'Muito poucos subtipos',
                'current': num_subtypes,
                'min': TAXONOMY_CONSTRAINTS['MIN_SUBTYPES_PER_TYPE'],
                'severity': 'WARNING'
            })
        
        # Valida skills por subtipo
        for l2, l2_skills in l2_distribution.get(l1, {}).items():
            count = len(l2_skills)
            if count < TAXONOMY_CONSTRAINTS['MIN_SKILLS_PER_SUBTYPE']:
                validation_issues.append({
                    'level': 'L2',
                    'category': f'{l1}/{l2}',
                    'issue': 'Muito poucas skills neste subtipo',
                    'current': count,
                    'min': TAXONOMY_CONSTRAINTS['MIN_SKILLS_PER_SUBTYPE'],
                    'severity': 'WARNING'
                })
            if count > TAXONOMY_CONSTRAINTS['MAX_SKILLS_PER_SUBTYPE']:
                validation_issues.append({
                    'level': 'L2',
                    'category': f'{l1}/{l2}',
                    'issue': 'Muitas skills neste subtipo (precisa chunking)',
                    'current': count,
                    'max': TAXONOMY_CONSTRAINTS['MAX_SKILLS_PER_SUBTYPE'],
                    'severity': 'CRITICAL',
                    'recommendation': f'Split em k={optimal_k(count, TAXONOMY_CONSTRAINTS["MAX_CHUNK_SIZE"])} chunks'
                })
    
    # Calcula métricas de entropia
    avg_skills_per_type = total_skills / num_types if num_types > 0 else 0
    avg_skills_per_subtype = sum(len(skills) for skills in l2_distribution.values()) / sum(len(subtypes) for subtypes in l2_distribution.values()) if l2_distribution else 0
    
    # Calcula chunking necessário
    chunking_needed = []
    for l1, l1_data in l3_distribution.items():
        for l2, l2_data in l1_data.items():
            for l3, l3_skills in l2_data.items():
                count = len(l3_skills)
                if count > TAXONOMY_CONSTRAINTS['MAX_CHUNK_SIZE']:
                    k = optimal_k(count, TAXONOMY_CONSTRAINTS['MAX_CHUNK_SIZE'])
                    chunking_needed.append({
                        'path': f'{l1}/{l2}/{l3}',
                        'current_count': count,
                        'recommended_chunks': k,
                        'avg_chunk_size': count // k
                    })
    
    # Gera relatório
    report = {
        'timestamp': Path().stat().st_mtime,
        'total_skills': total_skills,
        'valid_skills': len(valid_skills),
        'invalid_skills': len(invalid_skills),
        'levels_distribution': dict(levels_distribution),
        'types': {
            'count': num_types,
            'distribution': {l1: len(skills) for l1, skills in l1_distribution.items()},
            'average_per_type': avg_skills_per_type
        },
        'subtypes': {
            'total': sum(len(subtypes) for subtypes in l2_distribution.values()),
            'average_per_type': sum(len(subtypes) for subtypes in l2_distribution.values()) / num_types if num_types > 0 else 0,
            'average_skills_per_subtype': avg_skills_per_subtype
        },
        'validation_issues': validation_issues,
        'chunking_needed': chunking_needed,
        'constraints': TAXONOMY_CONSTRAINTS,
        'invalid_skills_details': invalid_skills[:20]  # Primeiros 20
    }
    
    return report


def optimal_k(n: int, max_chunk: int = 150, min_chunk: int = 40) -> int:
    """
    Retorna o número de chunks k tal que nenhum grupo exceda max_chunk
    e nenhum seja pequeno demais para valer o overhead.
    
    Fórmula: k = ceil(N / max_chunk), com consolidação se avg < min_chunk
    """
    if n <= max_chunk:
        return 1  # Cabe num só chunk, sem divisão
    
    k = math.ceil(n / max_chunk)
    avg = n / k
    
    # Se o chunk médio ficou menor que min_chunk, consolida
    while avg < min_chunk and k > 1:
        k -= 1
        avg = n / k
    
    return k


def print_report(report: Dict):
    """Imprime relatório formatado no console."""
    print("\n" + "="*80)
    print("TAXONOMY ANALYSIS REPORT")
    print("="*80 + "\n")
    
    if 'error' in report:
        print(f"❌ ERROR: {report['error']}")
        return
    
    print(f"📊 TOTAL SKILLS: {report['total_skills']}")
    print(f"   ✅ Valid: {report['valid_skills']}")
    print(f"   ❌ Invalid: {report['invalid_skills']}")
    
    print(f"\n📋 LEVELS DISTRIBUTION:")
    for levels, count in sorted(report['levels_distribution'].items()):
        print(f"   {levels} nível(is): {count} skills")
    
    print(f"\n📁 TYPES (L1):")
    print(f"   Total: {report['types']['count']}")
    print(f"   Média por tipo: {report['types']['average_per_type']:.1f}")
    print(f"   Válido: {TAXONOMY_CONSTRAINTS['MIN_TYPES']} - {TAXONOMY_CONSTRAINTS['MAX_TYPES']}")
    
    status = "✅ PASS" if TAXONOMY_CONSTRAINTS['MIN_TYPES'] <= report['types']['count'] <= TAXONOMY_CONSTRAINTS['MAX_TYPES'] else "❌ FAIL"
    print(f"   Status: {status}")
    
    print(f"\n📂 SUBTYPES (L2):")
    print(f"   Total: {report['subtypes']['total']}")
    print(f"   Média por tipo: {report['subtypes']['average_per_type']:.1f}")
    print(f"   Média skills por subtype: {report['subtypes']['average_skills_per_subtype']:.1f}")
    
    print(f"\n⚠️  VALIDATION ISSUES: {len(report['validation_issues'])}")
    critical = [i for i in report['validation_issues'] if i.get('severity') == 'CRITICAL']
    warnings = [i for i in report['validation_issues'] if i.get('severity') == 'WARNING']
    
    if critical:
        print(f"\n   🔴 CRITICAL ({len(critical)}):")
        for issue in critical[:10]:  # Mostra primeiros 10
            print(f"      - {issue['category']}: {issue['issue']} (atual: {issue['current']}, limite: {issue.get('min', issue.get('max'))})")
        if len(critical) > 10:
            print(f"      ... e mais {len(critical) - 10}")
    
    if warnings:
        print(f"\n   🟡 WARNINGS ({len(warnings)}):")
        for issue in warnings[:10]:
            print(f"      - {issue['category']}: {issue['issue']} (atual: {issue['current']}, limite: {issue.get('min', issue.get('max'))})")
        if len(warnings) > 10:
            print(f"      ... e mais {len(warnings) - 10}")
    
    if report['chunking_needed']:
        print(f"\n✂️  CHUNKING NEEDED: {len(report['chunking_needed'])} L3 directories")
        for chunk in report['chunking_needed'][:5]:
            print(f"      - {chunk['path']}: {chunk['current_count']} skills → split em {chunk['recommended_chunks']} chunks (~{chunk['avg_chunk_size']} cada)")
        if len(report['chunking_needed']) > 5:
            print(f"      ... e mais {len(report['chunking_needed']) - 5}")
    
    print("\n" + "="*80)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze current skill taxonomy')
    parser.add_argument('--skills-dir', type=str, default=str(SKILLS_DIR),
                       help=f'Skills directory (default: {SKILLS_DIR})')
    parser.add_argument('--output', type=str, default=str(OUTPUT_REPORT),
                       help=f'Output report file (default: {OUTPUT_REPORT})')
    parser.add_argument('--quiet', action='store_true',
                       help='Do not print report to console')
    
    args = parser.parse_args()
    
    skills_dir = Path(args.skills_dir)
    
    print(f"🔍 Analyzing taxonomy in {skills_dir}...")
    
    # Analyze
    report = analyze_taxonomy(skills_dir)
    
    # Save report
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    if not args.quiet:
        print_report(report)
    
    print(f"\n📝 Report saved to: {args.output}")
    
    # Return exit code based on validation
    critical_issues = len([i for i in report.get('validation_issues', []) if i.get('severity') == 'CRITICAL'])
    return 1 if critical_issues > 0 else 0


if __name__ == '__main__':
    exit(main())
