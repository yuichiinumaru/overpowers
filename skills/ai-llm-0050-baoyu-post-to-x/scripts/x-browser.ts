import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      image: { type: 'string', multiple: true },
      submit: { type: 'boolean' },
      profile: { type: 'string' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: npx -y bun x-browser.ts <text> [options]

Options:
  --image <path>      Image file (repeatable, max 4)
  --submit            Submit the post
  --profile <dir>     Custom Chrome profile
  -h, --help          Show this help message
    `);
    return;
  }

  console.log(`X Browser posting placeholder for text: ${positionals[0]}`);
}

main().catch(console.error);
