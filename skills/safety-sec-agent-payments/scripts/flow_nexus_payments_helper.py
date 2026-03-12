import json

class FlowNexusPaymentsHelper:
    """Helper to generate JSON payloads for Flow Nexus payments MCP tools."""
    
    @staticmethod
    def get_ruv_balance_payload(user_id):
        return {
            "user_id": user_id
        }

    @staticmethod
    def get_ruv_history_payload(user_id, limit=50):
        return {
            "user_id": user_id,
            "limit": limit
        }

    @staticmethod
    def create_payment_link_payload(amount):
        return {
            "amount": amount
        }

    @staticmethod
    def configure_auto_refill_payload(enabled, threshold, amount):
        return {
            "enabled": enabled,
            "threshold": threshold,
            "amount": amount
        }

    @staticmethod
    def user_upgrade_payload(user_id, tier):
        return {
            "user_id": user_id,
            "tier": tier
        }

if __name__ == "__main__":
    helper = FlowNexusPaymentsHelper()
    
    print("Auto-Refill Payload:")
    payload = helper.configure_auto_refill_payload(True, 100, 50)
    print(json.dumps(payload, indent=4))
    
    print("\nPayment Link Payload:")
    link_payload = helper.create_payment_link_payload(50)
    print(json.dumps(link_payload, indent=4))
