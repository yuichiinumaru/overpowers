import os
import argparse
from guidance import models, gen, select

def structured_generation(model_name, prompt, choices=None, regex=None):
    """
    Perform structured generation using Guidance.
    
    Args:
        model_name (str): The name of the model to use (e.g., 'gpt-4o-mini', 'claude-3-5-sonnet-20240620').
        prompt (str): The input prompt.
        choices (list): Optional list of strings to select from.
        regex (str): Optional regex pattern to constrain the output.
    """
    print(f"Initializing Guidance with model: {model_name}")
    
    # Initialize the model based on provider
    if "claude" in model_name.lower():
        if not os.getenv("ANTHROPIC_API_KEY"):
            print("Error: ANTHROPIC_API_KEY environment variable not set.")
            return
        lm = models.Anthropic(model_name)
    else:
        if not os.getenv("OPENAI_API_KEY"):
            print("Error: OPENAI_API_KEY environment variable not set.")
            return
        lm = models.OpenAI(model_name)

    lm += prompt
    
    if choices:
        lm += select(choices, name="selection")
        print(f"Selection: {lm['selection']}")
    elif regex:
        lm += gen("output", regex=regex)
        print(f"Output: {lm['output']}")
    else:
        lm += gen("output", max_tokens=50)
        print(f"Output: {lm['output']}")

def main():
    parser = argparse.ArgumentParser(description="Guidance Structured Generation Helper")
    parser.add_argument("--model", default="gpt-4o-mini", help="Model name")
    parser.add_argument("--prompt", required=True, help="Input prompt")
    parser.add_argument("--choices", nargs="+", help="List of choices for selection")
    parser.add_argument("--regex", help="Regex pattern for generation")
    
    args = parser.parse_args()
    
    structured_generation(args.model, args.prompt, args.choices, args.regex)

if __name__ == "__main__":
    main()
