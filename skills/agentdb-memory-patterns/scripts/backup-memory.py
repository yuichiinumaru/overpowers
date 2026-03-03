#!/usr/bin/env python3
"""
Backup Memory Script
Backup dan restore memory system dengan kompresi dan timestamp otomatis.

Usage:
    python scripts/backup-memory.py                     # Quick backup (auto-named ZIP)
    python scripts/backup-memory.py --export            # Export dengan timestamp otomatis
    python scripts/backup-memory.py --export backup.zip # Export ke file tertentu
    python scripts/backup-memory.py --restore backup.zip
    python scripts/backup-memory.py --list              # List semua backups
"""

import json
import sys
import shutil
import zipfile
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class MemoryBackup:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent / 'docs' / 'knowledge'  # .agent/scripts -> .agent/memory
        self.entries_path = self.base_path / 'entries'
        self.index_file = self.base_path / 'index.json'
        self.backup_dir = Path(__file__).parent.parent.parent / '_backups'  # .agent/scripts -> .agent -> project/_backups

    def _get_timestamp(self) -> str:
        """Generate timestamp untuk nama file"""
        return datetime.now().strftime('%Y%m%d_%H%M%S')

    def _get_auto_filename(self, ext: str = 'zip') -> str:
        """Generate nama file backup otomatis dengan timestamp"""
        timestamp = self._get_timestamp()
        return f"memory_backup_{timestamp}.{ext}"

    def _ensure_backup_dir(self):
        """Pastikan folder _backups ada"""
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def _get_entry_count(self) -> int:
        """Hitung jumlah entries"""
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                index = json.load(f)
            return index.get('totalEntries', 0)
        return 0

    def export_zip(self, output_path: Optional[str] = None, compression_level: int = 9) -> Dict:
        """
        Export memory folder ke ZIP archive dengan kompresi maksimal.

        Args:
            output_path: Path output (jika None, auto-generate dengan timestamp)
            compression_level: Level kompresi 0-9 (default: 9 = maksimal)
        """
        self._ensure_backup_dir()

        # Auto-generate filename jika tidak disediakan
        if output_path is None:
            output_path = str(self.backup_dir / self._get_auto_filename('zip'))
        elif not os.path.dirname(output_path):
            # Jika hanya nama file, simpan di _backups
            output_path = str(self.backup_dir / output_path)

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        # Hitung ukuran sebelum kompresi
        original_size = sum(f.stat().st_size for f in self.base_path.rglob('*') if f.is_file())

        # Create ZIP dengan kompresi maksimal
        with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:
            for file in self.base_path.rglob('*'):
                if file.is_file():
                    arcname = file.relative_to(self.base_path)
                    zipf.write(file, arcname)

        compressed_size = output.stat().st_size
        compression_ratio = (1 - compressed_size / original_size) * 100 if original_size > 0 else 0

        stats = {
            'file': str(output),
            'filename': output.name,
            'files': sum(1 for _ in self.base_path.rglob('*') if _.is_file()),
            'entries': self._get_entry_count(),
            'original_size': original_size,
            'compressed_size': compressed_size,
            'compression_ratio': compression_ratio,
            'timestamp': self._get_timestamp()
        }

        return stats

    def export_json(self, output_path: Optional[str] = None) -> Dict:
        """Export semua memory ke single JSON file (tidak dikompresi)"""
        self._ensure_backup_dir()

        if output_path is None:
            output_path = str(self.backup_dir / self._get_auto_filename('json'))
        elif not os.path.dirname(output_path):
            output_path = str(self.backup_dir / output_path)

        backup = {
            'version': '1.1.0',
            'exportDate': datetime.now().isoformat(),
            'source': str(self.base_path),
            'totalEntries': self._get_entry_count(),
            'index': None,
            'entries': {}
        }

        # Export index
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                backup['index'] = json.load(f)

        # Export all entries
        for category_dir in self.entries_path.iterdir():
            if category_dir.is_dir():
                backup['entries'][category_dir.name] = {}
                for file in category_dir.glob('*.md'):
                    content = file.read_text(encoding='utf-8')
                    backup['entries'][category_dir.name][file.name] = content

        # Save backup
        output = Path(output_path)
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(backup, f, indent=2, ensure_ascii=False)

        stats = {
            'file': str(output),
            'filename': output.name,
            'categories': len(backup['entries']),
            'files': sum(len(files) for files in backup['entries'].values()),
            'entries': backup['totalEntries'],
            'size': output.stat().st_size,
            'timestamp': self._get_timestamp()
        }

        return stats

    def list_backups(self) -> List[Dict]:
        """List semua backup yang tersedia di folder _backups"""
        self._ensure_backup_dir()

        backups = []
        for file in sorted(self.backup_dir.glob('memory_backup_*'), reverse=True):
            stat = file.stat()
            backups.append({
                'filename': file.name,
                'path': str(file),
                'size': stat.st_size,
                'size_kb': stat.st_size / 1024,
                'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'type': 'ZIP' if file.suffix == '.zip' else 'JSON'
            })

        return backups

    def restore_zip(self, backup_path: str) -> Dict:
        """Restore dari ZIP backup"""
        backup_file = Path(backup_path)

        # Cek di _backups folder jika path tidak absolute
        if not backup_file.exists():
            backup_file = self.backup_dir / backup_path

        if not backup_file.exists():
            raise FileNotFoundError(f"Backup file not found: {backup_path}")

        # Create backup of current state first
        timestamp = self._get_timestamp()
        pre_restore_backup = self.backup_dir / f'pre-restore_{timestamp}.zip'

        # Backup current state sebelum restore
        if self.base_path.exists():
            with zipfile.ZipFile(pre_restore_backup, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
                for file in self.base_path.rglob('*'):
                    if file.is_file():
                        arcname = file.relative_to(self.base_path)
                        zipf.write(file, arcname)

        # Extract
        with zipfile.ZipFile(backup_file, 'r') as zipf:
            zipf.extractall(self.base_path)

        stats = {
            'restored_from': str(backup_file),
            'restored_files': sum(1 for _ in self.base_path.rglob('*') if _.is_file()),
            'pre_restore_backup': str(pre_restore_backup)
        }

        return stats

    def restore_json(self, backup_path: str, merge: bool = False) -> Dict:
        """Restore dari JSON backup"""
        backup_file = Path(backup_path)

        if not backup_file.exists():
            backup_file = self.backup_dir / backup_path

        if not backup_file.exists():
            raise FileNotFoundError(f"Backup file not found: {backup_path}")

        with open(backup_file, 'r', encoding='utf-8') as f:
            backup = json.load(f)

        stats = {'restored_files': 0, 'merged_entries': 0}

        # Restore index
        if backup.get('index'):
            if merge and self.index_file.exists():
                with open(self.index_file, 'r', encoding='utf-8') as f:
                    existing = json.load(f)

                for cat, data in backup['index'].get('categories', {}).items():
                    if cat not in existing['categories']:
                        existing['categories'][cat] = data
                        stats['merged_entries'] += data.get('count', 0)
                    else:
                        existing_ids = {e['id'] for e in existing['categories'][cat].get('entries', [])}
                        for entry in data.get('entries', []):
                            if entry['id'] not in existing_ids:
                                existing['categories'][cat]['entries'].append(entry)
                                existing['categories'][cat]['count'] += 1
                                existing['totalEntries'] += 1
                                stats['merged_entries'] += 1

                existing['lastUpdated'] = datetime.now().isoformat()

                with open(self.index_file, 'w', encoding='utf-8') as f:
                    json.dump(existing, f, indent=2, ensure_ascii=False)
            else:
                with open(self.index_file, 'w', encoding='utf-8') as f:
                    json.dump(backup['index'], f, indent=2, ensure_ascii=False)

        # Restore entries
        for category, files in backup.get('entries', {}).items():
            cat_dir = self.entries_path / category
            cat_dir.mkdir(parents=True, exist_ok=True)

            for filename, content in files.items():
                file_path = cat_dir / filename
                if not merge or not file_path.exists():
                    file_path.write_text(content, encoding='utf-8')
                    stats['restored_files'] += 1

        return stats


def main():
    """Main entry point"""
    backup = MemoryBackup()

    # Quick backup jika tidak ada argument
    if len(sys.argv) < 2:
        print("📦 Quick Backup (ZIP dengan timestamp)...")
        stats = backup.export_zip()
        print(f"\n✅ Backup berhasil!")
        print(f"   📁 File: {stats['filename']}")
        print(f"   📊 Entries: {stats['entries']}")
        print(f"   💾 Ukuran: {stats['original_size']/1024:.1f} KB → {stats['compressed_size']/1024:.1f} KB")
        print(f"   🗜️ Kompresi: {stats['compression_ratio']:.1f}%")
        print(f"   📍 Path: {stats['file']}")
        return

    mode = sys.argv[1]
    file_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        if mode == '--export':
            if file_path and file_path.endswith('.json'):
                print(f"📦 Exporting ke JSON...")
                stats = backup.export_json(file_path)
                print(f"\n✅ Export successful!")
                print(f"   📁 File: {stats['filename']}")
                print(f"   📊 Entries: {stats['entries']}")
                print(f"   💾 Size: {stats['size']/1024:.1f} KB")
            else:
                print(f"📦 Exporting ke ZIP (kompresi maksimal)...")
                stats = backup.export_zip(file_path)
                print(f"\n✅ Export successful!")
                print(f"   📁 File: {stats['filename']}")
                print(f"   📊 Entries: {stats['entries']}")
                print(f"   💾 Size: {stats['original_size']/1024:.1f} KB → {stats['compressed_size']/1024:.1f} KB")
                print(f"   🗜️ Compression: {stats['compression_ratio']:.1f}%")
            print(f"   📍 Path: {stats['file']}")

        elif mode == '--restore':
            if not file_path:
                print("❌ Please specify backup file to restore!")
                sys.exit(1)

            print(f"📥 Restoring from: {file_path}")

            if file_path.endswith('.zip'):
                stats = backup.restore_zip(file_path)
                print(f"\n✅ Restore successful!")
                print(f"   📊 Restored files: {stats['restored_files']}")
                print(f"   🔒 Pre-restore backup: {stats['pre_restore_backup']}")
            else:
                stats = backup.restore_json(file_path)
                print(f"\n✅ Restore successful!")
                print(f"   📊 Restored files: {stats['restored_files']}")

        elif mode == '--merge':
            if not file_path:
                print("❌ Please specify backup file to merge!")
                sys.exit(1)

            print(f"🔀 Merging from: {file_path}")
            stats = backup.restore_json(file_path, merge=True)
            print(f"\n✅ Merge successful!")
            print(f"   📊 New files: {stats['restored_files']}")
            print(f"   📊 Merged entries: {stats['merged_entries']}")

        elif mode == '--list':
            backups = backup.list_backups()
            if not backups:
                print("📁 No backups found in _backups folder")
            else:
                print(f"📁 Found {len(backups)} backup(s):\n")
                print(f"{'No':<3} {'Filename':<40} {'Size':<12} {'Date':<20} {'Type':<5}")
                print("-" * 85)
                for i, b in enumerate(backups, 1):
                    size_str = f"{b['size_kb']:.1f} KB"
                    print(f"{i:<3} {b['filename']:<40} {size_str:<12} {b['modified']:<20} {b['type']:<5}")

        elif mode == '--help' or mode == '-h':
            print(__doc__)
            print("\nOptions:")
            print("  (no args)           Quick backup ke ZIP dengan timestamp otomatis")
            print("  --export [file]     Export (default: ZIP dengan timestamp)")
            print("  --restore <file>    Restore dari backup")
            print("  --merge <file>      Merge backup dengan existing")
            print("  --list              List semua backup di folder _backups")
            print("  --help              Tampilkan help ini")
            print(f"\n📁 Backup folder: {backup.backup_dir}")

        else:
            print(f"❌ Unknown mode: {mode}")
            print("Use --help for usage information")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
