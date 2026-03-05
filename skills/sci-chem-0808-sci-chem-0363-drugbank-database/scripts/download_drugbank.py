#!/usr/bin/env python3
import argparse
import os
import sys

try:
    from drugbank_downloader import download_drugbank
except ImportError:
    print("Error: drugbank-downloader not found. Please install it with 'pip install drugbank-downloader'.")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Download DrugBank database.')
    parser.add_argument('--username', help='DrugBank username (or use DRUGBANK_USERNAME env var)')
    parser.add_argument('--password', help='DrugBank password (or use DRUGBANK_PASSWORD env var)')
    parser.add_argument('--version', help='Specific version to download (e.g., "5.1.10")')
    parser.add_argument('--output', help='Output path for the downloaded file')

    args = parser.parse_args()

    username = args.username or os.environ.get('DRUGBANK_USERNAME')
    password = args.password or os.environ.get('DRUGBANK_PASSWORD')

    if not username or not password:
        print("Error: Username and password must be provided via arguments or environment variables (DRUGBANK_USERNAME, DRUGBANK_PASSWORD).")
        sys.exit(1)

    print(f"Starting DrugBank download...")
    try:
        path = download_drugbank(
            username=username,
            password=password,
            version=args.version,
            path=args.output
        )
        print(f"Successfully downloaded DrugBank to: {path}")
    except Exception as e:
        print(f"Error downloading DrugBank: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
