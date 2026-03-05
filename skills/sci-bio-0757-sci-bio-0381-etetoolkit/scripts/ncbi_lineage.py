import sys
import argparse
from ete3 import NCBITaxa

def get_lineage(species_names):
    """
    Translates species names to TaxIDs and retrieves full lineages.
    """
    try:
        ncbi = NCBITaxa()
        name2taxid = ncbi.get_name_translator(species_names)
        
        for name in species_names:
            print(f"\n--- {name} ---")
            if name in name2taxid:
                taxid = name2taxid[name][0]
                lineage = ncbi.get_lineage(taxid)
                names = ncbi.get_taxid_translator(lineage)
                ranks = ncbi.get_rank(lineage)
                
                print(f"TaxID: {taxid}")
                print("Lineage:")
                for tid in lineage:
                    print(f"  {names[tid]} ({ranks[tid]})")
            else:
                print("Error: Species not found in NCBI database")

    except Exception as e:
        print(f"Error: {str(e)}")
        print("Note: First run will download ~300MB NCBI database.")

def main():
    parser = argparse.ArgumentParser(description="Get NCBI Taxonomy Lineage")
    parser.add_argument("species", nargs="+", help="Species names (e.g., 'Homo sapiens')")

    args = parser.parse_args()
    get_lineage(args.species)

if __name__ == "__main__":
    main()
