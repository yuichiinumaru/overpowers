#!/usr/bin/env node

/**
 * Search X using xAI API
 * 
 * Usage: node search.js [--days N] [--handles @user1,@user2] "query"
 */

const axios = require('axios');

const apiKey = process.env.XAI_API_KEY;
if (!apiKey) {
    console.error('Error: XAI_API_KEY environment variable not set.');
    process.exit(1);
}

const args = process.argv.slice(2);
let query = '';
let days = 30;
let handles = [];

for (let i = 0; i < args.length; i++) {
    if (args[i] === '--days') {
        days = parseInt(args[++i]);
    } else if (args[i] === '--handles') {
        handles = args[++i].split(',');
    } else {
        query = args[i];
    }
}

if (!query) {
    console.error('Usage: node search.js [--days N] [--handles @user1,@user2] "query"');
    process.exit(1);
}

console.log(`Searching X for: "${query}" (last ${days} days, handles: ${handles.join(', ') || 'any'})...`);

// This is a placeholder for the actual API call to xAI
// The SKILL.md specifies using the /v1/responses API with x_search tool

async function performSearch() {
    try {
        const response = await axios.post('https://api.x.ai/v1/responses', {
            model: process.env.SEARCH_X_MODEL || 'grok-4-1-fast',
            messages: [{ role: 'user', content: query }],
            tools: [{ type: 'x_search', parameters: { days, handles } }]
        }, {
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            }
        });

        console.log('Search Results:');
        console.log(JSON.stringify(response.data, null, 2));
    } catch (error) {
        console.error('Error performing search:', error.message);
        if (error.response) {
            console.error('API Response:', error.response.data);
        }
    }
}

// performSearch(); // Commented out as this is a helper template
console.log('\n[INFO] This script is a template. Ensure your API key is valid and the Grok API endpoint is reachable.');
