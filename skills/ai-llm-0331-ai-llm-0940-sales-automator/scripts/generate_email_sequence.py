import argparse

def generate_sequence(company, problem):
    print(f"Generating cold email sequence for {company} regarding {problem}...\n")
    
    # Touchpoint 1
    print("Touchpoint 1: Initial Outreach (Day 1)")
    print(f"Subject: Quick question about {problem} at {company}")
    print(f"Hi [Name],")
    print(f"I noticed that {company} might be facing some challenges with {problem}. We've helped similar companies overcome this by [Value Proposition].")
    print("Would you be open to a 10-minute chat next week to see if we could do the same for you?")
    print("Best,\n[My Name]\n")
    
    # Touchpoint 2
    print("Touchpoint 2: Value Add (Day 3)")
    print(f"Subject: Resource for {company}'s {problem}")
    print(f"Hi [Name],")
    print(f"Following up on my last email. I thought you might find this case study interesting - it shows how [Similar Company] solved {problem} and achieved [Result].")
    print("Is this something that's currently on your radar?")
    print("Best,\n[My Name]\n")
    
    # Touchpoint 3
    print("Touchpoint 3: The Breakup (Day 7)")
    print(f"Subject: Moving on / {problem}")
    print(f"Hi [Name],")
    print(f"I haven't heard back, so I assume {problem} isn't a priority for {company} right now. I'll stop reaching out for now.")
    print("If things change, feel free to reach back out.")
    print("Best,\n[My Name]\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a simple 3-step cold email sequence.")
    parser.add_argument("--company", required=True, help="Target company name")
    parser.add_argument("--problem", required=True, help="Problem the company is facing")
    args = parser.parse_args()
    
    generate_sequence(args.company, args.problem)
