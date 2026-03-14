#!/usr/bin/env python3
"""
Staging Cleanup Script
Removes processed skill files from .archive/staging/skills/ after verification.
Use ONLY after running process-skill-batches.py and verifying the results.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
STAGING_DIR = REPO_ROOT / ".archive/staging/skills"
PROCESSING_LOG = REPO_ROOT / ".docs" / "batch-processing-log.json"
CLEANUP_LOG = REPO_ROOT / ".docs" / "staging-cleanup-log.json"


def load_processing_log() -> Dict:
    """Load the processing log to know which files to clean up."""
    if not PROCESSING_LOG.exists():
        print(f"❌ Processing log not found: {PROCESSING_LOG}")
        print(f"   Please run process-skill-batches.py first!")
        return {}
    
    try:
        with open(PROCESSING_LOG, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load processing log: {e}")
        return {}


def get_files_to_cleanup(processed_results: List[Dict]) -> List[Dict]:
    """Get list of source files to delete based on processing results."""
    files_to_delete = []
    
    for result in processed_results:
        if result.get('status') == 'processed':
            source_path = result.get('source')
            if source_path:
                source_file = Path(source_path)
                if source_file.exists():
                    files_to_delete.append({
                        'source': str(source_file),
                        'destination': result.get('destination'),
                        'batch': result.get('batch'),
                        'skill_name': result.get('name')
                    })
    
    return files_to_delete


def cleanup_files(files_to_delete: List[Dict], dry_run: bool = False) -> Dict:
    """Delete processed source files from staging."""
    summary = {
        'total': len(files_to_delete),
        'deleted': 0,
        'not_found': 0,
        'errors': 0,
        'details': []
    }
    
    print(f"\n{'='*60}")
    if dry_run:
        print(f"DRY RUN - Would delete {len(files_to_delete)} files")
    else:
        print(f"Cleaning up {len(files_to_delete)} processed files from staging")
    print(f"{'='*60}\n")
    
    for file_info in files_to_delete:
        source_path = Path(file_info['source'])
        
        if not source_path.exists():
            summary['not_found'] += 1
            status_icon = "⚠️"
            message = "File not found (already deleted?)"
        else:
            try:
                if not dry_run:
                    source_path.unlink()
                summary['deleted'] += 1
                status_icon = "✅"
                message = "Deleted"
            except Exception as e:
                summary['errors'] += 1
                status_icon = "❌"
                message = f"Error: {str(e)}"
        
        print(f"{status_icon} {file_info['skill_name']:45s} ({file_info['batch']}) - {message}")
        
        summary['details'].append({
            'skill_name': file_info['skill_name'],
            'batch': file_info['batch'],
            'source': file_info['source'],
            'status': 'deleted' if status_icon == "✅" else ('not_found' if status_icon == "⚠️" else 'error'),
            'message': message
        })
    
    print(f"\n{'='*60}")
    print(f"Cleanup Summary:")
    print(f"  Total:       {summary['total']}")
    print(f"  Deleted:     {summary['deleted']}")
    print(f"  Not found:   {summary['not_found']}")
    print(f"  Errors:      {summary['errors']}")
    print(f"{'='*60}\n")
    
    return summary


def save_cleanup_log(summary: Dict, batches_cleaned: List[str]):
    """Save cleanup log for audit trail."""
    cleanup_data = {
        'timestamp': datetime.now().isoformat(),
        'batches_cleaned': batches_cleaned,
        'summary': summary,
        'details': summary['details']
    }
    
    # Load existing cleanup log if present
    existing_log = {}
    if CLEANUP_LOG.exists():
        try:
            with open(CLEANUP_LOG, 'r', encoding='utf-8') as f:
                existing_log = json.load(f)
        except:
            existing_log = {}
    
    # Append to cleanup history
    if 'history' not in existing_log:
        existing_log['history'] = []
    existing_log['history'].append(cleanup_data)
    existing_log['last_cleanup'] = datetime.now().isoformat()
    
    with open(CLEANUP_LOG, 'w', encoding='utf-8') as f:
        json.dump(existing_log, f, indent=2, ensure_ascii=False)
    
    print(f"📝 Cleanup log saved to: {CLEANUP_LOG}")


def verify_destination_exists(files_to_delete: List[Dict]) -> bool:
    """Verify that destination files exist before deleting source files."""
    missing_destinations = []
    
    for file_info in files_to_delete:
        dest_path = Path(file_info['destination']) if file_info.get('destination') else None
        if not dest_path or not dest_path.exists():
            missing_destinations.append(file_info)
    
    if missing_destinations:
        print(f"\n⚠️  WARNING: {len(missing_destinations)} destination files are missing!")
        print(f"   These source files will NOT be deleted:\n")
        for file_info in missing_destinations[:10]:  # Show first 10
            print(f"   - {file_info['skill_name']} ({file_info['batch']})")
            print(f"     Destination: {file_info.get('destination', 'N/A')}")
        if len(missing_destinations) > 10:
            print(f"   ... and {len(missing_destinations) - 10} more")
        return False
    
    return True


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Clean up processed skill files from staging')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be deleted without actually deleting')
    parser.add_argument('--force', action='store_true',
                       help='Skip destination verification (use with caution)')
    parser.add_argument('--batch', type=str, default=None,
                       help='Clean up specific batch only (e.g., --batch 031)')
    
    args = parser.parse_args()
    
    # Load processing log
    processing_log = load_processing_log()
    if not processing_log:
        return 1
    
    # Get batches to clean
    batches_to_clean = []
    all_results = []
    
    if args.batch:
        if args.batch in processing_log.get('batches', {}):
            batches_to_clean = [args.batch]
            batch_data = processing_log['batches'][args.batch]
            all_results = batch_data.get('results', [])
        else:
            print(f"❌ Batch {args.batch} not found in processing log")
            return 1
    else:
        # Clean all batches from processing log
        batches_to_clean = list(processing_log.get('batches', {}).keys())
        for batch_id, batch_data in processing_log.get('batches', {}).items():
            all_results.extend(batch_data.get('results', []))
    
    if not batches_to_clean:
        print(f"❌ No batches found to clean")
        return 1
    
    print(f"\n📋 Batches to clean: {', '.join(batches_to_clean)}")
    
    # Get files to delete
    files_to_delete = get_files_to_cleanup(all_results)
    
    if not files_to_delete:
        print(f"\n✅ No files to clean up (all files already deleted or not processed)")
        return 0
    
    # Verify destinations exist (unless --force)
    if not args.force and not args.dry_run:
        print(f"\n🔍 Verifying destination files exist...")
        if not verify_destination_exists(files_to_delete):
            print(f"\n❌ Aborting cleanup. Fix missing destinations or use --force to skip verification.")
            return 1
        print(f"✅ All destination files verified!")
    
    # Confirm before deleting (unless dry-run)
    if not args.dry_run:
        print(f"\n⚠️  ABOUT TO DELETE {len(files_to_delete)} FILES FROM STAGING")
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
    
    # Perform cleanup
    summary = cleanup_files(files_to_delete, dry_run=args.dry_run)
    
    # Save cleanup log
    if not args.dry_run and summary['deleted'] > 0:
        save_cleanup_log(summary, batches_to_clean)
        print(f"\n✅ Cleanup complete! {summary['deleted']} files deleted from staging.")
    elif args.dry_run:
        print(f"\n📝 DRY RUN - No files actually deleted")
    
    return 0 if summary['errors'] == 0 else 1


if __name__ == '__main__':
    exit(main())
