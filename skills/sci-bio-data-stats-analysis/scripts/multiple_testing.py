import sys
import pandas as pd
from statsmodels.stats.multitest import multipletests

def adjust_pvalues(csv_path, pval_col, method='fdr_bh'):
    """
    Adjusts p-values in a CSV file using multiple testing correction.
    methods: 'fdr_bh' (default), 'bonferroni', 'sidak', 'holm'
    """
    try:
        df = pd.read_csv(csv_path)
        if pval_col not in df.columns:
            print(f"Error: Column '{pval_col}' not found")
            return

        p_values = df[pval_col].values
        reject, p_adj, _, _ = multipletests(p_values, alpha=0.05, method=method)

        df[f'{pval_col}_adj_{method}'] = p_adj
        df[f'significant_{method}'] = reject

        output_path = csv_path.replace('.csv', f'_adjusted_{method}.csv')
        df.to_csv(output_path, index=False)

        print(f"--- Multiple Testing Correction ({method}) ---")
        print(f"Total tests: {len(p_values)}")
        print(f"Original significant (p < 0.05): {(p_values < 0.05).sum()}")
        print(f"Adjusted significant (α = 0.05): {reject.sum()}")
        print(f"✅ Results saved to: {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python multiple_testing.py <csv_path> <pvalue_col> [method: fdr_bh|bonferroni]")
    else:
        meth = sys.argv[3] if len(sys.argv) > 3 else 'fdr_bh'
        adjust_pvalues(sys.argv[1], sys.argv[2], meth)
