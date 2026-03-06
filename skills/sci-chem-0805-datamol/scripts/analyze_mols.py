import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Analyze molecules with datamol")
    parser.add_argument("--smiles", nargs="+", help="SMILES strings to analyze")
    parser.add_argument("--file", help="File containing molecules (SDF, SMI, CSV)")

    args = parser.parse_args()

    try:
        import datamol as dm
    except ImportError:
        print("Error: datamol not installed. Please install with: pip install datamol", file=sys.stderr)
        sys.exit(1)

    mols = []

    if args.smiles:
        print("Parsing SMILES...")
        for smi in args.smiles:
            mol = dm.to_mol(smi)
            if mol:
                mol = dm.standardize_mol(mol)
                mols.append(mol)
            else:
                print(f"Failed to parse SMILES: {smi}", file=sys.stderr)

    elif args.file:
        print(f"Reading file: {args.file}...")
        if args.file.endswith(".sdf"):
            df = dm.read_sdf(args.file)
            mols = df['mol'].tolist()
        else:
            df = dm.read_csv(args.file) # simplistic
            if 'smiles' in df.columns:
                mols = [dm.to_mol(s) for s in df['smiles']]
    else:
        parser.print_help()
        sys.exit(1)

    if not mols:
        print("No valid molecules found.", file=sys.stderr)
        sys.exit(1)

    print(f"Successfully loaded {len(mols)} valid molecules.")

    print("\nComputing descriptors...")
    # Just compute for the first one as an example to avoid long output
    if len(mols) > 0:
        desc = dm.descriptors.compute_many_descriptors(mols[0])
        print(f"Descriptors for first molecule:")
        for k, v in list(desc.items())[:5]: # print first 5
            print(f"  {k}: {v}")

    print("\nExtracting Bemis-Murcko scaffolds...")
    scaffolds = [dm.to_smiles(dm.to_scaffold_murcko(mol)) for mol in mols[:5]]
    for i, scaf in enumerate(scaffolds):
        print(f"  Mol {i+1} scaffold: {scaf}")

if __name__ == "__main__":
    main()
