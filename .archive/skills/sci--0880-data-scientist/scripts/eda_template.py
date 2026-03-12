import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def perform_basic_eda(df):
    """
    Perform basic exploratory data analysis on a pandas DataFrame.
    """
    print("--- Dataset Shape ---")
    print(df.shape)

    print("\n--- Data Types and Missing Values ---")
    info_df = pd.DataFrame({
        'Type': df.dtypes,
        'Missing': df.isnull().sum(),
        'Missing %': (df.isnull().sum() / len(df)) * 100
    })
    print(info_df)

    print("\n--- Summary Statistics (Numerical) ---")
    print(df.describe())

    return info_df
