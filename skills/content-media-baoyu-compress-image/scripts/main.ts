#!/usr/bin/env bun
import { $ } from "bun";
import { parseArgs } from "util";

const { values, positionals } = parseArgs({
  args: Bun.argv.slice(2),
  options: {
    output: { type: "string", short: "o" },
    format: { type: "string", short: "f", default: "webp" },
    quality: { type: "string", short: "q", default: "80" },
    keep: { type: "boolean", short: "k", default: false },
    recursive: { type: "boolean", short: "r", default: false },
    json: { type: "boolean", default: false },
  },
  allowPositionals: true,
});

if (positionals.length === 0) {
  console.log("Usage: main.ts <input> [options]");
  process.exit(1);
}

const input = positionals[0];

async function compress(file: string) {
  const ext = values.format === "jpeg" ? "jpg" : values.format;
  const output = values.output || file.replace(/\.[^/.]+$/, "") + "." + ext;
  
  console.log(`Compressing ${file} to ${output} (format: ${values.format}, quality: ${values.quality})...`);
  
  // Simplified logic - prefers cwebp if available
  try {
    await $`cwebp -q ${values.quality} ${file} -o ${output}`;
    if (!values.keep && file !== output) {
      await $`rm ${file}`;
    }
  } catch (e) {
    console.error(`Failed to compress ${file}: ${e}`);
  }
}

// Logic for recursive/file would go here
compress(input);
