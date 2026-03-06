import fs from 'fs';
import path from 'path';

// Usage: npx tsx scripts/create-justification.ts "decision-name" "Justification content here"

function generateRandomThreeWordId(): string {
  const words1 = ["swift", "silent", "bold", "quick", "bright", "cool", "dark", "light"];
  const words2 = ["emerald", "sapphire", "ruby", "silver", "golden", "crystal", "iron"];
  const words3 = ["river", "mountain", "forest", "ocean", "sky", "wind", "storm"];

  const w1 = words1[Math.floor(Math.random() * words1.length)];
  const w2 = words2[Math.floor(Math.random() * words2.length)];
  const w3 = words3[Math.floor(Math.random() * words3.length)];

  return `${w1}-${w2}-${w3}`;
}

function formatTitle(slug: string): string {
  return slug
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function createJustification(slug: string, content: string) {
  const date = new Date().toISOString().split('T')[0];
  const id = generateRandomThreeWordId();
  const title = formatTitle(slug);
  const fileName = `${id}-${slug}.md`;

  // Find project root assuming this script is in skills/<skill>/scripts/
  const projectRoot = path.join(__dirname, '..', '..', '..');
  const targetDir = path.join(projectRoot, '.agents', 'justifications');

  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  const filePath = path.join(targetDir, fileName);

  const fileContent = `---
date: ${date}
title: ${title}
---

${content}
`;

  fs.writeFileSync(filePath, fileContent);
  console.log(`Successfully created justification: ${filePath}`);
}

const args = process.argv.slice(2);
if (args.length < 1) {
  console.error('Usage: npx tsx scripts/create-justification.ts <decision-name> [content]');
  process.exit(1);
}

const slug = args[0];
let content = args[1];

if (!content) {
    // Read from stdin if no content provided
    content = fs.readFileSync(0, 'utf-8').trim();
}

createJustification(slug, content);
