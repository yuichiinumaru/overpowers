#!/usr/bin/env python3
import pandas as pd
import numpy as np
import pingouin as pg
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def detect_outliers(data, method='iqr', threshold=1.5):
    """Detect outliers using IQR or z-score method."""
    if method == 'iqr':
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        lower_bound = q1 - (threshold * iqr)
        upper_bound = q3 + (threshold * iqr)
        outliers = data[(data < lower_bound) | (data > upper_bound)]
    elif method == 'zscore':
        z_scores = np.abs(stats.zscore(data))
        outliers = data[z_scores > threshold]
    else:
        raise ValueError("Method must be 'iqr' or 'zscore'")
    return outliers

def check_normality(data, name='Variable', alpha=0.05, plot=False):
    """Check normality using Shapiro-Wilk test."""
    stat, p_value = stats.shapiro(data)
    is_normal = p_value > alpha
    
    result = {
        'variable': name,
        'statistic': stat,
        'p_value': p_value,
        'is_normal': is_normal,
        'interpretation': f"Data appears {'normal' if is_normal else 'non-normal'} (p={p_value:.4f})",
        'recommendation': "Proceed with parametric tests." if is_normal else "Consider non-parametric tests or transformation."
    }
    
    if plot:
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        sns.histplot(data, kde=True)
        plt.title(f'Histogram of {name}')
        
        plt.subplot(1, 2, 2)
        stats.probplot(data, dist="norm", plot=plt)
        plt.title(f'Q-Q Plot of {name}')
        plt.tight_layout()
        plt.show()
        
    return result

def check_normality_per_group(data, value_col, group_col, alpha=0.05):
    """Check normality for each group."""
    results = {}
    for group, group_data in data.groupby(group_col):
        results[group] = check_normality(group_data[value_col], name=f"{value_col} ({group_col}={group})", alpha=alpha)
    return results

def check_homogeneity_of_variance(data, value_col, group_col, alpha=0.05, plot=False):
    """Check homogeneity of variance using Levene's test."""
    groups = [group_data[value_col].values for name, group_data in data.groupby(group_col)]
    stat, p_value = stats.levene(*groups)
    is_homogeneous = p_value > alpha
    
    result = {
        'statistic': stat,
        'p_value': p_value,
        'is_homogeneous': is_homogeneous,
        'interpretation': f"Variances appear {'homogeneous' if is_homogeneous else 'heterogeneous'} (p={p_value:.4f})",
        'recommendation': "Proceed with standard tests." if is_homogeneous else "Use Welch's correction or non-parametric tests."
    }
    
    if plot:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=group_col, y=value_col, data=data)
        plt.title(f'Boxplot of {value_col} by {group_col}')
        plt.show()
        
    return result

def check_linearity(x, y, alpha=0.05, plot=False):
    """Check linearity between two continuous variables."""
    # Fit a simple linear regression to check residuals
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    predicted = intercept + slope * x
    residuals = y - predicted
    
    result = {
        'r_squared': r_value**2,
        'p_value': p_value,
        'interpretation': "Check residual plots for non-linear patterns."
    }
    
    if plot:
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        sns.scatterplot(x=x, y=y)
        sns.lineplot(x=x, y=predicted, color='red')
        plt.title('Scatter Plot with Fit')
        
        plt.subplot(1, 2, 2)
        sns.scatterplot(x=predicted, y=residuals)
        plt.axhline(0, color='red', linestyle='--')
        plt.title('Residuals vs Fitted')
        plt.xlabel('Fitted Values')
        plt.ylabel('Residuals')
        plt.tight_layout()
        plt.show()
        
    return result

def comprehensive_assumption_check(data, value_col, group_col=None, alpha=0.05):
    """Run comprehensive assumption checks on data."""
    results = {}
    
    # 1. Outlier detection
    if group_col:
        outliers = {}
        for group, group_data in data.groupby(group_col):
            outliers[group] = detect_outliers(group_data[value_col])
        results['outliers'] = {k: len(v) for k, v in outliers.items()}
    else:
        results['outliers'] = len(detect_outliers(data[value_col]))
        
    # 2. Normality
    if group_col:
        results['normality'] = check_normality_per_group(data, value_col, group_col, alpha)
    else:
        results['normality'] = check_normality(data[value_col], name=value_col, alpha=alpha)
        
    # 3. Homogeneity of variance (if groups exist)
    if group_col:
        results['homogeneity'] = check_homogeneity_of_variance(data, value_col, group_col, alpha)
        
    return results

if __name__ == "__main__":
    print("Assumption checks module loaded successfully.")