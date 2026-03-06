import os
import requests
import json
import argparse
from dotenv import load_dotenv

def submit_experiment(sequences, experiment_type, webhook_url=None):
    load_dotenv()
    api_key = os.getenv("ADAPTYV_API_KEY")
    if not api_key:
        print("❌ Error: ADAPTYV_API_KEY not found in environment or .env file.")
        return None

    base_url = "https://kq5jp7qj7wdqklhsxmovkzn4l40obksv.lambda-url.eu-central-1.on.aws"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "sequences": sequences,
        "experiment_type": experiment_type
    }
    if webhook_url:
        payload["webhook_url"] = webhook_url

    print(f"🚀 Submitting {experiment_type} experiment to Adaptyv...")
    try:
        response = requests.post(f"{base_url}/experiments", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        print(f"✅ Experiment submitted successfully! ID: {result.get('experiment_id')}")
        return result
    except requests.exceptions.RequestException as e:
        print(f"❌ Submission failed: {e}")
        if response.text:
            print(f"Response: {response.text}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Submit experiment to Adaptyv.")
    parser.add_argument("--file", help="FASTA file with sequences")
    parser.add_argument("--type", default="binding", choices=["binding", "expression", "thermostability", "enzyme_activity"], help="Experiment type")
    parser.add_argument("--webhook", help="Optional webhook URL for results")
    
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, "r") as f:
            sequences = f.read()
        submit_experiment(sequences, args.type, args.webhook)
    else:
        print("Usage: python experiment_template.py --file <fasta_file> [--type <type>] [--webhook <url>]")

if __name__ == "__main__":
    main()
