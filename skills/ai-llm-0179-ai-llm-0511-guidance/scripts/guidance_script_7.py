from guidance import models, gen

lm = models.Anthropic("claude-sonnet-4-5-20250929")

# Token healing enabled by default
lm += "The capital of France is " + gen("capital", max_tokens=5)
# Result: "The capital of France is Paris" (correct spacing)
