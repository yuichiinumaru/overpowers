#!/usr/bin/env python3
import argparse
import csv
import os

def create_batch_csv(output_path, complex_name, protein_path=None, ligand_description=None, protein_sequence=None):
    fieldnames = ['complex_name', 'protein_path', 'ligand_description', 'protein_sequence']
    
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            'complex_name': complex_name,
            'protein_path': protein_path or '',
            'ligand_description': ligand_description or '',
            'protein_sequence': protein_sequence or ''
        })
    print(f"Created batch CSV: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Prepare batch CSV for DiffDock.')
    parser.add_argument('--name', required=True, help='Complex name')
    parser.add_argument('--protein', help='Path to protein PDB file')
    parser.add_argument('--ligand', required=True, help='SMILES string or ligand file path')
    parser.add_argument('--sequence', help='Protein amino acid sequence')
    parser.add_argument('--output', default='batch_input.csv', help='Output CSV filename')

    args = parser.parse_args()

    if not args.protein and not args.sequence:
        print("Error: Either --protein (PDB path) or --sequence must be provided.")
        return

    create_batch_csv(args.output, args.name, args.protein, args.ligand, args.sequence)

if __name__ == "__main__":
    main()
