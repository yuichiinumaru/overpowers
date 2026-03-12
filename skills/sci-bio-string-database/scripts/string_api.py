import requests
import argparse
import json

def query_string(genes, species):
    url = "https://string-db.org/api/json/network"
    params = {
        "identifiers": "%0d".join(genes),
        "species": species
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="STRING API helper")
    parser.add_argument("--genes", required=True, help="Comma-separated genes")
    parser.add_argument("--species", required=True, help="NCBI taxon ID")
    args = parser.parse_args()
    result = query_string(args.genes.split(','), args.species)
    print(json.dumps(result, indent=2))
