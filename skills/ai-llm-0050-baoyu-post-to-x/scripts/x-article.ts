import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      cover: { type: 'string' },
      title: { type: 'string' },
      submit: { type: 'boolean' },
      profile: { type: 'string' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: npx -y bun x-article.ts <markdown> [options]

Options:
  --cover <path>      Cover image
  --title <text>      Override title
  --submit            Submit the post
  --profile <dir>     Custom Chrome profile
  -h, --help          Show this help message
    `);
    return;
  }

  console.log(`X Article posting placeholder for markdown: ${positionals[0]}`);
}

main().catch(console.error);
