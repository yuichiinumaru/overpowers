import argparse
import urllib.parse

def generate_meme_url(template, top, bottom, extension="png"):
    # Encode text for URL
    def encode_text(text):
        return urllib.parse.quote(text.replace(" ", "_").replace("?", "~q").replace("/", "~s"))

    top_encoded = encode_text(top)
    bottom_encoded = encode_text(bottom)
    
    return f"https://api.memegen.link/images/{template}/{top_encoded}/{bottom_encoded}.{extension}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate meme URL via memegen.link.")
    parser.add_argument("template", help="Meme template (e.g., buzz, drake, success)")
    parser.add_argument("top", help="Top text")
    parser.add_argument("bottom", help="Bottom text")
    parser.add_argument("--ext", default="png", choices=["png", "jpg", "webp", "gif"], help="File extension")
    
    args = parser.parse_args()
    
    url = generate_meme_url(args.template, args.top, args.bottom, args.ext)
    print(f"Generated Meme URL: {url}")
