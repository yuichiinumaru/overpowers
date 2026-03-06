import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="ToolUniverse Protein Therapeutic Design")
    parser.add_argument("--action", choices=["get_structure", "generate_backbones", "design_sequences", "validate"], required=True)
    parser.add_argument("--target", help="Target ID (UniProt or PDB) for get_structure")
    parser.add_argument("--steps", type=int, default=50, help="Diffusion steps for RFdiffusion")
    parser.add_argument("--backbone-pdb", help="PDB string for ProteinMPNN")
    parser.add_argument("--num-seqs", type=int, default=8, help="Number of sequences for ProteinMPNN")
    parser.add_argument("--sequence", help="Sequence string for ESMFold validation")

    args = parser.parse_args()

    try:
        from tooluniverse import ToolUniverse
        import numpy as np
    except ImportError:
        print("Error: tooluniverse or numpy not installed.", file=sys.stderr)
        sys.exit(1)

    tu = ToolUniverse()
    tu.load_tools()

    if args.action == "get_structure":
        if not args.target:
            print("Error: --target required for get_structure", file=sys.stderr)
            sys.exit(1)
        print(f"Searching for target structure: {args.target}")
        pdb_results = tu.tools.PDB_search_by_uniprot(uniprot_id=args.target)
        if pdb_results:
            best_pdb = sorted(pdb_results, key=lambda x: x['resolution'])[0]
            structure = tu.tools.PDB_get_structure(pdb_id=best_pdb['pdb_id'])
            print(json.dumps({'source': 'PDB', 'pdb_id': best_pdb['pdb_id'], 'resolution': best_pdb['resolution']}, indent=2))
        else:
            print("Could not find structure in PDB, checking AlphaFold...")
            # Fallback could be implemented here
            print("AlphaFold prediction skipped in this helper script.")

    elif args.action == "generate_backbones":
        print(f"Generating backbones with {args.steps} steps...")
        backbones = tu.tools.NvidiaNIM_rfdiffusion(diffusion_steps=args.steps)
        print(json.dumps(backbones, indent=2))

    elif args.action == "design_sequences":
        if not args.backbone_pdb:
            print("Error: --backbone-pdb required for design_sequences", file=sys.stderr)
            sys.exit(1)
        print(f"Designing sequences with ProteinMPNN...")
        sequences = tu.tools.NvidiaNIM_proteinmpnn(pdb_string=args.backbone_pdb, num_sequences=args.num_seqs, temperature=0.1)
        print(json.dumps(sequences, indent=2))

    elif args.action == "validate":
        if not args.sequence:
            print("Error: --sequence required for validate", file=sys.stderr)
            sys.exit(1)
        print(f"Validating sequence with ESMFold...")
        predicted = tu.tools.NvidiaNIM_esmfold(sequence=args.sequence)
        # Simplified output since we don't have the extract_plddt helper
        print("Structure prediction completed.")

if __name__ == "__main__":
    main()
