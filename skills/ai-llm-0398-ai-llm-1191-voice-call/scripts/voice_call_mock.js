#!/usr/bin/env node
/**
 * Mock script for voice call operations via Moltbot plugin
 */
const [,, cmd, ...args] = process.argv;

if (!cmd) {
    console.log("Usage: node voice_call_mock.js <call|status> [args]");
    process.exit(1);
}

if (cmd === "call") {
    console.log(`Starting mock voice call with args: ${args.join(' ')}`);
    console.log("Call ID: mock_12345");
} else if (cmd === "status") {
    console.log(`Checking status for call: ${args.join(' ')}`);
    console.log("Status: in-progress");
} else {
    console.log("Unknown command");
}
