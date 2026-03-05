import sys
import os
import json

def generate_curl_command(input_file, action, output_file, extra_options=None):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    instructions = {"parts": [{"file": input_file}]}
    
    if action == "convert":
        if not extra_options:
            ext = os.path.splitext(output_file)[1].lower().replace('.', '')
            instructions["output"] = {"type": ext}
        else:
            instructions["output"] = {"type": extra_options}
    elif action == "ocr":
        lang = extra_options if extra_options else "english"
        instructions["actions"] = [{"type": "ocr", "language": lang}]
    elif action == "redact":
        preset = extra_options if extra_options else "social-security-number"
        instructions["actions"] = [{
            "type": "redaction", 
            "strategy": "preset", 
            "strategyOptions": {"preset": preset}
        }]
    elif action == "watermark":
        text = extra_options if extra_options else "CONFIDENTIAL"
        instructions["actions"] = [{
            "type": "watermark",
            "text": text,
            "fontSize": 72,
            "opacity": 0.3,
            "rotation": -45
        }]
    elif action == "extract_text":
        instructions["output"] = {"type": "text"}
    elif action == "extract_tables":
        instructions["output"] = {"type": "xlsx"}
    else:
        print(f"Unknown action: {action}")
        return

    instructions_json = json.dumps(instructions)
    
    curl_cmd = f"""curl -X POST https://api.nutrient.io/build \\
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \\
  -F "{input_file}=@{input_file}" \\
  -F 'instructions={instructions_json}' \\
  -o {output_file}"""

    print("--- Nutrient DWS API Command ---")
    print("Ensure NUTRIENT_API_KEY is set in your environment.")
    print(curl_cmd)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python nutrient_api_helper.py <input_file> <action> <output_file> [extra_options]")
        print("Actions: convert, ocr, redact, watermark, extract_text, extract_tables")
    else:
        input_f = sys.argv[1]
        act = sys.argv[2]
        output_f = sys.argv[3]
        extra = sys.argv[4] if len(sys.argv) > 4 else None
        generate_curl_command(input_f, act, output_f, extra)
