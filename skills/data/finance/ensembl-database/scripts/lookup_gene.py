import sys
import argparse
import json
from ensembl_query import query_ensembl

def lookup_gene(symbol, species='human', get_sequence=False):
    """
    Looks up a gene by symbol and optionally retrieves its sequence.
    """
    # 1. Lookup ID
    print(f"Looking up gene: {symbol} in {species}...")
    endpoint = f"/lookup/symbol/{species}/{symbol}?expand=1"
    gene_data = query_ensembl(endpoint)
    
    if not gene_data:
        print(f"Error: Gene '{symbol}' not found")
        return

    print(f"Found {gene_data['id']} ({gene_data['biotype']}) at {gene_data['seq_region_name']}:{gene_data['start']}-{gene_data['end']}")

    results = {'gene': gene_data}

    # 2. Get Sequence
    if get_sequence:
        print("Retrieving sequence...")
        seq_endpoint = f"/sequence/id/{gene_data['id']}"
        seq_data = query_ensembl(seq_endpoint)
        if seq_data:
            results['sequence'] = seq_data

    return results

def main():
    parser = argparse.ArgumentParser(description="Lookup gene information from Ensembl")
    parser.add_argument("symbol", help="Gene symbol (e.g., BRCA2)")
    parser.add_argument("--species", default="human", help="Species name")
    parser.add_argument("--seq", action="store_true", help="Include sequence")
    parser.add_argument("--out", help="Output file path (JSON)")

    args = parser.parse_args()
    
    try:
        data = lookup_gene(args.symbol, args.species, args.seq)
        if data:
            if args.out:
                with open(args.out, 'w') as f:
                    json.dump(data, f, indent=2)
                print(f"✅ Results saved to: {args.out}")
            else:
                # Print summary
                g = data['gene']
                print(f"\nID: {g['id']}")
                print(f"Description: {g.get('description', 'N/A')}")
                if 'sequence' in data:
                    print(f"Sequence Length: {len(data['sequence']['seq'])}")
                    print(f"Sequence (first 50bp): {data['sequence']['seq'][:50]}...")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
