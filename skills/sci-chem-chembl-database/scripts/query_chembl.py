#!/usr/bin/env python3
import argparse
import sys
import json

try:
    from chembl_webresource_client.new_client import new_client
except ImportError:
    print("Error: chembl_webresource_client not found. Please install it with 'pip install chembl_webresource_client'.")
    sys.exit(1)

def get_molecule(chembl_id):
    molecule = new_client.molecule
    return molecule.get(chembl_id)

def search_molecule_by_name(name):
    molecule = new_client.molecule
    return list(molecule.filter(pref_name__icontains=name))

def query_activity(target_id, activity_type='IC50', max_value=100):
    activity = new_client.activity
    results = activity.filter(
        target_chembl_id=target_id,
        standard_type=activity_type,
        standard_value__lte=max_value
    )
    return list(results)

def main():
    parser = argparse.ArgumentParser(description='Query ChEMBL Database.')
    parser.add_argument('--id', help='Molecule ChEMBL ID (e.g., "CHEMBL25")')
    parser.add_argument('--name', help='Search molecule by name (e.g., "aspirin")')
    parser.add_argument('--target', help='Query activities for target ID (e.g., "CHEMBL203")')
    parser.add_argument('--type', default='IC50', help='Activity type (default: IC50)')
    parser.add_argument('--max-val', type=float, default=100, help='Max activity value (default: 100)')
    parser.add_argument('--output', help='Output JSON file name')

    args = parser.parse_args()

    result = None
    if args.id:
        result = get_molecule(args.id)
    elif args.name:
        result = search_molecule_by_name(args.name)
    elif args.target:
        result = query_activity(args.target, args.type, args.max_val)
    else:
        parser.print_help()
        sys.exit(0)

    if result:
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"Result saved to {args.output}")
        else:
            print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
