import os
import sys
import json
import time
import argparse
import requests

def run_actor(actor_id, input_data):
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        print("Error: APIFY_TOKEN environment variable is not set.")
        return None

    # Start the actor run
    url = f"https://api.apify.com/v2/acts/{actor_id}/runs?token={token}"
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, headers=headers, json=input_data)
        response.raise_for_status()
        
        run_data = response.json().get("data", {})
        run_id = run_data.get("id")
        
        print(f"Started run {run_id}. Waiting for completion...")
        
        # Poll for completion
        while True:
            time.sleep(5)
            status_url = f"https://api.apify.com/v2/actor-runs/{run_id}?token={token}"
            status_res = requests.get(status_url)
            status_res.raise_for_status()
            
            status_data = status_res.json().get("data", {})
            status = status_data.get("status")
            
            print(f"Status: {status}")
            
            if status == "SUCCEEDED":
                dataset_id = status_data.get("defaultDatasetId")
                break
            elif status in ["FAILED", "ABORTED", "TIMED-OUT"]:
                print(f"Run failed with status: {status}")
                return None
                
        # Fetch results
        dataset_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={token}"
        dataset_res = requests.get(dataset_url)
        dataset_res.raise_for_status()
        
        return dataset_res.json()
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Run Apify Actors and fetch results')
    parser.add_argument('--actor', required=True, help='Actor ID (e.g., apify/instagram-profile-scraper)')
    parser.add_argument('--input', required=True, help='JSON string containing input parameters')
    
    args = parser.parse_args()
    
    try:
        input_data = json.loads(args.input)
    except json.JSONDecodeError:
        print("Error: Input must be valid JSON")
        sys.exit(1)
        
    results = run_actor(args.actor, input_data)
    
    if results:
        print("\n--- Results ---")
        print(json.dumps(results, indent=2))
        
        # Option to save
        with open("apify_results.json", "w") as f:
            json.dump(results, f, indent=2)
        print("Saved to apify_results.json")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
