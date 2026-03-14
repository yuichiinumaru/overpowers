#!/usr/bin/env python3
"""
Migrate Auxiliary Skill Assets
Copies scripts/, references/, and other assets from original locations to skills/<name>/.
"""

import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
SKILLS_DIR = REPO_ROOT / "skills"
ORIGINS_REPORT = REPO_ROOT / ".docs" / "skill-origins-report.json"
MIGRATION_LOG = REPO_ROOT / ".docs" / "auxiliary-assets-migration-log.json"


def load_origins_report() -> Dict:
    """Load the origins report."""
    if not ORIGINS_REPORT.exists():
        print(f"❌ Origins report not found: {ORIGINS_REPORT}")
        return {}
    
    with open(ORIGINS_REPORT, 'r', encoding='utf-8') as f:
        return json.load(f)


def migrate_assets_for_skill(skill_name: str, assets: Dict) -> Dict:
    """Migrate auxiliary assets for a single skill."""
    result = {
        'skill': skill_name,
        'migrated': {
            'scripts': [],
            'references': [],
            'other': []
        },
        'errors': [],
        'timestamp': datetime.now().isoformat()
    }
    
    for asset_type in ['scripts', 'references', 'other']:
        asset_paths = assets.get(asset_type, [])
        
        for src_path in asset_paths:
            src = Path(src_path)
            if not src.exists():
                result['errors'].append({
                    'type': asset_type,
                    'file': str(src),
                    'error': 'Source file not found'
                })
                continue
            
            # Determine destination
            if asset_type == 'other':
                dest = SKILLS_DIR / skill_name / src.name
            else:
                dest = SKILLS_DIR / skill_name / asset_type / src.name
            
            try:
                # Create directory if needed
                dest.parent.mkdir(parents=True, exist_ok=True)
                
                # Copy file
                shutil.copy2(src, dest)
                
                result['migrated'][asset_type].append({
                    'source': str(src),
                    'destination': str(dest)
                })
                
            except Exception as e:
                result['errors'].append({
                    'type': asset_type,
                    'file': str(src),
                    'error': str(e)
                })
    
    return result


def migrate_all_assets(recommendations: Dict, priority: str = 'high') -> Dict:
    """Migrate assets based on priority level."""
    print(f"\n{'='*60}")
    print(f"MIGRATING {priority.upper()} PRIORITY ASSETS")
    print(f"{'='*60}\n")
    
    skills_to_migrate = recommendations.get(f'{priority}_priority', [])
    
    if not skills_to_migrate:
        print(f"✅ No {priority} priority assets to migrate")
        return {'migrated': 0, 'errors': 0}
    
    print(f"📊 Migrating {len(skills_to_migrate)} skills with {priority} priority assets...\n")
    
    total_migrated = 0
    total_errors = 0
    migration_results = []
    
    for i, rec in enumerate(skills_to_migrate, 1):
        skill_name = rec['skill']
        assets = {rec['action'].replace('migrate_', ''): rec['assets']}
        
        result = migrate_assets_for_skill(skill_name, assets)
        migration_results.append(result)
        
        migrated_count = sum(len(result['migrated'][t]) for t in ['scripts', 'references', 'other'])
        error_count = len(result['errors'])
        
        total_migrated += migrated_count
        total_errors += error_count
        
        status = "✅" if error_count == 0 else "⚠️"
        print(f"{status} {skill_name:45s} - {migrated_count} files migrated")
        if error_count > 0:
            for err in result['errors']:
                print(f"   ❌ {err['file']}: {err['error']}")
        
        # Progress indicator
        if i % 50 == 0 or i == len(skills_to_migrate):
            print(f"   Progress: {i}/{len(skills_to_migrate)}...")
    
    return {
        'migrated': total_migrated,
        'errors': total_errors,
        'results': migration_results
    }


def main():
    """Main entry point."""
    print(f"\n{'='*60}")
    print(f"AUXILIARY ASSETS MIGRATION")
    print(f"{'='*60}\n")
    
    # Load origins report
    print(f"📂 Loading origins report...")
    report = load_origins_report()
    if not report:
        return 1
    
    recommendations = report.get('recommendations', {})
    
    # Summary
    print(f"📊 Migration Summary from Report:")
    print(f"   High priority (scripts):   {recommendations.get('summary', {}).get('high_priority_count', 0)}")
    print(f"   Medium priority (refs):    {recommendations.get('summary', {}).get('medium_priority_count', 0)}")
    print(f"   Low priority (other):      {recommendations.get('summary', {}).get('low_priority_count', 0)}")
    
    # Confirm
    total = sum([
        recommendations.get('summary', {}).get('high_priority_count', 0),
        recommendations.get('summary', {}).get('medium_priority_count', 0),
        recommendations.get('summary', {}).get('low_priority_count', 0)
    ])
    
    print(f"\n⚠️  ABOUT TO MIGRATE {total} ASSETS")
    print(f"   This may take several minutes...")
    print(f"\n   Type 'yes' to confirm: ", end='')
    
    try:
        confirm = input().strip().lower()
        if confirm != 'yes':
            print(f"❌ Migration cancelled")
            return 1
    except:
        print(f"❌ Migration cancelled (no input)")
        return 1
    
    # Migrate by priority
    all_results = {
        'high': migrate_all_assets(recommendations, 'high'),
        'medium': migrate_all_assets(recommendations, 'medium'),
        'low': migrate_all_assets(recommendations, 'low')
    }
    
    # Save migration log
    migration_log = {
        'timestamp': datetime.now().isoformat(),
        'summary': {
            'total_migrated': sum(r.get('migrated', 0) for r in all_results.values()),
            'total_errors': sum(r.get('errors', 0) for r in all_results.values()),
            'by_priority': {
                'high': all_results['high'],
                'medium': all_results['medium'],
                'low': all_results['low']
            }
        },
        'details': all_results
    }
    
    with open(MIGRATION_LOG, 'w', encoding='utf-8') as f:
        json.dump(migration_log, f, indent=2, ensure_ascii=False)
    
    # Final summary
    print(f"\n{'='*60}")
    print(f"MIGRATION COMPLETE")
    print(f"{'='*60}")
    print(f"  Total files migrated: {migration_log['summary']['total_migrated']}")
    print(f"  Total errors:         {migration_log['summary']['total_errors']}")
    print(f"{'='*60}\n")
    
    print(f"📝 Migration log saved to: {MIGRATION_LOG}")
    print(f"✅ Migration complete!")
    
    return 0 if migration_log['summary']['total_errors'] == 0 else 1


if __name__ == '__main__':
    exit(main())
