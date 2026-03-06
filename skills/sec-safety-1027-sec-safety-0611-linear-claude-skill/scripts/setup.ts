#!/usr/bin/env node
console.log("Checking Linear setup...");
if (!process.env.LINEAR_API_KEY) {
    console.error("LINEAR_API_KEY is not set.");
    process.exit(1);
}
console.log("Linear setup looks good.");
