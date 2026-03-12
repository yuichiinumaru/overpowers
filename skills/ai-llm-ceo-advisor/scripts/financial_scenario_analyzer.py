#!/usr/bin/env python3
import argparse

def calculate_scenario(revenue, cogs, growth_rate):
    projected_revenue = revenue * (1 + growth_rate)
    projected_cogs = cogs * (1 + growth_rate * 0.8) # Assuming some variable cost scaling
    gross_profit = projected_revenue - projected_cogs
    return projected_revenue, gross_profit

def main():
    print("CEO Financial Scenario Analyzer")
    print("===============================")
    
    try:
        current_revenue = float(input("Current Annual Revenue: "))
        current_cogs = float(input("Current Annual COGS: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    scenarios = {
        "Worst Case": -0.1,
        "Base Case": 0.1,
        "Best Case": 0.3
    }
    
    print("\nProjections for next year:")
    print(f"{'Scenario':<15} | {'Revenue':<15} | {'Gross Profit':<15}")
    print("-" * 50)
    
    for name, rate in scenarios.items():
        rev, gp = calculate_scenario(current_revenue, current_cogs, rate)
        print(f"{name:<15} | {rev:<15.2f} | {gp:<15.2f}")

    print("\nNotes:")
    print("- Gross Profit assumes COGS scales at 80% of revenue growth.")
    print("- Strategic Reserve recommendation: 10-15% of Gross Profit.")

if __name__ == "__main__":
    main()
