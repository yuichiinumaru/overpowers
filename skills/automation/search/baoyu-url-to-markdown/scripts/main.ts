import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      output: { type: 'string', short: 'o' },
      wait: { type: 'boolean' },
      timeout: { type: 'string' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: npx -y bun main.ts <url> [options]

Options:
  -o, --output <path> Output file path
  --wait              Wait for user signal before capturing
  --timeout <ms>      Page load timeout (default: 30000)
  -h, --help          Show this help message
    `);
    return;
  }

  const url = positionals[0];
  console.log(`URL to Markdown placeholder for ${url}`);

  if (values.wait) {
    console.log('Wait mode: Press Enter when ready...');
    // Real implementation would wait for stdin
  }
}

main().catch(console.error);
