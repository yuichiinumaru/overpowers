import requests
import json
import argparse
from typing import Dict, List

def query_gwas_trait(trait: str, size: int = 20) -> List[Dict]:
    """Query the GWAS Catalog API for associations related to a trait."""
    base_url = "https://www.ebi.ac.uk/gwas/rest/api/traits/search/findByDiseaseTrait"

    print(f"Querying GWAS Catalog for trait: {trait}")

    try:
        response = requests.get(
            base_url,
            params={"diseaseTrait": trait, "size": size}
        )
        response.raise_for_status()
        data = response.json()

        # Check if we have results
        if "_embedded" in data and "traits" in data["_embedded"]:
            traits = data["_embedded"]["traits"]
            print(f"Found {len(traits)} matching traits.")

            all_associations = []

            # For each matching trait, get its associations
            for t in traits:
                trait_id = t["trait"]
                print(f"Fetching associations for: {trait_id}")

                # Check links
                if "_links" in t and "associations" in t["_links"]:
                    assoc_url = t["_links"]["associations"]["href"]

                    assoc_resp = requests.get(assoc_url, params={"size": 10})
                    if assoc_resp.status_code == 200:
                        assoc_data = assoc_resp.json()
                        if "_embedded" in assoc_data and "associations" in assoc_data["_embedded"]:
                            assocs = assoc_data["_embedded"]["associations"]
                            all_associations.extend(assocs)

            print(f"Total associations found: {len(all_associations)}")
            return all_associations

        else:
            print("No matching traits found.")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error querying GWAS Catalog: {e}")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query GWAS Catalog API by disease trait")
    parser.add_argument("--trait", required=True, help="Disease or trait to search for (e.g. 'type 2 diabetes')")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of trait matches to fetch")
    parser.add_argument("--out", default="gwas_results.json", help="Output JSON file")

    args = parser.parse_args()

    results = query_gwas_trait(args.trait, args.limit)

    if results:
        with open(args.out, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.out}")

        # Print a sample
        print("\nSample Association:")
        sample = results[0]
        if "pvalue" in sample:
            print(f"P-value: {sample['pvalue']}")
        if "riskFrequency" in sample:
            print(f"Risk Frequency: {sample['riskFrequency']}")
