import cellxgene_census
import argparse
import sys

def query_census(organism, cell_type, tissue, output_file):
    print(f"🔍 Querying CELLxGENE Census for {cell_type} in {tissue} ({organism})...")
    
    with cellxgene_census.open_soma() as census:
        obs_filter = f"cell_type == '{cell_type}' and tissue_general == '{tissue}' and is_primary_data == True"
        
        print("📥 Fetching AnnData...")
        try:
            adata = cellxgene_census.get_anndata(
                census=census,
                organism=organism,
                obs_value_filter=obs_filter
            )
            print(f"✅ Retrieved {adata.n_obs} cells and {adata.n_vars} genes.")
            
            if output_file:
                print(f"💾 Saving to {output_file}...")
                adata.write_h5ad(output_file)
            return adata
        except Exception as e:
            print(f"❌ Query failed: {e}")
            return None

def main():
    parser = argparse.ArgumentParser(description="Query CELLxGENE Census.")
    parser.add_argument("--organism", default="Homo sapiens", help="Organism name")
    parser.add_argument("--cell-type", required=True, help="Cell type to filter by")
    parser.add_argument("--tissue", required=True, help="General tissue to filter by")
    parser.add_argument("--output", help="Output H5AD file")
    
    args = parser.parse_args()
    query_census(args.organism, args.cell_type, args.tissue, args.output)

if __name__ == "__main__":
    main()
