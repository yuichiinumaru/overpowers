#!/usr/bin/env python3
"""
Skill Origins Tracker
Uses manifest.json to trace skill origins and check for auxiliary assets in original locations.
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
STAGING_MANIFEST = REPO_ROOT / ".archive/staging/manifest.json"
ORIGINS_REPORT = REPO_ROOT / ".docs" / "skill-origins-report.json"
SAMPLE_SIZE = 13


def load_manifest() -> Dict:
    """Load staging manifest."""
    if not STAGING_MANIFEST.exists():
        print(f"❌ Manifest not found: {STAGING_MANIFEST}")
        return {}
    
    with open(STAGING_MANIFEST, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_auxiliary_assets(original_path: str) -> Dict:
    """Check for auxiliary assets in original skill directory."""
    assets = {
        'scripts': [],
        'references': [],
        'other': [],
        'exists': False
    }
    
    original = Path(original_path)
    if not original.exists():
        return assets
    
    assets['exists'] = True
    skill_dir = original.parent
    
    # Check for scripts/ subdirectory
    scripts_dir = skill_dir / 'scripts'
    if scripts_dir.exists():
        scripts = list(scripts_dir.glob('*'))
        assets['scripts'] = [str(s) for s in scripts]
    
    # Check for references/ subdirectory
    references_dir = skill_dir / 'references'
    if references_dir.exists():
        references = list(references_dir.glob('*'))
        assets['references'] = [str(r) for r in references]
    
    # Check for other files
    other_files = [
        str(f) for f in skill_dir.iterdir()
        if f.is_file() and f.suffix in ['.py', '.sh', '.md', '.txt', '.json', '.yaml', '.yml']
        and f.name != 'SKILL.md'
    ]
    if other_files:
        assets['other'] = other_files
    
    return assets


def analyze_skills_with_assets(manifest: Dict, sample_size: int = SAMPLE_SIZE) -> Dict:
    """Analyze skills to find which have auxiliary assets."""
    import random
    
    skills = manifest.get('skills', {})
    if isinstance(skills, dict):
        skill_list = list(skills.values())
    else:
        skill_list = skills
    
    print(f"📊 Total skills in manifest: {len(skill_list)}\n")
    
    # Check each skill for auxiliary assets
    skills_with_assets = []
    skills_checked = 0
    
    for skill in skill_list:
        original_path = skill.get('original_path', '')
        if not original_path:
            continue
        
        assets = check_auxiliary_assets(original_path)
        has_assets = any([assets.get('scripts'), assets.get('references'), assets.get('other')])
        
        if has_assets:
            skills_with_assets.append({
                'name': skill.get('name'),
                'original_path': original_path,
                'staged_path': skill.get('staged_path'),
                'auxiliary_assets': assets
            })
        
        skills_checked += 1
        
        # Progress indicator
        if skills_checked % 100 == 0:
            print(f"   Checked {skills_checked}/{len(skill_list)} skills...")
    
    print(f"\n✅ Found {len(skills_with_assets)} skills with auxiliary assets\n")
    
    # Select sample for detailed analysis
    sample = []
    if skills_with_assets:
        sample_size = min(sample_size, len(skills_with_assets))
        sample = random.sample(skills_with_assets, sample_size)
        
        print(f"📋 Sample analysis ({len(sample)} skills):\n")
        for i, skill in enumerate(sample, 1):
            print(f"  {i}. {skill['name']}")
            print(f"     Original: {skill['original_path']}")
            assets = skill['auxiliary_assets']
            if assets.get('scripts'):
                print(f"     Scripts: {len(assets['scripts'])} files")
                for s in assets['scripts'][:3]:
                    print(f"       - {Path(s).name}")
            if assets.get('references'):
                print(f"     References: {len(assets['references'])} files")
                for r in assets['references'][:3]:
                    print(f"       - {Path(r).name}")
            print()
    
    return {
        'total_skills': len(skill_list),
        'skills_with_assets': skills_with_assets,
        'sample': sample,
        'summary': {
            'total_with_assets': len(skills_with_assets),
            'percentage': round(len(skills_with_assets) / len(skill_list) * 100, 2) if skill_list else 0
        }
    }


def generate_migration_recommendations(analysis: Dict) -> Dict:
    """Generate recommendations for migrating auxiliary assets."""
    recommendations = {
        'high_priority': [],
        'medium_priority': [],
        'low_priority': [],
        'summary': {}
    }
    
    for skill in analysis.get('skills_with_assets', []):
        assets = skill.get('auxiliary_assets', {})
        
        # High priority: has scripts
        if assets.get('scripts'):
            recommendations['high_priority'].append({
                'skill': skill['name'],
                'reason': 'Has executable scripts',
                'assets': assets['scripts'],
                'action': 'migrate_scripts_to_skills_dir'
            })
        
        # Medium priority: has references
        elif assets.get('references'):
            recommendations['medium_priority'].append({
                'skill': skill['name'],
                'reason': 'Has reference documentation',
                'assets': assets['references'],
                'action': 'migrate_references_to_skills_dir'
            })
        
        # Low priority: other files
        elif assets.get('other'):
            recommendations['low_priority'].append({
                'skill': skill['name'],
                'reason': 'Has auxiliary files',
                'assets': assets['other'],
                'action': 'review_and_migrate_if_valuable'
            })
    
    recommendations['summary'] = {
        'high_priority_count': len(recommendations['high_priority']),
        'medium_priority_count': len(recommendations['medium_priority']),
        'low_priority_count': len(recommendations['low_priority']),
        'total_recommendations': len(recommendations['high_priority']) + len(recommendations['medium_priority']) + len(recommendations['low_priority'])
    }
    
    return recommendations


def main():
    """Main entry point."""
    print(f"\n{'='*60}")
    print(f"SKILL ORIGINS TRACKER")
    print(f"Tracing Original Locations & Auxiliary Assets")
    print(f"{'='*60}\n")
    
    # Load manifest
    print(f"📂 Loading manifest...")
    manifest = load_manifest()
    if not manifest:
        return 1
    
    # Analyze skills
    print(f"🔍 Analyzing skill origins and auxiliary assets...\n")
    analysis = analyze_skills_with_assets(manifest, SAMPLE_SIZE)
    
    # Generate recommendations
    print(f"📝 Generating migration recommendations...\n")
    recommendations = generate_migration_recommendations(analysis)
    
    # Save report
    report = {
        'timestamp': datetime.now().isoformat(),
        'manifest_source': str(STAGING_MANIFEST),
        'analysis': analysis,
        'recommendations': recommendations
    }
    
    with open(ORIGINS_REPORT, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"ORIGINS AUDIT SUMMARY")
    print(f"{'='*60}")
    print(f"  Total skills in manifest:     {analysis['total_skills']}")
    print(f"  Skills with auxiliary assets: {analysis['summary']['total_with_assets']}")
    print(f"  Percentage:                   {analysis['summary']['percentage']}%")
    print(f"\n  Recommendations:")
    print(f"    High priority (scripts):    {recommendations['summary']['high_priority_count']}")
    print(f"    Medium priority (refs):     {recommendations['summary']['medium_priority_count']}")
    print(f"    Low priority (other):       {recommendations['summary']['low_priority_count']}")
    print(f"{'='*60}\n")
    
    print(f"📝 Report saved to: {ORIGINS_REPORT}")
    
    # Show top recommendations
    if recommendations['high_priority']:
        print(f"\n🔴 HIGH PRIORITY MIGRATIONS (Scripts):")
        for rec in recommendations['high_priority'][:10]:
            print(f"   - {rec['skill']}: {len(rec['assets'])} script(s)")
        if len(recommendations['high_priority']) > 10:
            print(f"   ... and {len(recommendations['high_priority']) - 10} more")
    
    print(f"\n✅ Audit complete!")
    
    return 0


if __name__ == '__main__':
    exit(main())
