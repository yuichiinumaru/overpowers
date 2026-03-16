from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_classification_model(y_true, y_pred, y_prob=None):
    """
    Evaluate a classification model and print metrics.
    """
    metrics = {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, average='weighted'),
        'Recall': recall_score(y_true, y_pred, average='weighted'),
        'F1 Score': f1_score(y_true, y_pred, average='weighted')
    }

    if y_prob is not None:
        try:
            metrics['ROC AUC'] = roc_auc_score(y_true, y_prob, multi_class='ovr')
        except:
            pass

    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    return metrics
