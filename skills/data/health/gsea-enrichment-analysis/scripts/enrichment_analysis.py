import os
import pandas as pd
import omicverse as ov

def run_enrichment_analysis(gene_list, database="GO_Biological_Process_2021", organism="Human"):
    """
    Run gene set enrichment analysis using omicverse.

    Args:
        gene_list (list): List of gene symbols
        database (str): Name of the Enrichr database to use
        organism (str): Target organism (Human, Mouse, Yeast, Fly, Fish, Worm)

    Returns:
        DataFrame: Enrichment results
    """
    print(f"Running enrichment analysis for {len(gene_list)} genes...")
    print(f"Database: {database} ({organism})")

    # 1. Download pathway database
    os.makedirs('genesets', exist_ok=True)
    gmt_file = f"genesets/{database}.gmt"

    if not os.path.exists(gmt_file):
        print(f"Downloading {database}...")
        ov.utils.download_pathway_database(database, organism)

    # 2. Load geneset file into dictionary format (REQUIRED step)
    print("Loading gene sets...")
    pathways_dict = ov.bulk.geneset_prepare(gmt_file)
    print(f"Loaded {len(pathways_dict)} pathways")

    # 3. Run enrichment
    print("Calculating enrichment...")
    enr = ov.bulk.geneset_enrichment(
        gene_list=gene_list,
        pathways_dict=pathways_dict,
        pvalue_cut=0.05,
        qvalue_cut=0.2
    )

    print(f"Found {len(enr)} enriched pathways")
    return enr

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run Pathway Enrichment Analysis")
    parser.add_argument("--genes", required=True, help="Path to file containing gene symbols (one per line)")
    parser.add_argument("--db", default="GO_Biological_Process_2021", help="Enrichr database name")
    parser.add_argument("--org", default="Human", help="Organism")
    parser.add_argument("--out", default="enrichment_results.csv", help="Output CSV file")

    args = parser.parse_args()

    # Read genes
    with open(args.genes, 'r') as f:
        genes = [line.strip() for line in f if line.strip()]

    # Run analysis
    results = run_enrichment_analysis(genes, args.db, args.org)

    # Save results
    if len(results) > 0:
        results.to_csv(args.out)
        print(f"Results saved to {args.out}")

        # Print top 5
        print("\nTop 5 Enriched Pathways:")
        print(results.head(5)[['Term', 'Overlap', 'P-value', 'Adjusted P-value']])
