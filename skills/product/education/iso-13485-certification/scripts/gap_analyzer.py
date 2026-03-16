import os
import argparse
import json

def analyze_gaps(docs_dir, output_file):
    # Mandatory procedures per ISO 13485 (simplified list for analysis)
    mandatory_procedures = [
        "Risk Management", "Software Validation", "Control of Documents", "Control of Records",
        "Internal Communication", "Management Review", "Human Resources", "Infrastructure Maintenance",
        "Contamination Control", "Customer Communication", "Design and Development", "Purchasing",
        "Verification of Purchased Product", "Production Control", "Product Cleanliness", "Installation",
        "Servicing", "Process Validation", "Sterilization Validation", "Product Identification",
        "Traceability", "Customer Property", "Preservation of Product", "Control of M&M Equipment",
        "Feedback", "Complaint Handling", "Regulatory Reporting", "Internal Audit",
        "Process Monitoring", "Product Monitoring", "Control of Nonconforming Product",
        "Corrective Action", "Preventive Action"
    ]
    
    findings = {
        "present": [],
        "missing": [],
        "compliance_percentage": 0
    }
    
    if not os.path.exists(docs_dir):
        print(f"Error: Directory {docs_dir} not found")
        return
        
    # Get all text from documents in directory
    doc_content = ""
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.lower().endswith(('.txt', '.md', '.doc', '.docx', '.pdf')):
                # In a real scenario, this would use proper parsers for PDF/DOCX
                # Here we just check filenames and a mock content search
                doc_content += file + " "
                
    for proc in mandatory_procedures:
        # Simple keyword matching for demo purposes
        if proc.lower() in doc_content.lower():
            findings["present"].append(proc)
        else:
            findings["missing"].append(proc)
            
    total = len(mandatory_procedures)
    findings["compliance_percentage"] = (len(findings["present"]) / total) * 100
    
    with open(output_file, 'w') as f:
        json.dump(findings, f, indent=2)
        
    print(f"✅ Gap analysis complete. Results saved to {output_file}")
    print(f"Summary: {len(findings['present'])} present, {len(findings['missing'])} missing.")
    print(f"Compliance: {findings['compliance_percentage']:.2f}%")

def main():
    parser = argparse.ArgumentParser(description='ISO 13485 QMS Gap Analyzer')
    parser.add_argument('--docs-dir', required=True, help='Directory of current QMS documents')
    parser.add_argument('--output', default='gap-report.json', help='Output JSON file for results')
    
    args = parser.parse_args()
    analyze_gaps(args.docs_dir, args.output)

if __name__ == "__main__":
    main()
