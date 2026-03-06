import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      submit: { type: 'boolean' },
      profile: { type: 'string' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: npx -y bun x-quote.ts <tweet-url> [<comment>] [options]

Options:
  --submit            Submit the post
  --profile <dir>     Custom Chrome profile
  -h, --help          Show this help message
    `);
    return;
  }

  console.log(`X Quote posting placeholder for URL: ${positionals[0]}, comment: ${positionals[1] || ''}`);
}

main().catch(console.error);
