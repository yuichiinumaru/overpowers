from guidance import models, gen

lm = models.Anthropic("claude-sonnet-4-5-20250929")

# JSON grammar (simplified)
json_grammar = """
{
    "name": <gen name regex="[A-Za-z ]+" max_tokens=20>,
    "age": <gen age regex="[0-9]+" max_tokens=3>,
    "email": <gen email regex="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" max_tokens=50>
}
"""

# Generate valid JSON
lm += gen("person", grammar=json_grammar)

print(lm["person"])  # Guaranteed valid JSON structure
