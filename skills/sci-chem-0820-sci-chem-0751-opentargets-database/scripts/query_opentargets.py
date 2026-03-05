import requests
import json

API_URL = "https://api.platform.opentargets.org/api/v4/graphql"

def execute_query(query, variables=None):
    """Execute a GraphQL query against the Open Targets API"""
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
        
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()

def search_entities(query, entity_types=None):
    """Search for targets, diseases, or drugs"""
    gql_query = """
    query SearchQuery($queryString: String!, $entityNames: [String!]) {
      search(queryString: $queryString, entityNames: $entityNames) {
        total
        hits {
          id
          name
          entity
        }
      }
    }
    """
    variables = {"queryString": query, "entityNames": entity_types or ["target", "disease", "drug"]}
    result = execute_query(gql_query, variables)
    return result.get("data", {}).get("search", {}).get("hits", [])

def get_target_info(ensembl_id):
    """Retrieve basic target information"""
    gql_query = """
    query TargetQuery($ensemblId: String!) {
      target(ensemblId: $ensemblId) {
        id
        approvedSymbol
        approvedName
        biootype
        tractability {
          modality
          id
          value
        }
      }
    }
    """
    variables = {"ensemblId": ensembl_id}
    result = execute_query(gql_query, variables)
    return result.get("data", {}).get("target")

def get_known_drugs_for_disease(efo_id):
    """Find drugs for a disease"""
    gql_query = """
    query KnownDrugsQuery($efoId: String!) {
      disease(efoId: $efoId) {
        id
        name
        knownDrugs {
          uniqueDrugs
          uniqueTargets
          rows {
            drug {
              id
              name
              drugType
            }
            phase
            status
            ctIds
          }
        }
      }
    }
    """
    variables = {"efoId": efo_id}
    result = execute_query(gql_query, variables)
    return result.get("data", {}).get("disease", {}).get("knownDrugs")

if __name__ == "__main__":
    import sys
    search_term = sys.argv[1] if len(sys.argv) > 1 else "BRCA1"
    try:
        print(f"Searching for '{search_term}'...")
        hits = search_entities(search_term)
        for hit in hits[:5]:
            print(f"- [{hit['entity']}] {hit['name']} ({hit['id']})")
    except Exception as e:
        print(f"Error: {e}")
