#!/usr/bin/env python3
"""
Skill Assets Auditor
Traces skill origins and identifies auxiliary assets (scripts/, references/) in staging.
Generates migration plan for valuable auxiliary files.
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
STAGING_DIR = REPO_ROOT / ".archive/staging"
SKILLS_DIR = REPO_ROOT / "skills"
PROCESSING_LOG = REPO_ROOT / ".docs" / "batch-processing-log.json"
AUDIT_REPORT = REPO_ROOT / ".docs" / "skill-assets-audit-report.json"
SAMPLE_SIZE = 13  # 1% sample for detailed analysis


def load_processing_log() -> Dict:
    """Load the batch processing log."""
    if not PROCESSING_LOG.exists():
        print(f"❌ Processing log not found: {PROCESSING_LOG}")
        return {}
    
    with open(PROCESSING_LOG, 'r', encoding='utf-8') as f:
        return json.load(f)


def discover_skill_origins() -> List[Dict]:
    """Discover all skills and their potential auxiliary assets in staging."""
    skills_with_assets = []
    
    # Get processed skills from log
    log = load_processing_log()
    if not log:
        return []
    
    all_skills = []
    for batch_id, batch_data in log['batches'].items():
        for result in batch_data.get('results', []):
            if result.get('status') == 'processed':
                all_skills.append({
                    'name': result.get('name'),
                    'batch': batch_id,
                    'destination': result.get('destination'),
                    'source_staging': result.get('source')
                })
    
    print(f"📊 Found {len(all_skills)} processed skills to audit\n")
    
    # Check for auxiliary assets in staging
    for skill in all_skills:
        skill_name = skill['name']
        staging_skill_dir = STAGING_DIR / 'skills' / skill_name
        
        auxiliary_assets = {
            'scripts': [],
            'references': [],
            'other': []
        }
        
        # Check if staging directory exists (might be deleted already)
        if staging_skill_dir.exists():
            # Check for scripts/ subdirectory
            scripts_dir = staging_skill_dir / 'scripts'
            if scripts_dir.exists():
                scripts = list(scripts_dir.glob('*'))
                if scripts:
                    auxiliary_assets['scripts'] = [str(s) for s in scripts]
            
            # Check for references/ subdirectory
            references_dir = staging_skill_dir / 'references'
            if references_dir.exists():
                references = list(references_dir.glob('*'))
                if references:
                    auxiliary_assets['references'] = [str(r) for r in references]
            
            # Check for other files in skill directory
            other_files = [
                f for f in staging_skill_dir.iterdir()
                if f.is_file() and f.name != 'SKILL.md'
            ]
            if other_files:
                auxiliary_assets['other'] = [str(f) for f in other_files]
        
        # Only include skills with auxiliary assets
        has_assets = any(auxiliary_assets.values())
        if has_assets:
            skill['auxiliary_assets'] = auxiliary_assets
            skill['has_assets'] = True
            skills_with_assets.append(skill)
        else:
            skill['has_assets'] = False
    
    return skills_with_assets


def analyze_sample(skills_with_assets: List[Dict], sample_size: int = SAMPLE_SIZE) -> List[Dict]:
    """Analyze a sample of skills with auxiliary assets in detail."""
    import random
    
    if not skills_with_assets:
        return []
    
    # Select random sample
    sample_size = min(sample_size, len(skills_with_assets))
    sample = random.sample(skills_with_assets, sample_size)
    
    print(f"📋 Analyzing sample of {len(sample)} skills with auxiliary assets...\n")
    
    # Detailed analysis
    for skill in sample:
        skill['sample_analysis'] = {
            'analyzed': True,
            'timestamp': datetime.now().isoformat(),
            'asset_types': [],
            'total_assets': 0,
            'recommendation': 'pending'
        }
        
        assets = skill.get('auxiliary_assets', {})
        
        # Count and categorize assets
        if assets.get('scripts'):
            skill['sample_analysis']['asset_types'].append('scripts')
            skill['sample_analysis']['total_assets'] += len(assets['scripts'])
        
        if assets.get('references'):
            skill['sample_analysis']['asset_types'].append('references')
            skill['sample_analysis']['total_assets'] += len(assets['references'])
        
        if assets.get('other'):
            skill['sample_analysis']['asset_types'].append('other')
            skill['sample_analysis']['total_assets'] += len(assets['other'])
        
        # Generate recommendation
        if skill['sample_analysis']['total_assets'] > 0:
            if 'scripts' in skill['sample_analysis']['asset_types']:
                skill['sample_analysis']['recommendation'] = 'migrate_scripts'
            elif 'references' in skill['sample_analysis']['asset_types']:
                skill['sample_analysis']['recommendation'] = 'migrate_references'
            else:
                skill['sample_analysis']['recommendation'] = 'review_manual'
    
    return sample


def generate_migration_plan(skills_with_assets: List[Dict], sample: List[Dict]) -> Dict:
    """Generate migration plan for auxiliary assets."""
    migration_plan = {
        'timestamp': datetime.now().isoformat(),
        'total_skills_with_assets': len(skills_with_assets),
        'sample_analyzed': len(sample),
        'assets_to_migrate': {
            'scripts': [],
            'references': [],
            'other': []
        },
        'migration_commands': [],
        'summary': {}
    }
    
    # Collect all assets to migrate
    for skill in skills_with_assets:
        skill_name = skill['name']
        assets = skill.get('auxiliary_assets', {})
        
        # Scripts
        for script_path in assets.get('scripts', []):
            src = Path(script_path)
            dest = SKILLS_DIR / skill_name / 'scripts' / src.name
            migration_plan['assets_to_migrate']['scripts'].append({
                'source': str(src),
                'destination': str(dest),
                'skill': skill_name
            })
            migration_plan['migration_commands'].append(
                f"mkdir -p skills/{skill_name}/scripts && cp {src} {dest}"
            )
        
        # References
        for ref_path in assets.get('references', []):
            src = Path(ref_path)
            dest = SKILLS_DIR / skill_name / 'references' / src.name
            migration_plan['assets_to_migrate']['references'].append({
                'source': str(src),
                'destination': str(dest),
                'skill': skill_name
            })
            migration_plan['migration_commands'].append(
                f"mkdir -p skills/{skill_name}/references && cp {src} {dest}"
            )
        
        # Other
        for other_path in assets.get('other', []):
            src = Path(other_path)
            dest = SKILLS_DIR / skill_name / src.name
            migration_plan['assets_to_migrate']['other'].append({
                'source': str(src),
                'destination': str(dest),
                'skill': skill_name
            })
            migration_plan['migration_commands'].append(
                f"cp {src} {dest}"
            )
    
    # Summary
    migration_plan['summary'] = {
        'total_scripts': len(migration_plan['assets_to_migrate']['scripts']),
        'total_references': len(migration_plan['assets_to_migrate']['references']),
        'total_other': len(migration_plan['assets_to_migrate']['other']),
        'total_assets': (
            len(migration_plan['assets_to_migrate']['scripts']) +
            len(migration_plan['assets_to_migrate']['references']) +
            len(migration_plan['assets_to_migrate']['other'])
        )
    }
    
    return migration_plan


def main():
    """Main entry point."""
    print(f"\n{'='*60}")
    print(f"SKILL ASSETS AUDITOR")
    print(f"Tracing Origins & Auxiliary Assets")
    print(f"{'='*60}\n")
    
    # Discover skills with auxiliary assets
    print(f"🔍 Discovering skill origins and auxiliary assets...")
    skills_with_assets = discover_skill_origins()
    
    if not skills_with_assets:
        print(f"\n✅ No skills with auxiliary assets found")
        print(f"   (All skills were standalone SKILL.md files)")
        return 0
    
    print(f"📊 Found {len(skills_with_assets)} skills with auxiliary assets\n")
    
    # Analyze sample
    print(f"📋 Analyzing {SAMPLE_SIZE} skill sample...\n")
    sample = analyze_sample(skills_with_assets, SAMPLE_SIZE)
    
    # Generate migration plan
    print(f"📝 Generating migration plan...\n")
    migration_plan = generate_migration_plan(skills_with_assets, sample)
    
    # Save audit report
    audit_report = {
        'timestamp': datetime.now().isoformat(),
        'skills_with_assets': skills_with_assets,
        'sample_analysis': sample,
        'migration_plan': migration_plan
    }
    
    with open(AUDIT_REPORT, 'w', encoding='utf-8') as f:
        json.dump(audit_report, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"AUDIT SUMMARY")
    print(f"{'='*60}")
    print(f"  Total skills processed:     {len(skills_with_assets) + sum(1 for s in discover_skill_origins() if not s.get('has_assets')) if skills_with_assets else 0}")
    print(f"  Skills with assets:         {len(skills_with_assets)}")
    print(f"  Sample analyzed:            {len(sample)}")
    print(f"\n  Assets to migrate:")
    print(f"    - Scripts:                {migration_plan['summary']['total_scripts']}")
    print(f"    - References:             {migration_plan['summary']['total_references']}")
    print(f"    - Other files:            {migration_plan['summary']['total_other']}")
    print(f"    - TOTAL:                  {migration_plan['summary']['total_assets']}")
    print(f"{'='*60}\n")
    
    print(f"📝 Audit report saved to: {AUDIT_REPORT}")
    print(f"📝 Migration plan: {AUDIT_REPORT}")
    
    # Show sample details
    if sample:
        print(f"\n📋 SAMPLE DETAILS:")
        for i, skill in enumerate(sample, 1):
            print(f"\n  {i}. {skill['name']}")
            print(f"     Batch: {skill['batch']}")
            assets = skill.get('auxiliary_assets', {})
            if assets.get('scripts'):
                print(f"     Scripts: {len(assets['scripts'])} files")
            if assets.get('references'):
                print(f"     References: {len(assets['references'])} files")
            if assets.get('other'):
                print(f"     Other: {len(assets['other'])} files")
            print(f"     Recommendation: {skill.get('sample_analysis', {}).get('recommendation', 'N/A')}")
    
    print(f"\n✅ Audit complete!")
    print(f"📝 Review report and execute migration if needed")
    
    return 0


if __name__ == '__main__':
    exit(main())
