import argparse
import os

def research_topic(topic):
    print(f"## 📅 Last 30 Days: {topic}\n")
    
    # This script mocks the tool calls mentioned in SKILL.md
    # In a real scenario, this would be executed by the agent using its tools
    
    print("### What's Working")
    print("- [Pattern 1 extracted from search]")
    print("- [Pattern 2 extracted from search]")
    
    print("\n### Common Mistakes")
    print("- [Mistake 1 identified from discussions]")
    
    print("\n### Key Techniques")
    print("- [Technique with source link]")
    
    print("\n### Sources")
    print("- [Brave Search URL 1]")
    print("- [Reddit URL 1]")
    
    print("\n### Ready-to-Use Prompt")
    print("```")
    print(f"You are an expert in {topic}. [Specific instructions based on findings]...")
    print("```")

def main():
    parser = argparse.ArgumentParser(description='Research recent trends on a topic')
    parser.add_argument('topic', help='Topic to research')
    
    args = parser.parse_args()
    research_topic(args.topic)

if __name__ == "__main__":
    main()
