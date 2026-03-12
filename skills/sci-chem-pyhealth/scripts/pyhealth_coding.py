from pyhealth.medcode import InnerMap, CrossMap
import sys

def translate_code(code, source_system, target_db):
    """Translate a medical code from one system to another"""
    print(f"Translating {code} from {source_system} to {target_db}...")
    cm = CrossMap(source_system, target_db)
    result = cm.map(code)
    return result

def get_code_info(code, system):
    """Get metadata for a medical code within its system"""
    print(f"Retrieving info for {code} in {system}...")
    im = InnerMap(system)
    try:
        name = im.lookup(code)
        return {"code": code, "name": name}
    except Exception:
        return {"code": code, "error": "Not found"}

if __name__ == "__main__":
    # Example: Translate ICD-9 to ICD-10
    code = sys.argv[1] if len(sys.argv) > 1 else "428.0" # Heart failure
    try:
        info = get_code_info(code, "ICD9CM")
        print(f"ICD-9 Info: {info}")
        
        translated = translate_code(code, "ICD9CM", "ICD10CM")
        print(f"ICD-10 Translation: {translated}")
    except Exception as e:
        print(f"Error: {e}")
