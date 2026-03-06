import os
import sys
import json
import requests
import argparse

def baidu_search(params):
    api_key = os.environ.get("BAIDU_API_KEY")
    if not api_key:
        print("Error: BAIDU_API_KEY environment variable is not set.")
        return None

    url = "https://qianfan.baidubce.com/v2/tools/baidu_search/search"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error during Baidu search: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 search.py '<JSON_PARAMS>'")
        sys.exit(1)
        
    try:
        params = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        print("Error: Invalid JSON input")
        sys.exit(1)
        
    result = baidu_search(params)
    if result:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
