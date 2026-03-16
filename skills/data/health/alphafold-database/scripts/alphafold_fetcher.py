#!/usr/bin/env python3
import argparse
import sys
import json
import urllib.request
import urllib.error
import os

ALPHAFOLD_API_BASE = "https://alphafold.ebi.ac.uk/api"

def fetch_prediction(uniprot_id):
    """Fetch AlphaFold prediction metadata for a UniProt ID."""
    url = f"{ALPHAFOLD_API_BASE}/prediction/{uniprot_id}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        if e.code == 404:
            print(f"Prediction not found for UniProt ID: {uniprot_id}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        return None

def download_file(url, output_path):
    """Download a file from a URL to the specified output path."""
    try:
        print(f"Downloading {url} to {output_path}...")
        urllib.request.urlretrieve(url, output_path)
        print(f"Successfully downloaded {output_path}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="AlphaFold DB Fetcher")
    parser.add_argument("uniprot_id", help="UniProt ID (e.g., P00520)")
    parser.add_argument("--info-only", action="store_true", help="Only show metadata, do not download files")
    parser.add_argument("--download-cif", action="store_true", help="Download the mmCIF structure file")
    parser.add_argument("--download-pdb", action="store_true", help="Download the PDB structure file")
    parser.add_argument("--download-pae", action="store_true", help="Download the PAE JSON file")
    parser.add_argument("--outdir", default=".", help="Output directory for downloads")

    args = parser.parse_args()

    # Ensure output directory exists
    if not args.info_only and args.outdir != ".":
        os.makedirs(args.outdir, exist_ok=True)

    data = fetch_prediction(args.uniprot_id)
    if not data:
        sys.exit(1)

    print(f"Found {len(data)} prediction(s) for {args.uniprot_id}")

    for i, pred in enumerate(data):
        print(f"\nPrediction {i+1}:")
        print(f"  Entry ID: {pred.get('entryId')}")
        print(f"  Gene: {pred.get('gene')}")
        print(f"  Organism: {pred.get('organismScientificName')}")

        if args.info_only:
            continue

        # Download requested files
        if args.download_cif and 'cifUrl' in pred:
            out_path = os.path.join(args.outdir, f"{pred.get('entryId')}.cif")
            download_file(pred['cifUrl'], out_path)

        if args.download_pdb and 'pdbUrl' in pred:
            out_path = os.path.join(args.outdir, f"{pred.get('entryId')}.pdb")
            download_file(pred['pdbUrl'], out_path)

        if args.download_pae and 'paeImageUrl' in pred: # Actually PAE json URL despite name
            # Fix: the API sometimes calls it paeImageUrl but it's the json. Or paeDocUrl.
            # We'll construct the json URL directly as it's predictable
            entry_id = pred.get('entryId')
            pae_url = f"https://alphafold.ebi.ac.uk/files/{entry_id}-pae_v4.json"
            out_path = os.path.join(args.outdir, f"{entry_id}_pae.json")
            download_file(pae_url, out_path)

if __name__ == "__main__":
    main()
