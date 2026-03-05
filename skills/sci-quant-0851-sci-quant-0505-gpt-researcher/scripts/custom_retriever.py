"""
Template for creating a custom retriever for GPT Researcher.
Save this as gpt_researcher/retrievers/my_retriever/my_retriever.py
"""

class MyCustomRetriever:
    """
    Custom retriever implementation.
    """
    def __init__(self, query: str, headers: dict = None):
        self.query = query
        self.headers = headers or {}
        
    async def search(self, max_results: int = 10) -> list[dict]:
        """
        Execute the search and return results.
        Must return a list of dictionaries with 'title', 'href', and 'body'.
        """
        print(f"[MyCustomRetriever] Searching for: {self.query}")
        
        # Simulate API call
        results = [
            {
                "title": f"Result 1 for {self.query}",
                "href": "https://example.com/result1",
                "body": "This is the body of the first result."
            },
            {
                "title": f"Result 2 for {self.query}",
                "href": "https://example.com/result2",
                "body": "This is the body of the second result."
            }
        ]
        
        return results[:max_results]

# To use this, add it to gpt_researcher/actions/retriever.py:
# match retriever_name:
#     case "my_retriever":
#         from gpt_researcher.retrievers.my_retriever.my_retriever import MyCustomRetriever
#         return MyCustomRetriever
