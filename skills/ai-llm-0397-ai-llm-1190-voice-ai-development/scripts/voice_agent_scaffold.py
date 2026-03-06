#!/usr/bin/env python3
"""
Scaffold Voice AI application templates
"""
import sys
import os

def generate_vapi_template():
    return """
from flask import Flask, request, jsonify
import vapi

app = Flask(__name__)
client = vapi.Vapi(api_key="YOUR_KEY")

assistant = client.assistants.create(
    name="Support Agent",
    model={
        "provider": "openai",
        "model": "gpt-4o",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}]
    },
    voice={"provider": "11labs", "voiceId": "21m00Tcm4TlvDq8ikWAM"}
)

@app.route("/vapi/webhook", methods=["POST"])
def webhook():
    return jsonify({"ok": True})
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python voice_agent_scaffold.py <vapi|openai|deepgram>")
        sys.exit(1)

    template_type = sys.argv[1]
    filename = f"{template_type}_agent.py"

    if template_type == "vapi":
        with open(filename, "w") as f:
            f.write(generate_vapi_template().strip())
        print(f"Generated {filename}")
    else:
        print(f"Template type {template_type} not supported yet.")

if __name__ == "__main__":
    main()
