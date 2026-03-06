import requests
import os
import sys
import time

class PubMedQuery:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

    def __init__(self, api_key=None, email=None):
        self.api_key = api_key or os.environ.get("NCBI_API_KEY")
        self.email = email or os.environ.get("NCBI_EMAIL")
        if not self.email:
            # NCBI requires an email for E-utilities
            self.email = "agent@example.com"

    def _get_params(self, extra_params):
        params = {
            "db": "pubmed",
            "tool": "OverpowersAgent",
            "email": self.email
        }
        if self.api_key:
            params["api_key"] = self.api_key
        params.update(extra_params)
        return params

    def search(self, term, retmax=20):
        """Search PubMed and return PMIDs"""
        url = f"{self.BASE_URL}esearch.fcgi"
        params = self._get_params({
            "term": term,
            "retmax": retmax,
            "retmode": "json"
        })
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])

    def fetch_details(self, pmids, rettype="abstract", retmode="text"):
        """Fetch article details for PMIDs"""
        if isinstance(pmids, list):
            pmids = ",".join(pmids)
            
        url = f"{self.BASE_URL}efetch.fcgi"
        params = self._get_params({
            "id": pmids,
            "rettype": rettype,
            "retmode": retmode
        })
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text

    def get_summaries(self, pmids):
        """Fetch document summaries for PMIDs"""
        if isinstance(pmids, list):
            pmids = ",".join(pmids)
            
        url = f"{self.BASE_URL}esummary.fcgi"
        params = self._get_params({
            "id": pmids,
            "retmode": "json"
        })
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("result", {})

if __name__ == "__main__":
    query_term = sys.argv[1] if len(sys.argv) > 1 else "diabetes[tiab] AND 2024[dp]"
    pubmed = PubMedQuery()
    try:
        print(f"Searching for: {query_term}")
        pmids = pubmed.search(query_term, retmax=5)
        print(f"Found PMIDs: {pmids}")
        if pmids:
            summaries = pubmed.get_summaries(pmids)
            for pmid in pmids:
                s = summaries.get(pmid, {})
                print(f"- {pmid}: {s.get('title')}")
    except Exception as e:
        print(f"Error: {e}")
