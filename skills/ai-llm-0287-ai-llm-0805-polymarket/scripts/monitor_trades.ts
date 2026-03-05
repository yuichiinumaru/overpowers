/**
 * Polymarket Trade Monitor Template
 * 
 * This script demonstrates how to connect to Polymarket's WebSocket service
 * and subscribe to live trade activity.
 * 
 * Requirements:
 * npm install @polymarket/real-time-data-client
 */

import { RealTimeDataClient } from "@polymarket/real-time-data-client";

// Replace with a specific market slug to monitor, or leave empty for all trades
const MARKET_SLUG = process.argv[2] || "";

const onMessage = (message: any): void => {
    if (message.topic === "activity" && message.type === "trades") {
        const trade = message.payload;
        console.log(`[TRADE] Market: ${trade.market_slug} | Price: ${trade.price} | Size: ${trade.size} | Side: ${trade.side}`);
    }
};

const onConnect = (client: RealTimeDataClient): void => {
    console.log("Connected to Polymarket WebSocket");
    
    const subscription: any = {
        topic: "activity",
        type: "trades"
    };

    if (MARKET_SLUG) {
        subscription.filters = JSON.stringify({ market_slug: MARKET_SLUG });
        console.log(`Subscribing to trades for market: ${MARKET_SLUG}`);
    } else {
        console.log("Subscribing to all trades");
    }

    client.subscribe({
        subscriptions: [subscription]
    });
};

const onError = (error: Error): void => {
    console.error("WebSocket Error:", error.message);
};

const onDisconnect = (): void => {
    console.log("Disconnected from Polymarket WebSocket");
};

console.log("Starting Polymarket Trade Monitor...");
const client = new RealTimeDataClient({ 
    onMessage, 
    onConnect,
    onError,
    onDisconnect
});

client.connect();

// Handle graceful shutdown
process.on("SIGINT", () => {
    console.log("\nStopping monitor...");
    client.disconnect();
    process.exit();
});
