#!/usr/bin/env python3
import argparse

def main():
    print("CEO Strategic Analyzer")
    print("======================")
    
    company = input("Company Name: ")
    industry = input("Industry: ")
    
    print("\nSWOT Analysis")
    strengths = input("Strengths (comma separated): ").split(',')
    weaknesses = input("Weaknesses (comma separated): ").split(',')
    opportunities = input("Opportunities (comma separated): ").split(',')
    threats = input("Threats (comma separated): ").split(',')
    
    print(f"\nStrategic Report for {company}")
    print("-" * (21 + len(company)))
    
    print("\nStrategic Position:")
    print(f"Industry: {industry}")
    
    print("\nStrengths:")
    for s in strengths: print(f"  - {s.strip()}")
    
    print("\nWeaknesses:")
    for w in weaknesses: print(f"  - {w.strip()}")
    
    print("\nOpportunities:")
    for o in opportunities: print(f"  - {o.strip()}")
    
    print("\nThreats:")
    for t in threats: print(f"  - {t.strip()}")
    
    print("\nRecommendations:")
    if len(strengths) > len(weaknesses):
        print("  - Leverage core strengths to capture market share.")
    else:
        print("  - Prioritize operational improvements to address weaknesses.")
        
    if len(opportunities) > len(threats):
        print("  - Aggressively pursue identified growth opportunities.")
    else:
        print("  - Build strategic reserves and defensive moats against threats.")

if __name__ == "__main__":
    main()
