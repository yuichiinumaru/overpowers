#!/usr/bin/env python3
import os
import sys

def check_env():
    required_vars = ["AZURE_TEXT_TRANSLATION_ENDPOINT", "AZURE_TEXT_TRANSLATION_KEY", "AZURE_TEXT_TRANSLATION_REGION"]
    missing = [var for var in required_vars if not os.environ.get(var)]

    if missing:
        print(f"❌ Missing required environment variables: {', '.join(missing)}")
        print("Please set them before running the script.")
        sys.exit(1)

    print("✅ All required environment variables are set.")

    try:
        from azure.ai.translation.text import TextTranslationClient
        from azure.core.credentials import AzureKeyCredential

        endpoint = os.environ["AZURE_TEXT_TRANSLATION_ENDPOINT"]
        key = os.environ["AZURE_TEXT_TRANSLATION_KEY"]
        region = os.environ["AZURE_TEXT_TRANSLATION_REGION"]

        client = TextTranslationClient(endpoint=endpoint, credential=AzureKeyCredential(key), region=region)
        languages = client.get_languages()
        print("✅ Successfully connected to Azure Text Translation API.")
        print(f"Supported languages: {len(list(languages))}")

    except ImportError:
        print("❌ azure-ai-translation-text package is not installed.")
        print("Run: pip install azure-ai-translation-text")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Failed to connect to Azure Text Translation API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_env()
