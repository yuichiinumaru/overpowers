#!/usr/bin/env python3
import argparse
import os

def generate_script(sample_sheet, download_dir, clinical_dir, output_h5ad):
    content = f"""import omicverse as ov
import scanpy as sc

# Initialize plot settings
ov.plot_set()

# Define paths
sample_sheet_path = '{sample_sheet}'
download_dir = '{download_dir}'
clinical_dir = '{clinical_dir}'

print("Initializing TCGA helper...")
# Instantiate the TCGA helper
aml_tcga = ov.bulk.pyTCGA(sample_sheet_path, download_dir, clinical_dir)

print("Building AnnData object...")
# Build the AnnData object with raw counts, FPKM, and TPM layers
aml_tcga.adata_init()

# Initialise metadata and clinical information
print("Populating metadata...")
aml_tcga.adata_meta_init()

print("Initializing survival information...")
# Note: spelling 'survial' is intentional in the API
aml_tcga.survial_init()

# Save the enriched dataset
print(f"Exporting results to {output_h5ad}...")
aml_tcga.adata.write_h5ad('{output_h5ad}', compression='gzip')

print("Preprocessing complete!")
"""
    return content

def main():
    parser = argparse.ArgumentParser(description='Generate a TCGA preprocessing script for omicverse.')
    parser.add_argument('--sheet', help='Path to gdc_sample_sheet.tsv', default='gdc_sample_sheet.tsv')
    parser.add_argument('--download', help='Path to gdc_download directory', default='gdc_download')
    parser.add_argument('--clinical', help='Path to clinical.cart directory', default='clinical.cart')
    parser.add_argument('--output', help='Output script name', default='run_tcga_preprocess.py')
    parser.add_argument('--h5ad', help='Output h5ad file name', default='ov_tcga_processed.h5ad')

    args = parser.parse_args()

    content = generate_script(args.sheet, args.download, args.clinical, args.h5ad)
    
    with open(args.output, 'w') as f:
        f.write(content)
    
    print(f"Generated {args.output}")
    print(f"Review the generated script and run it with 'python3 {args.output}'")

if __name__ == "__main__":
    main()
