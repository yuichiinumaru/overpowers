import os
import argparse

TEMPLATE = """import * as React from "react";
import {{
  Html,
  Head,
  Preview,
  Body,
  Container,
  Heading,
  Text,
  Button,
  Tailwind,
  pixelBasedPreset
}} from '@react-email/components';

interface {name}EmailProps {{
  {props}
}}

export default function {name}Email({{ {prop_names} }}: {name}EmailProps) {{
  return (
    <Html lang="en">
      <Tailwind
        config={{{{
          presets: [pixelBasedPreset],
          theme: {{
            extend: {{
              colors: {{
                brand: '{primary_color}',
              }},
            }},
          }},
        }}}}
      >
        <Head />
        <Preview>{preview_text}</Preview>
        <Body className="bg-gray-100 font-sans">
          <Container className="max-w-xl mx-auto p-5">
            <Heading className="text-2xl text-gray-800">
              {title}
            </Heading>
            <Text className="text-base text-gray-800">
              Hello, this is your {name} email.
            </Text>
            <Button
              href="#"
              className="bg-brand text-white px-5 py-3 rounded block text-center no-underline"
            >
              Action Button
            </Button>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
}}

{name}Email.PreviewProps = {{
  {preview_props}
}} satisfies {name}EmailProps;
"""

def main():
    parser = argparse.ArgumentParser(description="React Email Template Scaffolder")
    parser.add_argument("name", help="Template name (e.g. Welcome)")
    parser.add_argument("--primary", default="#007bff", help="Primary brand color")
    parser.add_argument("--dir", default="emails", help="Output directory")
    
    args = parser.parse_args()
    
    os.makedirs(args.dir, exist_ok=True)
    
    file_content = TEMPLATE.format(
        name=args.name,
        props="name: string;",
        prop_names="name",
        primary_color=args.primary,
        preview_text=f"{args.name} Email",
        title=args.name,
        preview_props="name: 'John Doe'"
    )
    
    file_path = os.path.join(args.dir, f"{args.name.lower()}.tsx")
    with open(file_path, 'w') as f:
        f.write(file_content)
        
    print(f"Scaffolded {file_path}")

if __name__ == "__main__":
    main()
