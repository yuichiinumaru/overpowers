#!/usr/bin/env python3
"""
Vertex AI Prompt Templates Helper.
"""
import argparse

def generate_vertex_prompt(prompt, model="gemini-1.5-pro", temperature=0.7):
    """
    Simulates a call to Vertex AI Generative AI.
    """
    print(f"--- Vertex AI Simulation ---")
    print(f"Model: {model}")
    print(f"Temperature: {temperature}")
    print(f"Prompt Template: {prompt}")
    print(f"--- Output (Mock) ---")
    print("This is a mock response from the Vertex AI Prompt Templates helper.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use prompt templates | Generative AI on Vertex AI")
    parser.add_argument("--prompt", type=str, required=True, help="The prompt template to use")
    parser.add_argument("--model", type=str, default="gemini-1.5-pro", help="Vertex AI model to use")
    parser.add_argument("--temperature", type=float, default=0.7, help="Temperature for generation")

    args = parser.parse_args()
    generate_vertex_prompt(args.prompt, args.model, args.temperature)
