import sys

def search_web(query):
    return f"Search results for: {query}"

class Tool:
    def __init__(self, name, func, description):
        self.name = name
        self.func = func
        self.description = description

if __name__ == "__main__":
    tools = [
        Tool(
            name="WebSearch",
            func=search_web,
            description="Useful for when you need to answer questions about current events."
        )
    ]
    print(f"Initialized {len(tools)} tools for Agent.")
