import subprocess
import sys
import argparse

def search_zinc(mode, query, output_fields="zinc_id,smiles,catalogs,tranche"):
    """
    Search ZINC22 database via CartBlanche22 API.
    """
    base_url = "https://cartblanche22.docking.org/"
    
    if mode == "id":
        url = f"{base_url}substances.txt:zinc_id={query}&output_fields={output_fields}"
    elif mode == "smiles":
        # Note: SMILES should be URL-encoded if it contains special characters
        url = f"{base_url}smiles.txt:smiles={query}&output_fields={output_fields}"
    elif mode == "random":
        url = f"{base_url}substance/random.txt:count={query}&output_fields={output_fields}"
    else:
        print(f"Error: Unknown mode '{mode}'")
        return

    print(f"Searching ZINC22: {url}")
    try:
        result = subprocess.run(['curl', '-s', url], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error executing curl: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search ZINC22 database")
    parser.add_argument("mode", choices=["id", "smiles", "random"], help="Search mode")
    parser.add_argument("query", help="Query (ZINC ID, SMILES, or count for random)")
    parser.add_argument("--fields", default="zinc_id,smiles,catalogs,tranche", help="Output fields")
    
    args = parser.parse_args()
    search_zinc(args.mode, args.query, args.fields)
