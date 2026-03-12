import argparse

def calculate_k_factor(invites, conv_rate):
    """K = Invitations × Conversion Rate"""
    return invites * conv_rate

def calculate_max_reward(ltv, margin, target_cac):
    """Max Reward = (LTV × Margin) - Target CAC"""
    return (ltv * margin) - target_cac

def calculate_roi(revenue, rewards, tools, management):
    """ROI = (Revenue - Total Costs) / Total Costs"""
    total_costs = rewards + tools + management
    if total_costs == 0:
        return 0
    return (revenue - total_costs) / total_costs

def main():
    parser = argparse.ArgumentParser(description="Referral & Viral Growth Calculator")
    subparsers = parser.add_subparsers(dest="command")
    
    # K-Factor
    k_parser = subparsers.add_parser("k-factor", help="Calculate viral coefficient")
    k_parser.add_argument("--invites", type=float, required=True, help="Avg invites per user")
    k_parser.add_argument("--conv", type=float, required=True, help="Conversion rate (0-1)")
    
    # Max Reward
    reward_parser = subparsers.add_parser("max-reward", help="Calculate max referral reward")
    reward_parser.add_argument("--ltv", type=float, required=True, help="Customer Lifetime Value")
    reward_parser.add_argument("--margin", type=float, required=True, help="Gross margin (0-1)")
    reward_parser.add_argument("--cac", type=float, required=True, help="Target CAC")
    
    # ROI
    roi_parser = subparsers.add_parser("roi", help="Calculate referral program ROI")
    roi_parser.add_argument("--revenue", type=float, required=True, help="Total revenue from referrals")
    roi_parser.add_argument("--rewards", type=float, required=True, help="Total rewards paid")
    roi_parser.add_argument("--tools", type=float, default=0, help="Tooling costs")
    roi_parser.add_argument("--mgmt", type=float, default=0, help="Management costs")
    
    args = parser.parse_args()
    
    if args.command == "k-factor":
        k = calculate_k_factor(args.invites, args.conv)
        print(f"Viral Coefficient (K): {k:.4f}")
        if k > 1:
            print("Status: VIRAL (Exponential growth)")
        else:
            print("Status: AMPLIFIED (Supplementary growth)")
            
    elif args.command == "max-reward":
        max_r = calculate_max_reward(args.ltv, args.margin, args.cac)
        print(f"Max Recommended Referral Reward: ${max_r:.2f}")
        
    elif args.command == "roi":
        roi = calculate_roi(args.revenue, args.rewards, args.tools, args.mgmt)
        print(f"Referral Program ROI: {roi*100:.2f}%")

if __name__ == "__main__":
    main()
