#!/usr/bin/env python3
# Helper script to convert CSV to XLSX, preserving formatting

import argparse
import sys
import os

try:
    import pandas as pd
    from openpyxl import Workbook
    from openpyxl.utils.dataframe import dataframe_to_rows
except ImportError:
    print("Error: pandas and openpyxl are required.")
    print("Please install them using: pip install pandas openpyxl")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert CSV to Excel (XLSX).")
    parser.add_argument("input_csv", help="Path to the input CSV file.")
    parser.add_argument("output_xlsx", help="Path to the output XLSX file.")

    args = parser.parse_args()

    if not os.path.exists(args.input_csv):
        print(f"Error: File '{args.input_csv}' not found.")
        sys.exit(1)

    try:
        df = pd.read_csv(args.input_csv)

        wb = Workbook()
        ws = wb.active
        ws.title = "Data"

        for r in dataframe_to_rows(df, index=False, header=True):
            ws.append(r)

        wb.save(args.output_xlsx)
        print(f"Successfully converted {args.input_csv} to {args.output_xlsx}")

    except Exception as e:
        print(f"Error converting file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
