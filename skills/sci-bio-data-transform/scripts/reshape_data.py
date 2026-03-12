import sys
import pandas as pd

def melt_data(csv_path, id_vars, var_name='variable', value_name='value'):
    """
    Reshapes data from wide to long format (melt).
    id_vars: comma-separated column names to keep as identifiers
    """
    try:
        df = pd.read_csv(csv_path)
        id_list = id_vars.split(',')
        
        # Verify columns
        for col in id_list:
            if col not in df.columns:
                print(f"Error: ID column '{col}' not found")
                return

        df_long = df.melt(id_vars=id_list, var_name=var_name, value_name=value_name)
        
        output_path = csv_path.replace('.csv', '_long.csv')
        df_long.to_csv(output_path, index=False)
        
        print(f"--- Reshape Report (Wide -> Long) ---")
        print(f"Original shape: {df.shape}")
        print(f"New shape: {df_long.shape}")
        print(f"✅ Long-format data saved to: {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python reshape_data.py <csv_path> <id_columns_comma_separated> [var_name] [value_name]")
    else:
        var = sys.argv[3] if len(sys.argv) > 3 else 'variable'
        val = sys.argv[4] if len(sys.argv) > 4 else 'value'
        melt_data(sys.argv[1], sys.argv[2], var, val)
