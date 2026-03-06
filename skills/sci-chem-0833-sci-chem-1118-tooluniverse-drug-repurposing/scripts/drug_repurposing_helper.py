import sys

def score_repurposing_candidate(drug_name, target_score, safety_data, literature_count):
    """Score drug repurposing candidate (0-100)."""
    score = 0
    score += min(target_score * 40, 40)

    approval_status = safety_data.get('approval_status', 'experimental')
    if approval_status == 'approved':
        score += 20
    elif approval_status == 'clinical':
        score += 10

    if not safety_data.get('black_box_warning', False):
        score += 10

    score += min(literature_count / 5 * 20, 20)
    print(f"Drug Candidate: {drug_name} | Repurposing Score: {score}/100")
    return score

if __name__ == "__main__":
    score_repurposing_candidate("ExampleDrug", 0.85, {'approval_status': 'approved'}, 23)
