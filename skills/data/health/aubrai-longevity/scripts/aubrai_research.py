#!/usr/bin/env python3
import requests
import time
import argparse
import sys
import json

BASE_URL = "https://satisfied-light-production.up.railway.app/api/chat"

def submit_question(question, conversation_id=None):
    payload = {"message": question}
    if conversation_id:
        payload["conversationId"] = conversation_id
    
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 429:
        retry_after = int(response.headers.get("Retry-After", 60))
        print(f"Rate limited. Retrying after {retry_after} seconds...")
        time.sleep(retry_after)
        return submit_question(question, conversation_id)
    
    response.raise_for_status()
    return response.json()

def poll_job(job_id):
    while True:
        response = requests.get(f"{BASE_URL}/status/{job_id}")
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "completed":
            return data
        elif data.get("status") == "failed":
            raise Exception(f"Job failed: {data.get('error')}")
        
        print(f"Status: {data.get('status')}... waiting 5 seconds")
        time.sleep(5)

def main():
    parser = argparse.ArgumentParser(description="Aubrai Longevity Research Tool")
    parser.add_argument("question", help="The research question to ask")
    parser.add_argument("--conversation-id", help="Conversation ID for follow-up")
    args = parser.parse_args()

    try:
        print(f"Submitting question: {args.question}")
        initial_res = submit_question(args.question, args.conversation_id)
        job_id = initial_res.get("jobId")
        conv_id = initial_res.get("conversationId")
        
        print(f"Job ID: {job_id}")
        print(f"Conversation ID: {conv_id}")
        
        result = poll_job(job_id)
        print("\n--- Final Answer ---\n")
        print(result.get("result", {}).get("text", "No text returned"))
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
