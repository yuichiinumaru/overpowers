import omicverse as ov
import scanpy as sc
import sys

def run_lazy_pipeline(adata_path, species='human', sample_key='batch', output_report='report.html'):
    """Run OmicVerse lazy pipeline and generate report"""
    print(f"Loading data from {adata_path}...")
    adata = sc.read_h5ad(adata_path)
    
    print(f"Initializing mixed compute resources...")
    ov.settings.cpu_gpu_mixed_init()
    
    print(f"Running lazy pipeline for {species}...")
    ov.single.lazy(
        adata, 
        species=species, 
        sample_key=sample_key,
        batch_correction='harmony' # Default batch correction
    )
    
    print(f"Generating report to {output_report}...")
    ov.single.generate_scRNA_report(adata, save_path=output_report)
    
    return adata

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python omicverse_lazy.py <path_to_h5ad> [species] [sample_key]")
    else:
        path = sys.argv[1]
        species = sys.argv[2] if len(sys.argv) > 2 else 'human'
        key = sys.argv[3] if len(sys.argv) > 3 else 'batch'
        try:
            run_lazy_pipeline(path, species, key)
        except Exception as e:
            print(f"Error: {e}")
