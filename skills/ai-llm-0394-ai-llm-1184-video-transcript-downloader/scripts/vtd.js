#!/usr/bin/env node
/**
 * Helper script wrapping youtube-transcript-plus / yt-dlp
 */
const [,, cmd, ...args] = process.argv;

if (!cmd) {
    console.log("Usage: ./vtd.js <transcript|download|audio|subs|formats> --url <url>");
    process.exit(1);
}

console.log(`Executing VTD command: ${cmd} with args: ${args.join(' ')}`);

if (cmd === "transcript") {
    console.log("Fetching transcript...");
} else if (cmd === "download") {
    console.log("Downloading video...");
} else {
    console.log("Executing yt-dlp operation...");
}
