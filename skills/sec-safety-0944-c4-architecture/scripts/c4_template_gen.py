#!/usr/bin/env python3
import sys

TEMPLATES = {
    "context": """mermaid
C4Context
  title System Context - [System Name]

  Person(user, "User", "[Description]")
  System(app, "[System Name]", "[Description]")
  System_Ext(ext, "[External System]", "[Description]")

  Rel(user, app, "Uses")
  Rel(app, ext, "Connects to")
""",
    "container": """mermaid
C4Container
  title Container Diagram - [System Name]

  Person(user, "User", "[Description]")

  Container_Boundary(app, "[System Name]") {
    Container(web, "Web App", "[Tech]", "[Description]")
    Container(api, "API", "[Tech]", "[Description]")
    ContainerDb(db, "Database", "[Tech]", "[Description]")
  }

  Rel(user, web, "Uses")
  Rel(web, api, "Calls")
  Rel(api, db, "Reads/Writes")
"""
}

def main():
    if len(sys.argv) < 2:
        print("Usage: c4_template_gen.py [context|container]")
        sys.exit(1)
        
    level = sys.argv[1]
    if level in TEMPLATES:
        print(TEMPLATES[level])
    else:
        print(f"Unknown level: {level}")

if __name__ == "__main__":
    main()
