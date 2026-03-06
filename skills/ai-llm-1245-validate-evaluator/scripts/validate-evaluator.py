#!/usr/bin/env python3
"""
Helper script to validate an LLM evaluator against human labels.
Expected input: two CSV files or JSON arrays with 'human_label' and 'evaluator_label'.
For demonstration, this script runs a mock validation if no files are provided.
"""

import sys
import numpy as np
from sklearn.metrics import confusion_matrix

def compute_metrics(human_labels, eval_labels):
    # Ensure binary 'Pass' / 'Fail'
    tn, fp, fn, tp = confusion_matrix(human_labels, eval_labels, labels=['Fail', 'Pass']).ravel()
    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
    tnr = tn / (tn + fp) if (tn + fp) > 0 else 0
    return tpr, tnr

def bootstrap_ci(human_labels, eval_labels, p_obs, n_bootstrap=2000):
    n = len(human_labels)
    estimates = []
    h_arr = np.array(human_labels)
    e_arr = np.array(eval_labels)

    for _ in range(n_bootstrap):
        idx = np.random.choice(n, size=n, replace=True)
        h = h_arr[idx]
        e = e_arr[idx]

        tp = ((h == 'Pass') & (e == 'Pass')).sum()
        fn = ((h == 'Pass') & (e == 'Fail')).sum()
        tn = ((h == 'Fail') & (e == 'Fail')).sum()
        fp = ((h == 'Fail') & (e == 'Pass')).sum()

        tpr_b = tp / (tp + fn) if (tp + fn) > 0 else 0
        tnr_b = tn / (tn + fp) if (tn + fp) > 0 else 0
        denom = tpr_b + tnr_b - 1

        if abs(denom) < 1e-6:
            continue
        theta = (p_obs + tnr_b - 1) / denom
        estimates.append(np.clip(theta, 0, 1))

    if not estimates:
        return 0.0, 0.0
    return np.percentile(estimates, 2.5), np.percentile(estimates, 97.5)

if __name__ == "__main__":
    print("Running mock validation...")

    # Mock data: 50 Pass, 50 Fail
    # Evaluator is ~90% accurate on Pass, ~80% accurate on Fail
    human = ['Pass']*50 + ['Fail']*50
    # True positives: 45, False negatives: 5
    # True negatives: 40, False positives: 10
    evaluator = ['Pass']*45 + ['Fail']*5 + ['Fail']*40 + ['Pass']*10

    tpr, tnr = compute_metrics(human, evaluator)
    print(f"TPR (True Positive Rate): {tpr:.2f}")
    print(f"TNR (True Negative Rate): {tnr:.2f}")

    # Assume we observed 80% pass rate in production
    p_obs = 0.80
    theta_hat = (p_obs + tnr - 1) / (tpr + tnr - 1)
    print(f"Observed Pass Rate: {p_obs:.2f}")
    print(f"Corrected True Success Rate: {theta_hat:.2f}")

    lower, upper = bootstrap_ci(human, evaluator, p_obs)
    print(f"95% CI: [{lower:.2f}, {upper:.2f}]")
