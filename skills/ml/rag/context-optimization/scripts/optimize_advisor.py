import argparse

def advise_optimization(total_tokens, limit, components):
    utilization = total_tokens / limit
    recommendations = []
    
    if utilization > 0.7:
        recommendations.append(f"WARNING: Context utilization is {utilization:.1%}. Optimization recommended.")
        
        # Identify dominant component
        dominant_component = max(components, key=components.get)
        
        if dominant_component == "tool_outputs":
            recommendations.append("- Recommended: Observation Masking. Tool outputs dominate context. Replace verbose outputs with compact summaries or references.")
        elif dominant_component == "retrieved_docs":
            recommendations.append("- Recommended: Summarization or Partitioning. Retrieved documents are large. Use summarization or split task into sub-agents.")
        elif dominant_component == "history":
            recommendations.append("- Recommended: Compaction. Message history is large. Summarize early turns to preserve context.")
        
        if utilization > 0.85:
            recommendations.append("- URGENT: Context nearly full. Consider immediate partitioning or task checkpointing.")
    else:
        recommendations.append(f"OK: Context utilization is {utilization:.1%}. Below optimization threshold (70%).")
        
    return "\n".join(recommendations)

def main():
    parser = argparse.ArgumentParser(description='Advise on context optimization strategies.')
    parser.add_argument('--tokens', type=int, required=True, help='Current total tokens')
    parser.add_argument('--limit', type=int, required=True, help='Context window limit')
    parser.add_argument('--tool-outputs', type=int, default=0, help='Tokens in tool outputs')
    parser.add_argument('--history', type=int, default=0, help='Tokens in message history')
    parser.add_argument('--docs', type=int, default=0, help='Tokens in retrieved documents')

    args = parser.parse_args()
    
    components = {
        "tool_outputs": args.tool_outputs,
        "history": args.history,
        "retrieved_docs": args.docs
    }
    
    print(advise_optimization(args.tokens, args.limit, components))

if __name__ == "__main__":
    main()
