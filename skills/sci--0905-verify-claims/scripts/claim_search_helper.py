#!/usr/bin/env python3
import json
import urllib.parse
from typing import List, Dict

# Known reliable fact-checking domains
FACT_CHECK_DOMAINS = {
    "us_general": ["factcheck.org", "snopes.com", "politifact.com"],
    "uk_general": ["fullfact.org"],
    "intl_general": ["factcheck.afp.com", "reuters.com/fact-check", "apnews.com/hub/ap-fact-check"],
    "science_health": ["healthfeedback.org", "sciencefeedback.co", "climatefeedback.org"],
    "regional": {
        "pl": ["demagog.pl", "fakenews.pl"],
        "fr": ["lemonde.fr/les-decodeurs"],
        "de": ["correctiv.org/faktencheck"],
        "es": ["maldita.es", "newtral.es"],
        "pt": ["aosfatos.org", "lupa.uol.com.br"],
        "in": ["altnews.in", "boomlive.in"]
    }
}

def generate_search_queries(claim: str, categories: List[str] = None, lang: str = None) -> List[Dict[str, str]]:
    """
    Generate targeted search queries for specific fact-checking domains based on a claim.
    """
    domains_to_search = []

    # Add default general international domains
    domains_to_search.extend(FACT_CHECK_DOMAINS["intl_general"])

    # Add category-specific domains
    if categories:
        for cat in categories:
            if cat in FACT_CHECK_DOMAINS:
                domains_to_search.extend(FACT_CHECK_DOMAINS[cat])

    # Add language/region specific domains
    if lang and lang in FACT_CHECK_DOMAINS["regional"]:
        domains_to_search.extend(FACT_CHECK_DOMAINS["regional"][lang])

    # If no specific categories or lang provided, add US general as fallback
    if not categories and not lang:
        domains_to_search.extend(FACT_CHECK_DOMAINS["us_general"])
        domains_to_search.extend(FACT_CHECK_DOMAINS["uk_general"])

    # Deduplicate domains
    domains_to_search = list(set(domains_to_search))

    queries = []
    # Create site-specific search queries
    for domain in domains_to_search:
        # Extract key terms from claim (simplified version for the script)
        # In a real scenario, this might use NLP to extract entities and keywords
        key_terms = " ".join([word for word in claim.split() if len(word) > 3])

        query = f"site:{domain} {key_terms}"
        queries.append({
            "domain": domain,
            "query": query,
            "url": f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        })

    return queries

if __name__ == '__main__':
    sample_claim = "5G causes COVID-19"
    print("Testing claim search generation:")
    queries = generate_search_queries(sample_claim, categories=["science_health", "us_general"])
    print(json.dumps(queries, indent=2))
