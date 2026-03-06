import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      file: { type: 'string' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || (!values.file && positionals.length === 0)) {
    console.log(`
Usage: npx -y bun copy-to-clipboard.ts <text> | --file <file>

Options:
  --file <path>       File to copy from
  -h, --help          Show this help message
    `);
    return;
  }

  console.log(`Copy to clipboard placeholder`);
}

main().catch(console.error);
