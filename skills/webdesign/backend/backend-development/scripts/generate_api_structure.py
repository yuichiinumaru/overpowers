#!/usr/bin/env python3
"""
API Structure Generator
Creates a basic boilerplate structure for a REST API based on resource names.
"""
import sys
import argparse
import os

def generate_api_structure(resources, output_dir="api_app"):
    """
    Generate basic directory structure for API resources.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for resource in resources:
        resource_dir = os.path.join(output_dir, resource)
        if not os.path.exists(resource_dir):
            os.makedirs(resource_dir)

        # Create standard files
        with open(os.path.join(resource_dir, '__init__.py'), 'w') as f:
            pass

        with open(os.path.join(resource_dir, 'models.py'), 'w') as f:
            f.write(f"# Models for {resource}\n")

        with open(os.path.join(resource_dir, 'routes.py'), 'w') as f:
            f.write(f"# API Routes for {resource}\n")

        with open(os.path.join(resource_dir, 'schemas.py'), 'w') as f:
            f.write(f"# Pydantic Schemas for {resource}\n")

        with open(os.path.join(resource_dir, 'services.py'), 'w') as f:
            f.write(f"# Business Logic for {resource}\n")

    # Main app file
    with open(os.path.join(output_dir, 'main.py'), 'w') as f:
        f.write("# Main API Application Entrypoint\n")
        f.write("from fastapi import FastAPI\n\n")
        f.write("app = FastAPI()\n")

    print(f"Generated API structure in '{output_dir}/'")

def main():
    parser = argparse.ArgumentParser(description="API Structure Generator")
    parser.add_argument("resources", nargs="+", help="List of resources to generate (e.g. users products orders)")
    parser.add_argument("--output", type=str, default="api_app", help="Output directory (default: api_app)")

    args = parser.parse_args()

    generate_api_structure(args.resources, args.output)

if __name__ == "__main__":
    main()
