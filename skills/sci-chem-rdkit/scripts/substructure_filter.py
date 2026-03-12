from rdkit import Chem
import sys

def filter_by_substructure(smiles_list, smarts):
    """Filter molecules that contain a specific substructure"""
    query = Chem.MolFromSmarts(smarts)
    if not query:
        return "Invalid SMARTS pattern"
        
    hits = []
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol and mol.HasSubstructMatch(query):
            hits.append(smiles)
            
    return hits

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python substructure_filter.py <smarts_pattern> <smiles1> <smiles2> ...")
    else:
        pattern = sys.argv[1]
        smiles = sys.argv[2:]
        results = filter_by_substructure(smiles, pattern)
        print(f"Molecules matching {pattern}:")
        for r in results:
            print(f"  - {r}")
