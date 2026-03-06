from guidance import guidance, gen, models

@guidance
def generate_person(lm):
    """Generate a person with name and age."""
    lm += "Name: " + gen("name", max_tokens=20, stop="\n")
    lm += "\nAge: " + gen("age", regex=r"[0-9]+", max_tokens=3)
    return lm

# Use the function
lm = models.Anthropic("claude-sonnet-4-5-20250929")
lm = generate_person(lm)

print(lm["name"])
print(lm["age"])
