import sys
import pandas as pd
import numpy as np
from scipy import stats

def compare_groups(data_path, value_col, group_col, test_type='auto'):
    """
    Compares two groups from a CSV file.
    test_type: 'auto', 't-test', 'mann-whitney'
    """
    try:
        df = pd.read_csv(data_path)
        for col in [value_col, group_col]:
            if col not in df.columns:
                print(f"Error: Column '{col}' not found")
                return

        groups = df[group_col].unique()
        if len(groups) != 2:
            print(f"Error: Expected exactly 2 groups, found {len(groups)}: {groups}")
            return

        g1_data = df[df[group_col] == groups[0]][value_col].dropna()
        g2_data = df[df[group_col] == groups[1]][value_col].dropna()

        print(f"--- Comparison: {groups[0]} (n={len(g1_data)}) vs {groups[1]} (n={len(g2_data)}) ---")
        
        # Means and Stds
        print(f"{groups[0]}: Mean={g1_data.mean():.4f}, Std={g1_data.std():.4f}")
        print(f"{groups[1]}: Mean={g2_data.mean():.4f}, Std={g2_data.std():.4f}")

        # Check Variance (Levene's test)
        _, lev_p = stats.levene(g1_data, g2_data)
        equal_var = lev_p >= 0.05
        print(f"Levene's test for equal variances: p={lev_p:.4e} ({'Equal' if equal_var else 'Unequal'})")

        if test_type == 'mann-whitney':
            u_stat, p_val = stats.mannwhitneyu(g1_data, g2_data, alternative='two-sided')
            test_name = "Mann-Whitney U"
        else: # Default or explicitly 't-test'
            t_stat, p_val = stats.ttest_ind(g1_data, g2_data, equal_var=equal_var)
            test_name = "Independent t-test" + ("" if equal_var else " (Welch's)")

        print(f"\nResult ({test_name}):")
        print(f"p-value: {p_val:.4e}")
        if p_val < 0.05:
            print("✅ Statistically significant difference (p < 0.05)")
        else:
            print("❌ No statistically significant difference (p >= 0.05)")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python compare_groups.py <csv_path> <value_col> <group_col> [t-test|mann-whitney]")
    else:
        test = sys.argv[4] if len(sys.argv) > 4 else 'auto'
        compare_groups(sys.argv[1], sys.argv[2], sys.argv[3], test)
