import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(csv_path, index_col=0):
    """
    Generates a heatmap from a CSV matrix.
    index_col: column to use as index (labels)
    """
    try:
        df = pd.read_csv(csv_path, index_col=index_col)
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(df, cmap='viridis', annot=False, cbar_kws={'label': 'Expression'})
        
        plt.title('Expression Heatmap')
        
        output_path = csv_path.replace('.csv', '_heatmap.png')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()
        
        print(f"✅ Heatmap saved to: {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python plot_heatmap.py <csv_path> [index_column_index]")
    else:
        idx = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        plot_heatmap(sys.argv[1], idx)
