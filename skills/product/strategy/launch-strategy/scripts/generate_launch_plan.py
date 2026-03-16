import argparse
import os

def generate_launch_plan(product_name, product_desc):
    plan = f"""# Launch Strategy: {product_name}

## Product Description
{product_desc}

## ORB Framework Channels

### Owned Channels
- [ ] Email List: Start building early
- [ ] Blog: Share progress and insights
- [ ] Community: Slack/Discord for early testers

### Rented Channels
- [ ] Twitter/X: Threads about development
- [ ] LinkedIn: High-value posts for professional audience

### Borrowed Channels
- [ ] Podcasts: Identify guest opportunities
- [ ] Influencers: Reach out for reviews/demos

## Five-Phase Roadmap

### Phase 1: Internal Launch
- Recruit 10-20 early users
- Collect usability feedback

### Phase 2: Alpha Launch
- Landing page with waitlist
- Individual invites

### Phase 3: Beta Launch
- Broaden access
- Teaser marketing campaign

### Phase 4: Early Access
- Visual leaks (screenshots/GIFs)
- Batch invites

### Phase 5: Full Launch
- Open signups
- Product Hunt launch day

## Pre-Launch Checklist
- [ ] Landing page with value prop
- [ ] Waitlist setup
- [ ] Launch assets (videos/GIFs)
- [ ] Onboarding flow
- [ ] Analytics tracking
"""
    
    filename = f"launch_plan_{product_name.lower().replace(' ', '_')}.md"
    with open(filename, 'w') as f:
        f.write(plan)
    print(f"✅ Launch plan generated: {filename}")

def main():
    parser = argparse.ArgumentParser(description='Generate a structured launch plan')
    parser.add_argument('--name', required=True, help='Product Name')
    parser.add_argument('--desc', required=True, help='Product Description')
    
    args = parser.parse_args()
    generate_launch_plan(args.name, args.desc)

if __name__ == "__main__":
    main()
