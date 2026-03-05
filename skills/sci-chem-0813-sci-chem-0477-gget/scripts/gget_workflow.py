import gget
import pandas as pd
import sys

def gene_analysis_workflow(search_terms, species="human"):
    """Workflow: search -> info -> seq"""
    print(f"1. Searching for '{' '.join(search_terms)}' in {species}...")
    search_results = gget.search(search_terms, species=species)
    
    if search_results.empty:
        print("No genes found.")
        return
    
    # Get top 3 genes
    top_genes = search_results["ensembl_id"].head(3).tolist()
    print(f"2. Getting info for top genes: {', '.join(top_genes)}")
    info = gget.info(top_genes)
    
    print("3. Retrieving sequences (first gene)...")
    seq = gget.seq([top_genes[0]], translate=True)
    
    return {
        "search": search_results,
        "info": info,
        "sequence": seq
    }

if __name__ == "__main__":
    terms = sys.argv[1:] if len(sys.argv) > 1 else ["GABA", "receptor"]
    try:
        results = gene_analysis_workflow(terms)
        if results:
            print("\nWorkflow completed successfully.")
            print(f"Found {len(results['search'])} genes.")
    except Exception as e:
        print(f"Error: {e}")
