#!/usr/bin/env python3
"""
Basic Legal Disclaimer Generator
Generates common legal disclaimer templates (e.g., informational only, no attorney-client relationship).
"""
import sys
import argparse

def generate_disclaimer(company_name, disclaimer_type):
    """
    Generate standard disclaimer text.
    """
    disclaimers = {
        "informational": f"""**LEGAL DISCLAIMER**

The information provided by {company_name} ("we," "us," or "our") on our website or through our services is for general informational purposes only. All information is provided in good faith, however, we make no representation or warranty of any kind, express or implied, regarding the accuracy, adequacy, validity, reliability, availability, or completeness of any information.

Under no circumstance shall we have any liability to you for any loss or damage of any kind incurred as a result of the use of the site or reliance on any information provided on the site. Your use of the site and your reliance on any information is solely at your own risk.
""",
        "medical": f"""**MEDICAL DISCLAIMER**

The content provided by {company_name} is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

Never disregard professional medical advice or delay in seeking it because of something you have read or seen on our platform. Reliance on any information provided by {company_name} is solely at your own risk.
""",
        "financial": f"""**FINANCIAL/INVESTMENT DISCLAIMER**

The information provided by {company_name} does not constitute financial, investment, tax, or legal advice. We are not a registered investment advisor or broker-dealer.

All content is for informational and educational purposes only. You should not make any financial or investment decision based solely on the information provided by {company_name}. Always conduct your own research and consult with a licensed financial professional before making investment decisions.
"""
    }

    if disclaimer_type in disclaimers:
        print(disclaimers[disclaimer_type])
    else:
        print(f"Disclaimer type '{disclaimer_type}' not found. Available types: {', '.join(disclaimers.keys())}")

def main():
    parser = argparse.ArgumentParser(description="Basic Legal Disclaimer Generator")
    parser.add_argument("--company", required=True, help="Company Name")
    parser.add_argument("--type", choices=['informational', 'medical', 'financial'], default='informational', help="Type of disclaimer (default: informational)")

    args = parser.parse_args()

    generate_disclaimer(args.company, args.type)

if __name__ == "__main__":
    main()
