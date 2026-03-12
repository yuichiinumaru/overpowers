import os
import sys
import argparse
import requests
import json

class AIsaClient:
    BASE_URL = "https://api.aisa.one/apis/v1"

    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("AISA_API_KEY")
        if not self.api_key:
            print("Error: AISA_API_KEY environment variable not set.")
            sys.exit(1)
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _post(self, endpoint, data=None, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.post(url, headers=self.headers, json=data, params=params)
        response.raise_for_status()
        return response.json()

    def web_search(self, query, count=10):
        return self._post("/scholar/search/web", params={"query": query, "max_num_results": count})

    def scholar_search(self, query, count=10, year_from=None, year_to=None):
        params = {"query": query, "max_num_results": count}
        if year_from: params["as_ylo"] = year_from
        if year_to: params["as_yhi"] = year_to
        return self._post("/scholar/search/scholar", params=params)

    def smart_search(self, query, count=10):
        return self._post("/scholar/search/smart", params={"query": query, "max_num_results": count})

    def full_text_search(self, query, count=10):
        return self._post("/search/full", params={"query": query, "max_num_results": count})

    def tavily_search(self, query):
        return self._post("/tavily/search", data={"query": query})

    def explain(self, results):
        return self._post("/scholar/explain", data={"results": results, "language": "en", "format": "summary"})

def main():
    parser = argparse.ArgumentParser(description="OpenClaw Search Client")
    subparsers = parser.add_subparsers(dest="command", help="Search commands")

    # Web search
    web_parser = subparsers.add_parser("web", help="Web search")
    web_parser.add_argument("--query", required=True)
    web_parser.add_argument("--count", type=int, default=10)

    # Scholar search
    scholar_parser = subparsers.add_parser("scholar", help="Academic search")
    scholar_parser.add_argument("--query", required=True)
    scholar_parser.add_argument("--count", type=int, default=10)
    scholar_parser.add_argument("--year-from", type=int)
    scholar_parser.add_argument("--year-to", type=int)

    # Smart search
    smart_parser = subparsers.add_parser("smart", help="Hybrid search")
    smart_parser.add_argument("--query", required=True)
    smart_parser.add_argument("--count", type=int, default=10)

    # Full search
    full_parser = subparsers.add_parser("full", help="Full text search")
    full_parser.add_argument("--query", required=True)

    # Tavily
    tavily_parser = subparsers.add_parser("tavily-search", help="Tavily search")
    tavily_parser.add_argument("--query", required=True)

    # Verity (Multi-source + Explain)
    verity_parser = subparsers.add_parser("verity", help="Multi-source search with meta-analysis")
    verity_parser.add_argument("--query", required=True)

    args = parser.parse_args()
    client = AIsaClient()

    try:
        if args.command == "web":
            res = client.web_search(args.query, args.count)
            print(json.dumps(res, indent=2))
        elif args.command == "scholar":
            res = client.scholar_search(args.query, args.count, args.year_from, args.year_to)
            print(json.dumps(res, indent=2))
        elif args.command == "smart":
            res = client.smart_search(args.query, args.count)
            print(json.dumps(res, indent=2))
        elif args.command == "full":
            res = client.full_text_search(args.query)
            print(json.dumps(res, indent=2))
        elif args.command == "tavily-search":
            res = client.tavily_search(args.query)
            print(json.dumps(res, indent=2))
        elif args.command == "verity":
            print(f"Conducting deep research for: {args.query}...")
            # Simple version of verity logic
            smart_res = client.smart_search(args.query, count=5)
            # Filter results for explain endpoint
            results_to_explain = smart_res.get('results', [])
            explanation = client.explain(results_to_explain)
            print("\n=== Synthesized Answer ===")
            print(explanation.get('summary', 'No summary available.'))
            print("\n=== Usage ===")
            print(f"Cost: {explanation.get('usage', {}).get('cost', 'N/A')}")
    except Exception as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":
    main()
