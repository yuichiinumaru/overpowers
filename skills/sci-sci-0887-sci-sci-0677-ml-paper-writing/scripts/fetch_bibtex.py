#!/usr/bin/env python3
"""
Helper script to fetch BibTeX via DOI using CrossRef API.
Helps prevent hallucinated citations.
"""
import requests
import argparse
import sys

def doi_to_bibtex(doi: str) -> str:
    """Get verified BibTeX from DOI via CrossRef."""
    try:
        response = requests.get(
            f"https://doi.org/{doi}",
            headers={"Accept": "application/x-bibtex"}
        )
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error fetching BibTeX for DOI {doi}: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch BibTeX for a given DOI")
    parser.add_argument("doi", help="The DOI to fetch (e.g., 10.48550/arXiv.1706.03762)")

    args = parser.parse_args()

    bibtex = doi_to_bibtex(args.doi)
    print(bibtex)
