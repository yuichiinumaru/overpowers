import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(csv_path, value_col, group_col=None):
    """
    Plots distribution (histogram and violin) for a numeric column.
    """
    try:
        df = pd.read_csv(csv_path)
        if value_col not in df.columns:
            print(f"Error: Column '{value_col}' not found")
            return

        sns.set_style("whitegrid")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # Histogram / KDE
        if group_col and group_col in df.columns:
            sns.histplot(data=df, x=value_col, hue=group_col, kde=True, ax=ax1, element="step")
            sns.violinplot(data=df, x=group_col, y=value_col, ax=ax2)
        else:
            sns.histplot(data=df, x=value_col, kde=True, ax=ax1, color='steelblue')
            sns.violinplot(data=df, y=value_col, ax=ax2, color='lightgray')

        ax1.set_title(f'Distribution of {value_col}')
        ax2.set_title(f'Spread of {value_col}')

        output_path = csv_path.replace('.csv', f'_{value_col}_dist.png')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()
        
        print(f"✅ Distribution plot saved to: {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python plot_distribution.py <csv_path> <value_column> [group_column]")
    else:
        g_col = sys.argv[3] if len(sys.argv) > 3 else None
        plot_distribution(sys.argv[1], sys.argv[2], g_col)
