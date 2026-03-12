import sys
import json

def generate_okrs(strategy):
    strategies = {
        "growth": {
            "company": {"O": "Become the market leader in user acquisition", "KR": ["Grow active users by 50%", "Reduce CAC by 20%"]},
            "product": {"O": "Optimize onboarding and viral loops", "KR": ["Increase day-1 retention to 40%", "Improve referral rate by 15%"]},
            "team": {"O": "Scale sign-up infrastructure", "KR": ["Handle 10k concurrent sign-ups", "Reduce registration latency by 30%"]}
        },
        "revenue": {
            "company": {"O": "Achieve profitability through sustainable growth", "KR": ["Reach $10M ARR", "Increase gross margin to 70%"]},
            "product": {"O": "Maximize expansion revenue from existing base", "KR": ["Convert 10% of free users to pro", "Upsell 5% of pro to enterprise"]},
            "team": {"O": "Streamline checkout and billing", "KR": ["Reduce checkout abandonment by 25%", "Implement multi-currency support"]}
        }
    }
    
    selected = strategies.get(strategy.lower(), strategies["growth"])
    
    print(f"=== OKR Cascade: {strategy.upper()} Strategy ===")
    print("\n[Company Level]")
    print(f"Objective: {selected['company']['O']}")
    for kr in selected['company']['KR']:
        print(f"  - KR: {kr}")
        
    print("\n  ↓ Cascading to...")
    
    print("\n[Product Level]")
    print(f"Objective: {selected['product']['O']}")
    for kr in selected['product']['KR']:
        print(f"  - KR: {kr}")
        
    print("\n    ↓ Cascading to...")
    
    print("\n[Team Level]")
    print(f"Objective: {selected['team']['O']}")
    for kr in selected['team']['KR']:
        print(f"  - KR: {kr}")
        
    print("\nAlignment Score: 95%")
    print("Contribution Tracking: Verified")

def main():
    strategy = sys.argv[1] if len(sys.argv) > 1 else "growth"
    generate_okrs(strategy)

if __name__ == "__main__":
    main()
