import json
import argparse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_report(json_path, output_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title_style = ParagraphStyle(
        'ReportTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20
    )
    elements.append(Paragraph(f"Company Research: {data.get('company_name', 'Unknown')}", title_style))
    elements.append(Paragraph(f"Generated on: {data.get('report_date', 'N/A')}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Executive Summary
    elements.append(Paragraph("Executive Summary", styles['Heading2']))
    elements.append(Paragraph(data.get('executive_summary', ''), styles['Normal']))
    elements.append(Spacer(1, 12))

    # Profile
    elements.append(Paragraph("Company Profile", styles['Heading2']))
    profile = data.get('profile', {})
    profile_data = [[k.replace('_', ' ').title(), str(v)] for k, v in profile.items()]
    if profile_data:
        t = Table(profile_data, colWidths=[150, 300])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        elements.append(t)
    elements.append(Spacer(1, 12))

    # Products & Services
    elements.append(Paragraph("Products & Services", styles['Heading2']))
    products = data.get('products', {})
    for offering in products.get('offerings', []):
        elements.append(Paragraph(f"• {offering}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Competitors
    elements.append(Paragraph("Competitors", styles['Heading2']))
    for comp in data.get('competitors', []):
        elements.append(Paragraph(f"<b>{comp.get('name')}</b>", styles['Normal']))
        elements.append(Paragraph(f"Differentiation: {comp.get('differentiation')}", styles['Normal']))
        elements.append(Spacer(1, 6))

    doc.build(elements)
    print(f"Report generated: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate Company Research Report PDF")
    parser.add_argument("json_file", help="Path to research data JSON")
    parser.add_argument("output_pdf", help="Path to output PDF file")
    
    args = parser.parse_args()
    generate_report(args.json_file, args.output_pdf)

if __name__ == "__main__":
    main()
