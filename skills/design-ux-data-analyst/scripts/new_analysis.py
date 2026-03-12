#!/usr/bin/env python3
import os
import argparse

PANDAS_TEMPLATE = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
# df = pd.read_csv('data.csv')

# Data cleaning
# df.dropna(inplace=True)

# Exploratory Data Analysis
# print(df.describe())
# print(df.info())

# Visualizations
# sns.pairplot(df)
# plt.show()

# Key Insights
# ...
"""

SQL_TEMPLATE = """-- Data Analysis Query
-- Description: ...

WITH base_data AS (
    SELECT 
        *
    FROM 
        table_name
    WHERE 
        condition
)
SELECT
    dimension,
    COUNT(*) as count,
    AVG(metric) as average_metric
FROM
    base_data
GROUP BY
    1
ORDER BY
    2 DESC;
"""

def create_analysis(name, type):
    if type == 'pandas':
        filename = f"{name}.py"
        content = PANDAS_TEMPLATE
    else:
        filename = f"{name}.sql"
        content = SQL_TEMPLATE

    if os.path.exists(filename):
        print(f"Error: {filename} already exists.")
        return

    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Created {type} analysis template: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new data analysis template.")
    parser.add_argument("name", help="Name of the analysis file")
    parser.add_argument("--type", choices=['pandas', 'sql'], default='pandas', help="Type of analysis (pandas or sql)")
    args = parser.parse_args()

    create_analysis(args.name, args.type)
