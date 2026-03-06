#!/usr/bin/env python3
"""
Pipeline Validator Script
Validates data engineering pipeline configuration files (e.g., Airflow DAGs or dbt models).

Usage:
  python3 pipeline_validator.py --path ./dags
"""

import os
import argparse
import ast

def check_airflow_dag(filepath):
    print(f"Checking {filepath} for basic Airflow DAG patterns...")
    try:
        with open(filepath, 'r') as f:
            tree = ast.parse(f.read(), filename=filepath)

        has_dag = False
        has_default_args = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if target.id == 'default_args':
                            has_default_args = True
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'DAG':
                    has_dag = True

        if has_dag and not has_default_args:
            print(f"[WARNING] DAG found in {filepath} but missing 'default_args' dict.")
        elif has_dag:
            print(f"[OK] {filepath} appears to be a valid Airflow DAG.")

    except SyntaxError:
        print(f"[ERROR] Syntax error in {filepath}")
    except Exception as e:
        print(f"[ERROR] Could not parse {filepath}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Data Engineering Pipeline Validator")
    parser.add_argument("--path", required=True, help="Path to pipeline files (e.g., dags/)")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Path {args.path} does not exist.")
        return

    for root, _, files in os.walk(args.path):
        for file in files:
            if file.endswith('.py'):
                check_airflow_dag(os.path.join(root, file))

if __name__ == "__main__":
    main()
