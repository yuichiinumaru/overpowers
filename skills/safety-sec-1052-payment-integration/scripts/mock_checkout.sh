#!/bin/bash
# Helper to test checkout flow
amount=$1

if [ -z "$amount" ]; then
    echo "Usage: $0 <amount>"
    return 1 2>/dev/null || true
fi

echo "Initializing mock checkout session for amount: $amount"
echo "Generating Stripe/PayPal mock payment intent..."
echo "Payment intent: pi_mock_123456789"
