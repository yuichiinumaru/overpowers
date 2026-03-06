#!/usr/bin/env python3
import os
import sys

def check_env():
    required_vars = ["AZURE_DOCUMENT_TRANSLATION_ENDPOINT", "AZURE_DOCUMENT_TRANSLATION_KEY", "AZURE_SOURCE_CONTAINER_URL", "AZURE_TARGET_CONTAINER_URL"]
    missing = [var for var in required_vars if not os.environ.get(var)]

    if missing:
        print(f"❌ Missing required environment variables: {', '.join(missing)}")
        print("Please set them before running the script.")
        sys.exit(1)

    print("✅ All required environment variables are set.")

    try:
        from azure.ai.translation.document import DocumentTranslationClient
        from azure.core.credentials import AzureKeyCredential

        endpoint = os.environ["AZURE_DOCUMENT_TRANSLATION_ENDPOINT"]
        key = os.environ["AZURE_DOCUMENT_TRANSLATION_KEY"]

        client = DocumentTranslationClient(endpoint, AzureKeyCredential(key))
        formats = client.get_supported_document_formats()
        print("✅ Successfully connected to Azure Document Translation API.")
        print(f"Supported formats: {len(list(formats))}")

    except ImportError:
        print("❌ azure-ai-translation-document package is not installed.")
        print("Run: pip install azure-ai-translation-document")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Failed to connect to Azure Document Translation API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_env()
