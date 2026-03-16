import sys
try:
    from idc_index import IDCClient
except ImportError:
    print("Error: 'idc-index' package not found. Install with: pip install idc-index")
    sys.exit(1)

def run_query(sql):
    client = IDCClient()
    print(f"Running query: {sql}")
    results = client.sql_query(sql)
    print(results)

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "SELECT collection_id, COUNT(*) as series_count FROM index GROUP BY collection_id LIMIT 10"
    run_query(query)
