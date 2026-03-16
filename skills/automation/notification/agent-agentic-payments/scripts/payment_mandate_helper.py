import json
from datetime import datetime, timedelta

class PaymentMandateHelper:
    """Helper to generate JSON payloads for agentic-payments MCP tools."""
    
    @staticmethod
    def create_mandate_payload(agent_id, holder_id, amount_cents, currency="USD", period="daily", kind="intent", merchant_restrictions=None, days_valid=30):
        expires_at = (datetime.utcnow() + timedelta(days=days_valid)).strftime("%Y-%m-%dT%H:%M:%SZ")
        return {
            "agent_id": agent_id,
            "holder_id": holder_id,
            "amount_cents": amount_cents,
            "currency": currency,
            "period": period,
            "kind": kind,
            "merchant_restrictions": merchant_restrictions or [],
            "expires_at": expires_at
        }

    @staticmethod
    def authorize_payment_payload(mandate_id, amount_cents, merchant, description, metadata=None):
        return {
            "mandate_id": mandate_id,
            "amount_cents": amount_cents,
            "merchant": merchant,
            "description": description,
            "metadata": metadata or {}
        }

    @staticmethod
    def consensus_payload(payment_id, required_agents, threshold, timeout_seconds=300):
        return {
            "payment_id": payment_id,
            "required_agents": required_agents,
            "threshold": threshold,
            "timeout_seconds": timeout_seconds
        }

if __name__ == "__main__":
    helper = PaymentMandateHelper()
    
    mandate = helper.create_mandate_payload(
        "shopping-bot@agentics", 
        "user@example.com", 
        50000, 
        merchant_restrictions=["amazon.com"]
    )
    print("Mandate Payload:")
    print(json.dumps(mandate, indent=4))
    
    print("\nAuthorization Payload:")
    auth = helper.authorize_payment_payload(
        "mandate_abc123",
        2999,
        "amazon.com",
        "Book purchase"
    )
    print(json.dumps(auth, indent=4))
