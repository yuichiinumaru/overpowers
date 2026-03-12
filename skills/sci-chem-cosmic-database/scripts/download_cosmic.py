#!/usr/bin/env python3
import argparse
import requests
import os
import sys
import base64

def get_common_file_path(data_type, assembly='GRCh38', version='latest'):
    shortcuts = {
        'mutations': f'{assembly}/cosmic/{version}/CosmicMutantExport.tsv.gz',
        'gene_census': f'{assembly}/cosmic/{version}/cancer_gene_census.csv',
        'resistance_mutations': f'{assembly}/cosmic/{version}/CosmicResistanceMutations.tsv.gz',
        'structural_variants': f'{assembly}/cosmic/{version}/CosmicStructuralExport.tsv.gz',
        'gene_expression': f'{assembly}/cosmic/{version}/CosmicCompleteGeneExpression.tsv.gz',
        'copy_number': f'{assembly}/cosmic/{version}/CosmicCompleteCNA.tsv.gz',
        'fusion_genes': f'{assembly}/cosmic/{version}/CosmicFusionExport.tsv.gz'
    }
    return shortcuts.get(data_type)

def download_file(email, password, filepath, output_filename=None):
    # COSMIC uses basic auth to get a download token
    auth_str = f"{email}:{password}"
    auth_b64 = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        'Authorization': f'Basic {auth_b64}'
    }
    
    url = f"https://cancer.sanger.ac.uk/cosmic/file_download/{filepath}"
    
    print(f"Requesting download link for {filepath}...")
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    download_url = response.json().get('url')
    if not download_url:
        print("Error: Could not retrieve download URL.")
        return

    if not output_filename:
        output_filename = os.path.basename(filepath)

    print(f"Downloading to {output_filename}...")
    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(output_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    print("Download complete.")

def main():
    parser = argparse.ArgumentParser(description='Download data from COSMIC database.')
    parser.add_argument('email', help='COSMIC registered email')
    parser.add_argument('--password', help='COSMIC password (or use COSMIC_PASSWORD env var)')
    parser.add_argument('--data-type', help='Shorthand data type (e.g., mutations, gene_census)')
    parser.add_argument('--filepath', help='Full path to file on COSMIC server')
    parser.add_argument('--assembly', default='GRCh38', help='Genome assembly (default: GRCh38)')
    parser.add_argument('--output', help='Output filename')

    args = parser.parse_args()

    password = args.password or os.environ.get('COSMIC_PASSWORD')
    if not password:
        print("Error: Password must be provided via --password or COSMIC_PASSWORD environment variable.")
        sys.exit(1)

    filepath = args.filepath
    if args.data_type:
        filepath = get_common_file_path(args.data_type, args.assembly)
    
    if not filepath:
        print("Error: Must provide either --filepath or a valid --data-type.")
        sys.exit(1)

    try:
        download_file(args.email, password, filepath, args.output)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
