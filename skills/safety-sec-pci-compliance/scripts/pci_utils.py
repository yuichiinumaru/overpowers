#!/usr/bin/env python3
import re
import json

def validate_card_number(card_number):
    """Validate card number format using Luhn algorithm."""
    # Remove spaces and dashes
    card_number = re.sub(r'[\s-]', '', card_number)

    # Check if all digits
    if not card_number.isdigit():
        return False

    # Luhn algorithm
    def luhn_checksum(card_num):
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_num)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    return luhn_checksum(card_number) == 0

def mask_pan(pan):
    """Mask Primary Account Number (PAN)."""
    if not pan:
        return pan
    pan_str = str(pan)
    if len(pan_str) < 10:
        return "****"
    return f"{pan_str[:6]}{'*' * (len(pan_str) - 10)}{pan_str[-4:]}"

def sanitize_payment_data(data):
    """Remove sensitive data from dictionary (suitable for logging)."""
    prohibited_fields = ['cvv', 'cvv2', 'cvc', 'pin', 'password', 'secret']
    sanitized = data.copy()

    # Mask PAN if present
    for key in sanitized:
        if 'card_number' in key.lower() or 'pan' in key.lower():
            sanitized[key] = mask_pan(sanitized[key])

    # Remove prohibited data
    for field in prohibited_fields:
        for key in list(sanitized.keys()):
            if field in key.lower():
                sanitized.pop(key, None)

    return sanitized

if __name__ == "__main__":
    # Quick test
    test_card = "4242 4242 4242 4242"
    print(f"Validating {test_card}: {validate_card_number(test_card)}")
    
    test_data = {
        "user_id": 123,
        "card_number": "4242424242424242",
        "cvv": "123",
        "amount": 100.00
    }
    print(f"Original Data: {test_data}")
    print(f"Sanitized Data: {sanitize_payment_data(test_data)}")
