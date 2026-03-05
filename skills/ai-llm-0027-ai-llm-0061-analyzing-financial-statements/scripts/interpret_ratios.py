import json
import argparse
import sys

def interpret_ratios(results):
    interpretations = {}

    # Profitability
    prof = results.get('profitability', {})
    prof_interp = {}
    if 'Net Margin' in prof:
        val = prof['Net Margin']
        prof_interp['Net Margin'] = "Strong" if val > 0.15 else "Moderate" if val > 0.05 else "Weak"
    if 'ROE' in prof:
        val = prof['ROE']
        prof_interp['ROE'] = "Excellent" if val > 0.15 else "Average" if val > 0.1 else "Poor"
    interpretations['profitability'] = prof_interp

    # Liquidity
    liq = results.get('liquidity', {})
    liq_interp = {}
    if 'Current Ratio' in liq:
        val = liq['Current Ratio']
        liq_interp['Current Ratio'] = "Healthy" if val > 1.5 else "Adequate" if val > 1.0 else "Risky"
    if 'Quick Ratio' in liq:
        val = liq['Quick Ratio']
        liq_interp['Quick Ratio'] = "Strong" if val > 1.0 else "Vulnerable"
    interpretations['liquidity'] = liq_interp

    # Leverage
    lev = results.get('leverage', {})
    lev_interp = {}
    if 'Debt-to-Equity' in lev:
        val = lev['Debt-to-Equity']
        lev_interp['Debt-to-Equity'] = "Conservative" if val < 1.0 else "Highly Leveraged" if val > 2.0 else "Moderate"
    if 'Interest Coverage' in lev:
        val = lev['Interest Coverage']
        lev_interp['Interest Coverage'] = "Safe" if val > 3.0 else "At Risk"
    interpretations['leverage'] = lev_interp

    # Valuation
    val_ratios = results.get('valuation', {})
    val_interp = {}
    if 'P/E' in val_ratios:
        val = val_ratios['P/E']
        val_interp['P/E'] = "Value" if val < 15 else "Growth/Expensive" if val > 25 else "Fair"
    interpretations['valuation'] = val_interp

    return interpretations

def main():
    parser = argparse.ArgumentParser(description='Interpret financial ratios')
    parser.add_argument('--results', required=True, help='JSON string containing calculated ratios')
    
    args = parser.parse_args()
    
    try:
        results = json.loads(args.results)
        interpretations = interpret_ratios(results)
        print(json.dumps(interpretations, indent=2))
        
    except json.JSONDecodeError:
        print("Error: Invalid JSON results provided", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error interpreting ratios: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
