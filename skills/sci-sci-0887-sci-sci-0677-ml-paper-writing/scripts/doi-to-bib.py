#!/usr/bin/env python3
import sys
import argparse
import requests

def doi_to_bibtex(doi):
    """Get verified BibTeX from DOI via CrossRef."""
    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error fetching DOI {doi}: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Fetch verified BibTeX from a DOI.")
    parser.add_argument("doi", help="The DOI to fetch (e.g., 10.48550/arXiv.1706.03762)")
    args = parser.parse_args()

    bibtex = doi_to_bibtex(args.doi)
    print(bibtex)

if __name__ == "__main__":
    main()
