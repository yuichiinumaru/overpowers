import sys
import pandas as pd
import numpy as np

def clean_data(csv_path, outlier_col=None):
    """
    Cleans CSV data: removes duplicates, NAs, and optionally outliers.
    """
    try:
        df = pd.read_csv(csv_path)
        initial_count = len(df)
        
        # Remove duplicates
        df = df.drop_duplicates()
        dup_removed = initial_count - len(df)
        
        # Remove NAs
        df = df.dropna()
        na_removed = initial_count - dup_removed - len(df)
        
        print(f"--- Cleaning Report for {csv_path} ---")
        print(f"Initial rows: {initial_count}")
        print(f"Duplicates removed: {dup_removed}")
        print(f"Rows with NAs removed: {na_removed}")
        
        # Outlier removal (IQR)
        if outlier_col:
            if outlier_col in df.columns:
                Q1 = df[outlier_col].quantile(0.25)
                Q3 = df[outlier_col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR
                df = df[(df[outlier_col] >= lower) & (df[outlier_col] <= upper)]
                print(f"Outliers removed in '{outlier_col}': {initial_count - dup_removed - na_removed - len(df)}")
            else:
                print(f"Warning: Column '{outlier_col}' not found for outlier removal")

        output_path = csv_path.replace('.csv', '_cleaned.csv')
        df.to_csv(output_path, index=False)
        print(f"Final rows: {len(df)}")
        print(f"✅ Cleaned data saved to: {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_csv.py <csv_path> [outlier_column]")
    else:
        out_col = sys.argv[2] if len(sys.argv) > 2 else None
        clean_data(sys.argv[1], out_col)
