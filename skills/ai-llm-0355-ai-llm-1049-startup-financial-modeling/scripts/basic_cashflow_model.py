#!/usr/bin/env python3
import argparse
import csv

def generate_projection(months, starting_cash, monthly_burn, monthly_revenue_growth, initial_revenue):
    projection = []
    cash = starting_cash
    revenue = initial_revenue

    for month in range(1, months + 1):
        net_burn = monthly_burn - revenue
        cash -= net_burn

        projection.append({
            "Month": month,
            "Starting Cash": round(cash + net_burn, 2),
            "Revenue": round(revenue, 2),
            "Expenses": round(monthly_burn, 2),
            "Net Burn": round(net_burn, 2),
            "Ending Cash": round(cash, 2)
        })

        # Increase revenue for next month
        revenue = revenue * (1 + monthly_revenue_growth)

    return projection

def main():
    parser = argparse.ArgumentParser(description="Generate a simple monthly cash flow projection.")
    parser.add_argument("--months", type=int, default=12, help="Number of months to project")
    parser.add_argument("--starting-cash", type=float, required=True, help="Initial cash balance")
    parser.add_argument("--monthly-expenses", type=float, required=True, help="Fixed monthly expenses (burn)")
    parser.add_argument("--initial-revenue", type=float, default=0, help="Initial monthly revenue")
    parser.add_argument("--revenue-growth", type=float, default=0.05, help="Monthly revenue growth rate (e.g., 0.05 for 5%)")
    parser.add_argument("--output", default="cashflow_projection.csv", help="Output CSV file")

    args = parser.parse_args()

    projection = generate_projection(
        args.months,
        args.starting_cash,
        args.monthly_expenses,
        args.revenue_growth,
        args.initial_revenue
    )

    with open(args.output, "w", newline='') as f:
        fieldnames = ["Month", "Starting Cash", "Revenue", "Expenses", "Net Burn", "Ending Cash"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for row in projection:
            writer.writerow(row)

    print(f"Generated {args.months}-month cash flow projection at {args.output}")

    # Calculate runway
    runway_months = 0
    for row in projection:
        if row["Ending Cash"] > 0:
            runway_months += 1
        else:
            break

    if runway_months < args.months:
        print(f"⚠️ Warning: Cash runs out in month {runway_months+1}")
    else:
        print(f"✅ Cash runway extends beyond the {args.months}-month projection period")

if __name__ == "__main__":
    main()
