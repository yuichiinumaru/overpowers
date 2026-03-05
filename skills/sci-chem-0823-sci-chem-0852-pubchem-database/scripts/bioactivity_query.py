import requests
import json
import pandas as pd

def get_bioassay_summary(cid):
    """Get bioassay summary for a compound"""
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/assaysummary/JSON"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def summarize_bioactivities(cid):
    """Generate bioactivity summary statistics"""
    data = get_bioassay_summary(cid)
    if not data:
        return {"error": "No data found"}
        
    table = data.get('Table', {})
    rows = table.get('Row', [])
    
    # Simple counting based on assay outcome
    active = 0
    inactive = 0
    other = 0
    
    for row in rows:
        # PUG-REST assay summary usually has 'Outcome' in a specific column
        # This is a simplification; actual parsing depends on column headers
        outcome = row.get('Cell', [None]*10)[3] # Typical outcome column
        if outcome == 'Active':
            active += 1
        elif outcome == 'Inactive':
            inactive += 1
        else:
            other += 1
            
    return {
        "total_assays": len(rows),
        "active": active,
        "inactive": inactive,
        "other": other
    }

def get_compound_annotations(cid, section=None):
    """Get PUG-View annotations"""
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON"
    if section:
        url += f"?heading={section}"
        
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == "__main__":
    import sys
    cid = sys.argv[1] if len(sys.argv) > 1 else 2244 # Aspirin
    try:
        summary = summarize_bioactivities(cid)
        print(f"Bioactivity Summary for CID {cid}:")
        print(json.dumps(summary, indent=2))
    except Exception as e:
        print(f"Error: {e}")
