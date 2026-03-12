import os
try:
    from tooluniverse import ToolUniverse
except ImportError:
    print("Error: tooluniverse package not installed. Run: pip install tooluniverse")
    exit(1)

def quickstart():
    """
    Basic quickstart for ToolUniverse SDK.
    """
    print("Initializing ToolUniverse...")
    tu = ToolUniverse(use_cache=True)
    
    print("Loading tools (this may take a few seconds)...")
    tu.load_tools()
    
    # Example: Search for a gene
    print("\nExample: Searching for UniProt entry for 'APP' (Amyloid Beta Precursor Protein)")
    try:
        result = tu.tools.UniProt_get_entry_by_accession(accession="P05067")
        print(f"Gene Name: {result.get('genes', [{}])[0].get('geneName', {}).get('value')}")
        print(f"Full Name: {result.get('proteinDescription', {}).get('recommendedName', {}).get('fullName', {}).get('value')}")
    except Exception as e:
        print(f"Error during tool execution: {e}")

    # Example: Find tools
    print("\nFinding tools for 'toxicity prediction'...")
    tools = tu.run({
        "name": "Tool_Finder_Keyword",
        "arguments": {"description": "toxicity", "limit": 5}
    })
    
    if isinstance(tools, dict) and 'tools' in tools:
        for tool in tools['tools']:
            print(f"- {tool['name']}: {tool['description']}")

if __name__ == "__main__":
    quickstart()
