import sys
import argparse
from bioservices import UniProt

def convert_ids(input_file, from_db, to_db):
    print(f"🔄 Converting IDs from {from_db} to {to_db}...")
    u = UniProt(verbose=False)
    
    with open(input_file, 'r') as f:
        ids = [line.strip() for line in f if line.strip()]
    
    print(f"📄 Loaded {len(ids)} IDs.")
    
    # UniProt mapping supports list of IDs
    mapping = u.mapping(fr=from_db, to=to_db, query=ids)
    
    print("✅ Conversion Results:")
    print(mapping)
    return mapping

def main():
    parser = argparse.ArgumentParser(description="Batch ID converter using UniProt Mapping.")
    parser.add_argument("input", help="File with IDs (one per line)")
    parser.add_argument("--from-db", default="UniProtKB_AC-ID", help="Source database (default: UniProtKB_AC-ID)")
    parser.add_argument("--to-db", default="KEGG", help="Target database (default: KEGG)")
    
    args = parser.parse_args()
    convert_ids(args.input, args.from_db, args.to_db)

if __name__ == "__main__":
    main()
