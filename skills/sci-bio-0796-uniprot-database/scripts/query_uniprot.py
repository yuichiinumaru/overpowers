#!/usr/bin/env python3
import argparse
import requests
import json
import sys

BASE_URL = "https://rest.uniprot.org/uniprotkb"

def search_proteins(query, format='json', limit=10):
    url = f"{BASE_URL}/search"
    params = {
        'query': query,
        'format': format,
        'size': limit
    }
    print(f"Searching UniProt for: {query}...")
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text

def get_protein(accession, format='json'):
    url = f"{BASE_URL}/{accession}.{format}"
    print(f"Retrieving protein {accession}...")
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def main():
    parser = argparse.ArgumentParser(description='Query UniProt Database.')
    parser.add_argument('--search', help='Search query (e.g., "gene:BRCA1 AND reviewed:true")')
    parser.add_argument('--accession', help='Protein accession (e.g., "P12345")')
    parser.add_argument('--format', choices=['json', 'fasta', 'tsv', 'xml'], default='json', help='Output format (default: json)')
    parser.add_argument('--limit', type=int, default=10, help='Max search results (default: 10)')
    parser.add_argument('--output', help='Output file name')

    args = parser.parse_args()

    try:
        if args.search:
            result = search_proteins(args.search, args.format, args.limit)
        elif args.accession:
            result = get_protein(args.accession, args.format)
        else:
            parser.print_help()
            sys.exit(0)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"Result saved to {args.output}")
        else:
            print(result)
            
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to UniProt API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
