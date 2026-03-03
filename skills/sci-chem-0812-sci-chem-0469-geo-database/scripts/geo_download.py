import GEOparse
import os
import pandas as pd

def download_and_parse_gse(gse_id, destdir="./data"):
    """Download and parse a GEO Series"""
    if not os.path.exists(destdir):
        os.makedirs(destdir)
        
    print(f"Downloading/parsing {gse_id} to {destdir}...")
    gse = GEOparse.get_GEO(geo=gse_id, destdir=destdir)
    
    print(f"Title: {gse.metadata.get('title', ['N/A'])[0]}")
    print(f"Samples: {len(gse.gsms)}")
    
    # Extract expression matrix if possible
    if hasattr(gse, 'pivot_samples'):
        expression_df = gse.pivot_samples('VALUE')
        print(f"Expression matrix shape: {expression_df.shape}")
        return gse, expression_df
        
    return gse, None

if __name__ == "__main__":
    import sys
    gse_id = sys.argv[1] if len(sys.argv) > 1 else "GSE123456"
    try:
        gse, expr = download_and_parse_gse(gse_id)
        if expr is not None:
            output_file = f"{gse_id}_expression.csv"
            expr.to_csv(output_file)
            print(f"Saved expression data to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
