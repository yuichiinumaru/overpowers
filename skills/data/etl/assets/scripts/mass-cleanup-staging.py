#!/usr/bin/env python3
"""
Mass Staging Cleanup
Cleans up ALL processed skills from staging after verification.
"""

import json
from pathlib import Path
from datetime import datetime

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
STAGING_DIR = REPO_ROOT / ".archive/staging/skills"
PROCESSING_LOG = REPO_ROOT / ".docs" / "batch-processing-log.json"
CLEANUP_LOG = REPO_ROOT / ".docs" / "mass-cleanup-log.json"


def main():
    """Clean up all processed skills from staging."""
    print(f"\n{'='*60}")
    print(f"MASS STAGING CLEANUP")
    print(f"{'='*60}\n")
    
    # Load processing log
    if not PROCESSING_LOG.exists():
        print(f"❌ Processing log not found: {PROCESSING_LOG}")
        return 1
    
    with open(PROCESSING_LOG, 'r', encoding='utf-8') as f:
        log = json.load(f)
    
    # Collect all processed skills
    all_processed = []
    for batch_id, batch_data in log['batches'].items():
        for result in batch_data.get('results', []):
            if result.get('status') == 'processed':
                source = result.get('source')
                if source:
                    all_processed.append({
                        'source': source,
                        'batch': batch_id,
                        'name': result.get('name')
                    })
    
    if not all_processed:
        print(f"✅ No processed skills found to clean")
        return 0
    
    print(f"📊 Found {len(all_processed)} processed skills to clean from staging")
    print(f"   Across {len(log['batches'])} batches")
    
    # Confirm
    print(f"\n⚠️  ABOUT TO DELETE {len(all_processed)} FILES FROM STAGING")
    print(f"   This action CANNOT be undone!")
    print(f"\n   Type 'yes' to confirm: ", end='')
    
    try:
        confirm = input().strip().lower()
        if confirm != 'yes':
            print(f"❌ Cleanup cancelled")
            return 1
    except:
        print(f"❌ Cleanup cancelled (no input)")
        return 1
    
    # Delete files
    print(f"\n🗑️  Deleting files from staging...\n")
    
    deleted = 0
    not_found = 0
    errors = 0
    
    for item in all_processed:
        source_path = Path(item['source'])
        
        if not source_path.exists():
            not_found += 1
            status = "⚠️"
            msg = "Not found (already deleted?)"
        else:
            try:
                source_path.unlink()
                deleted += 1
                status = "✅"
                msg = "Deleted"
            except Exception as e:
                errors += 1
                status = "❌"
                msg = f"Error: {str(e)}"
        
        # Show progress every 100 files
        if (deleted + not_found + errors) % 100 == 0:
            print(f"   Progress: {deleted + not_found + errors}/{len(all_processed)}...")
    
    # Save cleanup log
    cleanup_data = {
        'timestamp': datetime.now().isoformat(),
        'total_processed': len(all_processed),
        'deleted': deleted,
        'not_found': not_found,
        'errors': errors,
        'batches_cleaned': len(log['batches'])
    }
    
    with open(CLEANUP_LOG, 'w', encoding='utf-8') as f:
        json.dump(cleanup_data, f, indent=2, ensure_ascii=False)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"CLEANUP SUMMARY")
    print(f"{'='*60}")
    print(f"  Total:        {len(all_processed)}")
    print(f"  Deleted:      {deleted}")
    print(f"  Not found:    {not_found}")
    print(f"  Errors:       {errors}")
    print(f"{'='*60}\n")
    
    # Check remaining files in staging
    remaining = list(STAGING_DIR.glob("*.md"))
    print(f"📁 Remaining files in staging: {len(remaining)}")
    
    if len(remaining) > 0:
        print(f"   (These may be from batches not in processing log)")
    
    print(f"\n✅ Cleanup complete!")
    print(f"📝 Cleanup log saved to: {CLEANUP_LOG}")
    
    return 0 if errors == 0 else 1


if __name__ == '__main__':
    exit(main())
