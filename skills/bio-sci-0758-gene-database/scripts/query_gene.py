import sys
import requests
import json
import argparse

def query_gene(search_term=None, gene_id=None, organism=None, output_format='json'):
    """
    Query NCBI Gene using E-utilities.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    
    if gene_id:
        # Use ESummary
        url = f"{base_url}esummary.fcgi"
        params = {
            "db": "gene",
            "id": gene_id,
            "retmode": output_format
        }
    else:
        # Use ESearch
        url = f"{base_url}esearch.fcgi"
        query = search_term
        if organism:
            query += f" AND {organism}[organism]"
        params = {
            "db": "gene",
            "term": query,
            "retmode": output_format
        }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if output_format == 'json':
            return response.json()
        else:
            return response.text

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Query NCBI Gene via E-utilities")
    parser.add_argument("--search", help="Search term (e.g., BRCA1)")
    parser.add_argument("--id", help="NCBI Gene ID")
    parser.add_argument("--organism", help="Organism filter")
    parser.add_argument("--format", default="json", help="Output format")
    parser.add_argument("--out", help="Output file path")

    args = parser.parse_args()
    
    result = query_gene(args.search, args.id, args.organism, args.format)
    if result:
        if args.out:
            with open(args.out, 'w') as f:
                if isinstance(result, dict):
                    json.dump(result, f, indent=2)
                else:
                    f.write(result)
            print(f"✅ Results saved to: {args.out}")
        else:
            if isinstance(result, dict):
                print(json.dumps(result, indent=2))
            else:
                print(result)

if __name__ == "__main__":
    main()
