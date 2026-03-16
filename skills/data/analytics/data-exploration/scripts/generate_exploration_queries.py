#!/usr/bin/env python3
"""
Data Exploration Queries Generator
Generates common SQL data profiling queries based on a given table name and column.
"""
import sys
import argparse

def generate_queries(table_name, column_name):
    """
    Generate standard data profiling queries for a given table and column.
    """
    print(f"-- Data Exploration Queries for Table: {table_name}\n")

    print("-- 1. Basic Shape and Structure")
    print(f"SELECT COUNT(*) AS total_rows FROM {table_name};")
    print(f"SELECT * FROM {table_name} LIMIT 10;\n")

    if column_name:
        print(f"-- 2. Profiling Column: {column_name}")

        print(f"\n-- 2.1 Null and Missing Values")
        print(f"SELECT")
        print(f"  COUNT(*) AS total_rows,")
        print(f"  SUM(CASE WHEN {column_name} IS NULL THEN 1 ELSE 0 END) AS null_count,")
        print(f"  (SUM(CASE WHEN {column_name} IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS null_percentage")
        print(f"FROM {table_name};\n")

        print(f"-- 2.2 Distinct Values and Cardinality")
        print(f"SELECT COUNT(DISTINCT {column_name}) AS distinct_values FROM {table_name};\n")

        print(f"-- 2.3 Top 10 Most Frequent Values (Distribution)")
        print(f"SELECT {column_name}, COUNT(*) AS frequency")
        print(f"FROM {table_name}")
        print(f"GROUP BY {column_name}")
        print(f"ORDER BY frequency DESC")
        print(f"LIMIT 10;\n")

        print(f"-- 2.4 Basic Numeric Stats (Use only if {column_name} is numeric)")
        print(f"SELECT")
        print(f"  MIN({column_name}) AS min_val,")
        print(f"  MAX({column_name}) AS max_val,")
        print(f"  AVG({column_name}) AS avg_val")
        print(f"FROM {table_name}")
        print(f"WHERE {column_name} IS NOT NULL;\n")

def main():
    parser = argparse.ArgumentParser(description="Data Exploration Queries Generator")
    parser.add_argument("--table", required=True, help="Name of the table to explore")
    parser.add_argument("--column", help="Optional specific column to profile")

    args = parser.parse_args()

    generate_queries(args.table, args.column)

if __name__ == "__main__":
    main()
