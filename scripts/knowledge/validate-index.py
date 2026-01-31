#!/usr/bin/env python3
"""
Validate Index Script
Validasi konsistensi antara index.json dan file entries.

Usage:
    python scripts/validate-index.py --report
    python scripts/validate-index.py --fix
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import datetime


class IndexValidator:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent / 'docs' / 'knowledge'  # .agent/scripts -> .agent/memory
        self.entries_path = self.base_path / 'entries'
        self.index_file = self.base_path / 'index.json'

    def validate(self) -> Tuple[List[Dict], List[Dict]]:
        """
        Validate index vs actual files.
        Returns: (orphaned_entries, unindexed_files)
        """
        orphaned = []  # In index but file missing
        unindexed = []  # File exists but not in index

        if not self.index_file.exists():
            print("❌ Index file not found!")
            return [], []

        with open(self.index_file, 'r', encoding='utf-8') as f:
            index = json.load(f)

        # Collect all indexed files
        indexed_files = set()

        for cat_name, cat_data in index.get('categories', {}).items():
            for entry in cat_data.get('entries', []):
                file_path = entry.get('file', '')
                full_path = self.base_path / file_path

                if not full_path.exists():
                    orphaned.append({
                        'category': cat_name,
                        'entry': entry,
                        'expected_path': str(full_path)
                    })
                else:
                    indexed_files.add(str(full_path.resolve()))

        # Find unindexed files
        for category_dir in self.entries_path.iterdir():
            if category_dir.is_dir():
                for file in category_dir.glob('*.md'):
                    if str(file.resolve()) not in indexed_files:
                        unindexed.append({
                            'category': category_dir.name,
                            'file': str(file),
                            'filename': file.name
                        })

        return orphaned, unindexed

    def fix(self, orphaned: List[Dict], unindexed: List[Dict]) -> Dict:
        """Fix inconsistencies"""
        fixed = {
            'removed_orphans': 0,
            'added_unindexed': 0
        }

        with open(self.index_file, 'r', encoding='utf-8') as f:
            index = json.load(f)

        # Remove orphaned entries
        for orphan in orphaned:
            cat = orphan['category']
            entry_id = orphan['entry'].get('id')

            if cat in index['categories']:
                original_count = len(index['categories'][cat]['entries'])
                index['categories'][cat]['entries'] = [
                    e for e in index['categories'][cat]['entries']
                    if e.get('id') != entry_id
                ]
                if len(index['categories'][cat]['entries']) < original_count:
                    index['categories'][cat]['count'] -= 1
                    index['totalEntries'] -= 1
                    fixed['removed_orphans'] += 1

        # Add unindexed files
        for unidx in unindexed:
            cat = unidx['category']
            file_path = Path(unidx['file'])

            # Read file to extract info
            try:
                content = file_path.read_text(encoding='utf-8')
                title = content.split('\n')[0].replace('# ', '').strip()

                # Extract tags if present
                tags = []
                for line in content.split('\n'):
                    if line.startswith('**Tags:**'):
                        tags_str = line.replace('**Tags:**', '').strip()
                        tags = [t.strip() for t in tags_str.split(',') if t.strip()]
                        break

                # Create entry
                entry = {
                    'id': file_path.stem,
                    'title': title[:100],
                    'file': f"entries/{cat}/{file_path.name}",
                    'tags': tags,
                    'addedBy': 'validate-index.py'
                }

                # Ensure category exists
                if cat not in index['categories']:
                    index['categories'][cat] = {
                        'description': f'{cat.title()} entries',
                        'count': 0,
                        'entries': []
                    }

                index['categories'][cat]['entries'].append(entry)
                index['categories'][cat]['count'] += 1
                index['totalEntries'] += 1
                fixed['added_unindexed'] += 1

            except Exception as e:
                print(f"⚠️ Could not process {file_path}: {e}")

        # Update timestamp
        index['lastUpdated'] = datetime.now().isoformat()

        # Save
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)

        return fixed


def main():
    """Main entry point"""
    if len(sys.argv) < 2 or sys.argv[1] not in ['--report', '--fix']:
        print("Usage: python validate-index.py [--report | --fix]")
        print("\nOptions:")
        print("  --report    Show validation report only")
        print("  --fix       Fix inconsistencies automatically")
        sys.exit(1)

    mode = sys.argv[1]
    validator = IndexValidator()

    print("🔍 Validating index.json...")
    orphaned, unindexed = validator.validate()

    # Report
    print("\n" + "=" * 60)
    print("📊 VALIDATION REPORT")
    print("=" * 60)

    if orphaned:
        print(f"\n🚨 ORPHANED ENTRIES ({len(orphaned)}):")
        print("   (In index but file missing)")
        for o in orphaned:
            print(f"   - [{o['category']}] {o['entry'].get('title', 'Unknown')}")
            print(f"     Expected: {o['expected_path']}")
    else:
        print("\n✅ No orphaned entries found")

    if unindexed:
        print(f"\n⚠️ UNINDEXED FILES ({len(unindexed)}):")
        print("   (File exists but not in index)")
        for u in unindexed:
            print(f"   - [{u['category']}] {u['filename']}")
    else:
        print("\n✅ No unindexed files found")

    print("\n" + "=" * 60)

    # Fix if requested
    if mode == '--fix' and (orphaned or unindexed):
        print("\n🔧 Fixing inconsistencies...")
        fixed = validator.fix(orphaned, unindexed)
        print(f"\n✅ Fixed!")
        print(f"   - Removed {fixed['removed_orphans']} orphaned entries")
        print(f"   - Added {fixed['added_unindexed']} unindexed files")
    elif mode == '--fix':
        print("\n✅ Nothing to fix!")
    else:
        if orphaned or unindexed:
            print("\n💡 Run with --fix to automatically fix these issues")


if __name__ == '__main__':
    main()
