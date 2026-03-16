import json
import sys

def validate_excalidraw(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        required_fields = ["type", "version", "elements", "appState"]
        missing = [field for field in required_fields if field not in data]
        
        if missing:
            print(f"❌ Invalid Excalidraw file. Missing fields: {', '.join(missing)}")
            return False
        
        if data["type"] != "excalidraw":
            print(f"❌ Invalid type: {data['type']}. Expected 'excalidraw'")
            return False
            
        print("✅ Valid Excalidraw JSON structure.")
        return True
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_excalidraw.py <file.excalidraw>")
        sys.exit(1)
    validate_excalidraw(sys.argv[1])
