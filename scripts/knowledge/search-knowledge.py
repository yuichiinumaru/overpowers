#!/usr/bin/env python3
"""
Search Knowledge Script
Cari knowledge dari memory system.

Usage:
    python scripts/search-knowledge.py "oracle commit"
    python scripts/search-knowledge.py --category gotchas "error"
    python scripts/search-knowledge.py --tags critical,database "mysql"
"""

import json
import sys
import re
from pathlib import Path
from typing import Optional, List, Dict
from datetime import datetime


class KnowledgeSearcher:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent / 'docs' / 'knowledge'  # .agent/scripts -> .agent/memory
        self.entries_path = self.base_path / 'entries'
        self.index_file = self.base_path / 'index.json'

    def search(
        self,
        query: str,
        category: Optional[str] = None,
        tags: Optional[List[str]] = None,
        limit: int = 10
    ) -> List[Dict]:
        """Search knowledge entries"""

        if not self.index_file.exists():
            print("❌ Index file not found!")
            return []

        with open(self.index_file, 'r', encoding='utf-8') as f:
            index = json.load(f)

        results = []
        query_lower = query.lower()

        # Search through all categories
        for cat_name, cat_data in index.get('categories', {}).items():
            # Filter by category if specified
            if category and cat_name != category:
                continue

            for entry in cat_data.get('entries', []):
                score = 0

                # Search in title
                if query_lower in entry.get('title', '').lower():
                    score += 10

                # Search in tags
                entry_tags = entry.get('tags', [])
                for tag in entry_tags:
                    if query_lower in tag.lower():
                        score += 5

                # Filter by tags if specified
                if tags:
                    if not any(t in entry_tags for t in tags):
                        continue

                # Search in file content
                file_path = self.base_path / entry.get('file', '')
                if file_path.exists():
                    content = file_path.read_text(encoding='utf-8').lower()
                    if query_lower in content:
                        score += 3
                        # Bonus for multiple occurrences
                        score += min(content.count(query_lower), 5)

                if score > 0:
                    results.append({
                        'entry': entry,
                        'category': cat_name,
                        'score': score,
                        'file': str(file_path)
                    })

        # Sort by score (descending)
        results.sort(key=lambda x: x['score'], reverse=True)

        # Update access stats
        for result in results[:limit]:
            self._update_access_stats(result['category'], result['entry']['id'])

        return results[:limit]

    def _update_access_stats(self, category: str, entry_id: str):
        """Update access count and last accessed time"""
        try:
            with open(self.index_file, 'r', encoding='utf-8') as f:
                index = json.load(f)

            for entry in index['categories'].get(category, {}).get('entries', []):
                if entry.get('id') == entry_id:
                    entry['accessCount'] = entry.get('accessCount', 0) + 1
                    entry['lastAccessed'] = datetime.now().strftime('%Y-%m-%d')
                    break

            with open(self.index_file, 'w', encoding='utf-8') as f:
                json.dump(index, f, indent=2, ensure_ascii=False)
        except Exception:
            pass  # Silent fail for stats update

    def get_preview(self, file_path: str, max_lines: int = 5) -> str:
        """Get preview of file content"""
        try:
            path = Path(file_path)
            if path.exists():
                lines = path.read_text(encoding='utf-8').split('\n')
                # Skip header lines (title, metadata)
                content_start = 0
                for i, line in enumerate(lines):
                    if line.strip() == '---':
                        content_start = i + 1
                        break
                preview_lines = lines[content_start:content_start + max_lines]
                return '\n'.join(preview_lines).strip()
        except Exception:
            pass
        return ''


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python search-knowledge.py [options] <query>")
        print("\nOptions:")
        print("  --category <cat>    Filter by category (gotchas, patterns, decisions, context)")
        print("  --tags <t1,t2>      Filter by tags (comma-separated)")
        print("  --limit <n>         Limit results (default: 10)")
        print("  --json              Output as JSON")
        print("\nExamples:")
        print('  python search-knowledge.py "oracle commit"')
        print('  python search-knowledge.py --category gotchas "error"')
        print('  python search-knowledge.py --tags critical "database"')
        sys.exit(1)

    # Parse arguments - fixed to handle flags in any position
    args = sys.argv[1:]
    category = None
    tags = None
    limit = 10
    json_output = False
    query_parts = []

    i = 0
    while i < len(args):
        if args[i] == '--category' and i + 1 < len(args):
            category = args[i + 1]
            i += 2
        elif args[i] == '--tags' and i + 1 < len(args):
            tags = [t.strip() for t in args[i + 1].split(',')]
            i += 2
        elif args[i] == '--limit' and i + 1 < len(args):
            limit = int(args[i + 1])
            i += 2
        elif args[i] == '--json':
            json_output = True
            i += 1
        elif not args[i].startswith('--'):
            query_parts.append(args[i])
            i += 1
        else:
            i += 1  # Skip unknown flags

    query = ' '.join(query_parts)

    if not query:
        print("❌ Please provide a search query!")
        sys.exit(1)

    # Search
    searcher = KnowledgeSearcher()
    results = searcher.search(query, category, tags, limit)

    if json_output:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        if not results:
            print(f"🔍 No results found for: '{query}'")
        else:
            print(f"🔍 Found {len(results)} result(s) for: '{query}'\n")
            print("=" * 60)

            for i, result in enumerate(results, 1):
                entry = result['entry']
                print(f"\n{i}. [{result['category'].upper()}] {entry['title']}")
                print(f"   Score: {result['score']} | Tags: {', '.join(entry.get('tags', []))}")
                print(f"   File: {result['file']}")

                # Show preview
                preview = searcher.get_preview(result['file'])
                if preview:
                    print(f"   Preview: {preview[:100]}...")

                print("-" * 60)


if __name__ == '__main__':
    main()
