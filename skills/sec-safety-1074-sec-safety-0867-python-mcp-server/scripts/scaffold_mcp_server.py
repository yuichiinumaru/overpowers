#!/usr/bin/env python3
import os
import sys
import argparse

TEMPLATE = """#!/usr/bin/env python3
'''
MCP Server for {service_name}.
'''

from typing import Optional, List, Dict, Any
from enum import Enum
import httpx
import json
from pydantic import BaseModel, Field, field_validator, ConfigDict
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("{service_name}_mcp")

# Constants
# API_BASE_URL = "https://api.example.com/v1"

# Enums
class ResponseFormat(str, Enum):
    '''Output format for tool responses.'''
    MARKDOWN = "markdown"
    JSON = "json"

# Pydantic Models for Input Validation
class SampleInput(BaseModel):
    '''Input model for sample operations.'''
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True
    )

    query: str = Field(..., description="Search string", min_length=2)
    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN, description="Output format")

# Tool definitions
@mcp.tool(
    name="{service_name}_sample_tool",
    annotations={{
        "title": "Sample Tool",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }}
)
async def sample_tool(params: SampleInput) -> str:
    '''Sample tool description.
    
    Args:
        params (SampleInput): Validated input parameters
        
    Returns:
        str: Formatted response
    '''
    return f"You searched for: {{params.query}} in {{params.response_format}} format"

if __name__ == "__main__":
    mcp.run()
"""

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Python MCP server.")
    parser.get_current_config = parser.add_argument("name", help="Service name (e.g., github, jira)")
    parser.add_argument("-o", "--output", help="Output file path", default=None)
    
    args = parser.parse_args()
    service_name = args.name.lower().replace("-", "_")
    output_path = args.output or f"{service_name}_mcp.py"
    
    content = TEMPLATE.format(service_name=service_name)
    
    with open(output_path, "w") as f:
        f.write(content)
    
    print(f"✅ Scaffolded MCP server: {output_path}")
    print(f"Next steps:")
    print(f"1. Install dependencies: pip install mcp[fastmcp] httpx pydantic")
    print(f"2. Run the server: python {output_path}")

if __name__ == "__main__":
    main()
