import sys
import argparse
from bioservices import UniProt, KEGG, PSICQUIC

def analyze_protein(protein_name, email):
    print(f"🧬 Starting comprehensive analysis for: {protein_name}")
    
    # 1. UniProt Search
    print("🔍 Searching UniProt...")
    u = UniProt(verbose=False)
    res = u.search(protein_name, columns="id,entry name,genes,organism")
    print("UniProt Results:")
    print(res)
    
    # Extract first ID if possible (simplified)
    lines = res.strip().split('\n')
    if len(lines) > 1:
        uniprot_id = lines[1].split('\t')[0]
        print(f"✅ Identified UniProt ID: {uniprot_id}")
        
        # 2. KEGG Pathway Mapping
        print(f"🗺️ Mapping {uniprot_id} to KEGG pathways...")
        k = KEGG(verbose=False)
        # This is a simplified mapping logic
        mapping = u.mapping(fr="UniProtKB_AC-ID", to="KEGG", query=uniprot_id)
        print(f"KEGG Mapping: {mapping}")
        
        # 3. PSICQUIC Interactions
        print(f"🔗 Querying PSICQUIC for interactions...")
        p = PSICQUIC(verbose=False)
        try:
            interactions = p.query("intact", f"{uniprot_id}")
            print(f"✅ Found {len(interactions)} interactions in IntAct.")
        except Exception as e:
            print(f"⚠️ PSICQUIC query failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Protein analysis workflow using BioServices.")
    parser.add_argument("protein", help="Protein name or entry (e.g., ZAP70_HUMAN)")
    parser.add_argument("email", help="Email for NCBI services")
    
    args = parser.parse_args()
    analyze_protein(args.protein, args.email)

if __name__ == "__main__":
    main()
