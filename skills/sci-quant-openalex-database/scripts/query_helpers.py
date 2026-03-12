from typing import List, Dict, Any, Optional
from .openalex_client import OpenAlexClient

def find_author_works(author_name: str, client: OpenAlexClient, limit: int = 100) -> List[Dict[str, Any]]:
    # Step 1: Find author ID
    author_search = client._make_request("/authors", params={'search': author_name, 'per-page': 1})
    if not author_search.get('results'):
        return []
    
    author_id = author_search['results'][0]['id'].split('/')[-1]
    
    # Step 2: Get works
    response = client.search_works(filter_params={"authorships.author.id": author_id}, per_page=min(limit, 200))
    return response.get('results', [])

def find_institution_works(institution_name: str, client: OpenAlexClient, limit: int = 100) -> List[Dict[str, Any]]:
    # Step 1: Find institution ID
    inst_search = client._make_request("/institutions", params={'search': institution_name, 'per-page': 1})
    if not inst_search.get('results'):
        return []
    
    inst_id = inst_search['results'][0]['id'].split('/')[-1]
    
    # Step 2: Get works
    response = client.search_works(filter_params={"authorships.institutions.id": inst_id}, per_page=min(limit, 200))
    return response.get('results', [])

def find_highly_cited_recent_papers(topic: str, years: str, client: OpenAlexClient, limit: int = 100) -> List[Dict[str, Any]]:
    response = client.search_works(
        search=topic,
        filter_params={"publication_year": years},
        sort="cited_by_count:desc",
        per_page=min(limit, 200)
    )
    return response.get('results', [])

def get_open_access_papers(search_term: str, client: OpenAlexClient, oa_status: str = "any", limit: int = 100) -> List[Dict[str, Any]]:
    filter_params = {"is_oa": "true"}
    if oa_status != "any":
        filter_params["open_access.oa_status"] = oa_status
        
    response = client.search_works(
        search=search_term,
        filter_params=filter_params,
        per_page=min(limit, 200)
    )
    return response.get('results', [])

def get_publication_trends(search_term: str, filter_params: Optional[Dict[str, str]], client: OpenAlexClient) -> List[Dict[str, Any]]:
    f_params = filter_params.copy() if filter_params else {}
    return client.group_by('works', 'publication_year', filter_params=f_params)

def analyze_research_output(entity_type: str, entity_name: str, client: OpenAlexClient, years: Optional[str] = None) -> Dict[str, Any]:
    # Find entity ID first
    search_resp = client._make_request(f"/{entity_type}", params={'search': entity_name, 'per-page': 1})
    if not search_resp.get('results'):
        return {"error": "Entity not found"}
    
    entity = search_resp['results'][0]
    entity_id = entity['id'].split('/')[-1]
    
    filter_key = "authorships.author.id" if entity_type == 'authors' else "authorships.institutions.id"
    filters = {filter_key: entity_id}
    if years:
        filters["publication_year"] = years
        
    # Get total count and metadata
    works_resp = client.search_works(filter_params=filters, per_page=1)
    total_works = works_resp.get('meta', {}).get('count', 0)
    
    # Get OA stats
    oa_group = client.group_by('works', 'is_oa', filter_params=filters)
    oa_count = next((item['count'] for item in oa_group if item['key'] == 'true'), 0)
    
    # Get top topics
    topics = client.group_by('works', 'topics.id', filter_params=filters)
    
    return {
        "entity_name": entity.get('display_name'),
        "total_works": total_works,
        "open_access_count": oa_count,
        "open_access_percentage": (oa_count / total_works * 100) if total_works > 0 else 0,
        "top_topics": topics[:10]
    }
