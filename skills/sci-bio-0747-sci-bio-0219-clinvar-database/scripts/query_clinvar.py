import argparse
import requests
import json

def query_clinvar(gene, significance=None):
    print(f"🔍 Searching ClinVar for gene: {gene}...")
    
    term = f"{gene}[gene]"
    if significance:
        term += f" AND {significance}[CLNSIG]"
        
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "clinvar",
        "term": term,
        "retmode": "json",
        "retmax": 10
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        search_results = response.json()
        
        ids = search_results.get("esearchresult", {}).get("idlist", [])
        print(f"✅ Found {len(ids)} variants.")
        
        if ids:
            print(f"IDs: {', '.join(ids)}")
            # In a real tool, we would fetch summaries for these IDs
        return ids
    except Exception as e:
        print(f"❌ ClinVar query failed: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Query ClinVar database.")
    parser.add_argument("gene", help="Gene symbol")
    parser.add_argument("--significance", help="Clinical significance (e.g., pathogenic)")
    
    args = parser.parse_args()
    query_clinvar(args.gene, args.significance)

if __name__ == "__main__":
    main()
