import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      title: { type: 'string' },
      summary: { type: 'string' },
      author: { type: 'string' },
      cover: { type: 'string' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0) {
    console.log(`
Usage: npx -y bun wechat-api.ts <html_file> [options]

Options:
  --title <text>      Article title
  --summary <text>    Article summary
  --author <name>     Author name
  --cover <path>      Cover image path
  -h, --help          Show this help message
    `);
    return;
  }

  console.log(`WeChat API posting placeholder for ${positionals[0]}`);
}

main().catch(console.error);
