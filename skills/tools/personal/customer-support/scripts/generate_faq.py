import sys

def generate_faq(tickets):
    output = "# Frequently Asked Questions\n\n"
    for ticket in tickets:
        ticket = ticket.strip()
        if not ticket: continue
        output += f"### {ticket}\n[AI generated answer based on knowledge base]\n\n"
    return output

if __name__ == "__main__":
    # Expects ticket subjects/summaries from stdin
    tickets = sys.stdin.readlines()
    if tickets:
        print(generate_faq(tickets))
    else:
        print("No ticket data provided.")
