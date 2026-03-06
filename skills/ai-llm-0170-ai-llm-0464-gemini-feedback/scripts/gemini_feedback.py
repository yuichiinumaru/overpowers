import base64
import os
import sys
import argparse
import google.generativeai as genai

def main():
    parser = argparse.ArgumentParser(description="Get feedback from Gemini API on a diagram image.")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("context", nargs="?", default="Technical diagram for ML/AI textbook", help="Context for the diagram (optional)")
    args = parser.parse_args()

    if 'GEMINI_API_KEY' not in os.environ:
        print("Error: GEMINI_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-2.0-flash')

    try:
        with open(args.image_path, 'rb') as f:
            img = base64.standard_b64encode(f.read()).decode()
    except FileNotFoundError:
        print(f"Error: Image file not found at {args.image_path}", file=sys.stderr)
        sys.exit(1)

    prompt = f'''Review this diagram for a textbook. Be concise and specific.

Context: {args.context}

Please provide:
1. Overall assessment (1-2 sentences)
2. Specific issues to fix (be detailed about visual problems like alignment, overlapping, etc.)
3. Suggestions for improvement
'''

    try:
        response = model.generate_content([prompt, {'mime_type': 'image/png', 'data': img}])
        print(response.text)
    except Exception as e:
        print(f"Error calling Gemini API: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
