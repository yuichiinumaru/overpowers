import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: npx -y bun md-to-html.ts <markdown_file> [options]

Options:
  -h, --help          Show this help message
    `);
    return;
  }

  console.log(`X Article Markdown to HTML placeholder for ${positionals[0]}`);
}

main().catch(console.error);
