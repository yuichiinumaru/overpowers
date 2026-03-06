import omicverse as ov
import pandas as pd
import argparse
from statsmodels import robust

def run_wgcna(input_file, species, n_genes, output_prefix):
    print("🧬 Starting WGCNA analysis...")
    ov.plot_set()
    
    print(f"📥 Loading data: {input_file}")
    data = pd.read_csv(input_file, index_col=0)
    
    # Filtering top variable genes
    print(f"🔍 Filtering top {n_genes} variable genes...")
    gene_mad = data.apply(robust.mad)
    data_filtered = data.T.loc[gene_mad.sort_values(ascending=False).index[:n_genes]]
    
    print("🚀 Initializing PyWGCNA...")
    wgcna = ov.bulk.pyWGCNA(
        name=output_prefix, 
        species=species, 
        geneExp=data_filtered.T, 
        save=True
    )
    
    print("🛠️ Preprocessing...")
    wgcna.preprocess()
    
    print("📈 Calculating soft threshold...")
    wgcna.calculate_soft_threshold()
    
    print("🔗 Constructing adjacency matrix...")
    wgcna.calculating_adjacency_matrix()
    
    print("✨ WGCNA object prepared. Ready for module detection.")
    return wgcna

def main():
    parser = argparse.ArgumentParser(description="Bulk WGCNA analysis with omicverse.")
    parser.add_argument("--input", required=True, help="Expression matrix CSV")
    parser.add_argument("--species", default="mus musculus", help="Species name")
    parser.add_argument("--n-genes", type=int, default=2000, help="Number of top variable genes to keep")
    parser.add_argument("--output", default="wgcna_res", help="Output prefix")
    
    args = parser.parse_args()
    run_wgcna(args.input, args.species, args.n_genes, args.output)

if __name__ == "__main__":
    main()
