import argparse
import pandas as pd
import numpy as np
import os
import sys

try:
    from molfeat.calc import FPCalculator, RDKitDescriptors2D
    from molfeat.trans import MoleculeTransformer
    from molfeat.trans.pretrained import PretrainedMolTransformer
except ImportError:
    print("Error: molfeat not installed. Run 'pip install molfeat' first.")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Batch featurization of molecules using molfeat.')
    parser.add_argument('input', help='Input CSV file containing SMILES')
    parser.add_argument('--column', default='smiles', help='Column name for SMILES')
    parser.add_argument('--method', default='ecfp', help='Featurization method (ecfp, maccs, desc2d, or pretrained name)')
    parser.add_argument('--output', help='Output file path (.csv or .npy)')
    parser.add_argument('--jobs', type=int, default=-1, help='Number of parallel jobs (-1 for all)')
    parser.add_argument('--ignore-errors', action='store_true', help='Skip invalid molecules')

    args = parser.parse_argument()

    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} not found.")
        return

    df = pd.read_csv(args.input)
    if args.column not in df.columns:
        print(f"Error: Column {args.column} not found in {args.input}")
        return

    smiles_list = df[args.column].tolist()

    # Determine featurizer
    if args.method == 'ecfp':
        calc = FPCalculator("ecfp", radius=3)
        transformer = MoleculeTransformer(calc, n_jobs=args.jobs, ignore_errors=args.ignore_errors)
    elif args.method == 'maccs':
        calc = FPCalculator("maccs")
        transformer = MoleculeTransformer(calc, n_jobs=args.jobs, ignore_errors=args.ignore_errors)
    elif args.method == 'desc2d':
        calc = RDKitDescriptors2D()
        transformer = MoleculeTransformer(calc, n_jobs=args.jobs, ignore_errors=args.ignore_errors)
    else:
        # Try as pretrained model
        try:
            transformer = PretrainedMolTransformer(args.method, n_jobs=args.jobs, ignore_errors=args.ignore_errors)
        except Exception as e:
            print(f"Error initializing pretrained transformer: {e}")
            return

    print(f"Featurizing {len(smiles_list)} molecules using {args.method}...")
    features = transformer(smiles_list)

    if args.output:
        if args.output.endswith('.npy'):
            np.save(args.output, features)
            print(f"Features saved to {args.output}")
        else:
            # Default to CSV
            output_df = pd.DataFrame(features)
            output_df.to_csv(args.output, index=False)
            print(f"Features saved to {args.output}")
    else:
        print(f"Featurization complete. Shape: {features.shape}")

if __name__ == "__main__":
    main()
