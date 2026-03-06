import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="ChEMBL Database Example Queries")
    parser.add_argument("--action", choices=["molecule", "target", "activity", "drug"], required=True)
    parser.add_argument("--query", required=True, help="Search query")

    args = parser.parse_args()

    try:
        from chembl_webresource_client.new_client import new_client
    except ImportError:
        print("Error: chembl_webresource_client not installed.", file=sys.stderr)
        sys.exit(1)

    if args.action == "molecule":
        print(f"Searching for molecule: {args.query}...")
        molecule = new_client.molecule
        if args.query.startswith("CHEMBL"):
            res = molecule.get(args.query)
            print(json.dumps(res, indent=2))
        else:
            results = molecule.filter(pref_name__icontains=args.query)
            print(f"Found {len(results)} results. Showing first 1:")
            if results: print(json.dumps(results[0], indent=2))

    elif args.action == "target":
        print(f"Searching for target: {args.query}...")
        target = new_client.target
        results = target.filter(pref_name__icontains=args.query)
        print(f"Found {len(results)} results. Showing first 1:")
        if results: print(json.dumps(results[0], indent=2))

    elif args.action == "activity":
        print(f"Searching for activity for target/molecule: {args.query}...")
        activity = new_client.activity
        if args.query.startswith("CHEMBL"):
            # Assume it's a target ID for this example
            results = activity.filter(target_chembl_id=args.query, standard_type="IC50").order_by("standard_value")
            print(f"Found {len(results)} results. Showing first 1:")
            if results: print(json.dumps(results[0], indent=2))
        else:
            print("Please provide a ChEMBL ID for activity search.")

if __name__ == "__main__":
    main()
