import sys

def suggest_optimization(context_type, size_ratio):
    print(f"Optimization Strategy for: {context_type}")
    print("-" * 40)
    
    if context_type == "tool_outputs" and size_ratio > 0.6:
        print("RECOMMENDATION: Observation Masking")
        print("- Replace verbose outputs with compact references.")
        print("- Preserve key metrics/findings, discard raw logs.")
    elif context_type == "message_history" and size_ratio > 0.5:
        print("RECOMMENDATION: Compaction")
        print("- Summarize early conversation turns.")
        print("- Keep recent turns and key decisions intact.")
    elif context_type == "retrieved_docs" and size_ratio > 0.4:
        print("RECOMMENDATION: Just-in-Time Loading / Partitioning")
        print("- Remove irrelevant docs from active context.")
        print("- Use sub-agents for specific doc analysis.")
    else:
        print("RECOMMENDATION: Monitor & Budget")
        print("- Context seems balanced. Continue monitoring.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python context_optimizer.py <context_type> <size_ratio_float>")
        print("Types: tool_outputs, message_history, retrieved_docs")
        sys.exit(1)
        
    suggest_optimization(sys.argv[1], float(sys.argv[2]))
