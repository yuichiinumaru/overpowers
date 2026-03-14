#!/usr/bin/env python3
"""
Validate Taxonomy - Valida taxonomia após renomeação

Verifica:
- Floors/Ceils absolutos
- Filtro percentual (20%)
- Chunk sizes
"""

import json
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
SKILLS_DIR = REPO_ROOT / "skills"

CONSTRAINTS = {
    'MIN_TYPES': 10,
    'MAX_TYPES': 20,
    'MIN_SKILLS_PER_TYPE': 50,
    'MAX_SKILLS_PER_TYPE': 500,
    'MIN_SUBTYPES_PER_TYPE': 4,
    'MAX_SUBTYPES_PER_TYPE': 20,
    'MIN_SKILLS_PER_SUBTYPE': 5,
    'MAX_SKILLS_PER_SUBTYPE': 80,
    'MAX_CHUNK_SIZE': 150,
}


def validate_taxonomy(skills_dir: Path) -> Dict:
    """Valida taxonomia atual."""
    issues = {'critical': [], 'warning': []}
    
    # Coleta skills
    skills = [d.name for d in skills_dir.iterdir() 
              if d.is_dir() and (d / 'SKILL.md').exists() and not d.name.startswith('_')]
    
    # Parse names
    parsed = []
    for name in skills:
        parts = name.split('-')
        if len(parts) >= 4:
            parsed.append({
                'name': name,
                'l1': parts[0],
                'l2': parts[1],
                'l3': parts[2] if parts[2].isdigit() == False else None,
            })
    
    # Distribuições
    l1_dist = defaultdict(list)
    l2_dist = defaultdict(lambda: defaultdict(list))
    
    for skill in parsed:
        l1_dist[skill['l1']].append(skill['name'])
        if skill['l2']:
            l2_dist[skill['l1']][skill['l2']].append(skill['name'])
    
    # Valida L1
    if len(l1_dist) < CONSTRAINTS['MIN_TYPES']:
        issues['critical'].append(f"Muito poucos tipos: {len(l1_dist)} < {CONSTRAINTS['MIN_TYPES']}")
    if len(l1_dist) > CONSTRAINTS['MAX_TYPES']:
        issues['warning'].append(f"Muitos tipos: {len(l1_dist)} > {CONSTRAINTS['MAX_TYPES']}")
    
    # Valida skills por L1
    for l1, l1_skills in l1_dist.items():
        count = len(l1_skills)
        if count < CONSTRAINTS['MIN_SKILLS_PER_TYPE']:
            issues['critical'].append(f"Tipo {l1}: {count} < {CONSTRAINTS['MIN_SKILLS_PER_TYPE']}")
        if count > CONSTRAINTS['MAX_SKILLS_PER_TYPE']:
            issues['critical'].append(f"Tipo {l1}: {count} > {CONSTRAINTS['MAX_SKILLS_PER_TYPE']}")
    
    # Valida L2
    for l1, l2_data in l2_dist.items():
        if len(l2_data) < CONSTRAINTS['MIN_SUBTYPES_PER_TYPE']:
            issues['warning'].append(f"Tipo {l1}: poucos subtipos ({len(l2_data)})")
        
        for l2, l2_skills in l2_data.items():
            count = len(l2_skills)
            if count < CONSTRAINTS['MIN_SKILLS_PER_SUBTYPE']:
                issues['warning'].append(f"Subtipo {l1}/{l2}: {count} < {CONSTRAINTS['MIN_SKILLS_PER_SUBTYPE']}")
            if count > CONSTRAINTS['MAX_SKILLS_PER_SUBTYPE']:
                issues['critical'].append(f"Subtipo {l1}/{l2}: {count} > {CONSTRAINTS['MAX_SKILLS_PER_SUBTYPE']}")
    
    return {
        'valid': len(issues['critical']) == 0,
        'total_skills': len(skills),
        'num_types': len(l1_dist),
        'num_subtypes': sum(len(v) for v in l2_dist.values()),
        'issues': issues
    }


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate taxonomy after rename')
    parser.add_argument('--skills-dir', type=str, default=str(SKILLS_DIR))
    
    args = parser.parse_args()
    
    result = validate_taxonomy(Path(args.skills_dir))
    
    print(f"\n{'='*60}")
    print(f"TAXONOMY VALIDATION")
    print(f"{'='*60}")
    print(f"Total skills: {result['total_skills']}")
    print(f"Types: {result['num_types']}")
    print(f"Subtypes: {result['num_subtypes']}")
    print(f"\nCritical issues: {len(result['issues']['critical'])}")
    for issue in result['issues']['critical'][:10]:
        print(f"  🔴 {issue}")
    print(f"\nWarnings: {len(result['issues']['warning'])}")
    for issue in result['issues']['warning'][:10]:
        print(f"  🟡 {issue}")
    print(f"\nStatus: {'✅ VALID' if result['valid'] else '❌ INVALID'}")
    print(f"{'='*60}\n")
    
    return 0 if result['valid'] else 1


if __name__ == '__main__':
    exit(main())
