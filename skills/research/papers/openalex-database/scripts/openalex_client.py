import requests
import time
import random
from typing import Dict, List, Any, Optional

class OpenAlexClient:
    """
    A simple client for the OpenAlex API with rate limiting and retry logic.
    """
    
    BASE_URL = "https://api.openalex.org"
    
    def __init__(self, email: Optional[str] = None):
        self.email = email
        self.session = requests.Session()
        if email:
            self.session.params = {'mailto': email}
            
    def _make_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None, max_retries: int = 3) -> Dict[str, Any]:
        url = f"{self.BASE_URL}{endpoint}" if not endpoint.startswith('http') else endpoint
        
        for attempt in range(max_retries):
            try:
                response = self.session.get(url, params=params, timeout=30)
                
                if response.status_code == 429:
                    # Rate limited - exponential backoff with jitter
                    wait_time = (2 ** attempt) + random.random()
                    print(f"Rate limited. Waiting {wait_time:.2f}s...")
                    time.sleep(wait_time)
                    continue
                    
                response.raise_for_status()
                return response.json()
                
            except requests.RequestException as e:
                if attempt == max_retries - 1:
                    raise
                wait_time = (2 ** attempt) + random.random()
                time.sleep(wait_time)
        
        return {}

    def search_works(self, search: Optional[str] = None, filter_params: Optional[Dict[str, str]] = None, 
                     sort: Optional[str] = None, per_page: int = 200, page: int = 1, 
                     select: Optional[List[str]] = None) -> Dict[str, Any]:
        params = {
            'per-page': per_page,
            'page': page
        }
        if search:
            params['search'] = search
        if filter_params:
            filter_str = ",".join([f"{k}:{v}" for k, v in filter_params.items()])
            params['filter'] = filter_str
        if sort:
            params['sort'] = sort
        if select:
            params['select'] = ",".join(select)
            
        return self._make_request("/works", params=params)

    def get_entity(self, entity_type: str, entity_id: str) -> Dict[str, Any]:
        # Handle full URLs vs short IDs
        eid = entity_id.split('/')[-1] if '/' in entity_id else entity_id
        return self._make_request(f"/{entity_type}/{eid}")

    def batch_lookup(self, entity_type: str, ids: List[str], id_field: str = 'doi') -> List[Dict[str, Any]]:
        if not ids:
            return []
        
        # OpenAlex batch limit is typically 50
        results = []
        for i in range(0, len(ids), 50):
            chunk = ids[i:i+50]
            filter_val = "|".join(chunk)
            response = self._make_request(f"/{entity_type}", params={'filter': f"{id_field}:{filter_val}", 'per-page': 50})
            results.extend(response.get('results', []))
        return results

    def group_by(self, entity_type: str, group_field: str, filter_params: Optional[Dict[str, str]] = None) -> List[Dict[str, Any]]:
        params = {'group_by': group_field}
        if filter_params:
            filter_str = ",".join([f"{k}:{v}" for k, v in filter_params.items()])
            params['filter'] = filter_str
            
        response = self._make_request(f"/{entity_type}", params=params)
        return response.get('group_by', [])

    def paginate_all(self, endpoint: str, params: Dict[str, Any], max_results: int = 1000) -> List[Dict[str, Any]]:
        results = []
        current_params = params.copy()
        current_params['per-page'] = 200
        
        # Use cursor-based pagination if not already specified
        if 'cursor' not in current_params:
            current_params['cursor'] = '*'
            
        while len(results) < max_results:
            response = self._make_request(endpoint, params=current_params)
            new_results = response.get('results', [])
            if not new_results:
                break
                
            results.extend(new_results)
            
            next_cursor = response.get('meta', {}).get('next_cursor')
            if not next_cursor:
                break
            current_params['cursor'] = next_cursor
            
        return results[:max_results]
