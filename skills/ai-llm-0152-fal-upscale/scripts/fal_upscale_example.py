import os
import sys

def check_fal_key():
    key = os.getenv("FAL_KEY")
    if not key:
        print("❌ Error: FAL_KEY environment variable is not set.")
        return False
    print("✅ FAL_KEY is set.")
    return True

def upscale_example():
    if not check_fal_key():
        return
    
    print("Example Python snippet for fal.ai upscaling:")
    print("""
import fal_client

result = fal_client.subscribe(
    "fal-ai/aura-sr",
    arguments={
        "image_url": "https://example.com/image.jpg"
    },
)
print(result)
""")

if __name__ == "__main__":
    upscale_example()
