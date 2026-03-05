import xml.etree.ElementTree as ET
import pandas as pd
import os

def parse_hmdb_xml(xml_file, limit=100):
    """
    Basic parser for HMDB metabolite XML.
    Note: HMDB XML files can be very large (GBs).
    """
    print(f"Parsing {xml_file} (limit: {limit})...")
    
    # Use iterparse for memory efficiency if possible
    context = ET.iterparse(xml_file, events=('end',))
    metabolites = []
    
    count = 0
    for event, elem in context:
        if elem.tag.endswith('metabolite'):
            metabolite = {}
            # Basic fields (namespace handling might be needed depending on file)
            for child in elem:
                tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
                if tag in ['accession', 'name', 'chemical_formula', 'monisotopic_molecular_weight', 'smiles', 'inchi']:
                    metabolite[tag] = child.text
            
            metabolites.append(metabolite)
            count += 1
            
            # Clean up element to save memory
            elem.clear()
            
            if count >= limit:
                break
                
    return pd.DataFrame(metabolites)

def load_hmdb_csv(csv_file):
    """Load HMDB CSV export"""
    return pd.read_csv(csv_file)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if file_path.endswith('.xml'):
            df = parse_hmdb_xml(file_path)
            print(df.head())
        elif file_path.endswith('.csv'):
            df = load_hmdb_csv(file_path)
            print(df.head())
    else:
        print("Usage: python hmdb_parser.py <path_to_hmdb_file>")
