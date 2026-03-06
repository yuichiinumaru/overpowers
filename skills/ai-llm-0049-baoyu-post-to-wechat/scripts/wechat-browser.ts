import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      markdown: { type: 'string' },
      images: { type: 'string' },
      title: { type: 'string' },
      content: { type: 'string' },
      image: { type: 'string' },
      submit: { type: 'boolean' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help) {
    console.log(`
Usage: npx -y bun wechat-browser.ts [options]

Options:
  --markdown <path>   Markdown file path
  --images <path>     Directory with images
  --title <text>      Post title
  --content <text>    Post content
  --image <path>      Single image path
  --submit            Submit the post
  -h, --help          Show this help message
    `);
    return;
  }

  console.log('WeChat Browser posting placeholder');
}

main().catch(console.error);
