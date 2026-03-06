import pubchempy as pcp
import pandas as pd
import sys

def search_by_name(name, max_results=10):
    """Search compounds by name"""
    print(f"Searching for '{name}'...")
    compounds = pcp.get_compounds(name, 'name')
    return compounds[:max_results]

def get_compound_properties(identifier, namespace='name', properties=None):
    """Get specific properties for a compound"""
    if properties is None:
        properties = ['MolecularFormula', 'MolecularWeight', 'CanonicalSMILES', 'XLogP', 'TPSA']
    
    print(f"Retrieving properties for {identifier}...")
    props = pcp.get_properties(properties, identifier, namespace)
    return props

def similarity_search(smiles, threshold=85, max_records=50):
    """Perform Tanimoto similarity search"""
    print(f"Performing similarity search (threshold={threshold})...")
    similar_compounds = pcp.get_compounds(
        smiles,
        'smiles',
        searchtype='similarity',
        Threshold=threshold,
        MaxRecords=max_records
    )
    return similar_compounds

def print_compound_info(compound):
    """Print formatted compound information"""
    print(f"\nCID: {compound.cid}")
    print(f"IUPAC Name: {compound.iupac_name}")
    print(f"Formula: {compound.molecular_formula}")
    print(f"MW: {compound.molecular_weight}")
    print(f"SMILES: {compound.canonical_smiles}")
    if compound.xlogp:
        print(f"XLogP: {compound.xlogp}")

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "aspirin"
    try:
        results = search_by_name(name)
        if results:
            print_compound_info(results[0])
        else:
            print("No results found.")
    except Exception as e:
        print(f"Error: {e}")
