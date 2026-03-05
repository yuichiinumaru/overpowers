#!/usr/bin/env python3
import sys

def scaffold_pricing_strategy():
    print("--- Pricing Strategy Document Scaffolder ---")
    project_name = input("Project/Product Name: ")
    filename = f"pricing_strategy_{project_name.lower().replace(' ', '_')}.md"
    
    content = f"""# Pricing Strategy: {project_name}

## 1. Context
- **Business Model**: 
- **Target Customer**: 
- **Go-to-Market Motion**: 

## 2. Market & Competition
- **Primary Value Delivered**: 
- **Key Alternatives**: 
- **Competitor Pricing Models**: 

## 3. Pricing Fundamentals
### Value Metric
- **Selected Metric**: (e.g., Per user, per usage, flat fee)
- **Validation**: Does price scale naturally as customers get more value?

## 4. Tier Design (Good / Better / Best)
### Tier 1: Good
- **Persona**: 
- **Price Level**: 
- **Packaging/Limits**: 

### Tier 2: Better (Anchor)
- **Persona**: 
- **Price Level**: 
- **Packaging/Limits**: 

### Tier 3: Best / Enterprise
- **Persona**: 
- **Price Level**: 
- **Packaging/Limits**: 

## 5. Pricing Research & Validation
- **Research Method**: (e.g., Van Westendorp, Conjoint)
- **Key Insights**: 

## 6. Risks & Tradeoffs
- 
- 

## Validation Checklist
- [ ] Clear value metric
- [ ] Distinct tier personas
- [ ] Research-backed price range
- [ ] Conversion-safe entry tier
- [ ] Expansion path exists
- [ ] Enterprise handled explicitly
"""
    
    with open(filename, 'w') as f:
        f.write(content)
        
    print(f"\nScaffolded pricing strategy document: {filename}")

if __name__ == "__main__":
    try:
        scaffold_pricing_strategy()
    except KeyboardInterrupt:
        print("\nScaffolding cancelled.")
        sys.exit(0)
