import sys
import requests
import json
import argparse

def fetch_gene_datasets(symbol=None, gene_id=None, taxon='human'):
    """
    Fetch gene data using NCBI Datasets API.
    """
    base_url = "https://api.ncbi.nlm.nih.gov/datasets/v2/gene"
    
    if gene_id:
        url = f"{base_url}/id/{gene_id}"
    else:
        url = f"{base_url}/symbol/{symbol}/taxon/{taxon}"

    try:
        print(f"Fetching data from NCBI Datasets API...")
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Fetch gene data via NCBI Datasets API")
    parser.add_argument("--symbol", help="Gene symbol")
    parser.add_argument("--taxon", default="human", help="Taxon (default: human)")
    parser.add_argument("--gene-id", help="NCBI Gene ID")
    parser.add_argument("--out", help="Output file path")

    args = parser.parse_args()
    
    result = fetch_gene_datasets(args.symbol, args.gene_id, args.taxon)
    if result:
        if args.out:
            with open(args.out, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"✅ Results saved to: {args.out}")
        else:
            print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
