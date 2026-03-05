import os
import sys
import argparse
from pathlib import Path

try:
    from azure.ai.contentunderstanding import ContentUnderstandingClient
    from azure.ai.contentunderstanding.models import AnalyzeInput
    from azure.identity import DefaultAzureCredential
except ImportError:
    print("Error: azure-ai-contentunderstanding or azure-identity not installed.")
    sys.exit(1)

def analyze(analyzer_id, source_url):
    endpoint = os.environ.get("CONTENTUNDERSTANDING_ENDPOINT")
    if not endpoint:
        print("Error: CONTENTUNDERSTANDING_ENDPOINT environment variable is not set.")
        return None

    try:
        credential = DefaultAzureCredential()
        client = ContentUnderstandingClient(endpoint=endpoint, credential=credential)

        print(f"Starting analysis with {analyzer_id} for {source_url}...")
        poller = client.begin_analyze(
            analyzer_id=analyzer_id,
            inputs=[AnalyzeInput(url=source_url)]
        )

        result = poller.result()
        return result
    except Exception as e:
        print(f"Error during analysis: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Azure AI Content Understanding CLI')
    parser.add_argument('--type', choices=['document', 'image', 'audio', 'video'], required=True)
    parser.add_argument('--url', required=True, help='Source URL to analyze')
    
    args = parser.parse_args()
    
    analyzer_map = {
        'document': 'prebuilt-documentSearch',
        'image': 'prebuilt-imageSearch',
        'audio': 'prebuilt-audioSearch',
        'video': 'prebuilt-videoSearch'
    }
    
    analyzer_id = analyzer_map[args.type]
    result = analyze(analyzer_id, args.url)
    
    if result and result.contents:
        content = result.contents[0]
        print("\n--- Analysis Result ---")
        if hasattr(content, 'markdown'):
            print(content.markdown)
        else:
            print("No markdown content available.")
            
        if args.type in ['audio', 'video'] and hasattr(content, 'transcript_phrases'):
            print("\n--- Transcript ---")
            for phrase in content.transcript_phrases:
                print(f"[{phrase.start_time}] {phrase.text}")

if __name__ == "__main__":
    main()
