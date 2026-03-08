import sys
import requests
import json
import argparse

def search_ena(result_type, query, output_format='json', limit=100, output_file=None):
    """
    Search ENA Portal API.
    result_type: read_run, study, sample, assembly, etc.
    """
    base_url = "https://www.ebi.ac.uk/ena/portal/api/search"
    params = {
        "result": result_type,
        "query": query,
        "format": output_format,
        "limit": limit
    }

    try:
        print(f"Searching ENA for {result_type} with query: {query}...")
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        if output_format == 'json':
            data = response.json()
            if output_file:
                with open(output_file, 'w') as f:
                    json.dump(data, f, indent=2)
                print(f"✅ Saved {len(data)} results to {output_file}")
            else:
                print(json.dumps(data[:5], indent=2))
                if len(data) > 5:
                    print(f"... and {len(data)-5} more results")
        else:
            if output_file:
                with open(output_file, 'w') as f:
                    f.write(response.text)
                print(f"✅ Saved results to {output_file}")
            else:
                print(response.text[:1000])

    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Search ENA Portal API")
    parser.add_argument("result", help="Result type (e.g., read_run, study, sample)")
    parser.add_argument("query", help="Query string (e.g., study_accession=PRJEB1234)")
    parser.add_argument("--format", default="json", choices=["json", "tsv", "csv"], help="Output format")
    parser.add_argument("--limit", type=int, default=100, help="Max results")
    parser.add_argument("--out", help="Output file path")

    args = parser.parse_args()
    search_ena(args.result, args.query, args.format, args.limit, args.out)

if __name__ == "__main__":
    main()
