/**
 * Polymarket Market Data Fetcher
 * 
 * This script demonstrates how to fetch market data from the Polymarket API.
 * 
 * Usage:
 * ts-node get_market_data.ts <market_slug>
 */

import axios from 'axios';

const MARKET_SLUG = process.argv[2];

if (!MARKET_SLUG) {
    console.error("Please provide a market slug.");
    console.log("Usage: ts-node get_market_data.ts <market_slug>");
    process.exit(1);
}

const API_BASE_URL = 'https://clob.polymarket.com';

async function getMarketData(slug: string) {
    try {
        console.log(`Fetching data for market: ${slug}...`);
        
        // Note: This is an example endpoint, refer to api.md for exact endpoints
        const response = await axios.get(`${API_BASE_URL}/markets/${slug}`);
        
        if (response.status === 200) {
            console.log("Market Data:");
            console.log(JSON.stringify(response.data, null, 2));
        } else {
            console.error(`Failed to fetch data. Status: ${response.status}`);
        }
    } catch (error: any) {
        console.error("Error fetching market data:", error.message);
        if (error.response) {
            console.error("Response data:", error.response.data);
        }
    }
}

getMarketData(MARKET_SLUG);
