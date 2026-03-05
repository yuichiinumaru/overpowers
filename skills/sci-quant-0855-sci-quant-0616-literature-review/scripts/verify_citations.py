import re
import argparse
import json
import requests
import os

def extract_dois(text):
    # Regex for DOI extraction
    doi_pattern = r'10\.\d{4,9}/[-._;()/:A-Z0-9]+'
    return re.findall(doi_pattern, text, re.IGNORECASE)

def verify_doi(doi):
    """Simple verification by checking if DOI resolves."""
    url = f"https://doi.org/{doi}"
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False

def get_crossref_metadata(doi):
    """Retrieve metadata from CrossRef API."""
    url = f"https://api.crossref.org/works/{doi}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('message')
    except requests.RequestException:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description='Verify DOIs and generate citation metadata.')
    parser.add_argument('input', help='Input Markdown file')
    parser.add_argument('--output', help='Output JSON report')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} not found.")
        return

    with open(args.input, 'r') as f:
        content = f.read()

    dois = list(set(extract_dois(content)))
    print(f"Found {len(dois)} unique DOIs.")

    report = {
        "summary": {
            "total_found": len(dois),
            "verified": 0,
            "failed": 0
        },
        "results": []
    }

    for doi in dois:
        print(f"Verifying {doi}...", end=' ', flush=True)
        is_valid = verify_doi(doi)
        if is_valid:
            print("OK")
            report["summary"]["verified"] += 1
            metadata = get_crossref_metadata(doi)
            report["results"].append({
                "doi": doi,
                "status": "verified",
                "metadata": metadata
            })
        else:
            print("FAILED")
            report["summary"]["failed"] += 1
            report["results"].append({
                "doi": doi,
                "status": "failed"
            })

    output_path = args.output or f"{os.path.splitext(args.input)[0]}_citation_report.json"
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nVerification report saved to {output_path}")

if __name__ == "__main__":
    main()
