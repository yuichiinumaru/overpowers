#!/usr/bin/env python3
import argparse
import sys
import json

try:
    import datamol as dm
    import pandas as pd
except ImportError:
    print("Error: datamol or pandas not found. Please install them with 'pip install datamol pandas'.")
    sys.exit(1)

def process_smiles(smiles_list):
    mols = [dm.to_mol(smi) for smi in smiles_list]
    mols = [dm.standardize_mol(m) for m in mols if m is not None]
    return mols

def analyze_mols(mols):
    if not mols:
        return None
    desc_df = dm.descriptors.batch_compute_many_descriptors(mols, n_jobs=-1)
    return desc_df

def main():
    parser = argparse.ArgumentParser(description='Molecular analysis using datamol.')
    parser.add_argument('--smiles', nargs='+', help='List of SMILES strings')
    parser.add_argument('--sdf', help='Path to SDF file')
    parser.add_argument('--output-csv', help='Output descriptors to CSV')
    parser.add_argument('--viz', help='Output visualization image (e.g., mols.png)')

    args = parser.parse_args()

    mols = []
    if args.smiles:
        mols = process_smiles(args.smiles)
    elif args.sdf:
        print(f"Reading SDF from {args.sdf}...")
        df = dm.read_sdf(args.sdf)
        mols = df['mol'].tolist()
    else:
        parser.print_help()
        sys.exit(0)

    if not mols:
        print("No valid molecules found.")
        sys.exit(1)

    print(f"Processing {len(mols)} molecules...")
    desc_df = analyze_mols(mols)
    
    if desc_df is not None:
        if args.output_csv:
            desc_df.to_csv(args.output_csv, index=False)
            print(f"Descriptors saved to {args.output_csv}")
        else:
            print(desc_df.head())

    if args.viz:
        dm.viz.to_image(mols, outfile=args.viz)
        print(f"Visualization saved to {args.viz}")

if __name__ == "__main__":
    main()
