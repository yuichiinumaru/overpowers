#!/usr/bin/env python3
import sys

def generate_blueprint(name):
    template = f"""# Vibe Coding Blueprint: {name}

## 1. System Architecture
- Purpose:
- Tech Stack:
- Data Models:

## 2. API Contracts
- Endpoints:
- Authentication:

## 3. Agent Orchestration
- Architect Agent: Design schema and OpenAPI specs
- Backend Agent: Implement FastAPI endpoints
- Frontend Agent: Build UI components
- Testing Agent: Generate Pytest suite

## 4. Constraints
- Performance:
- Security:
- Style Guide:
"""
    filename = f"{name.lower().replace(' ', '_')}_blueprint.md"
    with open(filename, 'w') as f:
        f.write(template)
    print(f"Blueprint generated: {filename}")

if __name__ == "__main__":
    service_name = sys.argv[1] if len(sys.argv) > 1 else "New Service"
    generate_blueprint(service_name)
