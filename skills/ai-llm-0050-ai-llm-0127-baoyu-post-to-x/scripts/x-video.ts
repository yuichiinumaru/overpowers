import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      video: { type: 'string' },
      submit: { type: 'boolean' },
      profile: { type: 'string' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || positionals.length === 0 || !values.video) {
    console.log(`
Usage: npx -y bun x-video.ts <text> --video <path> [options]

Options:
  --video <path>      Video file (MP4, MOV, WebM)
  --submit            Submit the post
  --profile <dir>     Custom Chrome profile
  -h, --help          Show this help message
    `);
    return;
  }

  console.log(`X Video posting placeholder for text: ${positionals[0]}, video: ${values.video}`);
}

main().catch(console.error);
