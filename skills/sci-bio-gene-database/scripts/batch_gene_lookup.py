import sys
import argparse
import json
import time
from query_gene import query_gene

def batch_lookup(symbols=None, ids=None, organism='human'):
    """
    Performs batch lookup of genes.
    """
    results = []
    
    if symbols:
        symbol_list = symbols.split(',')
        for sym in symbol_list:
            print(f"Looking up symbol: {sym}...")
            res = query_gene(search_term=sym, organism=organism)
            if res:
                results.append({'query': sym, 'result': res})
            time.sleep(0.4) # Rate limiting (3 requests/sec)
            
    if ids:
        id_list = ids.split(',')
        for gid in id_list:
            print(f"Looking up ID: {gid}...")
            res = query_gene(gene_id=gid)
            if res:
                results.append({'query': gid, 'result': res})
            time.sleep(0.4)

    return results

def main():
    parser = argparse.ArgumentParser(description="Batch NCBI Gene lookup")
    parser.add_argument("--symbols", help="Comma-separated gene symbols")
    parser.add_argument("--ids", help="Comma-separated gene IDs")
    parser.add_argument("--organism", default="human", help="Organism for symbols")
    parser.add_argument("--out", help="Output JSON file")

    args = parser.parse_args()
    
    if not args.symbols and not args.ids:
        print("Error: Provide --symbols or --ids")
        return

    data = batch_lookup(args.symbols, args.ids, args.organism)
    
    if args.out:
        with open(args.out, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✅ Batch results saved to: {args.out}")
    else:
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
