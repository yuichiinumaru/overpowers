import { renderMermaid } from 'beautiful-mermaid';
import { readFileSync, writeFileSync } from 'fs';
import { parseArgs } from 'util';

const options = {
  output: { type: 'string' as const },
  ascii: { type: 'boolean' as const },
  stdin: { type: 'boolean' as const },
  theme: { type: 'string' as const }
};

const { values, positionals } = parseArgs({ args: process.argv.slice(2), options, strict: false });

async function main() {
  let mermaidCode = '';

  if (values.stdin) {
    mermaidCode = readFileSync(0, 'utf-8');
  } else if (positionals.length > 0) {
    mermaidCode = readFileSync(positionals[0], 'utf-8');
  } else {
    console.error('Usage: npx tsx render.ts [file] --output [out.svg] --ascii --theme [theme]');
    process.exit(1);
  }

  try {
    if (values.ascii) {
      console.log("Rendering ASCII...");
      const asciiResult = await renderMermaid(mermaidCode, { format: 'ascii' });
      console.log(asciiResult);
    } else if (values.output) {
      console.log(`Rendering SVG to ${values.output} with theme ${values.theme || 'default'}...`);
      const svg = await renderMermaid(mermaidCode, { format: 'svg', theme: values.theme });
      writeFileSync(values.output, svg);
      console.log('Done!');
    } else {
      console.error('Either --output or --ascii must be provided.');
      process.exit(1);
    }
  } catch (error) {
    console.error('Error rendering diagram:', error);
    process.exit(1);
  }
}

main().catch(console.error);
