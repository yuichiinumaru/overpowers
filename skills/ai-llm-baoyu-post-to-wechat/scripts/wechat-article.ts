import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      html: { type: 'string' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || !values.html) {
    console.log(`
Usage: npx -y bun wechat-article.ts --html <html_file>

Options:
  --html <path>       HTML file path
  -h, --help          Show this help message
    `);
    return;
  }

  console.log(`WeChat Article Browser posting placeholder for ${values.html}`);
}

main().catch(console.error);
