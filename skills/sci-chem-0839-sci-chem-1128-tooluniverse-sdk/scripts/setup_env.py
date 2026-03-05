import os
import sys

def setup_env():
    """
    Set up environment variables for ToolUniverse SDK.
    """
    env_content = """# ToolUniverse Environment Configuration
export OPENAI_API_KEY="sk-..."
export NCBI_API_KEY="..."
# export DISGENET_API_KEY="..."
"""
    with open('.env.tooluniverse', 'w') as f:
        f.write(env_content)
    
    print("Created .env.tooluniverse template.")
    print("Please edit it with your API keys and run: source .env.tooluniverse")

if __name__ == "__main__":
    setup_env()
