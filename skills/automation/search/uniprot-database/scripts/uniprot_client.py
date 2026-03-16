import argparse
import requests
import sys
import json
import time

BASE_URL = "https://rest.uniprot.org/uniprotkb"

def search_proteins(query, format="json", fields=None):
    url = f"{BASE_URL}/search"
    params = {"query": query, "format": format}
    if fields:
        params["fields"] = fields
    response = requests.get(url, params=params)
    response.raise_for_status()
    if format == "json":
        return response.json()
    return response.text

def get_protein(accession, format="json"):
    url = f"{BASE_URL}/{accession}.{format}"
    response = requests.get(url)
    response.raise_for_status()
    if format == "json":
        return response.json()
    return response.text

def map_ids(ids, from_db="UniProtKB_AC-ID", to_db="Ensembl"):
    submit_url = "https://rest.uniprot.org/idmapping/run"
    data = {
        "from": from_db,
        "to": to_db,
        "ids": ",".join(ids)
    }
    response = requests.post(submit_url, data=data)
    response.raise_for_status()
    job_id = response.json()["jobId"]

    status_url = f"https://rest.uniprot.org/idmapping/status/{job_id}"
    while True:
        status_res = requests.get(status_url)
        status_res.raise_for_status()
        status_data = status_res.json()
        if "jobStatus" in status_data and status_data["jobStatus"] == "FINISHED":
            break
        elif "jobStatus" in status_data and status_data["jobStatus"] == "ERROR":
            print(f"ID mapping job failed: {status_data}", file=sys.stderr)
            return None
        time.sleep(1)

    results_url = f"https://rest.uniprot.org/idmapping/results/{job_id}"
    res = requests.get(results_url)
    res.raise_for_status()
    return res.json()

def main():
    parser = argparse.ArgumentParser(description="UniProt Database REST API Client")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Search command
    search_p = subparsers.add_parser("search")
    search_p.add_argument("query", help="Search query (e.g., 'insulin AND organism_name:\"Homo sapiens\"')")
    search_p.add_argument("--format", default="json", choices=["json", "tsv", "fasta"])
    search_p.add_argument("--fields", help="Comma-separated list of fields to return")

    # Get command
    get_p = subparsers.add_parser("get")
    get_p.add_argument("accession", help="UniProt accession number")
    get_p.add_argument("--format", default="json", choices=["json", "txt", "fasta", "xml"])

    # Map command
    map_p = subparsers.add_parser("map")
    map_p.add_argument("ids", nargs="+", help="List of IDs to map")
    map_p.add_argument("--from-db", default="UniProtKB_AC-ID", help="Source database")
    map_p.add_argument("--to-db", default="Ensembl", help="Target database")

    args = parser.parse_args()

    if args.command == "search":
        result = search_proteins(args.query, args.format, args.fields)
        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(result)

    elif args.command == "get":
        result = get_protein(args.accession, args.format)
        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(result)

    elif args.command == "map":
        result = map_ids(args.ids, args.from_db, args.to_db)
        if result:
            print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
