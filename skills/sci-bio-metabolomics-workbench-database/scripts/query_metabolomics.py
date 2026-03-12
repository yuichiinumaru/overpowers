import requests
import json
import argparse
from typing import Dict, List, Any

def get_compound_info(cid: str) -> Dict[str, Any]:
    """Get compound information by PubChem CID."""
    print(f"Fetching compound info for CID: {cid}")
    url = f"https://www.metabolomicsworkbench.org/rest/compound/pubchem_id/{cid}/all"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error querying Metabolomics Workbench: {e}")
        return {}

def list_public_studies() -> Dict[str, Any]:
    """List all available public studies."""
    print("Fetching list of public studies...")
    url = "https://www.metabolomicsworkbench.org/rest/study/study_id/ST/summary"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error querying Metabolomics Workbench: {e}")
        return {}

def search_mass(mz: float, tolerance: float = 0.05, ion: str = "M+H") -> Dict[str, Any]:
    """Search for compounds by m/z value with specific adduct."""
    print(f"Searching m/z {mz} (±{tolerance}) with ion {ion}...")
    url = f"https://www.metabolomicsworkbench.org/rest/refmet/match/{mz}/{ion}/{tolerance}/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error querying Metabolomics Workbench: {e}")
        return {}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query Metabolomics Workbench REST API")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Compound info command
    parser_compound = subparsers.add_parser("compound", help="Get compound info by PubChem CID")
    parser_compound.add_argument("--cid", required=True, help="PubChem CID (e.g. 5950)")
    parser_compound.add_argument("--out", default="compound.json", help="Output file")

    # Studies command
    parser_studies = subparsers.add_parser("studies", help="List all public studies")
    parser_studies.add_argument("--out", default="studies.json", help="Output file")

    # Mass search command
    parser_mass = subparsers.add_parser("mass", help="Search by m/z value")
    parser_mass.add_argument("--mz", type=float, required=True, help="m/z value")
    parser_mass.add_argument("--tol", type=float, default=0.05, help="m/z tolerance")
    parser_mass.add_argument("--ion", default="M+H", help="Adduct ion (e.g. M+H, M-H)")
    parser_mass.add_argument("--out", default="mass_search.json", help="Output file")

    args = parser.parse_args()

    results = None

    if args.command == "compound":
        results = get_compound_info(args.cid)
    elif args.command == "studies":
        results = list_public_studies()
    elif args.command == "mass":
        results = search_mass(args.mz, args.tol, args.ion)
    else:
        parser.print_help()

    if results:
        with open(args.out, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.out}")
