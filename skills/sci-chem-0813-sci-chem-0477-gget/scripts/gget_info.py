import gget
import sys
import json

def get_gene_info(ens_ids):
    """Retrieve comprehensive gene/transcript metadata"""
    if isinstance(ens_ids, str):
        ens_ids = [ens_ids]
    
    print(f"Fetching info for: {', '.join(ens_ids)}")
    info = gget.info(ens_ids)
    return info

if __name__ == "__main__":
    ids = sys.argv[1:] if len(sys.argv) > 1 else ["ENSG00000034713"]
    try:
        result = get_gene_info(ids)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
