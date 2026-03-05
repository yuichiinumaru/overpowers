from guidance import models, gen, select
import os

def run_example():
    # Placeholder for guidance example
    # lm = models.OpenAI("gpt-4")
    print("Guidance example: Constraining output to specific choices")
    # result = lm + "The sentiment is " + select(["positive", "negative", "neutral"], name="sentiment")
    # print(f"Result: {result['sentiment']}")
    print("Note: Requires ANTHROPIC_API_KEY or OPENAI_API_KEY and 'guidance' package.")

if __name__ == "__main__":
    run_example()
