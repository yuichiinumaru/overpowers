import outlines
from typing import Literal
import sys

def main():
    # Usage: python example_classification.py "prompt" "option1" "option2" ...
    if len(sys.argv) < 3:
        print("Usage: python example_classification.py <prompt> <option1> <option2> ...")
        print("Example: python example_classification.py \"Sentiment of 'This is great!': \" \"positive\" \"negative\" \"neutral\"")
        sys.exit(1)

    prompt = sys.argv[1]
    options = sys.argv[2:]

    print(f"Loading model and setting up classification for options: {options}...")
    
    # Using a small model for example purposes
    try:
        model = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")
        generator = outlines.generate.choice(model, options)
        
        print(f"Prompt: {prompt}")
        result = generator(prompt)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have 'outlines' and 'transformers' installed:")
        print("pip install outlines transformers torch")

if __name__ == "__main__":
    main()
