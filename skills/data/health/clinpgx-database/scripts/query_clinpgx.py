#!/usr/bin/env python3
import argparse
import requests
import json
import sys
import time

BASE_URL = "https://api.clinpgx.org/v1"

def rate_limited_get(url, params=None):
    # 2 requests per second max
    response = requests.get(url, params=params)
    time.sleep(0.5)
    response.raise_for_status()
    return response.json()

def get_gene_info(gene_symbol):
    url = f"{BASE_URL}/gene/{gene_symbol}"
    print(f"Retrieving gene info for {gene_symbol}...")
    return rate_limited_get(url)

def get_chemical_info(name):
    url = f"{BASE_URL}/chemical"
    params = {"name": name}
    print(f"Searching for chemical: {name}...")
    return rate_limited_get(url, params)

def get_gene_drug_pair(gene, drug):
    url = f"{BASE_URL}/geneDrugPair"
    params = {"gene": gene, "drug": drug}
    print(f"Retrieving gene-drug pair: {gene} - {drug}...")
    return rate_limited_get(url, params)

def main():
    parser = argparse.ArgumentParser(description='Query ClinPGx Database.')
    parser.add_argument('--gene', help='Gene symbol (e.g., "CYP2D6")')
    parser.add_argument('--chemical', help='Chemical/Drug name (e.g., "warfarin")')
    parser.add_argument('--drug', help='Drug name for gene-drug pair (requires --gene)')
    parser.add_argument('--output', help='Output JSON file name')

    args = parser.parse_args()

    try:
        if args.gene and args.drug:
            result = get_gene_drug_pair(args.gene, args.drug)
        elif args.gene:
            result = get_gene_info(args.gene)
        elif args.chemical:
            result = get_chemical_info(args.chemical)
        else:
            parser.print_help()
            sys.exit(0)

        if result:
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(result, f, indent=2)
                print(f"Result saved to {args.output}")
            else:
                print(json.dumps(result, indent=2))
                
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to ClinPGx API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
