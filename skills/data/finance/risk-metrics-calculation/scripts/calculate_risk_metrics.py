import argparse
import numpy as np

def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)

def calculate_var(returns, confidence_level=0.95):
    return np.percentile(returns, 100 * (1 - confidence_level))

def calculate_cvar(returns, confidence_level=0.95):
    var = calculate_var(returns, confidence_level)
    return np.mean(returns[returns <= var])

def calculate_drawdown(returns):
    cumulative_returns = np.cumsum(returns)
    peak = np.maximum.accumulate(cumulative_returns)
    drawdown = cumulative_returns - peak
    return drawdown

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate portfolio risk metrics")
    parser.add_argument("--returns", nargs="+", type=float, required=True, help="List of historical returns")
    parser.add_argument("--rf", type=float, default=0.0, help="Risk-free rate")
    parser.add_argument("--conf", type=float, default=0.95, help="Confidence level for VaR/CVaR")
    
    args = parser.parse_args()
    returns = np.array(args.returns)
    
    print(f"Sharpe Ratio: {calculate_sharpe_ratio(returns, args.rf):.4f}")
    print(f"VaR ({args.conf*100}%): {calculate_var(returns, args.conf):.4f}")
    print(f"CVaR ({args.conf*100}%): {calculate_cvar(returns, args.conf):.4f}")
    print(f"Max Drawdown: {np.min(calculate_drawdown(returns)):.4f}")
