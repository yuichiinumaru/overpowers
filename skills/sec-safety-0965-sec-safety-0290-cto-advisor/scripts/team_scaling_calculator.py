#!/usr/bin/env python3

def calculate_scaling(team_size):
    print(f"Team Scaling Calculator for {team_size} engineers\n")

    managers = max(1, team_size // 8)
    product = max(1, team_size // 10)
    qa = max(1, int(team_size * 0.15))

    print(f"Recommended Structure:")
    print(f"- Engineers: {team_size}")
    print(f"- Engineering Managers: {managers} (Ratio ~1:8)")
    print(f"- Product Managers: {product} (Ratio ~1:10)")
    print(f"- QA Engineers: {qa} (Ratio ~1.5:10)")
    print(f"\nTotal Team Size: {team_size + managers + product + qa}")

    print(f"\nEngineer Seniority Mix (3:4:2 target):")
    total_ratio = 9
    senior = int(team_size * (3/total_ratio))
    mid = int(team_size * (4/total_ratio))
    junior = team_size - senior - mid
    print(f"- Senior: {senior}")
    print(f"- Mid-level: {mid}")
    print(f"- Junior: {junior}")

if __name__ == "__main__":
    import sys
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    calculate_scaling(size)
