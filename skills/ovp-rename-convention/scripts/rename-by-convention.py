#!/usr/bin/env python3
"""
Rename by Convention - Aplica renomeação em massa baseada na taxonomia gerada

Modos:
- apply: Renomeia fisicamente os diretórios
- dry-run: Apenas mostra o que seria feito
- interactive: Pede confirmação para cada rename
"""

import json
import shutil
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
SKILLS_DIR = REPO_ROOT / "skills"
DEFAULT_MAPPING = REPO_ROOT / ".docs" / "taxonomy-mapping.json"


def apply_renames(mapping: Dict, mode: str = 'dry-run', skills_dir: Path = SKILLS_DIR) -> Dict:
    """
    Aplica renomeações baseadas no mapping.
    
    Args:
        mapping: Taxonomy mapping do generate-taxonomy.py
        mode: 'dry-run', 'apply', ou 'interactive'
        skills_dir: Diretório das skills
    """
    results = {
        'total': 0,
        'renamed': 0,
        'skipped': 0,
        'errors': 0,
        'details': []
    }
    
    for original, data in mapping.get('mapping', {}).items():
        results['total'] += 1
        
        old_path = skills_dir / original
        new_path = skills_dir / data['new_name']
        
        # Skip se não existe
        if not old_path.exists():
            results['skipped'] += 1
            results['details'].append({
                'original': original,
                'reason': 'Source not found',
                'status': 'skipped'
            })
            continue
        
        # Skip se já tem o nome correto
        if old_path == new_path:
            results['skipped'] += 1
            results['details'].append({
                'original': original,
                'reason': 'Already has correct name',
                'status': 'skipped'
            })
            continue
        
        # Check se destino já existe
        if new_path.exists():
            results['errors'] += 1
            results['details'].append({
                'original': original,
                'new_name': data['new_name'],
                'reason': 'Destination already exists',
                'status': 'error'
            })
            continue
        
        # Interactive mode: pede confirmação
        if mode == 'interactive':
            print(f"\nRename: {original}")
            print(f"   → {data['new_name']}")
            confirm = input("Confirm? (y/n/skip-all): ").strip().lower()
            if confirm == 'skip-all':
                mode = 'dry-run'
                results['skipped'] += 1
                continue
            elif confirm != 'y':
                results['skipped'] += 1
                continue
        
        # Dry-run: só loga
        if mode == 'dry-run':
            results['renamed'] += 1
            results['details'].append({
                'original': original,
                'new_name': data['new_name'],
                'status': 'would_rename'
            })
            print(f"Would rename: {original} → {data['new_name']}")
            continue
        
        # Apply mode: renomeia
        try:
            shutil.move(str(old_path), str(new_path))
            results['renamed'] += 1
            results['details'].append({
                'original': original,
                'new_name': data['new_name'],
                'status': 'renamed'
            })
            print(f"✅ Renamed: {original} → {data['new_name']}")
        except Exception as e:
            results['errors'] += 1
            results['details'].append({
                'original': original,
                'new_name': data['new_name'],
                'reason': str(e),
                'status': 'error'
            })
            print(f"❌ Error renaming {original}: {e}")
    
    return results


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Rename skills by taxonomy convention')
    parser.add_argument('--mapping', type=str, default=str(DEFAULT_MAPPING),
                       help=f'Mapping file (default: {DEFAULT_MAPPING})')
    parser.add_argument('--mode', type=str, default='dry-run',
                       choices=['dry-run', 'apply', 'interactive'],
                       help='Execution mode (default: dry-run)')
    parser.add_argument('--skills-dir', type=str, default=str(SKILLS_DIR),
                       help=f'Skills directory (default: {SKILLS_DIR})')
    
    args = parser.parse_args()
    
    # Load mapping
    with open(args.mapping, 'r', encoding='utf-8') as f:
        mapping = json.load(f)
    
    print(f"📋 Mode: {args.mode}")
    print(f"📊 Total skills in mapping: {len(mapping.get('mapping', {}))}")
    
    if args.mode == 'dry-run':
        print("⚠️  DRY-RUN: No files will be renamed\n")
    elif args.mode == 'apply':
        print("⚠️  APPLY MODE: Files WILL BE renamed\n")
    else:
        print("⚠️  INTERACTIVE MODE: Will ask for each rename\n")
    
    # Apply
    results = apply_renames(mapping, mode=args.mode, skills_dir=Path(args.skills_dir))
    
    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY:")
    print(f"  Total: {results['total']}")
    print(f"  Renamed: {results['renamed']}")
    print(f"  Skipped: {results['skipped']}")
    print(f"  Errors: {results['errors']}")
    print(f"{'='*60}")
    
    # Save results
    results_file = Path(args.mapping).parent / f"rename-results-{args.mode}.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n📝 Results saved to: {results_file}")
    
    return 0 if results['errors'] == 0 else 1


if __name__ == '__main__':
    exit(main())
