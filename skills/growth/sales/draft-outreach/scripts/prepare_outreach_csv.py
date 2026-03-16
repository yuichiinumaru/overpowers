import csv
import os

def create_template(filename="outreach_template.csv"):
    headers = ["Name", "Title", "Company", "Email", "LinkedIn_URL", "Notes"]
    example_data = [
        ["John Smith", "CTO", "Acme Corp", "john@acme.com", "https://linkedin.com/in/johnsmith", "Met at AI conference"],
        ["Sarah Jones", "Head of Engineering", "Globex", "", "https://linkedin.com/in/sarahjones", "Scaling AI features"]
    ]
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(example_data)
    print(f"Template created: {filename}")

if __name__ == "__main__":
    create_template()
