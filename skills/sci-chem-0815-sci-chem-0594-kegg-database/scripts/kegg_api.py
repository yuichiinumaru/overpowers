import requests
import sys

BASE_URL = "https://rest.kegg.jp"

def kegg_info(database):
    """Retrieve metadata about a KEGG database"""
    url = f"{BASE_URL}/info/{database}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def kegg_list(database, organism=None):
    """List entry identifiers and names"""
    if organism:
        url = f"{BASE_URL}/list/{database}/{organism}"
    else:
        url = f"{BASE_URL}/list/{database}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def kegg_find(database, query, option=None):
    """Search KEGG databases"""
    if option:
        url = f"{BASE_URL}/find/{database}/{query}/{option}"
    else:
        url = f"{BASE_URL}/find/{database}/{query}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def kegg_get(dbentries, option=None):
    """Retrieve database entries"""
    if isinstance(dbentries, list):
        dbentries = "+".join(dbentries)
    
    url = f"{BASE_URL}/get/{dbentries}"
    if option:
        url += f"/{option}"
        
    response = requests.get(url)
    response.raise_for_status()
    
    if option == 'image':
        return response.content
    return response.text

def kegg_conv(target_db, source_db):
    """Convert identifiers between databases"""
    url = f"{BASE_URL}/conv/{target_db}/{source_db}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def kegg_link(target_db, source_db):
    """Find related entries between databases"""
    url = f"{BASE_URL}/link/{target_db}/{source_db}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def kegg_ddi(dbentries):
    """Check for drug-drug interactions"""
    if isinstance(dbentries, list):
        dbentries = "+".join(dbentries)
    url = f"{BASE_URL}/ddi/{dbentries}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

if __name__ == "__main__":
    # Example: List human pathways
    try:
        print("Human Pathways (first 5):")
        pathways = kegg_list("pathway", "hsa")
        for line in pathways.split('\n')[:5]:
            print(line)
    except Exception as e:
        print(f"Error: {e}")
