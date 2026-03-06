#!/usr/bin/env python3
import json
import time
import urllib.request
import urllib.error
import argparse
import sys

API_URL_CHAT = "https://satisfied-light-production.up.railway.app/api/chat"
API_URL_STATUS = "https://satisfied-light-production.up.railway.app/api/chat/status/{}"

def submit_question(message, conversation_id=None):
    data = {"message": message}
    if conversation_id:
        data["conversationId"] = conversation_id

    req = urllib.request.Request(API_URL_CHAT, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'}, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print("Rate limit exceeded. Waiting 60 seconds...", file=sys.stderr)
            time.sleep(60)
            return submit_question(message, conversation_id)
        else:
            print(f"Error submitting question: {e.code} {e.reason}", file=sys.stderr)
            print(e.read().decode(), file=sys.stderr)
            sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}", file=sys.stderr)
        sys.exit(1)

def poll_status(job_id):
    url = API_URL_STATUS.format(job_id)
    req = urllib.request.Request(url)

    while True:
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode())
                if result.get("status") == "completed":
                    return result
                print("Status: {}, waiting...".format(result.get("status")), file=sys.stderr)
                time.sleep(5)
        except urllib.error.HTTPError as e:
            print(f"Error polling status: {e.code} {e.reason}", file=sys.stderr)
            sys.exit(1)
        except urllib.error.URLError as e:
            print(f"Connection error: {e.reason}", file=sys.stderr)
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Query Aubrai's longevity research engine.")
    parser.add_argument("message", help="The question to ask")
    parser.add_argument("--conversation-id", "-c", help="Conversation ID for follow-up questions")
    parser.add_argument("--output", "-o", choices=["text", "json"], default="text", help="Output format")
    args = parser.parse_args()

    print("Submitting question...", file=sys.stderr)
    submit_result = submit_question(args.message, args.conversation_id)

    job_id = submit_result.get("jobId")
    conv_id = submit_result.get("conversationId")

    if not job_id:
        print("Failed to get job ID", file=sys.stderr)
        print(json.dumps(submit_result, indent=2), file=sys.stderr)
        sys.exit(1)

    print(f"Job ID: {job_id}", file=sys.stderr)
    print(f"Conversation ID: {conv_id}", file=sys.stderr)
    print("Polling for completion...", file=sys.stderr)

    final_result = poll_status(job_id)

    if args.output == "json":
        print(json.dumps(final_result, indent=2))
    else:
        text = final_result.get("result", {}).get("text", "")
        if text:
            print(f"\n{text}")
        else:
            print("\nNo text returned in result.")
            print(json.dumps(final_result, indent=2))

if __name__ == "__main__":
    main()
