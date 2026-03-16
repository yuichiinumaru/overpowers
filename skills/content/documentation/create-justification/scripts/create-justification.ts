import fs from 'fs';
import path from 'path';

// Words for generating 3-word ID
const adjs = ['swift', 'silent', 'bright', 'dark', 'cool', 'warm', 'brave', 'calm', 'wild', 'sharp'];
const colors = ['red', 'blue', 'green', 'amber', 'emerald', 'ruby', 'cyan', 'indigo', 'jade', 'gold'];
const nouns = ['river', 'mountain', 'forest', 'ocean', 'wind', 'fire', 'star', 'moon', 'sun', 'cloud'];

function generateId(): string {
  const adj = adjs[Math.floor(Math.random() * adjs.length)];
  const color = colors[Math.floor(Math.random() * colors.length)];
  const noun = nouns[Math.floor(Math.random() * nouns.length)];
  return `${adj}-${color}-${noun}`;
}

function formatTitle(slug: string): string {
  return slug
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function main() {
  const args = process.argv.slice(2);
  if (args.length < 2) {
    console.error('Usage: npx tsx scripts/create-justification.ts "slug-name" "content"');
    process.exit(1);
  }

  const slug = args[0];
  const content = args.slice(1).join(' '); // Join remaining args in case content wasn't quoted properly
  const date = new Date().toISOString().split('T')[0];
  const title = formatTitle(slug);
  const id = generateId();

  const filename = `${id}-${slug}.md`;
  const dirPath = path.join(process.cwd(), '.agents', 'justifications');
  const filePath = path.join(dirPath, filename);

  const fileContent = `---
date: ${date}
title: ${title}
---

${content}
`;

  // Create dir if not exists
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }

  fs.writeFileSync(filePath, fileContent, 'utf-8');
  console.log(`Created justification file: ${filePath}`);
}

main();
