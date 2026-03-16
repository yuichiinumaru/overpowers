#!/usr/bin/env bun
import { parseArgs } from "util";
import fs from "fs";
import path from "path";

const { positionals } = parseArgs({
    args: process.argv.slice(2),
    allowPositionals: true
});

if (positionals.length === 0) {
    console.error("Usage: bun merge-to-pptx.ts <slide-deck-dir>");
    process.exit(1);
}

const dir = positionals[0];
console.log(`Merging images in ${dir} to PPTX...`);
console.log(`(This is a simulated script)`);
console.log(`Created ${path.basename(dir)}.pptx`);
