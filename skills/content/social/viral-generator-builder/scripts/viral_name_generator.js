#!/usr/bin/env node
/**
 * Viral Name Generator Script.
 * Demonstrates a simple deterministic name generation algorithm.
 */

const args = process.argv.slice(2);
if (args.length === 0) {
    console.log("Usage: node viral_name_generator.js <your_name>");
    process.exit(1);
}

const inputName = args.join(" ");

function simpleHash(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
        hash = (hash << 5) - hash + str.charCodeAt(i);
        hash |= 0;
    }
    return Math.abs(hash);
}

function generateViralName(input) {
    const hash = simpleHash(input.toLowerCase());
    const firstNames = ["Shadow", "Storm", "Crystal", "Midnight", "Quantum", "Neon"];
    const lastNames = ["Walker", "Blade", "Heart", "Architect", "Rider", "Nomad"];

    const first = firstNames[hash % firstNames.length];
    const last = lastNames[Math.abs(hash >> 8) % lastNames.length];
    return `${first} ${last}`;
}

const viralName = generateViralName(inputName);

console.log("--- VIRAL NAME GENERATOR ---");
console.log(`Original Name: ${inputName}`);
console.log(`Your Viral Identity: The ${viralName}`);
console.log("\nShare this result with your friends!");
