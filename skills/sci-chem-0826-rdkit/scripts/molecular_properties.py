from rdkit import Chem
from rdkit.Chem import Descriptors
import pandas as pd
import sys

def calculate_properties(smiles_list):
    """Calculate basic molecular properties for a list of SMILES"""
    results = []
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            results.append({"smiles": smiles, "error": "Invalid SMILES"})
            continue
            
        res = {
            "smiles": smiles,
            "MW": Descriptors.MolWt(mol),
            "LogP": Descriptors.MolLogP(mol),
            "HBD": Descriptors.NumHDonors(mol),
            "HBA": Descriptors.NumHAcceptors(mol),
            "TPSA": Descriptors.TPSA(mol),
            "RotBonds": Descriptors.NumRotatableBonds(mol)
        }
        
        # Lipinski Rule of Five check
        res['Lipinski_Pass'] = (res['MW'] <= 500 and 
                                res['LogP'] <= 5 and 
                                res['HBD'] <= 5 and 
                                res['HBA'] <= 10)
        results.append(res)
        
    return pd.DataFrame(results)

if __name__ == "__main__":
    smiles = sys.argv[1:] if len(sys.argv) > 1 else ["CC(=O)OC1=CC=CC=C1C(=O)O", "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"]
    df = calculate_properties(smiles)
    print(df.to_string(index=False))
