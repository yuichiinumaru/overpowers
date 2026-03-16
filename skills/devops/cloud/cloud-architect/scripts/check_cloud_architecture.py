#!/usr/bin/env python3
import argparse
import sys

def analyze_architecture(file_path):
    print(f"Analyzing cloud architecture defined in {file_path}...")
    try:
        with open(file_path, "r") as f:
            content = f.read().lower()

        components = {
            "compute": ["ec2", "lambda", "fargate", "gce", "cloud run", "aks", "eks"],
            "storage": ["s3", "ebs", "efs", "gcs", "blob storage"],
            "database": ["rds", "dynamodb", "aurora", "cloud sql", "firestore", "cosmos db"],
            "network": ["vpc", "alb", "nlb", "route53", "api gateway", "cdn", "cloudfront"]
        }

        found = {}
        for category, terms in components.items():
            found[category] = [term for term in terms if term in content]

        print("Architecture Components Found:")
        for category, terms in found.items():
            if terms:
                print(f"- {category.title()}: {', '.join(terms)}")
            else:
                print(f"- {category.title()}: None found (Consider adding)")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze cloud architecture definitions")
    parser.add_argument("file", help="Architecture document to analyze")

    args = parser.parse_args()
    analyze_architecture(args.file)
