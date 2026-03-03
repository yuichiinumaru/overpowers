import json
import argparse
import sys

def calculate_profitability(data):
    ratios = {}
    net_income = data.get('net_income')
    revenue = data.get('revenue')
    total_equity = data.get('total_equity')
    total_assets = data.get('total_assets')
    gross_profit = data.get('gross_profit')
    operating_income = data.get('operating_income')

    if net_income is not None and revenue:
        ratios['Net Margin'] = net_income / revenue
    if net_income is not None and total_equity:
        ratios['ROE'] = net_income / total_equity
    if net_income is not None and total_assets:
        ratios['ROA'] = net_income / total_assets
    if gross_profit is not None and revenue:
        ratios['Gross Margin'] = gross_profit / revenue
    if operating_income is not None and revenue:
        ratios['Operating Margin'] = operating_income / revenue
    return ratios

def calculate_liquidity(data):
    ratios = {}
    current_assets = data.get('current_assets')
    current_liabilities = data.get('current_liabilities')
    inventory = data.get('inventory', 0)
    cash = data.get('cash_and_equivalents', 0)

    if current_assets is not None and current_liabilities:
        ratios['Current Ratio'] = current_assets / current_liabilities
    if current_assets is not None and current_liabilities:
        ratios['Quick Ratio'] = (current_assets - inventory) / current_liabilities
    if cash is not None and current_liabilities:
        ratios['Cash Ratio'] = cash / current_liabilities
    return ratios

def calculate_leverage(data):
    ratios = {}
    total_debt = data.get('total_debt')
    total_equity = data.get('total_equity')
    operating_income = data.get('operating_income')
    interest_expense = data.get('interest_expense')

    if total_debt is not None and total_equity:
        ratios['Debt-to-Equity'] = total_debt / total_equity
    if operating_income is not None and interest_expense:
        ratios['Interest Coverage'] = operating_income / interest_expense
    return ratios

def calculate_efficiency(data):
    ratios = {}
    revenue = data.get('revenue')
    total_assets = data.get('total_assets')
    cogs = data.get('cogs')
    inventory = data.get('inventory')
    accounts_receivable = data.get('accounts_receivable')

    if revenue is not None and total_assets:
        ratios['Asset Turnover'] = revenue / total_assets
    if cogs is not None and inventory:
        ratios['Inventory Turnover'] = cogs / inventory
    if revenue is not None and accounts_receivable:
        ratios['Receivables Turnover'] = revenue / accounts_receivable
    return ratios

def calculate_valuation(data):
    ratios = {}
    stock_price = data.get('stock_price')
    eps = data.get('eps')
    book_value_per_share = data.get('book_value_per_share')
    sales_per_share = data.get('sales_per_share')

    if stock_price is not None and eps:
        ratios['P/E'] = stock_price / eps
    if stock_price is not None and book_value_per_share:
        ratios['P/B'] = stock_price / book_value_per_share
    if stock_price is not None and sales_per_share:
        ratios['P/S'] = stock_price / sales_per_share
    return ratios

def main():
    parser = argparse.ArgumentParser(description='Calculate financial ratios')
    parser.add_argument('--data', required=True, help='JSON string containing financial data')
    
    args = parser.parse_args()
    
    try:
        data = json.loads(args.data)
        
        results = {
            'profitability': calculate_profitability(data),
            'liquidity': calculate_liquidity(data),
            'leverage': calculate_leverage(data),
            'efficiency': calculate_efficiency(data),
            'valuation': calculate_valuation(data)
        }
        
        print(json.dumps(results, indent=2))
        
    except json.JSONDecodeError:
        print("Error: Invalid JSON data provided", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error calculating ratios: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
