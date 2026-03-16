import requests
import json

BASE_URL = "https://reactome.org/ContentService"

def query_pathway(pathway_id):
    url = f"{BASE_URL}/data/pathway/{pathway_id}/containedEvents"
    response = requests.get(url)
    return response.json()

def query_entity(entity_id):
    url = f"{BASE_URL}/data/query/{entity_id}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python reactome_query.py <pathway|entity> <id>")
        sys.exit(1)
    
    mode = sys.argv[1]
    query_id = sys.argv[2]
    
    if mode == 'pathway':
        print(json.dumps(query_pathway(query_id), indent=2))
    elif mode == 'entity':
        print(json.dumps(query_entity(query_id), indent=2))
