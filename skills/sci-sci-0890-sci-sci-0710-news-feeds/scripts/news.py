#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import argparse
import textwrap

FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'reuters': 'https://www.reutersagency.com/feed/?best-topics=political-general&post_type=best',
    'ap': 'https://rsshub.app/apnews/topics/ap-top-news',
    'guardian': 'https://www.theguardian.com/world/rss',
    'aljazeera': 'https://www.aljazeera.com/xml/rss/all.xml',
    'npr': 'https://feeds.npr.org/1001/rss.xml',
    'dw': 'https://rss.dw.com/rdf/rss-en-all'
}

def fetch_feed(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_rss(xml_data):
    if not xml_data:
        return []
    try:
        root = ET.fromstring(xml_data)
        items = []
        for item in root.findall('.//item'):
            title = item.find('title')
            link = item.find('link')
            desc = item.find('description')

            items.append({
                'title': title.text if title is not None else 'No title',
                'link': link.text if link is not None else '',
                'description': desc.text if desc is not None else ''
            })
        return items
    except Exception as e:
        print(f"Error parsing RSS: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Fetch latest news headlines from RSS feeds")
    parser.add_argument('--source', choices=list(FEEDS.keys()), help="Fetch from a specific source only")
    parser.add_argument('--topic', help="Filter by topic/keyword")
    parser.add_argument('--limit', type=int, default=5, help="Limit number of items per feed")
    args = parser.parse_args()

    sources = [args.source] if args.source else list(FEEDS.keys())

    for source in sources:
        print(f"--- {source.upper()} ---")
        url = FEEDS[source]
        xml_data = fetch_feed(url)
        items = parse_rss(xml_data)

        count = 0
        for item in items:
            if args.topic and args.topic.lower() not in item['title'].lower() and args.topic.lower() not in item['description'].lower():
                continue

            print(f"* {item['title']}")
            if item['link']:
                print(f"  Link: {item['link']}")

            count += 1
            if count >= args.limit:
                break

        if count == 0:
            print(f"No news found for topic '{args.topic}'" if args.topic else "No news found")
        print()

if __name__ == '__main__':
    main()
