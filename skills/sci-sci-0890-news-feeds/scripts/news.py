#!/usr/bin/env python3
"""
News Feed Fetcher using RSS feeds from major news organizations.
No external dependencies required (uses only standard library).
"""
import urllib.request
import xml.etree.ElementTree as ET
import argparse
import sys
from datetime import datetime
import re

# Dictionary of RSS feeds
FEEDS = {
    "bbc": {
        "top": "http://feeds.bbci.co.uk/news/rss.xml",
        "world": "http://feeds.bbci.co.uk/news/world/rss.xml",
        "business": "http://feeds.bbci.co.uk/news/business/rss.xml",
        "tech": "http://feeds.bbci.co.uk/news/technology/rss.xml",
        "science": "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
        "health": "http://feeds.bbci.co.uk/news/health/rss.xml"
    },
    "reuters": {
        "top": "http://feeds.reuters.com/reuters/topNews",
        "world": "http://feeds.reuters.com/Reuters/worldNews",
        "business": "http://feeds.reuters.com/reuters/businessNews",
        "tech": "http://feeds.reuters.com/reuters/technologyNews",
        "science": "http://feeds.reuters.com/reuters/scienceNews",
        "health": "http://feeds.reuters.com/reuters/healthNews"
    },
    "ap": {
        "top": "https://apnews.com/index.rss"
    },
    "guardian": {
        "top": "https://www.theguardian.com/uk/rss",
        "world": "https://www.theguardian.com/world/rss",
        "business": "https://www.theguardian.com/business/rss",
        "tech": "https://www.theguardian.com/technology/rss",
        "science": "https://www.theguardian.com/science/rss"
    },
    "aljazeera": {
        "top": "https://www.aljazeera.com/xml/rss/all.xml"
    },
    "npr": {
        "top": "https://feeds.npr.org/1001/rss.xml"
    },
    "dw": {
        "top": "https://rss.dw.com/rdf/rss-en-all"
    }
}

def clean_html(raw_html):
    """Remove HTML tags from a string."""
    if not raw_html:
        return ""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext.strip()

def fetch_feed(source_name, category, url, limit=8, topic=None):
    """Fetch and parse a single RSS feed."""
    items = []

    try:
        # User-Agent is required for some feeds that block scripts
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()

        root = ET.fromstring(xml_data)

        # Determine if RSS (item) or Atom/RDF
        channel_items = root.findall('.//item')
        if not channel_items:
            # Try finding items without channel (e.g. RDF)
            channel_items = [e for e in root if e.tag.endswith('item')]

        count = 0
        for item in channel_items:
            if count >= limit:
                break

            title_elem = item.find('title')
            # Handle namespaces if present
            if title_elem is None:
                title_elem = item.find('{http://purl.org/rss/1.0/}title')

            desc_elem = item.find('description')
            if desc_elem is None:
                desc_elem = item.find('{http://purl.org/rss/1.0/}description')

            link_elem = item.find('link')
            if link_elem is None:
                link_elem = item.find('{http://purl.org/rss/1.0/}link')

            date_elem = item.find('pubDate')
            if date_elem is None:
                date_elem = item.find('{http://purl.org/dc/elements/1.1/}date')

            title = title_elem.text if title_elem is not None else "No Title"
            desc = clean_html(desc_elem.text) if desc_elem is not None else ""
            link = link_elem.text if link_elem is not None else "#"
            pub_date = date_elem.text if date_elem is not None else ""

            # Filter by topic if specified
            if topic:
                topic_lower = topic.lower()
                if topic_lower not in title.lower() and topic_lower not in desc.lower():
                    continue

            items.append({
                'title': title,
                'description': desc,
                'link': link,
                'pubDate': pub_date
            })
            count += 1

        return items

    except Exception as e:
        print(f"Error fetching {source_name} ({category}): {e}", file=sys.stderr)
        return []

def print_markdown(source_name, items):
    """Print feed items in Markdown format."""
    if not items:
        return

    print(f"## {source_name.upper()}\n")
    for item in items:
        print(f"### [{item['title']}]({item['link']})")
        if item['pubDate']:
            print(f"*Published: {item['pubDate']}*")
        if item['description']:
            print(f"\n> {item['description']}\n")
        print("---")
    print("\n")

def list_sources():
    """Print available sources and categories."""
    print("# Available News Sources\n")
    for source, categories in FEEDS.items():
        cats = ", ".join(categories.keys())
        print(f"- **{source}**: {cats}")

def main():
    parser = argparse.ArgumentParser(description="Fetch latest news headlines from RSS feeds")
    parser.add_argument("--source", type=str, choices=list(FEEDS.keys()), help="Specific source to fetch from")
    parser.add_argument("--category", type=str, default="top", help="Category (e.g. top, world, tech) - see --list-sources")
    parser.add_argument("--topic", type=str, help="Filter headlines by keyword/topic")
    parser.add_argument("--limit", type=int, default=8, help="Max items per feed")
    parser.add_argument("--list-sources", action="store_true", help="List all available sources and categories")

    args = parser.parse_args()

    if args.list_sources:
        list_sources()
        return

    print(f"# News Briefing - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    if args.topic:
        print(f"*Filtering for topic: '{args.topic}'*\n")

    sources_to_fetch = [args.source] if args.source else list(FEEDS.keys())

    for source in sources_to_fetch:
        categories = FEEDS[source]

        # Default to 'top' if category not available for this source
        cat_to_fetch = args.category if args.category in categories else "top"

        url = categories[cat_to_fetch]
        items = fetch_feed(source, cat_to_fetch, url, limit=args.limit, topic=args.topic)

        display_name = f"{source.upper()} ({cat_to_fetch})"
        print_markdown(display_name, items)

if __name__ == "__main__":
    main()
