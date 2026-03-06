import sys
import pandas as pd
import numpy as np
from scipy import stats

def check_normality(data_path, column_name):
    """
    Checks normality of a column in a CSV file and recommends statistical tests.
    """
    try:
        df = pd.read_csv(data_path)
        if column_name not in df.columns:
            print(f"Error: Column '{column_name}' not found in {data_path}")
            return

        data = df[column_name].dropna()
        
        if len(data) < 3:
            print("Error: Insufficient data points (n < 3)")
            return

        print(f"--- Normality Analysis for '{column_name}' (n={len(data)}) ---")
        
        # Shapiro-Wilk test
        sw_stat, sw_p = stats.shapiro(data)
        print(f"Shapiro-Wilk test: W={sw_stat:.4f}, p={sw_p:.4e}")
        
        # D'Agostino-Pearson test (requires n >= 8)
        if len(data) >= 8:
            dp_stat, dp_p = stats.normaltest(data)
            print(f"D'Agostino-Pearson test: stat={dp_stat:.4f}, p={dp_p:.4e}")
        else:
            dp_p = 1.0 # Placeholder
            print("D'Agostino-Pearson test: Skipped (n < 8)")

        # Recommendation
        if sw_p < 0.05 or (len(data) >= 8 and dp_p < 0.05):
            print("\nResult: ❌ Data does NOT appear normally distributed (p < 0.05)")
            print("Recommendation: Use non-parametric tests (e.g., Mann-Whitney U, Kruskal-Wallis)")
        else:
            print("\nResult: ✅ Data appears normally distributed (p >= 0.05)")
            print("Recommendation: Use parametric tests (e.g., t-test, ANOVA)")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python normality_check.py <csv_path> <column_name>")
    else:
        check_normality(sys.argv[1], sys.argv[2])
