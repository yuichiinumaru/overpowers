from rcsbapi.search import TextQuery, AttributeQuery
from rcsbapi.search.attrs import rcsb_entity_source_organism, rcsb_entry_info

def search_by_text(query_text):
    """Search PDB by text query"""
    query = TextQuery(query_text)
    results = list(query())
    return results

def search_high_res_human(max_resolution=2.0):
    """Search for high-resolution human structures"""
    query1 = AttributeQuery(
        attribute=rcsb_entity_source_organism.scientific_name,
        operator="exact_match",
        value="Homo sapiens"
    )
    query2 = AttributeQuery(
        attribute=rcsb_entry_info.resolution_combined,
        operator="less",
        value=max_resolution
    )
    combined_query = query1 & query2
    results = list(combined_query())
    return results

if __name__ == "__main__":
    import sys
    search_term = sys.argv[1] if len(sys.argv) > 1 else "hemoglobin"
    try:
        print(f"Searching for '{search_term}'...")
        results = search_by_text(search_term)
        print(f"Found {len(results)} results. Top 10 IDs: {results[:10]}")
    except Exception as e:
        print(f"Error: {e}")
