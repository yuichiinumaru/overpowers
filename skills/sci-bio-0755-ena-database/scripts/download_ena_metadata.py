import sys
import requests
import argparse

def download_metadata(accession, output_file=None):
    """
    Download metadata for an accession using ENA Browser API (XML).
    """
    url = f"https://www.ebi.ac.uk/ena/browser/api/xml/{accession}"
    
    try:
        print(f"Downloading metadata for {accession}...")
        response = requests.get(url)
        response.raise_for_status()
        
        if not output_file:
            output_file = f"{accession}_metadata.xml"
            
        with open(output_file, 'w') as f:
            f.write(response.text)
            
        print(f"✅ Metadata saved to: {output_file}")

    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Download ENA metadata (XML)")
    parser.add_argument("accession", help="ENA Accession (e.g., ERR123456, PRJEB1234)")
    parser.add_argument("--out", help="Output file path")

    args = parser.parse_args()
    download_metadata(args.accession, args.out)

if __name__ == "__main__":
    main()
