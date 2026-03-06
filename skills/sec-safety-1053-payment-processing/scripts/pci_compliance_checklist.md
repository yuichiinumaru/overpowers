# PCI Compliance Checklist for Developers

This checklist provides a high-level overview of PCI DSS (Payment Card Industry Data Security Standard) requirements for developers implementing payment processing systems.

## 1. Do Not Store Prohibited Data
- [ ] NEVER store sensitive authentication data (SAD) after authorization:
    - [ ] Full contents of magnetic stripes or chip data.
    - [ ] Card verification codes (CVV, CVC, CID, etc.).
    - [ ] Personal Identification Numbers (PINs) or PIN blocks.

## 2. Protect Stored Primary Account Numbers (PAN)
- [ ] If PAN must be stored, ensure it is unreadable (e.g., using strong cryptography, hashing, or truncation).
- [ ] Mask PAN when displayed (show only first six and last four digits).
- [ ] Use tokenization (e.g., Stripe Tokens, PayPal Vault) to avoid storing PANs locally.

## 3. Secure Data Transmission
- [ ] Use strong cryptography and security protocols (e.g., TLS 1.2+) to safeguard sensitive cardholder data during transmission over open, public networks.
- [ ] Ensure all API calls to payment gateways are over HTTPS.

## 4. Secure Development Practices
- [ ] Follow secure coding practices (e.g., OWASP Top 10).
- [ ] Regularly update and patch all components, libraries, and frameworks.
- [ ] Implement robust error handling that does not leak sensitive information.

## 5. Access Control and Monitoring
- [ ] Restrict access to cardholder data to only those with a business "need to know."
- [ ] Use unique IDs for each person with computer access.
- [ ] Track and monitor all access to network resources and cardholder data.

## 6. Use PCI-Compliant Service Providers
- [ ] Verify that your payment gateway (Stripe, PayPal, etc.) is PCI DSS compliant.
- [ ] Use payment components (e.g., Stripe Elements, PayPal Smart Buttons) that keep sensitive data off your servers.
