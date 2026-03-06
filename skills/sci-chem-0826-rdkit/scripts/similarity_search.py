from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
import sys

def similarity_search(query_smiles, target_smiles_list, threshold=0.7):
    """Find molecules similar to query using Morgan fingerprints"""
    query_mol = Chem.MolFromSmiles(query_smiles)
    if not query_mol:
        return "Invalid query SMILES"
        
    query_fp = AllChem.GetMorganFingerprintAsBitVect(query_mol, 2, nBits=2048)
    
    hits = []
    for smiles in target_smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)
            sim = DataStructs.TanimotoSimilarity(query_fp, fp)
            if sim >= threshold:
                hits.append((smiles, sim))
                
    # Sort by similarity
    return sorted(hits, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python similarity_search.py <query_smiles> <smiles1> <smiles2> ...")
    else:
        query = sys.argv[1]
        targets = sys.argv[2:]
        results = similarity_search(query, targets)
        print(f"Results for query {query}:")
        for s, sim in results:
            print(f"  {s}: {sim:.3f}")
