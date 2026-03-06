#!/usr/bin/env python3
import os
import sys
import aiohttp
import asyncio

async def check_env():
    required_vars = ["AZURE_SPEECH_REGION", "AZURE_SPEECH_KEY"]
    missing = [var for var in required_vars if not os.environ.get(var)]

    if missing:
        print(f"❌ Missing required environment variables: {', '.join(missing)}")
        print("Please set them before running the script.")
        sys.exit(1)

    print("✅ All required environment variables are set.")

    region = os.environ["AZURE_SPEECH_REGION"]
    api_key = os.environ["AZURE_SPEECH_KEY"]
    endpoint = f"https://{region}.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint, headers=headers) as response:
                if response.status == 200:
                    print("✅ Successfully authenticated with Azure Speech Services API.")
                else:
                    error_text = await response.text()
                    print(f"❌ Failed to authenticate with Azure Speech Services API: {response.status} {error_text}")
                    sys.exit(1)

    except Exception as e:
        print(f"❌ Failed to connect to Azure Speech Services API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        import aiohttp
    except ImportError:
        print("❌ aiohttp package is not installed.")
        print("Run: pip install aiohttp")
        sys.exit(1)
    asyncio.run(check_env())
