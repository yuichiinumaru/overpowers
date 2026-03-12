#!/usr/bin/env python3
import argparse
import requests
import json
import sys

BASE_URL = "https://clinicaltrials.gov/api/v2/studies"

def search_studies(condition=None, intervention=None, status="RECRUITING", limit=10):
    params = {
        "pageSize": limit
    }
    if condition:
        params["query.cond"] = condition
    if intervention:
        params["query.intr"] = intervention
    if status:
        params["filter.overallStatus"] = status

    print(f"Searching ClinicalTrials.gov...")
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def get_study(nct_id):
    url = f"{BASE_URL}/{nct_id}"
    print(f"Retrieving study {nct_id}...")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    parser = argparse.ArgumentParser(description='Query ClinicalTrials.gov Database.')
    parser.add_argument('--condition', help='Study condition (e.g., "breast cancer")')
    parser.add_argument('--intervention', help='Intervention/Drug (e.g., "Pembrolizumab")')
    parser.add_argument('--id', help='NCT ID (e.g., "NCT04852770")')
    parser.add_argument('--status', default='RECRUITING', help='Overall status (default: RECRUITING)')
    parser.add_argument('--limit', type=int, default=10, help='Max results (default: 10)')
    parser.add_argument('--output', help='Output JSON file name')

    args = parser.parse_args()

    try:
        if args.id:
            result = get_study(args.id)
        elif args.condition or args.intervention:
            result = search_studies(args.condition, args.intervention, args.status, args.limit)
        else:
            parser.print_help()
            sys.exit(0)

        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"Result saved to {args.output}")
        else:
            print(json.dumps(result, indent=2))
            
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to ClinicalTrials.gov API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
