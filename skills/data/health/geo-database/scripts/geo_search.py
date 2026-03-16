from Bio import Entrez
import os

def search_geo_datasets(query, retmax=20, email=None):
    """Search GEO DataSets database"""
    Entrez.email = email or os.environ.get("NCBI_EMAIL")
    if not Entrez.email:
        raise ValueError("NCBI_EMAIL environment variable or email parameter required")
        
    handle = Entrez.esearch(
        db="gds",
        term=query,
        retmax=retmax,
        usehistory="y"
    )
    results = Entrez.read(handle)
    handle.close()
    return results

def get_summaries(id_list, db="gds"):
    """Fetch document summaries for GEO entries"""
    ids = ",".join(id_list)
    handle = Entrez.esummary(db=db, id=ids)
    summaries = Entrez.read(handle)
    handle.close()
    return summaries

if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "breast cancer AND Homo sapiens"
    try:
        results = search_geo_datasets(query)
        print(f"Found {results['Count']} datasets for query: {query}")
        if results['IdList']:
            summaries = get_summaries(results['IdList'][:5])
            for s in summaries:
                print(f"- {s.get('Accession')}: {s.get('title')}")
    except Exception as e:
        print(f"Error: {e}")
