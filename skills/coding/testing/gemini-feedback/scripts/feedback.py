#!/usr/bin/env python3
import base64
import os
import sys
import google.generativeai as genai

def review_diagram(image_path, context):
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))
    model = genai.GenerativeModel("gemini-2.0-flash")

    try:
        with open(image_path, "rb") as f:
            img = base64.standard_b64encode(f.read()).decode()
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        sys.exit(1)

    prompt = f"""Review this diagram for a textbook. Be concise and specific.

Context: {context}

Please provide:
1. Overall assessment (1-2 sentences)
2. Specific issues to fix (be detailed about visual problems like alignment, overlapping, etc.)
3. Suggestions for improvement
"""

    response = model.generate_content([prompt, {"mime_type": "image/png", "data": img}])
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python feedback.py <image_path> [context]")
        sys.exit(1)

    image_path = sys.argv[1]
    context = sys.argv[2] if len(sys.argv) > 2 else "Technical diagram for ML/AI textbook"

    review_diagram(image_path, context)
