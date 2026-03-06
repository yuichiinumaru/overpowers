import requests
import json
import os

class PayPalClient:
    def __init__(self, client_id=None, client_secret=None, mode='sandbox'):
        self.client_id = client_id or os.environ.get('PAYPAL_CLIENT_ID')
        self.client_secret = client_secret or os.environ.get('PAYPAL_CLIENT_SECRET')
        if not self.client_id or not self.client_secret:
            raise ValueError("PayPal Client ID and Secret must be provided or set in environment variables.")
        
        self.base_url = 'https://api-m.sandbox.paypal.com' if mode == 'sandbox' else 'https://api-m.paypal.com'
        self.access_token = self.get_access_token()

    def get_access_token(self):
        """Get OAuth access token."""
        url = f"{self.base_url}/v1/oauth2/token"
        headers = {"Accept": "application/json", "Accept-Language": "en_US"}

        response = requests.post(
            url,
            headers=headers,
            data={"grant_type": "client_credentials"},
            auth=(self.client_id, self.client_secret)
        )
        response.raise_for_status()
        return response.json()['access_token']

    def create_order(self, amount, currency='USD'):
        """Create a PayPal order."""
        url = f"{self.base_url}/v2/checkout/orders"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }

        payload = {
            "intent": "CAPTURE",
            "purchase_units": [{
                "amount": {
                    "currency_code": currency,
                    "value": str(amount)
                }
            }]
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def capture_order(self, order_id):
        """Capture payment for an order."""
        url = f"{self.base_url}/v2/checkout/orders/{order_id}/capture"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_order_details(self, order_id):
        """Get order details."""
        url = f"{self.base_url}/v2/checkout/orders/{order_id}"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python paypal_client.py <command> [args]")
        print("Commands: create <amount>, capture <order_id>, details <order_id>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    client = PayPalClient()
    
    if cmd == "create":
        print(json.dumps(client.create_order(sys.argv[2]), indent=2))
    elif cmd == "capture":
        print(json.dumps(client.capture_order(sys.argv[2]), indent=2))
    elif cmd == "details":
        print(json.dumps(client.get_order_details(sys.argv[2]), indent=2))
