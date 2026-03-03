import requests
import json
import argparse
import sys
from datetime import datetime, timedelta

class BioRxivSearcher:
    def __init__(self, verbose=False):
        self.base_url = "https://api.biorxiv.org/details/biorxiv"
        self.verbose = verbose

    def search_by_date_range(self, start_date, end_date):
        url = f"{self.base_url}/{start_date}/{end_date}"
        if self.verbose:
            print(f"📡 Querying: {url}")
        
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def download_pdf(self, doi, output_path):
        # Simplistic PDF URL generation for bioRxiv
        pdf_url = f"https://www.biorxiv.org/content/{doi}v1.full.pdf"
        if self.verbose:
            print(f"📥 Downloading PDF from: {pdf_url}")
        
        try:
            response = requests.get(pdf_url)
            response.raise_for_status()
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"✅ PDF saved to {output_path}")
            return True
        except Exception as e:
            print(f"❌ PDF download failed: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(description="Search bioRxiv database.")
    parser.add_argument("--start-date", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="End date (YYYY-MM-DD)")
    parser.add_argument("--days-back", type=int, help="Number of days to search back from today")
    parser.add_argument("--doi", help="Get details for a specific DOI")
    parser.add_argument("--download-pdf", help="Output path for PDF download (requires --doi)")
    parser.add_argument("--output", help="Output JSON file for metadata")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()
    searcher = BioRxivSearcher(verbose=args.verbose)

    if args.days_back:
        end_date = datetime.now().strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=args.days_back)).strftime("%Y-%m-%d")
    else:
        start_date = args.start_date
        end_date = args.end_date

    results = None
    if start_date and end_date:
        print(f"🔍 Searching bioRxiv from {start_date} to {end_date}...")
        results = searcher.search_by_date_range(start_date, end_date)
    elif args.doi:
        # bioRxiv API uses the same endpoint for DOI lookup if start/end are specific
        # But usually searching a range is more common.
        # This is a simplified placeholder for the full logic described in SKILL.md
        print(f"🔍 Fetching details for DOI: {args.doi}...")
        # For simplicity in this helper, we'll just note the DOI
        if args.download_pdf:
            searcher.download_pdf(args.doi, args.download_pdf)
            return

    if results:
        if args.output:
            with open(args.output, "w") as f:
                json.dump(results, f, indent=2)
            print(f"✅ Results saved to {args.output}")
        else:
            print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
