#!/usr/bin/env python3
"""
Helper script to fetch academic papers from Sci-Hub given a DOI.
Uses requests to download the PDF and saves it to research/papers/.
"""
import os
import re
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set up headers to mimic a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

def extract_doi(text):
    """Extract DOI from text."""
    # Match standard DOI format: 10.\d{4,9}/[-._;()/:A-Z0-9]+
    doi_pattern = re.compile(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', re.IGNORECASE)
    match = doi_pattern.search(text)
    return match.group(0) if match else None

def get_pdf_url(doi, domain="https://sci-hub.se"):
    """Find the PDF URL on Sci-Hub for a given DOI."""
    search_url = f"{domain}/{doi}"
    try:
        response = requests.get(search_url, headers=HEADERS, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Sci-Hub typically puts the PDF URL in an iframe or a specific button
        iframe = soup.find('iframe', id='pdf')
        if iframe and iframe.has_attr('src'):
            src = iframe['src']
            # Handle relative URLs
            if src.startswith('//'):
                return f"https:{src}"
            elif src.startswith('/'):
                return urljoin(domain, src)
            return src

        # Fallback: look for save/download button
        buttons = soup.find_all('button', onclick=re.compile(r'location\.href'))
        for btn in buttons:
            onclick = btn.get('onclick', '')
            match = re.search(r"location\.href='([^']+)'", onclick)
            if match:
                src = match.group(1)
                if src.startswith('//'):
                    return f"https:{src}"
                elif src.startswith('/'):
                    return urljoin(domain, src)
                return src

        return None
    except Exception as e:
        print(f"Error finding PDF URL: {e}")
        return None

def download_paper(doi, output_dir="research/papers"):
    """Download the paper and save it to the output directory."""
    clean_doi = doi.replace('/', '_')
    filename = f"paper_{clean_doi}.pdf"

    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    if os.path.exists(filepath):
        print(f"Paper already exists at: {filepath}")
        return filepath

    print(f"Fetching {doi}...")

    # Try different Sci-Hub domains
    domains = ["https://sci-hub.se", "https://sci-hub.ru", "https://sci-hub.st", "https://www.sci-hub.su"]
    pdf_url = None

    for domain in domains:
        print(f"Trying {domain}...")
        pdf_url = get_pdf_url(doi, domain)
        if pdf_url:
            break

    if not pdf_url:
        print(f"Could not find PDF URL for DOI: {doi} on any known Sci-Hub domain.")
        return None

    print(f"Downloading from: {pdf_url}")
    try:
        response = requests.get(pdf_url, headers=HEADERS, stream=True, timeout=30)
        response.raise_for_status()

        # Check if we actually got a PDF
        content_type = response.headers.get('Content-Type', '')
        if 'application/pdf' not in content_type:
            print("Warning: Response content-type is not application/pdf. It might be an interstitial page or error.")

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Successfully downloaded to: {filepath}")
        return filepath

    except Exception as e:
        print(f"Error downloading PDF: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch academic papers via Sci-Hub using DOI")
    parser.add_argument("dois", nargs='+', help="One or more DOIs to fetch")
    parser.add_argument("--output", default="research/papers", help="Output directory")

    args = parser.parse_args()

    for input_doi in args.dois:
        doi = extract_doi(input_doi)
        if not doi:
            print(f"Invalid DOI format: {input_doi}")
            continue

        download_paper(doi, args.output)
        print("-" * 40)
