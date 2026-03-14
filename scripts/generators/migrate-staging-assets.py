#!/usr/bin/env python3
"""
Process Remaining Staging Assets (Agents, Workflows, Hooks)
Migrates assets from staging to their proper destinations with full audit trail.
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
STAGING_DIR = REPO_ROOT / ".archive/staging"
AUDIT_LOG = REPO_ROOT / ".docs" / "staging-assets-audit.json"

# Destination mappings
DESTINATIONS = {
    'agents': REPO_ROOT / 'agents',
    'workflows': REPO_ROOT / 'workflows',
    'hooks': REPO_ROOT / 'hooks',
}


def discover_assets() -> Dict[str, List[Path]]:
    """Discover all remaining assets in staging."""
    assets = {}
    
    for asset_type, dest_dir in DESTINATIONS.items():
        staging_subdir = STAGING_DIR / asset_type
        if staging_subdir.exists():
            files = list(staging_subdir.glob("*.md"))
            assets[asset_type] = files
            print(f"📂 {asset_type.capitalize()}: {len(files)} files found")
        else:
            assets[asset_type] = []
            print(f"📂 {asset_type.capitalize()}: Directory not found")
    
    return assets


def migrate_asset(source: Path, asset_type: str) -> Dict:
    """Migrate a single asset to its destination."""
    result = {
        'source': str(source),
        'asset_type': asset_type,
        'filename': source.name,
        'status': 'pending',
        'destination': None,
        'error': None,
        'timestamp': datetime.now().isoformat()
    }
    
    dest_dir = DESTINATIONS.get(asset_type)
    if not dest_dir:
        result['status'] = 'error'
        result['error'] = f'Unknown asset type: {asset_type}'
        return result
    
    dest_file = dest_dir / source.name
    
    result['destination'] = str(dest_file)
    
    try:
        # Check if already exists
        if dest_file.exists():
            result['status'] = 'already_exists'
            result['error'] = 'Destination file already exists'
            return result
        
        # Copy file
        shutil.copy2(source, dest_file)
        result['status'] = 'migrated'
        
    except Exception as e:
        result['status'] = 'error'
        result['error'] = f'Failed to migrate: {str(e)}'
    
    return result


def migrate_all_assets(assets: Dict[str, List[Path]]) -> Dict[str, List[Dict]]:
    """Migrate all discovered assets."""
    all_results = {}
    
    for asset_type, files in assets.items():
        print(f"\n{'='*60}")
        print(f"Migrating {asset_type.upper()}...")
        print(f"{'='*60}\n")
        
        results = []
        migrated = 0
        skipped = 0
        errors = 0
        already_exists = 0
        
        for i, source_file in enumerate(files, 1):
            result = migrate_asset(source_file, asset_type)
            results.append(result)
            
            if result['status'] == 'migrated':
                migrated += 1
                status_icon = "✅"
            elif result['status'] == 'already_exists':
                already_exists += 1
                status_icon = "⚠️"
            elif result['status'] == 'error':
                errors += 1
                status_icon = "❌"
            else:
                skipped += 1
                status_icon = "⏭️"
            
            print(f"{status_icon} {source_file.name:50s} -> {result.get('destination', 'N/A')[-60:]}")
            if result.get('error') and result['status'] != 'already_exists':
                print(f"   ❌ Error: {result['error']}")
            
            # Progress indicator
            if i % 10 == 0 or i == len(files):
                print(f"   Progress: {i}/{len(files)}...")
        
        all_results[asset_type] = results
        
        print(f"\n{'='*60}")
        print(f"{asset_type.capitalize()} Summary:")
        print(f"  Migrated:       {migrated}")
        print(f"  Already exists: {already_exists}")
        print(f"  Errors:         {errors}")
        print(f"{'='*60}\n")
    
    return all_results


def save_audit_log(all_results: Dict):
    """Save comprehensive audit log."""
    audit_data = {
        'timestamp': datetime.now().isoformat(),
        'summary': {},
        'details': all_results
    }
    
    # Calculate summary
    for asset_type, results in all_results.items():
        audit_data['summary'][asset_type] = {
            'total': len(results),
            'migrated': sum(1 for r in results if r['status'] == 'migrated'),
            'already_exists': sum(1 for r in results if r['status'] == 'already_exists'),
            'errors': sum(1 for r in results if r['status'] == 'error')
        }
    
    # Save
    with open(AUDIT_LOG, 'w', encoding='utf-8') as f:
        json.dump(audit_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n📝 Audit log saved to: {AUDIT_LOG}")


def main():
    """Main entry point."""
    print(f"\n{'='*60}")
    print(f"STAGING ASSETS MIGRATION - AGENTS, WORKFLOWS, HOOKS")
    print(f"{'='*60}\n")
    
    # Discover assets
    print(f"🔍 Discovering assets in staging...")
    assets = discover_assets()
    
    total_assets = sum(len(files) for files in assets.values())
    
    if total_assets == 0:
        print(f"\n✅ No assets found in staging")
        return 0
    
    print(f"\n📊 Total assets to migrate: {total_assets}")
    
    # Confirm
    print(f"\n⚠️  ABOUT TO MIGRATE {total_assets} ASSETS")
    print(f"   Type 'yes' to confirm: ", end='')
    
    try:
        confirm = input().strip().lower()
        if confirm != 'yes':
            print(f"❌ Migration cancelled")
            return 1
    except:
        print(f"❌ Migration cancelled (no input)")
        return 1
    
    # Migrate all
    all_results = migrate_all_assets(assets)
    
    # Save audit log
    save_audit_log(all_results)
    
    # Final summary
    total_migrated = sum(
        sum(1 for r in results if r['status'] == 'migrated')
        for results in all_results.values()
    )
    total_errors = sum(
        sum(1 for r in results if r['status'] == 'error')
        for results in all_results.values()
    )
    
    print(f"\n{'='*60}")
    print(f"FINAL SUMMARY")
    print(f"{'='*60}")
    print(f"  Total assets:    {total_assets}")
    print(f"  Migrated:        {total_migrated}")
    print(f"  Errors:          {total_errors}")
    print(f"{'='*60}\n")
    
    print(f"✅ Migration complete!")
    print(f"📝 Review audit log at: {AUDIT_LOG}")
    
    return 0 if total_errors == 0 else 1


if __name__ == '__main__':
    exit(main())
