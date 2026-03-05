import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_scatter(csv_path, x_col, y_col, group_col=None):
    """
    Creates a scatter plot for two columns.
    """
    try:
        df = pd.read_csv(csv_path)
        for col in [x_col, y_col]:
            if col not in df.columns:
                print(f"Error: Column '{col}' not found")
                return

        sns.set_style("whitegrid")
        plt.figure(figsize=(8, 6))

        if group_col and group_col in df.columns:
            sns.scatterplot(data=df, x=x_col, y=y_col, hue=group_col, alpha=0.7, palette='viridis')
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        else:
            sns.scatterplot(data=df, x=x_col, y=y_col, alpha=0.6, color='steelblue')

        plt.title(f'{x_col} vs {y_col}')
        
        output_path = csv_path.replace('.csv', f'_scatter_{x_col}_{y_col}.png')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()
        
        print(f"✅ Scatter plot saved to: {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python plot_scatter.py <csv_path> <x_column> <y_column> [group_column]")
    else:
        g_col = sys.argv[4] if len(sys.argv) > 4 else None
        plot_scatter(sys.argv[1], sys.argv[2], sys.argv[3], g_col)
