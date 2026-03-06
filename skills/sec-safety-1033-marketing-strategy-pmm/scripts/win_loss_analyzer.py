import csv
import sys
from collections import Counter

def analyze_win_loss(csv_file):
    wins = 0
    losses = 0
    reasons = []
    competitors = []
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                outcome = row.get('Outcome', '').lower()
                if 'won' in outcome:
                    wins += 1
                elif 'lost' in outcome:
                    losses += 1
                
                reason = row.get('Reason', '')
                if reason:
                    reasons.append(reason)
                
                competitor = row.get('Competitor', '')
                if competitor:
                    competitors.append(competitor)
                    
        total = wins + losses
        win_rate = (wins / total * 100) if total > 0 else 0
        
        print(f"Win/Loss Analysis Summary:")
        print(f"Total Deals: {total}")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Win Rate: {win_rate:.2f}%")
        
        print("\nTop Reasons:")
        for reason, count in Counter(reasons).most_common(5):
            print(f"- {reason}: {count}")
            
        print("\nTop Competitors encountered:")
        for comp, count in Counter(competitors).most_common(5):
            print(f"- {comp}: {count}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python win_loss_analyzer.py <win_loss_csv_file>")
        print("CSV should have headers: Outcome, Reason, Competitor")
    else:
        analyze_win_loss(sys.argv[1])
