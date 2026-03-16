import sys
import requests
import time
import json
import argparse

def query_ensembl(endpoint, params=None, max_retries=3):
    """
    General purpose query for Ensembl REST API with rate limiting and error handling.
    """
    server = "https://rest.ensembl.org"
    headers = {"Content-Type": "application/json"}

    for attempt in range(max_retries):
        try:
            response = requests.get(
                f"{server}{endpoint}",
                headers=headers,
                params=params
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # Rate limited
                retry_after = int(response.headers.get('Retry-After', 1))
                print(f"Rate limited. Waiting {retry_after} seconds...")
                time.sleep(retry_after)
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt == max_retries - 1:
                raise e
            time.sleep(1)

    return None

def main():
    parser = argparse.ArgumentParser(description="Query Ensembl REST API")
    parser.add_argument("endpoint", help="API endpoint (e.g., /lookup/symbol/human/BRCA2)")
    parser.add_argument("--params", help="JSON string of parameters")
    parser.add_argument("--out", help="Output file path")

    args = parser.parse_args()
    
    params = json.loads(args.params) if args.params else None
    
    try:
        result = query_ensembl(args.endpoint, params)
        if result:
            if args.out:
                with open(args.out, 'w') as f:
                    json.dump(result, f, indent=2)
                print(f"✅ Results saved to: {args.out}")
            else:
                print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
