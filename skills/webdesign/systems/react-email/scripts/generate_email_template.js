#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
if (args.length < 2) {
    console.error('Usage: node generate_email_template.js <ComponentName> <OutputPath>');
    process.exit(1);
}

const componentName = args[0];
const outputPath = args[1];

const template = `import * as React from "react";
import {
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
} from '@react-email/components';

interface ${componentName}Props {
  name: string;
}

export default function ${componentName}({ name }: ${componentName}Props) {
  return (
    <Html lang="en">
      <Tailwind
        config={{
          presets: [pixelBasedPreset],
          theme: {
            extend: {
              colors: {
                brand: '#007bff',
              },
            },
          },
        }}
      >
        <Head />
        <Preview>Preview Text Here</Preview>
        <Body className="bg-gray-100 font-sans">
          <Container className="max-w-xl mx-auto p-5">
            <Heading className="text-2xl text-gray-800">
              Welcome!
            </Heading>
            <Text className="text-base text-gray-800">
              Hi {name}, this is a generated template!
            </Text>
            <Button
              href="https://example.com"
              className="bg-brand text-white px-5 py-3 rounded block text-center no-underline"
            >
              Action Required
            </Button>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
}

${componentName}.PreviewProps = {
  name: 'John Doe',
} satisfies ${componentName}Props;

export { ${componentName} };
`;

const destFile = path.join(outputPath, `${componentName}.tsx`);
fs.writeFileSync(destFile, template, 'utf8');
console.log(`Generated ${destFile}`);
