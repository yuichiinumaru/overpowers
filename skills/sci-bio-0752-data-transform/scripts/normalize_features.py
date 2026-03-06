import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

def normalize_data(csv_path, method='standard'):
    """
    Normalizes numeric columns in a CSV file.
    methods: 'standard' (Z-score), 'minmax' (0-1), 'robust' (median/IQR)
    """
    try:
        df = pd.read_csv(csv_path)
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) == 0:
            print("Error: No numeric columns found to normalize")
            return

        if method == 'standard':
            scaler = StandardScaler()
        elif method == 'minmax':
            scaler = MinMaxScaler()
        elif method == 'robust':
            scaler = RobustScaler()
        else:
            print(f"Error: Unknown method '{method}'")
            return

        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        
        output_path = csv_path.replace('.csv', f'_norm_{method}.csv')
        df.to_csv(output_path, index=False)
        
        print(f"--- Normalization Report ({method}) ---")
        print(f"Normalized columns: {list(numeric_cols)}")
        print(f"✅ Normalized data saved to: {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python normalize_features.py <csv_path> [standard|minmax|robust]")
    else:
        meth = sys.argv[2] if len(sys.argv) > 2 else 'standard'
        normalize_data(sys.argv[1], meth)
