#!/usr/bin/env python3
import sys
import os

def init_api_design(title):
    template = f"""# API Design Specification: {title}

## 1. Overview
[Context and purpose of the API]

## 2. Resource Mapping
- Resource: [Name]
- Base Path: `/api/v1/[resource]`

## 3. Endpoints
### GET `/api/v1/[resource]`
- Purpose: [List items]
- Auth Required: [Yes/No]
- Query Params: [page, limit, filter]

### POST `/api/v1/[resource]`
- Purpose: [Create item]
- Request Body: [JSON schema]

## 4. Error Handling
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 500: Internal Server Error

## 5. Versioning Strategy
- [Header-based or Path-based]
"""
    with open("api-design.md", "w") as f:
        f.write(template)
    print("Initialized api-design.md")

if __name__ == "__main__":
    title = sys.argv[1] if len(sys.argv) > 1 else "My API"
    init_api_design(title)
