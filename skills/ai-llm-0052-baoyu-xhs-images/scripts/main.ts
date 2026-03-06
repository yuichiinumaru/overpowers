import { parseArgs } from 'node:util';

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help) {
    console.log(`
Usage: npx -y bun main.ts [options]

Options:
  -h, --help          Show this help message
    `);
    return;
  }

  console.log('XHS Images placeholder');
}

main().catch(console.error);
