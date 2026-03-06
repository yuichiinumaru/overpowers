import os
import sys

def check_fal_key():
    key = os.getenv("FAL_KEY")
    if not key:
        print("❌ Error: FAL_KEY environment variable is not set.")
        return False
    print("✅ FAL_KEY is set.")
    return True

def generate_example():
    if not check_fal_key():
        return
    
    print("Example Python snippet for fal.ai generation:")
    print("""
import fal_client

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(log["message"])

result = fal_client.subscribe(
    "fal-ai/flux/schnell",
    arguments={
        "prompt": "A beautiful landscape"
    },
    with_logs=True,
    on_queue_update=on_queue_update,
)
print(result)
""")

if __name__ == "__main__":
    generate_example()
