#!/usr/bin/env python3
import sys

def analyze_eda(architecture_file):
    print(f"Analyzing AWS Serverless Event-Driven Architecture defined in: {architecture_file}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyze_eda(sys.argv[1])
    else:
        print("Usage: ./eda_analyzer.py <architecture_file.json/yml>")
