#!/usr/bin/env python3
import sys
import json
import PyPDF2

def extract_form_field_info(input_pdf, output_json):
    try:
        with open(input_pdf, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            fields = reader.get_fields()

            field_info = []
            if fields:
                for k, v in fields.items():
                    field_info.append({
                        "field_id": k,
                        "type": str(v.get('/FT', '')),
                        # Extract more data as needed per the skill doc
                    })

            with open(output_json, 'w') as out_f:
                json.dump(field_info, out_f, indent=2)
            print(f"Extracted info saved to {output_json}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_form_field_info.py <input.pdf> <field_info.json>")
        sys.exit(1)
    extract_form_field_info(sys.argv[1], sys.argv[2])
