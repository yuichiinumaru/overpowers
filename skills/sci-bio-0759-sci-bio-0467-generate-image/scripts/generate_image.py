import os
import sys
import json
import base64
import argparse
import requests
from pathlib import Path

def load_env():
    env_path = Path('.env')
    if not env_path.exists():
        # Try parent directory
        env_path = Path('../.env')
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    if key == 'OPENROUTER_API_KEY':
                        os.environ[key] = val.strip('"\'')

def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def generate_image(prompt, input_image=None, model="google/gemini-3-pro-image-preview", output_path="generated_image.png", api_key=None):
    if not api_key:
        api_key = os.environ.get("OPENROUTER_API_KEY")
    
    if not api_key:
        print("Error: OPENROUTER_API_KEY not found in environment or .env file.")
        print("Get an API key from https://openrouter.ai/keys and add it to your .env file:")
        print("OPENROUTER_API_KEY=your-api-key-here")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/overpowers",
        "X-Title": "Overpowers Image Generator",
        "Content-Type": "application/json"
    }

    if input_image:
        print(f"Editing image {input_image} with model {model}...")
        base64_image = encode_image(input_image)
        ext = Path(input_image).suffix.lower().replace('.', '')
        if ext == 'jpg': ext = 'jpeg'
        
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/{ext};base64,{base64_image}"
                        }
                    }
                ]
            }
        ]
    else:
        print(f"Generating new image with model {model}...")
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

    data = {
        "model": model,
        "messages": messages
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        
        # OpenRouter might return standard chat format or specific image format
        content = result['choices'][0]['message'].get('content', '')
        
        # Try to extract base64 from content (often markdown wrapped or raw data URI)
        if 'data:image/' in content:
            b64_data = content.split('base64,')[1].split(')')[0].split('"')[0].strip()
            image_data = base64.b64decode(b64_data)
            with open(output_path, 'wb') as f:
                f.write(image_data)
            print(f"✅ Image saved to {output_path}")
        else:
            print("Response did not contain expected image format. Raw response:")
            print(content[:500] + "..." if len(content) > 500 else content)
            
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Details: {e.response.text}")
    except Exception as e:
        print(f"Error processing response: {e}")

def main():
    load_env()
    
    parser = argparse.ArgumentParser(description="Generate or edit images via OpenRouter")
    parser.add_argument("prompt", help="Text description of the image or edit instructions")
    parser.add_argument("-i", "--input", help="Input image path for editing")
    parser.add_argument("-m", "--model", default="google/gemini-3-pro-image-preview", help="OpenRouter model ID")
    parser.add_argument("-o", "--output", default="generated_image.png", help="Output file path")
    parser.add_argument("--api-key", help="OpenRouter API key (overrides .env)")
    
    args = parser.parse_args()
    
    generate_image(args.prompt, args.input, args.model, args.output, args.api_key)

if __name__ == "__main__":
    main()
