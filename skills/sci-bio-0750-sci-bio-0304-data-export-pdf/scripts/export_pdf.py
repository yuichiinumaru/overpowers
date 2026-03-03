from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from datetime import datetime
import pandas as pd
import argparse
import sys
import os

def create_report(title, content, csv_data, output_path):
    print(f"📄 Creating PDF report: {output_path}...")
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Title
    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))

    # Content
    if content:
        story.append(Paragraph(content, styles['Normal']))
        story.append(Spacer(1, 0.3*inch))

    # Table
    if csv_data and os.path.exists(csv_data):
        print(f"📊 Adding table from {csv_data}...")
        df = pd.read_csv(csv_data).head(20) # Limit to 20 rows
        data = [df.columns.tolist()] + df.values.tolist()
        
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
        ]))
        story.append(table)

    print("🏗️ Building PDF...")
    doc.build(story)
    print("✅ PDF saved.")

def main():
    parser = argparse.ArgumentParser(description="Create a simple PDF report.")
    parser.add_argument("--title", default="Analysis Report", help="Report title")
    parser.add_argument("--content", help="Report text content")
    parser.add_argument("--csv", help="Input CSV for a summary table")
    parser.add_argument("--output", default="report.pdf", help="Output PDF file")
    
    args = parser.parse_args()
    create_report(args.title, args.content, args.csv, args.output)

if __name__ == "__main__":
    main()
