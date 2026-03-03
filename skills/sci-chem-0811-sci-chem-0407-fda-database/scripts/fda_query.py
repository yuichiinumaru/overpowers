import os
import requests
import time
from datetime import datetime, timedelta

class FDAQuery:
    BASE_URL = "https://api.fda.gov"

    def __init__(self, api_key=None, use_cache=True, cache_ttl=3600):
        self.api_key = api_key or os.environ.get("FDA_API_KEY")
        self.use_cache = use_cache
        self.cache_ttl = cache_ttl
        self._cache = {}

    def query(self, category, endpoint, search=None, count=None, limit=10, skip=0, sort=None):
        url = f"{self.BASE_URL}/{category}/{endpoint}.json"
        
        params = {
            "limit": limit,
            "skip": skip
        }
        
        if self.api_key:
            params["api_key"] = self.api_key
            
        if search:
            params["search"] = search
            
        if count:
            params["count"] = count
            
        if sort:
            params["sort"] = sort

        # Very simple in-memory cache
        cache_key = f"{category}_{endpoint}_{search}_{count}_{limit}_{skip}_{sort}"
        if self.use_cache and cache_key in self._cache:
            data, timestamp = self._cache[cache_key]
            if time.time() - timestamp < self.cache_ttl:
                return data

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if self.use_cache:
                self._cache[cache_key] = (data, time.time())
                
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def count_by_field(self, category, endpoint, search, field, exact=True):
        count_field = f"{field}.exact" if exact else field
        return self.query(category, endpoint, search=search, count=count_field)

    def query_drug_events(self, drug_name, limit=10):
        search = f"patient.drug.medicinalproduct:{drug_name}"
        return self.query("drug", "event", search=search, limit=limit)

    def query_drug_label(self, drug_name, brand=True):
        field = "openfda.brand_name" if brand else "openfda.generic_name"
        search = f"{field}:{drug_name}"
        return self.query("drug", "label", search=search, limit=1)

    def query_drug_recalls(self, drug_name=None, classification=None):
        search_parts = []
        if drug_name:
            search_parts.append(f"product_description:{drug_name}")
        if classification:
            search_parts.append(f"classification:Class+{classification}")
        
        search = "+AND+".join(search_parts) if search_parts else None
        return self.query("drug", "enforcement", search=search)

    def query_device_events(self, device_name, limit=10):
        search = f"device.generic_name:{device_name}"
        return self.query("device", "event", search=search, limit=limit)

    def query_device_classification(self, product_code):
        search = f"product_code:{product_code}"
        return self.query("device", "classification", search=search, limit=1)

    def query_device_510k(self, device_name=None, applicant=None):
        search_parts = []
        if device_name:
            search_parts.append(f"device_name:{device_name}")
        if applicant:
            search_parts.append(f"applicant:{applicant}")
        
        search = "+AND+".join(search_parts) if search_parts else None
        return self.query("device", "510k", search=search)

    def query_food_recalls(self, reason=None, classification=None):
        search_parts = []
        if reason:
            search_parts.append(f"reason_for_recall:{reason}")
        if classification:
            search_parts.append(f"classification:Class+{classification}")
            
        search = "+AND+".join(search_parts) if search_parts else None
        return self.query("food", "enforcement", search=search)

    def query_food_events(self, industry=None):
        search = f"products.industry_name:\"{industry}\"" if industry else None
        return self.query("food", "event", search=search)

    def query_animal_events(self, species=None, drug_name=None):
        search_parts = []
        if species:
            search_parts.append(f"animal.species:{species}")
        if drug_name:
            search_parts.append(f"drug.active_ingredients.active_ingredient:{drug_name}")
            
        search = "+AND+".join(search_parts) if search_parts else None
        return self.query("animalandveterinary", "event", search=search)

    def query_substance_by_unii(self, unii):
        search = f"codes.code:{unii}+AND+codes.code_system:UNII"
        return self.query("other", "substance", search=search, limit=1)

    def query_substance_by_name(self, name):
        search = f"names.name:{name}"
        return self.query("other", "substance", search=search, limit=1)

    def query_all(self, category, endpoint, search=None, max_results=1000):
        all_results = []
        skip = 0
        limit = 100
        
        while skip < max_results:
            result = self.query(category, endpoint, search=search, limit=limit, skip=skip)
            if "error" in result or "results" not in result:
                break
                
            all_results.extend(result["results"])
            
            if len(result["results"]) < limit:
                break
                
            skip += limit
            
        return {"results": all_results[:max_results]}
