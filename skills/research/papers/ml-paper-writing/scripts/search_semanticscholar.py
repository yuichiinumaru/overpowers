#!/usr/bin/env python3
"""
Helper script to search Semantic Scholar for papers.
Helps verify citations exist.
"""
import requests
import argparse

def search_paper(query: str, limit: int = 5):
    """Search for a paper using Semantic Scholar Graph API."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit={limit}&fields=title,authors,year,externalIds"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "data" not in data or not data["data"]:
            print(f"No results found for query: '{query}'")
            return

        print(f"Search results for: '{query}'\n")

        for i, paper in enumerate(data["data"], 1):
            title = paper.get("title", "Unknown Title")
            year = paper.get("year", "Unknown Year")
            authors = ", ".join([a.get("name", "") for a in paper.get("authors", [])][:3])
            if len(paper.get("authors", [])) > 3:
                authors += " et al."

            external_ids = paper.get("externalIds", {})
            doi = external_ids.get("DOI", "No DOI available")
            arxiv = external_ids.get("ArXiv", "No ArXiv ID available")

            print(f"{i}. {title} ({year})")
            print(f"   Authors: {authors}")
            if doi != "No DOI available":
                print(f"   DOI: {doi}")
            if arxiv != "No ArXiv ID available":
                print(f"   ArXiv: {arxiv}")
            print(f"   Paper ID: {paper.get('paperId')}\n")

    except Exception as e:
        print(f"Error searching Semantic Scholar: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search Semantic Scholar for papers")
    parser.add_argument("query", help="The search query (e.g., 'attention mechanism transformers Vaswani')")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of results to return")

    args = parser.parse_args()
    search_paper(args.query, args.limit)
