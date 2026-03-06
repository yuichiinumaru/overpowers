#!/usr/bin/env python3
import argparse
import json
import sys

try:
    from tooluniverse import ToolUniverse
except ImportError:
    print("Error: tooluniverse library not found. Please install it to use this script.")
    sys.exit(1)

def search_data(query, species=None, limit=10):
    tu = ToolUniverse()
    tu.load_tools()
    
    results = {}
    
    print(f"Searching ArrayExpress for: {query}...")
    try:
        ae_results = tu.tools.arrayexpress_search_experiments(
            keywords=query,
            species=species,
            limit=limit
        )
        results['ArrayExpress'] = ae_results
    except Exception as e:
        print(f"Error searching ArrayExpress: {e}")
        results['ArrayExpress'] = []

    print(f"Searching BioStudies for: {query}...")
    try:
        bs_results = tu.tools.biostudies_search_studies(
            query=query,
            limit=limit
        )
        results['BioStudies'] = bs_results
    except Exception as e:
        print(f"Error searching BioStudies: {e}")
        results['BioStudies'] = []
        
    return results

def main():
    parser = argparse.ArgumentParser(description='Search for expression and multi-omics data using ToolUniverse.')
    parser.add_argument('query', help='Search keywords (e.g., "breast cancer RNA-seq")')
    parser.add_argument('--species', help='Species scientific name (e.g., "Homo sapiens")')
    parser.add_argument('--limit', type=int, default=10, help='Maximum number of results (default: 10)')
    parser.add_argument('--output', help='Output JSON file name')

    args = parser.parse_args()

    results = search_data(args.query, args.species, args.limit)
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.output}")
    else:
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
