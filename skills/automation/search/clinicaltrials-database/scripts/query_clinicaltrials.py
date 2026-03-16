import argparse
import requests
import sys
import json

BASE_URL = "https://clinicaltrials.gov/api/v2/studies"

def search_studies(condition=None, intervention=None, location=None, sponsor=None, status=None, page_size=10, format="json", page_token=None, sort=None):
    params = {"pageSize": page_size, "format": format}
    if condition: params["query.cond"] = condition
    if intervention: params["query.intr"] = intervention
    if location: params["query.locn"] = location
    if sponsor: params["query.spons"] = sponsor
    if status:
        if isinstance(status, list):
            params["filter.overallStatus"] = ",".join(status)
        else:
            params["filter.overallStatus"] = status
    if page_token: params["pageToken"] = page_token
    if sort: params["sort"] = sort

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    if format == "csv":
        return response.text
    return response.json()

def get_study_details(nct_id):
    url = f"{BASE_URL}/{nct_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def extract_study_summary(study):
    protocol = study.get('protocolSection', {})
    ident = protocol.get('identificationModule', {})
    status = protocol.get('statusModule', {})
    design = protocol.get('designModule', {})

    return {
        "nct_id": ident.get('nctId'),
        "title": ident.get('briefTitle'),
        "status": status.get('overallStatus'),
        "phase": design.get('phases', []),
        "enrollment": design.get('enrollmentInfo', {}).get('count', 'N/A'),
        "last_update": status.get('lastUpdatePostDateStruct', {}).get('date'),
        "brief_summary": protocol.get('descriptionModule', {}).get('briefSummary', '')
    }

def main():
    parser = argparse.ArgumentParser(description="ClinicalTrials.gov Database Query")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Search command
    search_p = subparsers.add_parser("search")
    search_p.add_argument("--cond", help="Condition/disease")
    search_p.add_argument("--intr", help="Intervention/drug")
    search_p.add_argument("--status", help="Trial status (e.g., RECRUITING)")
    search_p.add_argument("--limit", type=int, default=10, help="Max results")

    # Get command
    get_p = subparsers.add_parser("get")
    get_p.add_argument("nct_id", help="NCT ID (e.g., NCT04852770)")

    args = parser.parse_args()

    if args.command == "search":
        print(f"Searching trials...")
        res = search_studies(condition=args.cond, intervention=args.intr, status=args.status, page_size=args.limit)
        print(f"Found {res.get('totalCount', 'unknown')} total trials. Showing up to {args.limit}:")
        for study in res.get('studies', []):
            summary = extract_study_summary(study)
            print(f"- {summary['nct_id']}: {summary['title'][:80]}... [{summary['status']}]")

    elif args.command == "get":
        print(f"Fetching details for {args.nct_id}...")
        study = get_study_details(args.nct_id)
        summary = extract_study_summary(study)
        print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
