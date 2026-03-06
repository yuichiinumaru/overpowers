#!/usr/bin/env python3
"""
Helper script to build a prompt template for Vertex AI.
"""
import sys

def build_template(template_name, params):
    param_string = ", ".join([f"[{p}]" for p in params])
    template = f"""Prompt Template: {template_name}
Parameters: {', '.join(params)}
Template Content:
Please generate an image based on the following description:
{param_string}
...
"""
    print(template)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vertex_prompt_template.py <template_name> [param1 param2 ...]")
        sys.exit(1)

    name = sys.argv[1]
    params = sys.argv[2:] if len(sys.argv) > 2 else ["subject", "style"]
    build_template(name, params)
