import argparse
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import json

def search_arxiv(query, max_results=100, days=365):
    base_url = "http://export.arxiv.org/api/query?"
    
    # Calculate date filter
    date_cutoff = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d%H%M%S')
    
    # Build query
    search_query = f'all:"{query}"'
    params = {
        "search_query": search_query,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    
    return response.text

def parse_arxiv_response(xml_data):
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    papers = []
    for entry in root.findall('atom:entry', ns):
        paper = {
            "title": entry.find('atom:title', ns).text.strip().replace('\n', ' '),
            "id": entry.find('atom:id', ns).text.split('/')[-1],
            "summary": entry.find('atom:summary', ns).text.strip().replace('\n', ' '),
            "published": entry.find('atom:published', ns).text,
            "link": entry.find('atom:link[@title="pdf"]', ns).attrib['href'] if entry.find('atom:link[@title="pdf"]', ns) is not None else entry.find('atom:link', ns).attrib['href']
        }
        papers.append(paper)
    return papers

def main():
    parser = argparse.ArgumentParser(description='arXiv Pattern Scanner')
    parser.add_argument('--query', '-q', default='agent AI pattern', help='Search query')
    parser.add_argument('--max-results', '-n', type=int, default=10, help='Max results')
    parser.add_argument('--days', '-d', type=int, default=30, help='Last N days')
    parser.add_argument('--export-md', help='Export to Markdown file')
    
    args = parser.parse_args()
    
    print(f"Searching arXiv for '{args.query}' from last {args.days} days...")
    xml_data = search_arxiv(args.query, args.max_results, args.days)
    papers = parse_arxiv_response(xml_data)
    
    if args.export_md:
        with open(args.export_md, 'w') as f:
            f.write(f"# arXiv Research Report: {args.query}\n\n")
            for p in papers:
                f.write(f"## {p['title']}\n")
                f.write(f"- **ID**: {p['id']}\n")
                f.write(f"- **Published**: {p['published']}\n")
                f.write(f"- **Link**: {p['link']}\n\n")
                f.write(f"{p['summary']}\n\n")
        print(f"Report exported to {args.export_md}")
    else:
        for p in papers:
            print(f"- {p['title']} ({p['id']})")

if __name__ == "__main__":
    main()
